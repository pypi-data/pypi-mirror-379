# Copyright 2023 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Iterable, Literal, Optional, Tuple, Dict, Any

import sqlalchemy as sa
from sqlalchemy.dialects.oracle.base import (
    OracleIdentifierPreparer,
    RESERVED_WORDS as ORACLE_RESERVED_WORDS,
)
from sqlalchemy.dialects.oracle.oracledb import OracleDialect_oracledb
import re

import ibis.expr.datatypes as dt
from ibis.backends.base.sql.alchemy import BaseAlchemyBackend
from third_party.ibis.ibis_addon.api import dvt_handle_failed_column_type_inference
from third_party.ibis.ibis_oracle.compiler import OracleCompiler
from third_party.ibis.ibis_oracle.datatypes import _get_type
import oracledb


EXTRA_RESERVED_WORDS = set(
    [
        "COLUMN",
        "ROWID",
    ]
)


def _ora_denormalize_name(self, name):
    """Oracle specific version of sqlalchemy/engine/default.py.denormalize_name()

    The original function upper cases most identifiers unless they require quoting
    before use in SQL. This includes when non standard characters are in play.

    This prevents dictionary queries from succeeding. Really, the presence of special
    characters should be irrelevant to upper/lower case decisions.

    This method uppercases identifiers that include special characters, otherwise it
    follows the original code path.
    """
    if name is None:
        return None

    if self.identifier_preparer._requires_quotes_illegal_chars(name):
        name = name.upper()
    return super(OracleDialect_oracledb, self).denormalize_name(name)


OracleDialect_oracledb.denormalize_name = _ora_denormalize_name


class DVTOracleIdentifierPreparer(OracleIdentifierPreparer):

    reserved_words = {
        x.lower() for x in ORACLE_RESERVED_WORDS.union(EXTRA_RESERVED_WORDS)
    }

    def quote_identifier(self, value):
        """Quote an identifier.

        This method adds extra path of upper casing the identifier if it is being quoted
        due to special characters. Otherwise we follow the original path.

        This is because all names are normalised to lower case in DVT which is fine because
        unquoted table name are upper cased automatically by Oracle. If we add quotes due to
        special characters then we lose the auto uppercase operation. This method forces it.
        """
        if self._requires_quotes_illegal_chars(value):
            return super().quote_identifier(value.upper())
        else:
            return super().quote_identifier(value)


OracleDialect_oracledb.preparer = DVTOracleIdentifierPreparer


class Backend(BaseAlchemyBackend):
    name = "oracle"
    compiler = OracleCompiler

    def __init__(self, arraysize: int = 500):
        super().__init__()
        self.arraysize = arraysize

    def do_connect(
        self,
        host: str = "localhost",
        user: Optional[str] = None,
        password: Optional[str] = None,
        port: int = 1521,
        database: Optional[str] = None,
        protocol: str = "TCP",
        thick_mode: bool = False,
        driver: Literal["oracledb"] = "oracledb",
        connect_args: Dict[str, Any] = None,
        url: Optional[str] = None,
    ) -> None:
        if driver != "oracledb":
            raise NotImplementedError("oracledb is currently the only supported driver")
        if url is None:
            if thick_mode or not user:
                # Configuration explicitly requests thick_mode or user not specified, credentials in wallet - requires thick_mode
                oracledb.init_oracle_client(
                    config_dir=connect_args.get("config_dir", None)
                )
            connect_args = {} if not connect_args else connect_args
            if user:
                connect_args.update(
                    {
                        "host": host,
                        "user": user,
                        "password": password,
                        "port": port,
                        "service_name": database,
                        "protocol": protocol,
                    }
                )
            sa_url = "oracle+oracledb://@"
        else:
            connect_args = {} if not connect_args else connect_args
            if thick_mode:
                # Configuration explicitly requests thick_mode.
                oracledb.init_oracle_client(
                    config_dir=connect_args.get("config_dir", None)
                )
            sa_url = sa.engine.url.make_url(url)

        engine = sa.create_engine(
            sa_url,
            poolclass=sa.pool.StaticPool,
            arraysize=self.arraysize,
            # The hardcoding of 128 below is not great but is the simplest way of dealing with:
            #   https://github.com/GoogleCloudPlatform/professional-services-data-validator/issues/1250
            # There is a quirk of SQLAlchemy behaviour that is discussed in comments of issue 1250 that
            # we cannot easily deal with, even if we "fixed" it it could be months or years before we can
            # take advantage of it.
            # We manage the max length of identifiers generated by DVT in clients.get_max_column_length()
            # and in all other cases re-use existing column names (i.e. we know the length is already fine).
            # Therefore the ugly hardcoding of 128 kicks the can down the road and unblocks a customer
            # who is working with Oracle 11g and a max identifier length of 30.
            max_identifier_length=128,
            # Pessimistic disconnect handling.
            pool_pre_ping=True,
            # oracledb connection arguments.
            connect_args=connect_args,
        )
        try:
            # Identify the session in Oracle as DVT, no-op if this fails.
            engine.raw_connection().driver_connection.module = "DVT"
        except Exception:
            pass

        @sa.event.listens_for(engine, "connect")
        def connect(dbapi_connection, connection_record):
            with dbapi_connection.cursor() as cur:
                cur.execute("ALTER SESSION SET TIME_ZONE='UTC'")
                # Standardise numeric formatting on en_US (issue 1033).
                cur.execute("ALTER SESSION SET NLS_NUMERIC_CHARACTERS='.,'")

        super().do_connect(engine)
        # the database / service name is usually obtained from tnsnames.ora, we fetch it here
        self.database_name = self.raw_sql(
            "select sys_context('USERENV', 'SERVICE_NAME') from dual"
        ).fetchall()[0][0]

    def _handle_failed_column_type_inference(
        self, table: sa.Table, nulltype_cols: Iterable[str]
    ) -> sa.Table:
        return dvt_handle_failed_column_type_inference(self, table, nulltype_cols)

    def _metadata(self, query) -> Iterable[Tuple[str, dt.DataType]]:
        if (
            re.search(r"^\s*SELECT\s", query, flags=re.MULTILINE | re.IGNORECASE)
            is not None
        ):
            query = f"({query})"

        with self.begin() as con:
            result = con.exec_driver_sql(f"SELECT * FROM {query} t0 WHERE ROWNUM <= 1")
            cursor = result.cursor
            yield from ((column[0], _get_type(column)) for column in cursor.description)

    def list_primary_key_columns(self, database: str, table: str) -> list:
        """Return a list of primary key column names."""
        list_pk_col_sql = """
            SELECT cc.column_name
            FROM all_cons_columns cc
            INNER JOIN all_constraints c ON (cc.owner = c.owner AND cc.constraint_name = c.constraint_name AND cc.table_name = c.table_name)
            WHERE c.owner = :1
            AND c.table_name = :2
            AND c.constraint_type = 'P'
            ORDER BY cc.position
        """
        with self.begin() as con:
            result = con.exec_driver_sql(
                list_pk_col_sql, parameters=(database.upper(), table.upper())
            )
            return [_[0] for _ in result.cursor.fetchall()]

    def raw_column_metadata(
        self, database: str = None, table: str = None, query: str = None
    ) -> Iterable[Tuple]:
        """Define this method to allow DVT to test if backend specific transformations may be needed for comparison.
        Partner method to _metadata that retains raw data type information instead of converting to Ibis types.
        This works in the same way as _metadata by running a query over the DVT source, either schema.table or a
        custom query, and fetching the first row. From the cursor we can detect data types of the row's columns.

        Returns:
            list: A list of tuples containing the standard 7 DB API fields:
                  https://peps.python.org/pep-0249/#description
        """

        def strip_prefix(s: str):
            if s.startswith("DB_TYPE_"):
                return s[8:]
            else:
                return s

        assert (database and table) or query, "We should never receive all args=None"
        if database and table:
            source = f'"{database}"."{table}"'.upper()
        elif query:
            source = f"({query})"

        with self.begin() as con:
            result = con.exec_driver_sql(f"SELECT * FROM {source} t0 WHERE ROWNUM <= 1")
            cursor = result.cursor
            yield from (
                (column[0], strip_prefix(column[1].name), *column[2:])
                for column in cursor.description
            )

    def is_char_type_padded(self, char_type: Tuple) -> bool:
        """Define this method if the backend supports character/string types that are padded and returns
        padded values, which DVT may want to trim"""
        return char_type[0] in ["CHAR", "NCHAR"]

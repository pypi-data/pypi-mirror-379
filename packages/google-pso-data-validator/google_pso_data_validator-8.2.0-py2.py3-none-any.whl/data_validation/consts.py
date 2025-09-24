# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Configuration Fields
# These are all keys into the config dict. Where these values come from the command line, these would
# match with the command line argument - so --secret-manager-type value would be inserted with the
# 'secret_manager_type' key.
# This is true for the most part, except where a typo gets introduced, i.e. --use-random-row became use_random_rows
# Fixing this would be a breaking change. A future cleanup to prevent this would be to use
# f'--{config_constant.repl('_','-')}' as the name argument to argparse.
SOURCE_TYPE = "source_type"
SECRET_MANAGER_TYPE = "secret_manager_type"
SECRET_MANAGER_PROJECT_ID = "secret_manager_project_id"
CONFIG = "config"
CONFIG_FILE = "config_file"
CONFIG_FILE_JSON = "config_file_json"
CONFIG_SOURCE_CONN_NAME = "source_conn_name"
CONFIG_TARGET_CONN_NAME = "target_conn_name"
CONFIG_SOURCE_CONN = "source_conn"
CONFIG_TARGET_CONN = "target_conn"
CONFIG_TYPE = "type"
CONFIG_DEFAULT_CAST = "default_cast"
CONFIG_CUSTOM = "custom"
CONFIG_CUSTOM_IBIS_EXPR = "ibis_expr"
CONFIG_CUSTOM_PARAMS = "params"
CONFIG_CUSTOM_PARAM_FORMAT_STR = "format_str"
CONFIG_SCHEMA_NAME = "schema_name"
CONFIG_TABLE_NAME = "table_name"
CONFIG_TARGET_SCHEMA_NAME = "target_schema_name"
CONFIG_TARGET_TABLE_NAME = "target_table_name"
CONFIG_LABELS = "labels"
CONFIG_COMPARISON_FIELDS = "comparison_fields"
CONFIG_FIELD_ALIAS = "field_alias"
CONFIG_AGGREGATES = "aggregates"
CONFIG_CALCULATED_FIELDS = "calculated_fields"
CONFIG_GROUPED_COLUMNS = "grouped_columns"
CONFIG_CALCULATED_SOURCE_COLUMNS = "source_calculated_columns"
CONFIG_CALCULATED_TARGET_COLUMNS = "target_calculated_columns"
CONFIG_USE_RANDOM_ROWS = "use_random_rows"
CONFIG_RANDOM_ROW_BATCH_SIZE = "random_row_batch_size"
CONFIG_PRIMARY_KEYS = "primary_keys"
CONFIG_TRIM_STRING_PKS = "trim_string_pks"  # now deprecated
CONFIG_CASE_INSENSITIVE_MATCH = "case_insensitive_match"
CONFIG_ROW_CONCAT = "concat"
CONFIG_ROW_HASH = "hash"
CONFIG_RUN_ID = "run_id"
CONFIG_START_TIME = "start_time"
CONFIG_END_TIME = "end_time"
CONFIG_SOURCE_COLUMN = "source_column"
CONFIG_TARGET_COLUMN = "target_column"
CONFIG_THRESHOLD = "threshold"
CONFIG_CAST = "cast"
CONFIG_CAST_BOOL_STRING = "bool_string"
CONFIG_CAST_UUID_STRING = "uuid_string"
CONFIG_DEPTH = "depth"
CONFIG_FORMAT = "format"
CONFIG_LIMIT = "limit"
CONFIG_FILTERS = "filters"
CONFIG_FILTER_SOURCE = "source"
CONFIG_FILTER_TARGET = "target"
CONFIG_MAX_RECURSIVE_QUERY_SIZE = "max_recursive_query_size"
CONFIG_SOURCE_QUERY = "source_query"
CONFIG_SOURCE_QUERY_FILE = "source_query_file"
CONFIG_TARGET_QUERY = "target_query"
CONFIG_TARGET_QUERY_FILE = "target_query_file"
CONFIG_CUSTOM_QUERY_TYPE = "custom_query_type"
CONFIG_FILTER_SOURCE_COLUMN = "source_column"
CONFIG_FILTER_SOURCE_VALUE = "source_value"
CONFIG_FILTER_TARGET_COLUMN = "target_column"
CONFIG_FILTER_TARGET_VALUE = "target_value"
CONFIG_EXCLUSION_COLUMNS = "exclusion_columns"
CONFIG_ALLOW_LIST = "allow_list"
CONFIG_FILTER_STATUS = "filter_status"

CONFIG_RESULT_HANDLER = "result_handler"

CONFIG_TYPE_AVG = "avg"
CONFIG_TYPE_BIT_XOR = "bit_xor"
CONFIG_TYPE_COUNT = "count"
CONFIG_TYPE_MAX = "max"
CONFIG_TYPE_MIN = "min"
CONFIG_TYPE_STD = "std"
CONFIG_TYPE_SUM = "sum"

# Default values
DEFAULT_NUM_RANDOM_ROWS = 10000

# Filter Type Options
FILTER_TYPE_CUSTOM = "custom"
FILTER_TYPE_EQUALS = "equals"
FILTER_TYPE_ISIN = "isin"

# Validation Types
COLUMN_VALIDATION = "Column"
GROUPED_COLUMN_VALIDATION = "GroupedColumn"
ROW_VALIDATION = "Row"
SCHEMA_VALIDATION = "Schema"
CUSTOM_QUERY = "Custom-query"

CONFIG_TYPES = [
    COLUMN_VALIDATION,
    GROUPED_COLUMN_VALIDATION,
    ROW_VALIDATION,
    SCHEMA_VALIDATION,
    CUSTOM_QUERY,
]

# State Manager Fields
DEFAULT_ENV_DIRECTORY = "~/.config/google-pso-data-validator/"
ENV_DIRECTORY_VAR = "PSO_DV_CONN_HOME"

# Yaml File Config Fields
YAML_RESULT_HANDLER = "result_handler"
YAML_SOURCE = "source"
YAML_TARGET = "target"
YAML_VALIDATIONS = "validations"

# Connection key constants.
SOURCE_TYPE_BIGQUERY = "BigQuery"
SOURCE_TYPE_DB2 = "DB2"
SOURCE_TYPE_FILESYSTEM = "FileSystem"
SOURCE_TYPE_IMPALA = "Impala"
SOURCE_TYPE_MSSQL = "MSSQL"
SOURCE_TYPE_MYSQL = "MySQL"
SOURCE_TYPE_ORACLE = "Oracle"
SOURCE_TYPE_POSTGRES = "Postgres"
SOURCE_TYPE_REDSHIFT = "Redshift"
SOURCE_TYPE_SNOWFLAKE = "Snowflake"
SOURCE_TYPE_SPANNER = "Spanner"
SOURCE_TYPE_TERADATA = "Teradata"

# BigQuery Result Handler Configs
RH_TYPE = "type"
RH_CONN = "connection"
PROJECT_ID = "project_id"
TABLE_ID = "table_id"
GOOGLE_SERVICE_ACCOUNT_KEY_PATH = "google_service_account_key_path"
API_ENDPOINT = "api_endpoint"
STORAGE_API_ENDPOINT = "storage_api_endpoint"

# Result Handler Output Table Fields
VALIDATION_TYPE = "validation_type"
VALIDATION_NAME = "validation_name"
AGGREGATION_TYPE = "aggregation_type"
GROUP_BY_COLUMNS = "group_by_columns"

SOURCE_TABLE_NAME = "source_table_name"
SOURCE_COLUMN_NAME = "source_column_name"
SOURCE_AGG_VALUE = "source_agg_value"

TARGET_TABLE_NAME = "target_table_name"
TARGET_COLUMN_NAME = "target_column_name"
TARGET_AGG_VALUE = "target_agg_value"

VALIDATION_STATUS = "validation_status"
VALIDATION_STATUS_SUCCESS = "success"
VALIDATION_STATUS_FAIL = "fail"
VALIDATION_STATUSES = [
    VALIDATION_STATUS_SUCCESS,
    VALIDATION_STATUS_FAIL,
]
VALIDATION_DIFFERENCE = "difference"
VALIDATION_PCT_DIFFERENCE = "pct_difference"
VALIDATION_PCT_THRESHOLD = "pct_threshold"

NUM_RANDOM_ROWS = "num_random_rows"

# Summary stats of Row Validation results
TOTAL_SOURCE_ROWS = "total_source_rows"
TOTAL_TARGET_ROWS = "total_target_rows"
TOTAL_ROWS_VALIDATED = "total_rows_validated"
TOTAL_ROWS_SUCCESS = "total_rows_success_validation_status"
TOTAL_ROWS_FAIL = "total_rows_fail_validation_status"
FAILED_SOURCE_NOT_IN_TARGET = "failed_rows_present_in_source_not_in_target"
FAILED_TARGET_NOT_IN_SOURCE = "failed_rows_present_in_target_not_in_source"
FAILED_PRESENT_IN_BOTH_TABLES = "failed_rows_present_in_both_source_and_target"

# Combiner only constants
COMBINER_TABLE_NAME = "dvt_table_name"
COMBINER_COLUMN_NAME = "dvt_column_name"
COMBINER_AGG_VALUE = "dvt_agg_value"

# SQL Template Formatting
# TODO: should this be managed in query_builder if that is the only place its used?
COUNT_STAR = "{count_star}"

# Validation metadata
RESULT_TYPE_SOURCE = "source"
RESULT_TYPE_TARGET = "target"
RESULT_TYPE_DIFFERENCES = "differences"

FORMAT_TYPE_CSV = "csv"
FORMAT_TYPE_JSON = "json"
FORMAT_TYPE_MINIMAL = "minimal"
FORMAT_TYPE_PYTHON = "python"
FORMAT_TYPE_TABLE = "table"
FORMAT_TYPE_TEXT = "text"
FORMAT_TYPES = [FORMAT_TYPE_CSV, FORMAT_TYPE_JSON, FORMAT_TYPE_TABLE, FORMAT_TYPE_TEXT]
RAW_QUERY_FORMAT_TYPES = [FORMAT_TYPE_MINIMAL, FORMAT_TYPE_PYTHON]

# Text Result Handler column filter list
COLUMN_FILTER_LIST = [
    AGGREGATION_TYPE,
    CONFIG_END_TIME,
    CONFIG_LABELS,
    VALIDATION_PCT_THRESHOLD,
    CONFIG_START_TIME,
    TARGET_TABLE_NAME,
    TARGET_COLUMN_NAME,
    VALIDATION_DIFFERENCE,
    CONFIG_PRIMARY_KEYS,
    GROUP_BY_COLUMNS,
    NUM_RANDOM_ROWS,
]
SCHEMA_VALIDATION_COLUMN_FILTER_LIST = [
    CONFIG_START_TIME,
    CONFIG_END_TIME,
    AGGREGATION_TYPE,
    VALIDATION_DIFFERENCE,
    CONFIG_PRIMARY_KEYS,
    GROUP_BY_COLUMNS,
    NUM_RANDOM_ROWS,
    VALIDATION_PCT_THRESHOLD,
]

# Constants for the named column used in generate partitions
# this cannot conflict with primary key column names
DVT_POS_COL = "dvt_pos_num"

# Default limit for the number of columns we will attempt in a single validation.
MAX_CONCAT_COLUMNS_DEFAULTS = {
    # Preventing: The concat function requires 2 to 254 arguments
    "mssql": 254,
    # Minimizing risk of: ORA-01489: result of string concatenation is too long
    "oracle": 125,
    # Preventing: cannot pass more than 100 arguments to a function
    "postgres": 99,
    # Minimizing risk of: [Error 3556] Too many columns defined for this table.
    "teradata": 500,
}

# CalculatedField expression constants.
CALC_FIELD_CAST = "cast"
CALC_FIELD_CONCAT = "concat"
CALC_FIELD_BYTE_LENGTH = "byte_length"
CALC_FIELD_EPOCH_SECONDS = "epoch_seconds"
CALC_FIELD_HASH = "hash"
CALC_FIELD_IFNULL = "ifnull"
CALC_FIELD_LENGTH = "length"
CALC_FIELD_PADDED_CHAR_LENGTH = "padded_char_length"
CALC_FIELD_RSTRIP = "rstrip"
CALC_FIELD_UPPER = "upper"

### STDLIB IMPORTS
pass
import copy

### LOCAL IMPORTS
pass

### PACKAGE IMPORTS
pass

### CONSTANTS

### GENERAL DB CONSTANTS ###
BASE_FROM STR = "from {}"
BASE_FROM_WHERE_ID_STR = "from {} where ID = {};"

BASE_SELECT_JSON_STR = "select json_extract(data, '$.{}'{})"
SELECT_JSON_ARG_STR = ", '$.{}'{}"  

CREATE_TABLE_STR = "CREATE TABLE {} (id varchar, data json);"
WRITE_JSON_STR = "insert into {} values (?, ?);"
READ_JSON_KEY_STR = "select json_extract(data, '$.{}') from {} where ID = {};"
READ_JSON_ROW_STR = "select * from {} where ID = {};"
READ_ALL_JSON_KEYS_STR = "select json_extract(data, '$.{}') from {};"
READ_ALL_ROWS_STR = "select * from {};"
READ_ALL_IDS_STR = 'select ID from {}'
UPDATE_ROW_STR = 'update {} set data = "{}" where ID = {};'
DELETE_ROW_STR = 'delete from {} where ID = {};'
ROW_EXISTS_STR = 'select count(*) from {} where ID = {};'


if __name__ == '__main__':
	#print(BASE_SELECT_JSON_STR.format('test', SELECT_JSON_ARG_STR))


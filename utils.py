### STDLIB IMPORTS
import copy

### LOCAL IMPORTS
from constants import BASE_SELECT_JSON_STR
from constants import SELECT_JSON_ARG_STR

### PACKAGE IMPORTS
pass

def multi_coln_read_str(args, read_type=): 
	num_args = len(args)
	read_str = copy.deepcopy(BASE_SELECT_JSON_STR)

	for idx, arg in enumerate(args):
		if idx+1 == num_args:
			read_str = read_str.format(arg, '')
		else:
			read_str = read_str.format(arg, SELECT_JSON_ARG_STR)

	return read_str

if __name__ == '__main__':
	pass
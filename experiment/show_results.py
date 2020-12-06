import sys
import glob
import csv
import numpy as np

if len(sys.argv) <= 3:
	print('Error, use like this:')
	print('<subject> <eye_lr> <control>')
	print('e.g.')
	print('shakespeare -1 1')
	exit()

subject_name = sys.argv[1]
eye_lr = int(sys.argv[2])
is_control = bool(int(sys.argv[3]))

print('subject_name: {}, eye_lr: {}, control: {}'.format(subject_name, eye_lr, is_control))

def string_to_bool(string):
	string = string.lower()
	if string in ['false']:
		return False
	elif string in ['true']:
		return True
	else:
		raise RuntimeError('Cannot parse as bool: "{}"'.format(string))

def parse_response(resp):
	if resp == 'w':
		return True
	elif resp == 's':
		return False
	elif resp == 'x':
		return None
	else:
		raise RuntimeError('Cannot parse response: "{}"'.format(string))

def load_data(subject_name, eye_lr, is_control):
	levels = []
	resp = []

	fnames = glob.glob('./data/{}_weber_*.csv'.format(subject_name))

	print('Loading data from: ')
	print('\n'.join(fnames))

	for fname in fnames:
		with open(fname, 'r', encoding='utf-8-sig') as data_file:
			reader = csv.DictReader(data_file)
			for row in reader:
				try:
					if int(row['eye_lr']) != eye_lr:
						continue
						
					show_dot = string_to_bool(row['show_dot'])
					if (not show_dot) != is_control:
						continue
					levels.append(int(row['level']))
					resp.append(parse_response(row['key_resp_2.keys']))
				except ValueError:
					continue # Ignore blank rows
	
	if len(resp) < 1:
		raise RuntimeError('Err, no data for user ' + subject_name)
				
	return np.array(levels).T, np.array(resp)
	
levels, resp = load_data(subject_name, eye_lr, is_control)

print(repr(levels))
print(repr(resp))


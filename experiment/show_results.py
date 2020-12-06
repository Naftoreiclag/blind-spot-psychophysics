import sys

if len(sys.argv) <= 3:
	print('Error, use like this:')
	print('<subject> <eye_lr> <control>')
	print('e.g.')
	print('shakespeare -1 1')

subject_name = sys.argv[1]
eye_lr = int(sys.argv[2])
is_control = bool(int(sys.argv[3]))

print('subject_name: {}, eye_lr: {}, control: {}'.format(subject_name, eye_lr, is_control))

def load_data(subject_name, eye_lr):
	level = []
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
					off_x.append(float(row['offset_x']))
					off_y.append(float(row['offset_y']))
					
					
					resp.append('j' in row['key_resp_2.keys'])
				except ValueError:
					continue # Ignore blank rows
	
	if len(resp) < 1:
		raise RuntimeError('Err, no data for user ' + subject_name)
				
	return np.array((off_x, off_y)).T, np.array(resp)


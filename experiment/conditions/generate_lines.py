import csv
import numpy as np
import json
import sys

if not len(sys.argv) >= 2:
	print('Args: <subject> <eye_lr>')
	exit(0)

subject_name = sys.argv[1]
eye_lr = int(sys.argv[2])

gap_size = 5

with open('../maps/{}_{}.json'.format(subject_name, eye_lr), 'r') as ofile:
	subject_name, eye_lr, ellipse = json.load(ofile)
	a, b, h, k = ellipse

## update these numbers for each user ##
blind_x = h    # x coordinate of center of blind spot
blind_y = k    # y coordinate of center of blind spot
blind_w = 2*a  # width of blind spot
blind_h = 2*b  # height of blind spot
##
bottom_line = blind_y - (gap_size/2)
middle_line = blind_y + (gap_size/2)    # these keep the real distance between lines at 4
top_line = middle_line + gap_size    # centered location of top line

delta_x = 0.3
bound_bottom = -4
bound_top = 4

num_repeats = 20
jitter_max = 0.2

print(top_line + delta_x*bound_top + jitter_max - 2)

with open('line_locs.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['bottom_y', 'middle_y', 'top_y', \
					'blind_x', 'blind_y', 'blind_w', 'blind_h', \
					'source_subject_name', 'source_eye_lr', 'delta_x', 'level', 'displacement', 'gap_size', 'test_gap_size'])
	for rep in range(num_repeats):
		# print('\n', rep)
		levels = np.round(np.arange(bound_bottom, bound_top+1), decimals=4)
		# No need to shuffle the levels because PsychoPy already does that
		#np.random.shuffle(levels)
		for lev in levels:
			jitter = (np.random.random() - 0.5)*2*jitter_max

			displacement = np.round(lev*delta_x, decimals=4)

			bottom_loc = bottom_line + jitter
			middle_loc = middle_line + jitter
			top_loc = top_line + displacement + jitter
			test_gap_size = gap_size + displacement

			row = [bottom_loc, middle_loc, top_loc, blind_x, blind_y, blind_w, blind_h, subject_name, eye_lr, delta_x, lev, displacement, gap_size, test_gap_size]
			writer.writerow(row)
			# print(row)

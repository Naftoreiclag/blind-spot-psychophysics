import csv
import numpy as np

## update these numbers for each user ##
blind_x = -2    # x coordinate of center of blind spot
blind_y = -2    # y coordinate of center of blind spot
blind_w = 2    # width of blind spot
blind_h = 2    # height of blind spot
##
bottom_line = blind_y - blind_h
middle_line = blind_y + blind_h    # these keep the real distance between lines at 4
top_line = middle_line + 4    # centered location of top line

delta_x = 0.1
num_levels = 3

num_repeats = 5
jitter_max = 0.1

with open('line_locs.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['bottom_y', 'middle_y', 'top_y', \
					'blind_x', 'blind_y', 'blind_w', 'blind_h'])
	for rep in range(num_repeats):
		print('\n', rep)
		levels = np.round(np.arange(-num_levels, num_levels+1), decimals=4)
		np.random.shuffle(levels)
		for lev in levels:
			jitter = (np.random.random() - 0.5)*jitter_max

			bottom_loc = bottom_line + jitter
			middle_loc = middle_line + jitter
			top_loc = top_line + np.round(lev*delta_x, decimals=4) + jitter

			row = [bottom_loc, middle_loc, top_loc, blind_x, blind_y, blind_w, blind_h]
			writer.writerow(row)
			print(row)
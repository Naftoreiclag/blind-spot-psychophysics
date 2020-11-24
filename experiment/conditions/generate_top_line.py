import csv
import numpy as np

delta_x = 0.1
num_levels = 3
num_repeats = 20
jitter_amount = 0.1

with open('top_line_locs.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['top_loc', 'jitter'])
	for rep in range(num_repeats):
		print('\n', rep)
		levels = np.round(np.arange(-num_levels, num_levels+1), decimals=4)
		np.random.shuffle(levels)
		for lev in levels:
			loc = np.round(lev*delta_x, decimals=4)

			jitter = (np.random.random() - 0.5)*jitter_amount

			writer.writerow([loc, jitter])
			print(loc, jitter)
import csv
import numpy as np

delta_x = 0.1
num_levels = 3

with open('top_line_locs.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['loc'])
	for lev in np.arange(-num_levels, num_levels+1):
		p = np.round(lev*delta_x, decimals=4)
		print(p)
		writer.writerow([p])
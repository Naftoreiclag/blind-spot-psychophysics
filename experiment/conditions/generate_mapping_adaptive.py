import csv
import sys
import random

if len(sys.argv) < 5:
	print('Arguments: ')
	print('<x> <y> <rad> <num_samples>')
	exit(0)

center_x = float(sys.argv[1])
center_y = float(sys.argv[2])
radius = float(sys.argv[3])
num_samples = int(sys.argv[4])

def sample():
	while True:
		x = random.uniform(-radius, radius)
		y = random.uniform(-radius, radius)
		
		d = (x*x+y*y)**0.5
		
		if d <= radius:
			return (x + center_x, y + center_y)

samples = [sample() for _ in range(num_samples)]


with open('mapping.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['offset_x', 'offset_y'])
	for p in samples:
		writer.writerow(p)
	

import matplotlib.pyplot as plt


plt.scatter([a[0] for a in samples], [a[1] for a in samples])
plt.show()

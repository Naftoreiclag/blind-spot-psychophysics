import csv

import random

radius = 4
num_samples = 150

random.seed(0)

def sample():
	while True:
		x = random.uniform(-radius, radius)
		y = random.uniform(-radius, radius)
		
		d = (x*x+y*y)**0.5
		
		if d <= radius:
			return (x, y)

samples = [sample() for _ in range(num_samples)]


with open('mapping.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['offset_x', 'offset_y'])
	for p in samples:
		writer.writerow(p)
	

import matplotlib.pyplot as plt


plt.scatter([a[0] for a in samples], [a[1] for a in samples])
plt.show()

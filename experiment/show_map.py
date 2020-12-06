import sys
import glob
import csv
import json
import numpy as np
import matplotlib.pyplot as plt
import os

if not len(sys.argv) >= 2:
	print('Args: <subject> <eye_lr>')
	exit(0)

subject_name = sys.argv[1]
eye_lr = int(sys.argv[2])

print('subject_name: {}, eye_lr: {}'.format(subject_name, eye_lr))

def load_data(subject_name, eye_lr):
	off_x = []
	off_y = []
	resp = []

	fnames = glob.glob('./data/{}_map_*.csv'.format(subject_name))

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

locs, resp = load_data(subject_name, eye_lr)

def extract_ellipse(weights, bias):
	Q, W, E, R = weights
	T = bias
	
	w = -T + (Q*Q)/(4*E) + (W*W)/(4/R)
	
	a = (w/E)**0.5
	b = (w/R)**0.5
	h = -Q/(2*E)
	k = -W/(2*R)
	
	return a,b,h,k
	
def ensure_folders_exist(output_fname):
	output_folder = ''.join(os.path.split(output_fname)[:-1])
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)
		return False
	else:
		return True
	
def save_blind_spot(subject_name, eye_lr, ellipse):
	filename = 'maps/{}_{}.json'.format(subject_name, eye_lr)
	ensure_folders_exist(filename)
	with open(filename, 'w') as ofile:
		json.dump([subject_name, eye_lr, ellipse], ofile)
	

def fit_svm(locs, resp):
	from sklearn import svm
	
	samples = locs
	
	blind_spot_center = np.median(samples[~resp], axis=0)
	print(blind_spot_center)

	print(np.mean(samples - blind_spot_center, axis=0))
	D = np.hstack((samples - blind_spot_center, (samples - blind_spot_center)**2))
	y = np.array([(1 if x else -1) for x in resp])

	clf = svm.LinearSVC(C = 1, max_iter=100000, loss='hinge')
	clf.fit(D, y)

	weights = clf.coef_[0]
	bias = clf.intercept_[0]
	print(weights, bias)

	a,b,h,k = extract_ellipse(weights, bias)

	h += blind_spot_center[0]
	k += blind_spot_center[1]
	
	print('Ellipse parameters:')
	print('(x-h)a^-2 + (y-k)b^-2 = 1')
	print('a: ', a)
	print('b: ', b)
	print('h: ', h)
	print('k: ', k)
	
	
	delta = 0.025
	X, Y = np.meshgrid(np.arange(blind_spot_center[0]-4, blind_spot_center[0]+4, delta), np.arange(blind_spot_center[1]-4, blind_spot_center[1]+4, delta))
	Xs = X - blind_spot_center[0]
	Ys = Y - blind_spot_center[1]
	Z = Xs * weights[0] + Ys * weights[1] + Xs*Xs*weights[2] + Ys*Ys*weights[3] + bias

	fig, ax = plt.subplots()
	CS = ax.contour(X, Y, Z, levels=[-1, 0, 1], colors='k')
	ax.clabel(CS, inline=1, fontsize=10)
	ax.scatter(samples[resp,0], samples[resp,1])
	ax.scatter(samples[~resp,0], samples[~resp,1])
	ax.plot([blind_spot_center[0]], [blind_spot_center[1]], marker='o', markersize=3, color="red")
	ax.set_xlim(-8, 8)
	ax.set_ylim(-8, 8)
	ax.set_aspect('equal')
	plt.show()
	
	return a,b,h,k

if True:
	ellipse = fit_svm(locs, resp)
	
	save_blind_spot(subject_name, eye_lr, ellipse)
else:
	plt.scatter(locs[:, 0], locs[:, 1])
	plt.scatter(locs[~resp, 0], locs[~resp, 1])
	plt.show()

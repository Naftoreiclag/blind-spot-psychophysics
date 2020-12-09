import sys
import glob
import csv
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from collections import defaultdict 
from scipy.stats import norm
import os

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

	
def ensure_folders_exist(output_fname):
	output_folder = ''.join(os.path.split(output_fname)[:-1])
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)
		return False
	else:
		return True

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

ALIASES = {
	'c' : 1,
	'j' : 2, 
	'k' : 3,
	't' : 4,
	'l' : 5,
}



EYE_NAMES = {
	-1 : 'Right',
	1 : 'Left',
}

CONTROL_NAMES = {
	1 : 'Control',
	0 : 'Test',
}

def make_title():
	name = 'Subject {}'.format(ALIASES[subject_name[0]])
	
	if eye_lr == 1:
		if is_control:
			return name + ', Right, Nasal (Not Blind)'
		else:
			return name + ', Left, Temporal (Blind)'
	else:
		if is_control:
			return name + ', Left, Nasal (Not Blind)'
		else:
			return name + ', Right, Temporal (Blind)'

def cm_to_deg(x):
	return np.arctan(x/30) * 180 / np.pi
	
def plot_it(resp, levels):
	# In[137]:

	#get_ipython().run_line_magic('matplotlib', 'inline')


	# In[138]:


	responses = [x for x in resp]
	#responses = sorted(responses)
	#responses = [False] * len(responses)
	levels = [x for x in levels]


	# In[139]:


	n = len(responses)

	responses_by_level = defaultdict(list)

	for i in range(n):
		if responses[i] == None:
			continue
		responses_by_level[levels[i]].append(int(responses[i]))

	responses_by_level


	# In[140]:


	percentages = defaultdict(list)

	for level in responses_by_level:
		resps = responses_by_level[level]
		percentages[level] = np.sum(resps) / len(resps)
		
	percentages


	# In[141]:


	# make sure everything is sorted
	all_values = list(zip(percentages.keys(), percentages.values()))
	all_values = np.array(sorted(all_values, key=lambda x: x[0]))
	all_values


	# In[142]:


	x = all_values[:,0]
	p = all_values[:,1]
	# p = [0, 0.1, 0.3, 0.55, 0.7, 0.9, 1]  # test: something that actually looks like a psychometric function


	# In[143]:


	(mu, sigma), cov = curve_fit(norm.cdf, x, p, [0,1]) # last argument is initialization
	print('mu', mu, 'sigma', sigma)

	with open('all_mu_sigmas.csv', 'a') as f:
		writer = csv.writer(f)
		# writer.writerow(['', 'mu', 'sigma'])
		writer.writerow([make_title(), mu, sigma])


	# In[144]:


	fig, ax = plt.subplots(figsize=(4.5,4))
	
	x_in_deg = cm_to_deg(x*0.03)
	
	ax.scatter(x_in_deg, p, c='r', label='Level Mean')
	ax.set_ylim(0, 1)
	ax.plot(x_in_deg, norm.cdf(x, mu, sigma), label='Fit')
	ax.legend()
	ax.set_xlabel('displacement (deg)')
	ax.set_ylabel('positive response rate')


	# In[ ]:

	ax.set_title(make_title())
	
	ofname = 'fig/plot_{}_{}_{}.png'.format(ALIASES[subject_name[0]], EYE_NAMES[eye_lr], CONTROL_NAMES[is_control])
	ensure_folders_exist(ofname)
	
	plt.savefig(ofname)
	plt.show()
	

plot_it(resp, levels)



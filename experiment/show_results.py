import sys
import glob
import csv
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from collections import defaultdict 
from scipy.stats import norm

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

def make_title():
	if eye_lr == 1:
		if is_control:
			return subject_name + ', right, nasal (not blind)'
		else:
			return subject_name + ', left, temporal (blind)'
	else:
		if is_control:
			return subject_name + ', left, nasal (not blind)'
		else:
			return subject_name + ', right, temporal (blind)'

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


	plt.scatter(x, p, c='r')
	plt.ylim(0, 1)
	plt.plot(x, norm.cdf(x, mu, sigma))


	# In[ ]:

	plt.title(make_title())
	plt.show()
	

plot_it(resp, levels)



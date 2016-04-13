def calc_mortgage_payment( amt, rate, period ):
	'''
	amt: Initial Mortgage Amount (Principal)
	rate: bank interest rate (in decimal not %)
	period: 15, 20, 25 yrs
	Calculate Mortgage assuming monthly payment 
	'''
	r = rate/12 # Monthly Rate
	n = period * 12 # Period in Months
	M = amt * (r * (1 + r)**n) / ((1 + r)**n - 1)

	return M

def save_tsv(fid, data):
	'''
	save data to a tsv
	fid: file id
	data: a list of dicts
	'''
	headers = data[0].keys()
	f = open(fid,'w')
	f.write('\t'.join(headers)+'\n')
	for d in data:
		items = [str(d[h]) for h in headers]
		f.write('\t'.join(items) + '\n')
	f.close()

def load_tsv(fid, delim='\t'):
	'''
	load properties from file
	fid: file id
	delim: delimiter ie \t or ,
	Return a list of dicts, where each dict is a prop
	'''
	f = open(fid,'r')
	headers = f.readline().strip().split(delim)
	headers =  [h.strip() for h in headers]
	properties = []
	for line in f:
		if len(line.strip()) == 0:
			break
		items = line.strip().split(delim)
		p = {}
		for i in range(len(headers)):
			try: p[headers[i]] = float(items[i])
			except: p[headers[i]] = items[i]
		properties += [p]
		
	f.close()
	return properties


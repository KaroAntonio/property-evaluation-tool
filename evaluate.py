import csv
from tools import *

# Params
down = 25000 					# Down Payment
down_cap = 30000
insurance = 100					# Home or Otherwise
utils = 400						# Hydro, Electricity, Waste, Gas, Internet
r = 0.025						# Mortgage Rate
p = 25 							# Amortization Period

# Headers to display
headers = ['cashflow', 'income', 'cost', 'beds','list', 'address']

costs = [insurance, utils]

properties = load_tsv('properties.tsv')

print('\t'.join(headers))

def get_max_offer(prop, cap):
	'''
	prop: property dict
	cap: limit on max offer
	Return Max offer that can be made while maintaining +ve cashflow
	'''
	offer = 0 
	while True:
		offer += 10000
		down = offer * 0.05
		mp = calc_mortgage_payment( offer - down, r, p )
		mt = (prop['taxes'] + prop['taxes+']) / 12
		cost = mp + mt + sum(costs) + prop['fees'] 
		cashflow = prop['income'] - cost
		if cashflow < 0 or offer > cap or down > down_cap:
			print(offer, cashflow)
			return offer - 10000

for prop in properties:
	# Income (Monthly) 
	prop['income'] = prop['beds'] * prop['rent']

	# Mortgage Payment
	down = prop['list'] * 0.05
	prop['down'] = down
	mp = calc_mortgage_payment( prop['list'] - down, r, p ) 
	prop['monthly_payment'] = mp

	# Taxes
	mt = (prop['taxes'] + prop['taxes+']) / 12

	# Cost (Monthly)
	prop['cost'] = mp + mt + sum(costs) + prop['fees'] 

	# Cashflow (Mothly)
	prop['cashflow'] = prop['income'] - prop['cost']
	
	# Max Offer 
	prop['max_offer'] = get_max_offer(prop, 700000) 
	#prop['max_offer'] = prop['max_offer'] if prop['cashflow'] > 0 else 0

# Sort According to Cashflow
properties.sort(key = lambda x: x['cashflow'], reverse = True)

for prop in properties:
	# Display
	items = []
	for d in headers:
		try: items += [str(int(prop[d]))]
		except: items += [str(prop[d])]
	disp_str = "\t".join(items)
	print(disp_str)

# Output to TSV
save_tsv('results.tsv', properties)




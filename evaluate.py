import csv
from tools import *

# Params
rent = 650						# Avg Rent per Room
down = 40000 					# Down Payment
insurance = 100					# Home or Otherwise
utils = 500						# Hydro, Electricity, Waste, Gas, Internet
other = 50 / 12						# Additional Fixed Costs (ie Water Tax)
r = 0.027						# Mortgage Rate
p = 25 							# Amortization Period

# Headers to display
disp = ['cash', 'income', 'cost', 'beds','list', 'address']

costs = [insurance, utils, other]

properties = load_tsv('properties.tsv')

print('\t'.join(disp))
for prop in properties:
	# Income (Monthly) 
	prop['income'] = prop['beds'] * rent

	# Mortgage Payment
	mp = calc_mortgage_payment( prop['list'] - down, r, p) 
	prop['monthly_payment'] = mp

	# Taxes
	mt = prop['taxes'] / 12

	# Cost (Monthly)
	prop['cost'] = mp + mt + sum(costs) + prop['fees']

	# Cashflow 
	prop['cash'] = prop['income'] - prop['cost']

# Sort According to Cashflow
properties.sort(key = lambda x: x['cash'], reverse = True)

for prop in properties:
	# Display
	items = []
	for d in disp:
		try: items += [str(int(prop[d]))]
		except: items += [str(prop[d])]
	disp_str = "\t".join(items)
	print(disp_str)

# Output to TSV
save_tsv('results.tsv', properties)




# -*- coding: UTF-8 -*-

"""
Kaggle Challenge: 
"http://www.kaggle.com/c/acquire-valued-shoppers-challenge/" 
'Reduce the data and generate features' by Triskelion 
After a forum post by BreakfastPirate
Very mediocre and hacky code, single-purpose, but pretty fast
Some refactoring by Zygmunt Zając <zygmunt@fastml.com>
"""

from datetime import datetime, date
from collections import defaultdict

loc_offers = "../Data/offers"
loc_transactions = "../Data/transactions"
loc_train = "../Data/trainHistory"
loc_test = "../Data/testHistory"

# will be created
loc_reduced = "../Data/reduced.csv" 
loc_out_train = "../Data/train-0512.vw"
loc_out_test = "../Data/test-0512.vw"

# feature set
loc_agg_txn_product = "../Data/aggregation/agg_txns_by_product"
loc_agg_txn_company = "../Data/aggregation/agg_txns_by_company"
loc_agg_txn_category = "../Data/aggregation/agg_txns_by_category"
loc_agg_txn_brand = "../Data/aggregation/agg_txns_by_brand"
loc_agg_txn_company_category = "../Data/aggregation/agg_txns_by_company_category"
loc_agg_txn_company_brand = "../Data/aggregation/agg_txns_by_company_brand"
loc_agg_txn_category_brand = "../Data/aggregation/agg_txns_by_category_brand"
loc_agg_txn_customer = "../Data/aggregation/agg_txns_by_customer"
loc_agg_txn_chain_product = "../Data/aggregation/agg_txns_by_chain_product"
loc_agg_txn_chain_company = "../Data/aggregation/agg_txns_by_chain_company"
loc_agg_txn_chain_category = "../Data/aggregation/agg_txns_by_chain_category"
loc_agg_txn_chain_brand = "../Data/aggregation/agg_txns_by_chain_brand"
loc_agg_txn_chain_company_category = "../Data/aggregation/agg_txns_by_chain_company_category"
loc_agg_txn_chain_company_brand = "../Data/aggregation/agg_txns_by_chain_company_brand"
loc_agg_txn_chain_category_brand = "../Data/aggregation/agg_txns_by_chain_category_brand"
loc_agg_txn_chain = "../Data/aggregation/agg_txns_by_chain"
loc_agg_txn_company_dept = "../Data/aggregation/agg_txns_by_company_dept"
loc_agg_txn_chain_company_dept = "../Data/aggregation/agg_txns_by_chain_company_dept"
loc_agg_txn_dept_brand = "../Data/aggregation/agg_txns_by_dept_brand"
loc_agg_txn_chain_dept_brand = "../Data/aggregation/agg_txns_by_chain_dept_brand"
loc_agg_txn_customer_dept = "../Data/aggregation/agg_txns_by_customer_dept"
loc_agg_txn_product_dept = "../Data/aggregation/agg_txns_by_product_dept"

def diff_days(s1,s2):
	date_format = "%Y-%m-%d"
	a = datetime.strptime(s1, date_format)
	b = datetime.strptime(s2, date_format)
	delta = b - a
	return delta.days

def generate_features(loc_train, loc_test, loc_transactions, loc_out_train, loc_out_test):
	#keep a dictionary with the offerdata
	offers = {}
	for e, line in enumerate( open(loc_offers) ):
		row = line.strip().split(",")
		offers[ row[0] ] = row

	# load dictionaries of aggreation results
	agg_txn_by_product = {}
	for e, line in enumerate( open(loc_agg_txn_product) ):
		row = line.strip().split(",")
		agg_txn_by_product[','.join([row[0],row[1],row[2]])] = row

	agg_txn_by_company = {}
	for e, line in enumerate( open(loc_agg_txn_company) ):
		row = line.strip().split(",")
		agg_txn_by_company[row[0]] = row

	agg_txn_by_category = {}
	for e, line in enumerate( open(loc_agg_txn_category) ):
		row = line.strip().split(",")
		agg_txn_by_category[row[0]] = row

	agg_txn_by_brand = {}
	for e, line in enumerate( open(loc_agg_txn_brand) ):
		row = line.strip().split(",")
		agg_txn_by_brand[row[0]] = row

	agg_txn_by_company_category = {}
	for e, line in enumerate( open(loc_agg_txn_company_category) ):
		row = line.strip().split(",")
		agg_txn_by_company_category[','.join([row[0],row[1]])] = row	
	
	agg_txn_by_company_brand = {}
	for e, line in enumerate( open(loc_agg_txn_company_brand) ):
		row = line.strip().split(",")
		agg_txn_by_company_brand[','.join([row[0],row[1]])] = row

	agg_txn_by_category_brand = {}
	for e, line in enumerate( open(loc_agg_txn_category_brand) ):
		row = line.strip().split(",")
		agg_txn_by_category_brand[','.join([row[0],row[1]])] = row

	agg_txn_by_customer = {}
	for e, line in enumerate( open(loc_agg_txn_customer) ):
		row = line.strip().split(",")
		agg_txn_by_customer[row[0]] = row

	agg_txn_by_chain_product = {}
	for e, line in enumerate( open(loc_agg_txn_chain_product) ):
		row = line.strip().split(",")
		agg_txn_by_chain_product[','.join([row[0],row[1],row[2],row[3]])] = row

	agg_txn_by_chain_company = {}
	for e, line in enumerate( open(loc_agg_txn_chain_company) ):
		row = line.strip().split(",")
		agg_txn_by_chain_company[','.join([row[0],row[1]])] = row

	agg_txn_by_chain_category = {}
	for e, line in enumerate( open(loc_agg_txn_chain_category) ):
		row = line.strip().split(",")
		agg_txn_by_chain_category[','.join([row[0],row[1]])] = row

	agg_txn_by_chain_brand = {}
	for e, line in enumerate( open(loc_agg_txn_chain_brand) ):
		row = line.strip().split(",")
		agg_txn_by_chain_brand[','.join([row[0],row[1]])] = row

	agg_txn_by_chain_company_category = {}
	for e, line in enumerate( open(loc_agg_txn_chain_company_category) ):
		row = line.strip().split(",")
		agg_txn_by_chain_company_category[','.join([row[0],row[1],row[2]])] = row

	agg_txn_by_chain_company_brand = {}
	for e, line in enumerate( open(loc_agg_txn_chain_company_brand) ):
		row = line.strip().split(",")
		agg_txn_by_chain_company_brand[','.join([row[0],row[1],row[2]])] = row

	agg_txn_by_chain_category_brand = {}
	for e, line in enumerate( open(loc_agg_txn_chain_category_brand) ):
		row = line.strip().split(",")
		agg_txn_by_chain_category_brand[','.join([row[0],row[1],row[2]])] = row

	agg_txn_by_chain = {}
	for e, line in enumerate( open(loc_agg_txn_chain) ):
		row = line.strip().split(",")
		agg_txn_by_chain[row[0]] = row

	agg_txn_by_company_dept = {}
	for e, line in enumerate( open(loc_agg_txn_company_dept) ):
		row = line.strip().split(",")
		agg_txn_by_company_dept[','.join([row[0],row[1]])] = row

	agg_txn_by_chain_company_dept = {}
	for e, line in enumerate( open(loc_agg_txn_chain_company_dept) ):
		row = line.strip().split(",")
		agg_txn_by_chain_company_dept[','.join([row[0],row[1],row[2]])] = row

	agg_txn_by_dept_brand = {}
	for e, line in enumerate( open(loc_agg_txn_dept_brand) ):
		row = line.strip().split(",")
		agg_txn_by_dept_brand[','.join([row[0],row[1]])] = row

	agg_txn_by_chain_dept_brand = {}
	for e, line in enumerate( open(loc_agg_txn_chain_dept_brand) ):
		row = line.strip().split(",")
		agg_txn_by_chain_dept_brand[','.join([row[0],row[1],row[2]])] = row

	agg_txn_by_customer_dept = {}
	for e, line in enumerate( open(loc_agg_txn_customer_dept) ):
		row = line.strip().split(",")
		agg_txn_by_customer_dept[','.join([row[0],row[1]])] = row

	agg_txn_by_product_dept = {}
	for e, line in enumerate( open(loc_agg_txn_product_dept) ):
		row = line.strip().split(",")
		agg_txn_by_product_dept[','.join([row[0],row[1],row[2]])] = row


	#keep two dictionaries with the shopper id's from test and train
	train_ids = {}
	test_ids = {}
	for e, line in enumerate( open(loc_train) ):
		if e > 0:
			row = line.strip().split(",")
			train_ids[row[0]] = row
	num_test = 0
	for e, line in enumerate( open(loc_test) ):
		if e > 0:
			row = line.strip().split(",")
			test_ids[row[0]] = row
			num_test = num_test+1

	print "number of test is " + str(num_test)
	#open two output files
	with open(loc_out_train, "wb") as out_train, open(loc_out_test, "wb") as out_test:
		#iterate through reduced dataset 
		last_id = 0
		features = defaultdict(float)
		num_test = 0;
		for e, line in enumerate( open(loc_transactions) ):
			if e > 0: #skip header
				#poor man's csv reader
				row = line.strip().split(",")
				#write away the features when we get to a new shopper id
				if last_id != row[0] and e != 1:
					
					# update aggregation features
					key = ','.join([offers[history[2]][3],offers[history[2]][1],offers[history[2]][5]])
					features['product_num_of_txn'] = agg_txn_by_product[key][4]
					features['product_num_of_customer'] = agg_txn_by_product[key][3]
					#features['product_average_txn'] = float(agg_txn_by_product[key][4])/float(agg_txn_by_product[key][3])
					#features['product_total_quantity'] = agg_txn_by_product[key][5]

					key = str(offers[history[2]][3])
					features['company_num_of_txn'] = agg_txn_by_company[key][2]
					features['company_num_of_customer'] = agg_txn_by_company[key][1]
					#features['company_average_txn'] = float(agg_txn_by_company[key][2])/float(agg_txn_by_company[key][1])
					#features['company_total_quantity'] = agg_txn_by_company[key][3]

					key = str(offers[history[2]][1])
					features['category_num_of_txn'] = agg_txn_by_category[key][2]
					features['category_num_of_customer'] = agg_txn_by_category[key][1]
					#features['category_average_txn'] = float(agg_txn_by_category[key][2])/float(agg_txn_by_category[key][1])
					#features['category_total_quantity'] = agg_txn_by_category[key][3]

					key = str(offers[history[2]][5])
					features['brand_num_of_txn'] = agg_txn_by_brand[key][2]
					features['brand_num_of_customer'] = agg_txn_by_brand[key][1]
					#features['brand_average_txn'] = float(agg_txn_by_brand[key][2])/float(agg_txn_by_brand[key][1])
					#features['brand_total_quantity'] = agg_txn_by_brand[key][3]

					key = ','.join([offers[history[2]][3],offers[history[2]][1]])
					features['company_category_num_of_txn'] = agg_txn_by_company_category[key][3]
					features['company_category_num_of_customer'] = agg_txn_by_company_category[key][2]										
					#features['company_category_average_txn'] = float(agg_txn_by_company_category[key][3])/float(agg_txn_by_company_category[key][2])
					#features['company_category_total_quantity'] = agg_txn_by_company_category[key][4]

					key = ','.join([offers[history[2]][3],offers[history[2]][5]])
					features['company_brand_num_of_txn'] = agg_txn_by_company_brand[key][3]
					features['company_brand_num_of_customer'] = agg_txn_by_company_brand[key][2]	
					#features['company_brand_average_txn'] = float(agg_txn_by_company_brand[key][3])/float(agg_txn_by_company_brand[key][2])
					#features['company_brand_total_quantity'] = agg_txn_by_company_brand[key][4]

					key = ','.join([offers[history[2]][1],offers[history[2]][5]])
					features['category_brand_num_of_txn'] = agg_txn_by_category_brand[key][3]
					features['category_brand_num_of_customer'] = agg_txn_by_category_brand[key][2]
					#features['category_brand_average_txn'] = float(agg_txn_by_category_brand[key][3])/float(agg_txn_by_category_brand[key][2])
					#features['category_brand_total_quantity'] = agg_txn_by_category_brand[key][4]

					key = last_id
					features['customer_num_of_product'] = agg_txn_by_customer[key][1]	
					features['customer_num_of_txn'] = agg_txn_by_customer[key][2]
					#features['customer_average_txn'] = float(agg_txn_by_customer[key][2])/float(agg_txn_by_customer[key][1])

					#key = ','.join([history[1], offers[history[2]][3],offers[history[2]][1],offers[history[2]][5]])
					#if key in agg_txn_by_chain_product:
					#	features['chain_product_num_of_txn'] = agg_txn_by_chain_product[key][5]
					#	features['chain_product_num_of_customer'] = agg_txn_by_chain_product[key][4]
					#	features['chain_product_average_txn'] = float(agg_txn_by_chain_product[key][5])/float(agg_txn_by_chain_product[key][4])
					#	features['chain_product_average_quantity'] = float(agg_txn_by_chain_product[key][6])/float(agg_txn_by_chain_product[key][4])

					#key = ','.join([history[1],offers[history[2]][3]])
					#if key in agg_txn_by_chain_company:
					#	features['chain_company_num_of_txn'] = agg_txn_by_chain_company[key][3]
					#	features['chain_company_num_of_customer'] = agg_txn_by_chain_company[key][2]
					#	features['chain_company_average_txn'] = float(agg_txn_by_chain_company[key][3])/float(agg_txn_by_chain_company[key][2])
					#	features['chain_company_average_quantity'] = float(agg_txn_by_chain_company[key][4])/float(agg_txn_by_chain_company[key][2])

					#key = ','.join([history[1],offers[history[2]][1]])
					#if key in agg_txn_by_chain_category:
					#	features['chain_category_num_of_txn'] = agg_txn_by_chain_category[key][3]
					#	features['chain_category_num_of_customer'] = agg_txn_by_chain_category[key][2]
					#	features['chain_category_average_txn'] = float(agg_txn_by_chain_category[key][3])/float(agg_txn_by_chain_category[key][2])
					#	features['chain_category_average_quantity'] = float(agg_txn_by_chain_category[key][4])/float(agg_txn_by_chain_category[key][2])

					#key = ','.join([history[1],offers[history[2]][5]])
					#if key in agg_txn_by_chain_brand:
					#	features['chain_brand_num_of_txn'] = agg_txn_by_chain_brand[key][3]
					#	features['chain_brand_num_of_customer'] = agg_txn_by_chain_brand[key][2]
					#	features['chain_brand_average_txn'] = float(agg_txn_by_chain_brand[key][3])/float(agg_txn_by_chain_brand[key][2])
					#	features['chain_brand_average_quantity'] = float(agg_txn_by_chain_brand[key][4])/float(agg_txn_by_chain_brand[key][2])

					#key = ','.join([history[1],offers[history[2]][3],offers[history[2]][1]])
					#if key in agg_txn_by_chain_company_category:
					#	features['chain_company_category_num_of_txn'] = agg_txn_by_chain_company_category[key][4]
					#	features['chain_company_category_num_of_customer'] = agg_txn_by_chain_company_category[key][3]
					#	features['chain_company_category_average_txn'] = float(agg_txn_by_chain_company_category[key][4])/float(agg_txn_by_chain_company_category[key][3])
					#	features['chain_company_category_average_quantity'] = float(agg_txn_by_chain_company_category[key][5])/float(agg_txn_by_chain_company_category[key][3])

					#key = ','.join([history[1],offers[history[2]][3],offers[history[2]][5]])
					#if key in agg_txn_by_chain_company_brand:
					#	features['chain_company_brand_num_of_txn'] = agg_txn_by_chain_company_brand[key][4]
					#	features['chain_company_brand_num_of_customer'] = agg_txn_by_chain_company_brand[key][3]
					#	features['chain_company_brand_average_txn'] = float(agg_txn_by_chain_company_brand[key][4])/float(agg_txn_by_chain_company_brand[key][3])
					#	features['chain_company_brand_average_quantity'] = float(agg_txn_by_chain_company_brand[key][5])/float(agg_txn_by_chain_company_brand[key][3])

					#key = ','.join([history[1],offers[history[2]][1],offers[history[2]][5]])
					#if key in agg_txn_by_chain_category_brand:
					#	features['chain_category_brand_num_of_txn'] = agg_txn_by_chain_category_brand[key][4]
					#	features['chain_category_brand_num_of_customer'] = agg_txn_by_chain_category_brand[key][3]
					#	features['chain_category_brand_average_txn'] = float(agg_txn_by_chain_category_brand[key][4])/float(agg_txn_by_chain_category_brand[key][3])
					#	features['chain_category_brand_average_quantity'] = float(agg_txn_by_chain_category_brand[key][5])/float(agg_txn_by_chain_category_brand[key][3])

					#key = str(history[1])
					#if key in agg_txn_by_chain:
					#	features['chain_num_of_txn'] = agg_txn_by_chain[key][2]
					#	features['chain_num_of_customer'] = agg_txn_by_chain[key][1]
					#	features['chain_average_txn'] = float(agg_txn_by_chain[key][2])/float(agg_txn_by_chain[key][1])
					#	features['chain_average_quantity'] = float(agg_txn_by_chain[key][3])/float(agg_txn_by_chain[key][1])

					#key = ','.join([offers[history[2]][3],history[2]])
					#if key in agg_txn_by_company_dept:
					#	features['company_dept_num_of_txn'] = agg_txn_by_company_dept[key][3]
					#	features['company_dept_num_of_customer'] = agg_txn_by_company_dept[key][2]
					#features['company_dept_average_txn'] = float(agg_txn_by_company_dept[key][3])/float(agg_txn_by_company_dept[key][2])
					#features['company_dept_average_quantity'] = float(agg_txn_by_company_dept[key][4])/float(agg_txn_by_company_dept[key][2])

					#key = ','.join([history[1],offers[history[2]][3],history[2]])
					#if key in agg_txn_by_chain_company_dept:
					#	features['chain_company_dept_num_of_txn'] = agg_txn_by_chain_company_dept[key][4]
					#	features['chain_company_dept_num_of_customer'] = agg_txn_by_chain_company_dept[key][3]
					#features['chain_company_dept_average_txn'] = float(agg_txn_by_chain_company_dept[key][4])/float(agg_txn_by_chain_company_dept[key][3])
					#features['chain_company_dept_average_quantity'] = float(agg_txn_by_chain_company_dept[key][5])/float(agg_txn_by_chain_company_dept[key][3])

					#key = ','.join([history[2],offers[history[2]][5]])
					#if key in agg_txn_by_dept_brand:
					#	features['dept_brand_num_of_txn'] = agg_txn_by_dept_brand[key][3]
					#	features['dept_brand_num_of_customer'] = agg_txn_by_dept_brand[key][2]
					#features['dept_brand_average_txn'] = float(agg_txn_by_dept_brand[key][3])/float(agg_txn_by_dept_brand[key][2])
					#features['dept_brand_average_quantity'] = float(agg_txn_by_dept_brand[key][4])/float(agg_txn_by_dept_brand[key][2])

					#key = ','.join([history[1],history[2],offers[history[2]][5]])
					#if key in agg_txn_by_chain_dept_brand:
					#	features['chain_dept_brand_num_of_txn'] = agg_txn_by_chain_dept_brand[key][4]
					#	features['chain_dept_brand_num_of_customer'] = agg_txn_by_chain_dept_brand[key][3]
					#features['chain_dept_brand_average_txn'] = float(agg_txn_by_chain_dept_brand[key][4])/float(agg_txn_by_chain_dept_brand[key][3])
					#features['chain_dept_brand_average_quantity'] = float(agg_txn_by_chain_dept_brand[key][5])/float(agg_txn_by_chain_dept_brand[key][3])

					product_key = ','.join([offers[history[2]][3],offers[history[2]][1],offers[history[2]][5]])
					dept = agg_txn_by_product_dept[product_key][3]
					key = ','.join([last_id,dept])
					if key in agg_txn_by_customer_dept:
						features['customer_dept_num_of_product'] = agg_txn_by_customer_dept[key][2]
						features['customer_dept_num_of_txn'] = agg_txn_by_customer_dept[key][3]
					#features['chain_dept_brand_average_txn'] = float(agg_txn_by_chain_dept_brand[key][4])/float(agg_txn_by_chain_dept_brand[key][3])
					#features['chain_dept_brand_average_quantity'] = float(agg_txn_by_chain_dept_brand[key][5])/float(agg_txn_by_chain_dept_brand[key][3])



					#generate negative features
					if "has_bought_company" not in features:
						features['never_bought_company'] = 1
					
					if "has_bought_category" not in features:
						features['never_bought_category'] = 1
						
					if "has_bought_brand" not in features:
						features['never_bought_brand'] = 1
						
					if "has_bought_brand" in features and "has_bought_category" in features and "has_bought_company" in features:
						features['has_bought_brand_company_category'] = 1
					
					if "has_bought_brand" in features and "has_bought_category" in features:
						features['has_bought_brand_category'] = 1
					
					if "has_bought_brand" in features and "has_bought_company" in features:
						features['has_bought_brand_company'] = 1
						
					outline = ""
					test = False
					for k, v in features.items():
						
						if k == "label" and v == 0.5:
							#test
							outline = "1 '" + last_id + " |f" + outline
							test = True
						elif k == "label":
							outline = str(v) + " '" + last_id + " |f" + outline
						else:
							outline += " " + k+":"+str(v) 
					outline += "\n"
					if test:
						num_test = num_test + 1
						out_test.write( outline )
						del test_ids[last_id]
					else:
						out_train.write( outline )
					#print "Writing features or storing them in an array"
					#reset features
					features = defaultdict(float)
				#generate features from transaction record
				#check if we have a test sample or train sample
				if row[0] in train_ids or row[0] in test_ids:
					#generate label and history
					if row[0] in train_ids:
						history = train_ids[row[0]]
						if train_ids[row[0]][5] == "t":
							features['label'] = 1
						else:
							features['label'] = 0
					else:
						history = test_ids[row[0]]
						features['label'] = 0.5
						
					#print "label", label 
					#print "trainhistory", train_ids[row[0]]
					#print "transaction", row
					#print "offers", offers[ train_ids[row[0]][2] ]
					#print
					
					features['offer_value'] = offers[ history[2] ][4]
					features['offer_quantity'] = offers[ history[2] ][2]
					offervalue = offers[ history[2] ][4]
					
					features['total_spend'] += float( row[10] )
					
					if offers[ history[2] ][3] == row[4]:
						features['has_bought_company'] += 1.0
						features['has_bought_company_q'] += float( row[9] )
						features['has_bought_company_a'] += float( row[10] )
						
						date_diff_days = diff_days(row[6],history[-1])
						if date_diff_days < 30:
							features['has_bought_company_30'] += 1.0
							features['has_bought_company_q_30'] += float( row[9] )
							features['has_bought_company_a_30'] += float( row[10] )
						if date_diff_days < 60:
							features['has_bought_company_60'] += 1.0
							features['has_bought_company_q_60'] += float( row[9] )
							features['has_bought_company_a_60'] += float( row[10] )
						if date_diff_days < 90:
							features['has_bought_company_90'] += 1.0
							features['has_bought_company_q_90'] += float( row[9] )
							features['has_bought_company_a_90'] += float( row[10] )
						if date_diff_days < 180:
							features['has_bought_company_180'] += 1.0
							features['has_bought_company_q_180'] += float( row[9] )
							features['has_bought_company_a_180'] += float( row[10] )
					
					if offers[ history[2] ][1] == row[3]:
						
						features['has_bought_category'] += 1.0
						features['has_bought_category_q'] += float( row[9] )
						features['has_bought_category_a'] += float( row[10] )
						date_diff_days = diff_days(row[6],history[-1])
						if date_diff_days < 30:
							features['has_bought_category_30'] += 1.0
							features['has_bought_category_q_30'] += float( row[9] )
							features['has_bought_category_a_30'] += float( row[10] )
						if date_diff_days < 60:
							features['has_bought_category_60'] += 1.0
							features['has_bought_category_q_60'] += float( row[9] )
							features['has_bought_category_a_60'] += float( row[10] )
						if date_diff_days < 90:
							features['has_bought_category_90'] += 1.0
							features['has_bought_category_q_90'] += float( row[9] )
							features['has_bought_category_a_90'] += float( row[10] )						
						if date_diff_days < 180:
							features['has_bought_category_180'] += 1.0
							features['has_bought_category_q_180'] += float( row[9] )
							features['has_bought_category_a_180'] += float( row[10] )				
					if offers[ history[2] ][5] == row[5]:
						features['has_bought_brand'] += 1.0
						features['has_bought_brand_q'] += float( row[9] )
						features['has_bought_brand_a'] += float( row[10] )
						date_diff_days = diff_days(row[6],history[-1])
						if date_diff_days < 30:
							features['has_bought_brand_30'] += 1.0
							features['has_bought_brand_q_30'] += float( row[9] )
							features['has_bought_brand_a_30'] += float( row[10] )
						if date_diff_days < 60:
							features['has_bought_brand_60'] += 1.0
							features['has_bought_brand_q_60'] += float( row[9] )
							features['has_bought_brand_a_60'] += float( row[10] )
						if date_diff_days < 90:
							features['has_bought_brand_90'] += 1.0
							features['has_bought_brand_q_90'] += float( row[9] )
							features['has_bought_brand_a_90'] += float( row[10] )						
						if date_diff_days < 180:
							features['has_bought_brand_180'] += 1.0
							features['has_bought_brand_q_180'] += float( row[9] )
							features['has_bought_brand_a_180'] += float( row[10] )	
				last_id = row[0]
				if e % 100000 == 0:
					print e
	
	print 'The number of test instance is ' + str(num_test)

	#fill missing test cases
	if len(test_ids)>0:
		with open("../Data/testMissing", "wb") as out_missing:
			for key, value in test_ids.iteritems():
				out_missing.write(key+",0.5\n")




#generate_features(loc_train, loc_test, loc_transactions, loc_out_train, loc_out_test)


if __name__ == '__main__':
	#reduce_data(loc_offers, loc_transactions, loc_reduced)
	generate_features(loc_train, loc_test, loc_reduced, loc_out_train, loc_out_test)

	
	

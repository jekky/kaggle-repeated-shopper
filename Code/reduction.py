from datetime import datetime, date
from collections import defaultdict


loc_offers = "../Data/offers"
loc_transactions = "../Data/transactions"
loc_train = "../Data/trainHistory"
loc_test = "../Data/testHistory"

###
def reduce_data_by_offer(loc_offers, loc_transactions, loc_reduced):
	start = datetime.now()
	#get all categories and comps on offer in a dict
	offers_cat = {}
	offers_co = {}
	for e, line in enumerate( open(loc_offers) ):
		offers_cat[ line.split(",")[1] ] = 1
		offers_co[ line.split(",")[3] ] = 1
	
	#open output file
	with open(loc_reduced, "wb") as outfile:
		#go through transactions file and reduce
		reduced = 0
		for e, line in enumerate( open(loc_transactions) ):
			if e == 0:
				outfile.write( line ) #print header
			else:
				#only write when if category in offers dict
				if line.split(",")[3] in offers_cat or line.split(",")[4] in offers_co:
					outfile.write( line )
					reduced += 1
			#progress
			if e % 5000000 == 0:
				print e, reduced, datetime.now() - start
	print e, reduced, datetime.now() - start


###
def reduce_data_by_customer(loc_reduced):
	start = datetime.now()
	#get all categories and comps on offer in a dict
	train_cust_ids = {}
	for e, line in enumerate( open(loc_train) ):
		row = line.strip().split(",")
		train_cust_ids[ row[0] ] = 1

	test_cust_ids = {}
	for e, line in enumerate( open(loc_test) ):
		test_cust_ids[ row[0] ] = 1

	#open output file
	with open(loc_reduced, "wb") as outfile:
		#go through transactions file and reduce
		reduced = 0
		for e, line in enumerate( open(loc_transactions) ):
			if e == 0:
				outfile.write( line ) #print header
			else:
				row = line.strip().split(",")
				#only write when if category in offers dict
				if row[0] in train_cust_ids or \
				   row[0] in test_cust_ids:
					outfile.write( line )
					reduced += 1
				else:
					print str(row[0]) + " not in history\n"
			#progress
			if e % 5000000 == 0:
				print e, reduced, datetime.now() - start
	print e, reduced, datetime.now() - start

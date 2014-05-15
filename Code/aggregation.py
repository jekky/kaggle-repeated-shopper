from datetime import datetime, date
from collections import defaultdict

##
##
def aggregate_txns_by_product(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[4], row[3], row[5]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])


			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)


##
##
def aggregate_txns_by_company(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = str(row[4])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)


##
##
def aggregate_txns_by_category(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = str(row[3])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)

##
##
def aggregate_txns_by_brand(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = str(row[5])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)


##
##
def aggregate_txns_by_company_category(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[4], row[3]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])


			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)


##
##
def aggregate_txns_by_company_brand(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[4], row[5]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)

##
##
def aggregate_txns_by_category_brand(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[3], row[5]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)


###
###	
def aggregate_txns_by_customer(loc_transactions, loc_output):
	start = datetime.now()
	agg_result = {}

	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
			product_key = '.'.join([row[4],row[3],row[5]])
		
			key = str(row[0])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if product_key not in product_keys:
					agg_result[key]["num_of_products"] += 1
					product_keys[product_key] = 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				product_keys = {}
				product_keys[product_key] = 1
				agg_result[key]["num_of_products"] = 1.0

		if e % 5000000 == 0:
				print e, datetime.now() - start


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)		


###
###
def aggregate_txns_by_chain_product(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[1], row[4], row[3], row[5]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)

###
###
def aggregate_txns_by_chain_company(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[1], row[4]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)

###
###
def aggregate_txns_by_chain_category(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[1], row[3]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)


###
###
def aggregate_txns_by_chain_brand(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[1], row[5]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)

###
###
def aggregate_txns_by_chain_company_category(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[1], row[4], row[3]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)


###
###
def aggregate_txns_by_chain_company_brand(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[1], row[4], row[5]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)

###
###
def aggregate_txns_by_chain_category_brand(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[1], row[3], row[5]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)


###
###
def aggregate_txns_by_chain(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = str(row[1])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)

###
###
def aggregate_txns_by_company_dept(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[4], row[2]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)

###
###
def aggregate_txns_by_chain_company_dept(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[1], row[4], row[2]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])

			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)

###
###
def aggregate_txns_by_dept_brand(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[2], row[5]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])
			
			last_id = row[0]

	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)


###
###
def aggregate_txns_by_chain_dept_brand(loc_transactions, loc_output):
	agg_result = {}

	last_id = 0
	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
		
			key = ','.join([row[1], row[2], row[5]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if last_id != row[0]:
					agg_result[key]["num_of_customers"] += 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				agg_result[key]["num_of_customers"] = 1.0

			agg_result[key]['total_quantity'] += int(row[9])
			
			last_id = row[0]


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)


###
###	
def aggregate_txns_by_customer_dept(loc_transactions, loc_output):
	start = datetime.now()
	agg_result = {}

	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
			product_key = ','.join([row[4],row[5]])
		
			key = ','.join([row[0], row[2]])
			#print key
			if key in agg_result:
				# num of txn
				agg_result[key]["num_of_txn"] += 1
				
				# num of customers
				if product_key not in product_keys:
					agg_result[key]["num_of_products"] += 1
					product_keys[product_key] = 1

			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["num_of_txn"] = 1.0

				#if last_id != row[0]:
				product_keys = {}
				product_keys[product_key] = 1
				agg_result[key]["num_of_products"] = 1.0

		if e % 5000000 == 0:
				print e, datetime.now() - start


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)		

###
###	
def aggregate_txns_by_product_dept(loc_transactions, loc_output):
	start = datetime.now()
	agg_result = {}

	for e, line in enumerate( open(loc_transactions) ):
		if e > 0: #skip header
			#poor man's csv reader
			row = line.strip().split(",")
			product_key = ','.join([row[4],row[3],row[5]])
		
			key = product_key
			#print key
			if key in agg_result:
				# num of txn
				if agg_result[key]["dept"] != row[2]:
					agg_result[key]["dept"] += str(agg_result[key]["dept"]) + "," + str(row[2])
				
			else:
				agg_result[key] = defaultdict(float)
				agg_result[key]["dept"] = row[2]

		if e % 5000000 == 0:
				print e, datetime.now() - start


	# output agg_result
	with open(loc_output, "wb") as output:
		for key, features in agg_result.items():
			line = key

			for k, v in features.items():
				line += "," + str(v)

			line += "\n"
			output.write(line)		
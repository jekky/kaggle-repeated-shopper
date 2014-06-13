#!/usr/bin/env python

# Split trainHistory into multiple cross validation set

import sys, csv, math

loc_train = "trainHistory.csv"

train_set_prefix="cv_train"
test_set_prefix="cv_test"

def save_to_csv(train_ids, offer_ids, from_range, to_range, file_name, mode):
	print "Generating", file_name
	with open(file_name, mode) as csvfile:
		offer_ids_keys = offer_ids.keys()
		csvout = csv.writer(csvfile, lineterminator='\n')
		if mode != "ab":
			csvout.writerow("id,chain,offer,market,repeattrips,repeater,offerdate".split(",")) 
			
		for j in range(from_range, to_range):
				print "j:", j
				if j < len(offer_ids_keys):					
					offer_key = offer_ids_keys[j]
					ids = offer_ids[offer_key]
					print "ids[0:3]", ids[0:3]
					for id in ids:
						csvout.writerow(train_ids[id])
						
	csvfile.close()					
		
def gen_cv_set(loc_train, num_of_sets):

	train_test_ratio = 0.5
	
	print "num_of_sets: ", num_of_sets, "sets"
	train_ids = {}
	offer_ids = {}
	
	for e, line in enumerate( open(loc_train) ):
		if e > 0:
			row = line.strip('\r\n').split(",")
			train_ids[row[0]] = row  
			
			offer_id = row[2]
			if offer_id in offer_ids:
				offer_ids[offer_id].append(row[0])				
			else:
				offer_ids[offer_id] = [row[0]]
				
	offers_per_set = int(math.ceil(float(len(offer_ids)) / num_of_sets))
	offers_per_train_set = int(offers_per_set * train_test_ratio)
	offers_per_test_set = offers_per_set - offers_per_train_set
		
	total_offer_set = offers_per_set * num_of_sets
	print "len(offer_ids):", len(offer_ids), "offers_per_set:", offers_per_set, "total_offer_set:",total_offer_set
	
	for i in range(num_of_sets):
		#print "Offer range per set", i*offers_per_set, (i+1)*offers_per_set
		#train set
		#if i > 0:
		print "train set from_range", 0, "to_range", i*offers_per_set
		save_to_csv(train_ids, offer_ids, 0, i*offers_per_set, train_set_prefix + str(i) + ".csv", "wb")
			
		print "train set from_range", (i+1)*offers_per_set, "to_range", total_offer_set
		save_to_csv(train_ids, offer_ids, (i+1)*offers_per_set, total_offer_set, train_set_prefix + str(i) + ".csv", "ab")
		
		#test set
		print "test set from_range", i*offers_per_set, "to_range", (i+1)*offers_per_set
		save_to_csv(train_ids, offer_ids, i*offers_per_set, (i+1)*offers_per_set, test_set_prefix + str(i) + ".csv", "wb")
		print "-"	

if __name__ == "__main__":		
	gen_cv_set(loc_train, 5)
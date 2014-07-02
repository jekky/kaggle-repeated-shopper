#!/usr/bin/env python

import numpy as np

loc_vw_train = "../Data/train-0518.vw"

##
#
def read_vw_data(loc_vw_data):
	XList, yList = [], []
	idList = []
	for e, line in enumerate( open(loc_vw_data) ):
		row = line.strip().split("|")
		label = float((row[0].split(" "))[0])
		iid = row[0].split(" ")[1][1:]
		yList.append(label)
		idList.append(iid)
		raw_features = row[1][2:]

		features = list(float(item.split(":")[1]) for item in raw_features.split(" "))
		XList.append(features)

	X = np.array(XList)
	y = np.array(yList)

	return X, y, idList

##
#
def gen_submission(ids, probs, loc_output):
	with open(loc_output, "wb") as output:
		output.write( "id,repeatProbability\n" )
		for e, id in enumerate(ids):
			line = id + "," + str(probs[e]) + "\n"
			output.write(line)

##
#
def prepare_evaluation_data(loc_pred, loc_test):
	preds_dict = {}
	for e, line in enumerate( open(loc_pred) ):
		row = line.strip().split(" ")
		preds_dict[row[1]] = float(row[0])

	preds = []
	labels = []
	for e, line in enumerate( open(loc_test) ):
		if e>0:
			row = line.strip().split(",")
			if row[0] in preds_dict:
				if row[5]=='t':
					labels.append(1)
				else:
					labels.append(0)

				preds.append(preds_dict[row[0]])

	return np.array(labels), np.array(preds)


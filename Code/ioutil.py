import numpy as np

loc_vw_train = "../Data/train-0518.vw"

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

def gen_submission(ids, probs, loc_output):
	with open(loc_output, "wb") as output:
		output.write( "id,repeatProbability\n" )
		for e, id in enumerate(ids):
			line = id + "," + str(probs[e]) + "\n"
			output.write(line)

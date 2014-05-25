#!/usr/bin/env python

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
from ioutil import *

'''
Design: 
* search space: a numpy multidimensional array created by meshgrid
'''

class Classifier:
	clf = None
	optimal_params = []

	def init_classifier(self, params):
		# overrided by subclass
		pass

	def tune(self, space, loc_cv_train, loc_cv_test):
		dims = []
		meshgrid_cmd = 'np.meshgrid('
		for idx in range(0, len(space)):
			dims.append(np.linspace(space[idx][0], space[idx][1], space[idx][2]))
			meshgrid_cmd += 'dims[' + str(idx) + ']'
			if idx<len(space)-1:
				meshgrid_cmd += ','
		meshgrid_cmd += ')'
		print "[Debug] meshgrid cmd : " + meshgrid_cmd + "\n"
		param_space = eval(meshgrid_cmd)

		zip_cmd = 'zip('
		for idx in range(0, len(param_space)):
			zip_cmd += 'param_space[' + str(idx) + '].flatten()'
			if idx<len(param_space)-1:
				zip_cmd += ','
		zip_cmd += ')'

		print "[Debug] zip cmd : " + zip_cmd + "\n"
		param_candidates = eval(zip_cmd)

		best_score = -1.0
		for candidate in param_candidates:
			print "[Info] parameter candidate: " + str(candidate) + "\n"
			self.init_classifier(candidate)
			score = self.cross_validate(loc_cv_train, loc_cv_test)
			if is_better(score, best_score):
				optimal_params = candidate

	#
	def cross_validate(self, loc_cv_train, loc_cv_test):
		ave_score = 0.0
		for cv_train, cv_test in zip(loc_cv_train,loc_cv_test):
			X_train, y_train, cv_train_ids = read_vw_data(cv_train)
			X_test, y_test, cv_test_ids = read_vw_data(cv_test)

			self.clf.fit(X_train, y_train)

			probs = self.clf.predict_proba(X_test)[:,1]
			score = self.eval_classification(y_test, probs)
			print '[Info] AUC Score: ' + str(score)
			ave_score += score

		return ave_score/len(loc_cv_train)

	
	#
	def eval_classification(self, label, preds):
		#override by method
		return 0.0

	#
	def is_better(self, score1, score2):
		return (score1>score2)

class RFClassifier(Classifier):
	criterion = None
	def __init__(self,criterion):
		self.criterion = criterion


	def init_classifier(self, params):
		self.clf = RandomForestClassifier(n_estimators=int(params[0]), \
									 	  min_samples_split=int(params[1]), \
								 	 	  min_samples_leaf=int(params[2]), \
								 	 	  n_jobs=-1, 
								 	 	  criterion=self.criterion);

	#
	def eval_classification(self, label, preds):
		return roc_auc_score(label, preds)

	#
	def is_better(self, score1, score2):
		return score1>score2



def random_forest_classification(X, y, params):

	clf = RandomForestClassifier(n_estimators=1000, min_samples_split=10, \
								 min_samples_leaf=10, n_jobs=-1, criterion='gini');
	clf.fit(X,y)

	return clf

def extra_tree_classification(X, y, params):
	clf = ExtraTreesClassifier(n_estimators=1000, min_samples_split=10, \
							   min_samples_leaf=10, n_jobs=-1, criterion='entropy');
	clf.fit(X,y)

	return clf

def gradient_boosting_classification(X, y, params):
	clf = GradientBoostingClassifier(learning_rate=0.05, subsample=0.5, \
										max_depth=6, n_estimators=50);
	clf.fit(X,y)

	return clf
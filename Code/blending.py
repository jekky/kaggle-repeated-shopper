#!/usr/bin/env python

import numpy as np
from file_path import *
from ioutil import *

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

clfs = [
	RandomForestClassifier(n_estimators=1000, min_samples_split=10, \
							min_samples_leaf=10, n_jobs=-1, criterion='gini'),
	RandomForestClassifier(n_estimators=1000, min_samples_split=10, \
							min_samples_leaf=10, n_jobs=-1, criterion='entropy'),
	ExtraTreesClassifier(n_estimators=1000, min_samples_split=10, \
							   min_samples_leaf=10, n_jobs=-1, criterion='gini'),
	ExtraTreesClassifier(n_estimators=1000, min_samples_split=10, \
							   min_samples_leaf=10, n_jobs=-1, criterion='entropy'),
	GradientBoostingClassifier(learning_rate=0.05, subsample=0.5, \
								max_depth=6, n_estimators=100)];

def blending(clfs, loc_train, loc_test, loc_cv_train, loc_cv_test):
	X, y, all_train_ids = read_vw_data(loc_train)
	X_test, y_test, all_test_ids = read_vw_data(loc_test)

	blend_train = np.zeros([X.shape[0], len(clfs)])
	blend_test = np.zeros([X_test.shape[0], len(clfs)])

	for j, clf in enumerate(clfs):
		print j, clf

		blend_test_j = np.zeros([X_test.shape[0], len(loc_cv_train)])
		for idx, (train, test) in enumerate(zip(loc_cv_train, loc_cv_test)):
			X_train, y_train, train_ids = read_vw_data(train)
			X_valid, y_valid, valid_ids = read_vw_data(test)

			clf.fit(X_train, y_train)
			y_valid_preds = clf.predict_proba(X_valid)[:,1]

			valid_idx = [all_train_ids.index(id) for id in valid_ids]
			blend_train[valid_idx, j] = y_valid_preds
			blend_test_j[:, idx] = clf.predict_proba(X_test)[:,1]

		blend_test[:,j] = blend_test_j.mean(1)

	print 
	print "Blending ..."

	clf = LogisticRegression()
	clf.fit(blend_train, y)
	y_preds = clf.predict_proba(blend_test)[:,1]

	print "Linear stretch of predictions to [0,1]"
	y_preds = (y_preds - y_preds.min()) / (y_preds.max() - y_preds.min())

	print "Generating submission ..."
	gen_submission(all_test_ids, y_preds, loc_blending_submission)

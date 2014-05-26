#!/usr/bin/env python

import numpy as np
from file_path import *
from ioutil import *

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
								max_depth=6, n_estimators=100);
]

def blending(X, y, X_test, clfs, loc_cv_train, loc_cv_test):
	blend_train = np.zeros(X.shape[0], len(clfs))
	blend_test = np.zeros(X_test.shape[0], len(clfs))

	for j, clf in enumerate(clfs):
		print j, clf

		blend_test_j = np.zeros(X_test.shape[0], len(loc_cv_train))
		for train, test in zip(loc_cv_train, loc_cv_test):
			X_train, y_train, train_ids = read_vw_data(train)
			X_valid, y_valid, valid_ids = read_vw_data(test)

			clf.fit(X_train, y_train)
			y_valid_preds = clf.predict_proba(X_valid)[:,1]

			blend_train[valid_ids, j] = y_valid_preds
			blend_test_j = clf.predict_proba(X_test)[:,1]

		blend_test[:,j] = blend_test_j.mean(1)

	print 
	print "Blending..."

	clf = LogisticRegression()
    clf.fit(blend_train, y)
    y_preds = clf.predict_proba(blend_test)[:,1]

    print "Linear stretch of predictions to [0,1]"
    y_preds = (y_preds - y_preds.min()) / (y_preds.max() - y_preds.min())

    

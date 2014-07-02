#!/usr/bin/env python

import numpy as np
from sklearn.metrics import roc_auc_score

def average_auc(y, preds):
	auc = 0.0

	for 
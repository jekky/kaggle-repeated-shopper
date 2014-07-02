# input
loc_offers = "../Data/offers"
loc_transactions = "../Data/transactions"
loc_train = "../Data/trainHistory"
loc_test = "../Data/testHistory"


## train, test, valid feature files
# train and test feature file
loc_train_vw = "../Data/train.vw"
loc_test_vw = "../Data/test.vw"

# cross validation
loc_cv_train_raw = ["../Data/cv/cv_train0.csv",
				"../Data/cv/cv_train1.csv",
				"../Data/cv/cv_train2.csv",
				"../Data/cv/cv_train3.csv",
				"../Data/cv/cv_train4.csv"]

loc_cv_test_raw = ["../Data/cv/cv_test0.csv",
				"../Data/cv/cv_test1.csv",
				"../Data/cv/cv_test2.csv",
				"../Data/cv/cv_test3.csv",
				"../Data/cv/cv_test4.csv"]

loc_cv_train_vw = ["../Data/cv/cv_train0.vw",
				"../Data/cv/cv_train1.vw",
				"../Data/cv/cv_train2.vw",
				"../Data/cv/cv_train3.vw",
				"../Data/cv/cv_train4.vw"]

loc_cv_test_vw = ["../Data/cv/cv_test0.vw",
			   "../Data/cv/cv_test1.vw",
			   "../Data/cv/cv_test2.vw",
			   "../Data/cv/cv_test3.vw",
			   "../Data/cv/cv_test4.vw"]

loc_cv_test_preds = ["../Data/cv/cv_test0.pred.txt",
					"../Data/cv/cv_test1.pred.txt",
					"../Data/cv/cv_test2.pred.txt",
					"../Data/cv/cv_test3.pred.txt",
					"../Data/cv/cv_test4.pred.txt"]


# will be created
loc_reduced = "../Data/reduced.csv" 
loc_out_train = "../Data/train-valid-0618.vw"
loc_out_test = "../Data/test-valid-0618.vw"

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
loc_agg_txn_customer_dept_company_brand = "../Data/aggregation/agg_txns_by_customer_dept_company_brand"
loc_agg_dept_category_company_brand = "../Data/aggregation/agg_dept_by_category_company_brand"


# output submissions
loc_blending_submission = "../Submission/blending.txt"
loc_rf_submission = "../Submission/rf.txt"
loc_et_submission = "../Submission/et.txt"
loc_gbm_submission = "../Submission/gbm.txt"
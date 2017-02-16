# -*- coding: utf-8 -*-
#import dataiku
import pandas as pd, numpy as np
#from dataiku import pandasutils as pdu

def get_min_max(): 
	# Recipe inputs
	by_IDRestaurant_prep = dataiku.Dataset("by_IDRestaurant_prep")
	by_IDRestaurant_prep_df = by_IDRestaurant_prep.get_dataframe()

	t = dataiku.Dataset("by_IDRestaurant_prep")
	t_df = t.get_dataframe()
	t_df["MAXprediction_1_sum"]=t_df["prediction_1_sum"].max()
	t_df["MINprediction_1_sum"]=t_df["prediction_1_sum"].min()
	t_df["MAXfollowers"]=t_df["RFollowers"].max()
	t_df["MINfollowers"]=t_df["RFollowers"].min()

	# Recipe outputs
	by_IDRestaurant_prep_coded = dataiku.Dataset("by_IDRestaurant_prep_coded")
	by_IDRestaurant_prep_coded.write_with_schema(t_df)

if __name__ == "__main__":
	det_min_max() 

import csv
import random
import os
import argparse
from os import listdir
from os.path import isfile, join
from test_gen_strategy import TestGenStrategy
import precentage_strat
import double_cross_feature_strat

###
# strategies
# add new strategy here 
# 
prec_strat = TestGenStrategy(precentage_strat.createTestSetPrecentage)
dcf_strat = TestGenStrategy(double_cross_feature_strat.createTestSetDoubleCrossFeature)

parser = argparse.ArgumentParser(description='Generate anomallies in Normall data sets.')
parser.add_argument("--precent", help="precentage mode",action='store_true')
parser.add_argument("--dcf",help="double cross feature mode",action='store_true')
parser.add_argument("--srcpath",help="increase output verbosity")
parser.add_argument("--destpath",help="increase output verbosity")
parser.add_argument("--mfs",type=int,help="minimal_substitute_features")
parser.add_argument("--testSize",type=int,help="test set size in precentage from each trainig set")
parser.add_argument("--csvdelimiter",help="csv delimiter")
args = parser.parse_args()

if args.srcpath:
	srcpath = args.srcpath
else:
	srcpath = "data_sets\\"
if args.destpath:
	destpath = args.destpath
else:
	destpath = "res_sets\\"
if args.csvdelimiter:
	delim = args.csvdelimiter
else:
	delim = ","
if args.testSize:
	test_size = args.testSize
else:
	test_size = 20

if args.dcf:
	if args.mfs:
		mfs = args.mfs
	else:
		mfs = 3
	prec_strat.generate(srcpath,destpath,test_size,delim,minimal_substitute_features=mfs)

elif args.precent:
	if args.mfs:
		mfs = args.mfs
	else:
		mfs = 3	
	prec_strat.generate(srcpath,destpath,test_size,delim)

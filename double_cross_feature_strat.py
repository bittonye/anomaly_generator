import csv
import random
import os
import copy
from os import listdir
from os.path import isfile, join
from collections import OrderedDict
from test_gen_strategy import TestGenStrategy

def createTestSetDoubleCrossFeature(self,srcpath="data_sets\\",destpath="res_sets\\",test_set_size=20,delim=",",**kwargs) :
	path = srcpath
	res_path = destpath
	if "minimal_substitute_features" not in kwargs:
		minimal_substitute_features = 3
	else:
		minimal_substitute_features = kwargs["minimal_substitute_features"]
	files_dict = {}
	user_delimiter = delim

	csv_files = [ f for f in listdir(path) if (isfile(join(path,f)) and (f.endswith('.csv'))) ]
	if not os.path.exists(destpath):
		os.makedirs(destpath)

	for csv_file_name in csv_files:
		files_dict[csv_file_name] = []
		test_rows = 0
		train_rows = 0
		features = OrderedDict()
		with open(path+csv_file_name, 'r') as f:
			first_line = f.readline()
			for item in first_line.split(user_delimiter):
				item = item.strip()
				features[item] = 0
			features["class"] = 0
		with open(path+csv_file_name) as csvfile:
			reader = csv.DictReader(csvfile)
			row_count = sum(1 for row in reader)
			test_rows = (test_set_size*row_count)/100
			train_rows = row_count - test_rows
			test_rows_chosen = []
			for i in range(0,test_rows+1):
				test_rows_chosen.append(random.randint(1, row_count))
			index = 1
			csvfile.seek(0)
			csvfile.next()
			train_rows_list = []
			for row in reader:
				if index == 1:
					index = index + 1
					continue
				if index in test_rows_chosen:
					row["class"] = "good"
					files_dict[csv_file_name].append(row)
				else:
					train_rows_list.append(row)
				index = index + 1
			with open(res_path+csv_file_name+".training", 'w') as writecsvfile:
				writer = csv.DictWriter(writecsvfile, delimiter=',', lineterminator='\n', fieldnames=features)
				writer.writeheader()
				writer.writerows(train_rows_list)


	for csv_file in files_dict:
		tmp_list = copy.deepcopy(files_dict[csv_file])
		all_files = files_dict.keys()
		random.shuffle(all_files)
		chosen_fetures_num = random.randint(len(features)/minimal_substitute_features, len(features))
		feature_samples = random.sample(features,chosen_fetures_num)
		for other_file in all_files:
			if csv_file == other_file:
				continue
			for row1, row2 in zip(files_dict[csv_file],files_dict[other_file]):
				row2_sample_num = random.randint(1, len(feature_samples))
				row2_samples = random.sample(feature_samples,row2_sample_num)
				for sample in row2_samples:
					row1[sample] = row2[sample]
				row1["class"] = "bad"
		with open(res_path + csv_file + '.test', 'w') as writecsvfile:
				writer = csv.DictWriter(writecsvfile, delimiter=',', lineterminator='\n', fieldnames=features)
				writer.writeheader()
				writer.writerows(files_dict[csv_file]+tmp_list)

import csv
import random
import os
from os import listdir
from os.path import isfile, join
from collections import OrderedDict

path = 'data_sets\\' #"C:\\Users\\YONI\\Documents\\anomally_detector\\data_sets\\example\\"
directory = 'res_sets'
res_path = directory+'\\'
test_set_size = 20
user_delimiter = ','

csv_files = [ f for f in listdir(path) if (isfile(join(path,f)) and (f.endswith('.csv'))) ]
if not os.path.exists(directory):
	os.makedirs(directory)

test_rows_list = []

for csv_file_name in csv_files:
	test_rows = 0
	train_rows = 0
	features = OrderedDict()
	with open(path+csv_file_name, 'r') as f:
		first_line = f.readline()
		for item in first_line.split(user_delimiter):
			item = item.strip()
			features[item] = 0
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
				test_rows_list.append(row)
			else:
				train_rows_list.append(row)
			index = index + 1
		with open(res_path+csv_file_name+".training", 'w') as writecsvfile:
			writer = csv.DictWriter(writecsvfile, delimiter=',', lineterminator='\n', fieldnames=features)
			writer.writeheader()
			writer.writerows(train_rows_list)


with open(res_path+'all_data_sets.test.csv', 'w') as writecsvfile:
			writer = csv.DictWriter(writecsvfile, delimiter=',', lineterminator='\n', fieldnames=features)
			writer.writeheader()
			writer.writerows(test_rows_list)

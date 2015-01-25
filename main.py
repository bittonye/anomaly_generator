import csv
import os
from os import listdir
from os.path import isfile, join

path = 'data_sets\\' #"C:\\Users\\YONI\\Documents\\anomally_detector\\data_sets\\example\\"
directory = 'res_sets'
res_path = directory+'\\'
test_set_size = 20

csv_files = [ f for f in listdir(path) if (isfile(join(path,f)) and (f.endswith('.csv'))) ]
if not os.path.exists(directory):
	os.makedirs(directory)

for csv_file_name in csv_files:
	test_rows = 0
	train_rows = 0
	with open(path+csv_file_name) as csvfile:
		reader = csv.DictReader(csvfile)
		row_count = sum(1 for row in reader)
		test_rows = (test_set_size*row_count)/100
		train_rows = row_count - test_rows
		index = 1
		csvfile.seek(0)
		csvfile.next()
		train_rows_list = []
		test_rows_list  = []
		features = []
		for row in reader:
			if index == 1:
				features = list(row.keys())
			if index >= train_rows:
				test_rows_list.append(row)
			else:
				train_rows_list.append(row)
			index = index + 1
		with open(res_path+csv_file_name+".test", 'w') as writecsvfile:
			writer = csv.DictWriter(writecsvfile, delimiter=',', lineterminator='\n', fieldnames=features)
			writer.writeheader()
			writer.writerows(test_rows_list)
		with open(res_path+csv_file_name+".training", 'w') as writecsvfile:
			writer = csv.DictWriter(writecsvfile, delimiter=',', lineterminator='\n', fieldnames=features)
			writer.writeheader()
			writer.writerows(train_rows_list)



import csv
import random
import os
from os import listdir
from os.path import isfile, join


path = 'data_sets\\' #"C:\\Users\\YONI\\Documents\\anomally_detector\\data_sets\\example\\"
directory = 'res_sets'
res_path = directory+'\\'
test_set_size = 20
files_dict = {}

csv_files = [ f for f in listdir(path) if (isfile(join(path,f)) and (f.endswith('.csv'))) ]
if not os.path.exists(directory):
	os.makedirs(directory)

for csv_file_name in csv_files:
	files_dict[csv_file_name] = []
	test_rows = 0
	train_rows = 0
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
		features = []
		for row in reader:
			if index == 1:
				features = list(row.keys())
			if index in test_rows_chosen:
				files_dict[csv_file_name].append(row)
			else:
				train_rows_list.append(row)
			index = index + 1
		with open(res_path+csv_file_name+".training", 'w') as writecsvfile:
			writer = csv.DictWriter(writecsvfile, delimiter=',', lineterminator='\n', fieldnames=features)
			writer.writeheader()
			writer.writerows(train_rows_list)

for csv_file in files_dict:
	for other_file in files_dict:
		if csv_file == other_file:
			continue
		for row1, row2 in zip(files_dict[csv_file],files_dict[other_file]):
			chosen_fetures_num = random.randint(1, len(row2.keys()))
			row2_samples = random.sample(row2.keys(),chosen_fetures_num)
			for sample in row2_samples:
				row1[sample] = row2[sample]
	with open(res_path + csv_file + '.test', 'w') as writecsvfile:
			writer = csv.DictWriter(writecsvfile, delimiter=',', lineterminator='\n', fieldnames=features)
			writer.writeheader()
			writer.writerows(files_dict[csv_file])

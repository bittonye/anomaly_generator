import csv
import os

from collections import OrderedDict
path = ""
csv_file_name = "Train.csv"
filter_feature_name = "UserID"
directory = "data_sets\\"
user_delimiter = ','
if not os.path.exists(directory):
	os.makedirs(directory)

users = {}
features = OrderedDict()
with open(csv_file_name, 'r') as f:
	first_line = f.readline()
	for item in first_line.split(user_delimiter):
		item = item.strip()
		features[item] = 0


with open(csv_file_name) as csvfile:
		reader = csv.DictReader(csvfile)
		index = 1
		train_rows_list = []
		for row in reader:
			if index == 1:
				index = index + 1
				continue
			if row[filter_feature_name] not in users.keys():
				users[row[filter_feature_name]] = [row]
			else:
				users[row[filter_feature_name]].append(row)
			index = index + 1

for user in users.keys():
	with open(directory+user+'.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=features)
		writer.writeheader()
		for row in users[user]:
			featDict = OrderedDict()
			for feat in features:
				featDict[feat] = row[feat]
			writer.writerow(featDict)
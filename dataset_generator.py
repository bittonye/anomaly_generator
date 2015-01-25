import csv

# execfile("C:\\Users\\YONI\\Documents\\Projects\\degree\\attack detection methods\\anomaly_generator\\dataset_generator.py")
ROW_NUM = 10

path = "C:\\Users\\YONI\\Documents\\anomally_detector\\data_sets\\example\\"

users_num = 100
features_num = 20

directory = "data_sets\\"

if not os.path.exists(directory):
	os.makedirs(directory)

users = []
features = []

for i in range(0,users_num):
	users.append('user'+str(i))

for i in range(0,features_num):
	features.append('feature'+str(i))

for user in users:
	with open("data_sets\\"+user+'.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=features)
		writer.writeheader()
		for i in range(1,ROW_NUM):
			featDic = {}
			for feature in features:
				featDic[feature] = user + '_' + feature + '_' + str(i)
			writer.writerow(featDic)
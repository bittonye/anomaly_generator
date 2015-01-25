import csv

# execfile("C:\\Users\\YONI\\Documents\\Projects\\degree\\attack detection methods\\anomaly_generator\\dataset_generator.py")
ROW_NUM = 10

path = "C:\\Users\\YONI\\Documents\\anomally_detector\\data_sets\\example\\"

users = ['user1','user2','user3','user4','user5']

features = ['feature1','feature2','feature3','feature4','feature5']

for user in users:
	with open(path+user+'.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=features)
		writer.writeheader()
		for i in range(1,ROW_NUM):
			featDic = {}
			for feature in features:
				featDic[feature] = user + '_' + feature + '_' + str(i)
			writer.writerow(featDic)
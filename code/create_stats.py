import csv

def main():
	
	column_unique_elements = [ 'Bayview','Bernal', 'Castro', 'China','Crocker','Diamond','Downtown',
							'Excel','Finan','GGPark','Haight','InRich','InSun','Lakeshore','Marina',
							'Mission','MissBay','Nob','Noe','NorthB','OceanV','OutRich','OutMiss',
							'OutSun', 'PacHts', 'Parkside', 'Potrero','Presid','PresidHt','Russian',
							'Seacliff', 'SOMA', 'TIYBI', 'Twin' ,'Visit','WestTP','WestAdd' ]

	#year = [str(2001+i) for i in range(15)]
	year = ['2001']
	print len(column_unique_elements)
	for one_year in year:

		print one_year
		fp = open('../data/Data_'+one_year+'.csv')
		reader = csv.reader(fp)

		data_dict = {}
		for one in column_unique_elements:
			data_dict[one] = 0

		
		i = 0
		for row in reader:
			if i:
				data_dict[row[-3]] += 1
			i += 1

		print data_dict
		'''
		data_list = []
		data_list_2 = []
		i = 0
		for row in reader:
			if i:
				data_list.append(row[5])
				data_list_2.append(row[6])
			i+=1

	print max(data_list), min(data_list)
	print max(data_list_2), min(data_list_2)
	'''
if __name__ == '__main__':
	main()

import re
import pickle
import csv
from itertools import compress

def get_new_row(re_index_dict, unique_parameter_names, unique_value_list):

    append_list = []
    for one in ['n_*','z_*','lu_yr_*']:
        ind_list = re_index_dict[one]
        par_names = [unique_parameter_names[i] for i in ind_list]
        unique_values = [int(unique_value_list[i]) for i in ind_list]

        string = list(compress(par_names, unique_values))
        if len(string):
            write_string = string[0]
            if one=='lu_yr_*':
                append_list.append(write_string[6:])
            else:
                append_list.append(write_string[2:])
        else:
            append_list.append('NULL')
        

        ind_list.sort(reverse=True)
        for i in ind_list:
            del unique_value_list[i]

    unique_value_list.extend(append_list)
    return unique_value_list

def main():
    
    with open ('parameter_boolean', 'rb') as fp:
        parameter_boolean = pickle.load(fp)

    arr = []
    par = []
    for parameter, boolean in parameter_boolean:
        arr.append(boolean)
        par.append(parameter)

    re_index_dict = {'lu_yr_*':[], 'z_*':[], 'n_*':[]}
    unique_parameter_names = list(compress(par, arr))
    new_unique_parameter_names = list(compress(par, arr))

    for one_pattern, ind_list in re_index_dict.items():
        found = filter(re.compile(one_pattern).match, unique_parameter_names)
        if len(found):
            for one_found in found:
                ind_list.append(unique_parameter_names.index(one_found))
                new_unique_parameter_names.remove(one_found)
        re_index_dict[one_pattern] = ind_list

    additional = ['Neighborhood', 'Zoning', 'LandUse']
    new_unique_parameter_names.extend(additional)
    common_arr = [not i for i in arr]
    year = [str(2001+i) for i in range(15)]
    #year = ['temp']

    out_file = csv.writer(open('../data/Common.csv','w+'))
    out_file.writerow(list(compress(par, common_arr)))

    for one_year in year:

        print one_year
        fp = open('../data/'+one_year+'.csv')
        reader = csv.reader(fp)

        data_array = []
        for row in reader:
            data_array.append(row)
        
        parameter = data_array[0]
        data_array = data_array[1:]
        fp.close() 
    
        #Writing common data
        out_file.writerow(list(compress(data_array[0], common_arr)))

        #Writing re_index_dict elements data
        out_file_1 = csv.writer(open('../data/Data_'+one_year+'.csv','w+'))
        out_file_1.writerow(new_unique_parameter_names) 

        for one_row in data_array:
            unique_values_list = list(compress(one_row, arr))
            out_file_1.writerow(get_new_row(re_index_dict, unique_parameter_names, unique_values_list))
        
if __name__ == "__main__":
    main()

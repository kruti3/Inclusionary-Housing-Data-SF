import re
import pickle

pattern_datatype = { 'lu_yr_.*':True, 'z_.*':True,'MapBlkLot_.*':True,'n_*':True, 'LandUse_AsGiven':True,
                            'Zoning_AsGiven': True, 'ParkingMinReq': True, 'Area': True, 'Bldg_SqFt_Use': True,
                            'Env_1000_Dens':True, 'SHistoric1': True, 'DevPotential_Dens': True}

with open('../data/parameters_list.txt') as fp:
    content = fp.readlines()

parameter_list = [one.strip() for one in content]
parameter_boolean = []
for i in range(len(parameter_list)):
    parameter_boolean.append((parameter_list[i],False))

count = 0
ind_list = set()
global_list = set([i for i in range(len(parameter_list))])

for one_pattern, boolean in pattern_datatype.items():
    found = filter(re.compile(one_pattern).match, parameter_list)
    if len(found):
        for one_found in found:
            ind = parameter_list.index(one_found)
            parameter_boolean[ind] = (one_found,boolean)
            count += 1
            ind_list.add(ind)


with open('parameter_boolean', 'wb') as fp:
    pickle.dump(parameter_boolean, fp)
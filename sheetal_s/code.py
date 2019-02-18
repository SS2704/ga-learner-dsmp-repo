# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path,delimiter=",",skip_header=1)
print(data.shape)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_record=np.array(new_record,dtype='float')
print(new_record.shape)
census = np.concatenate((data,new_record), axis=0)
print(census)
#Code starts here



# --------------
#Code starts here
age = census[:,0]
#print(age)

max_age = np.amax(age)
print(max_age)

min_age = np.amin(age)
print(min_age)

age_mean = np.mean(age)
print(min_age)

age_std = np.std(age)
print(age_std)


# --------------
#Code starts here
#race = np.array(census, dtype='int')
#print(type(census[:,2]))
census[:,2].astype('int')
#print(type(census[:,2]))
race_0,race_1,race_2,race_3,race_4 = census[census[:,2]==0.], census[census[:,2]==1.], census[census[:,2]==2.], census[census[:,2]==3.], census[census[:,2]==4.]
#print(race_0)
#print('='*20)
#print(race_1)
#print('='*20)
#print(race_2)
#print('='*20)
#print(race_3)
#print('='*20)
#print(race_4)
#print('='*20)

len_0, len_1, len_2, len_3, len_4 = len(race_0),len(race_1),len(race_2),len(race_3),len(race_4)
#print(len_0)
#print(len_1)
#print(len_2)
#print(len_3)
#print(len_4)

len_array = np.array([len_0, len_1, len_2, len_3, len_4 ])
print((len_array))
minority_race = [i for i in range(len(len_array)) if np.amin(len_array) == len_array[i]]
minority_race = minority_race[0]
print(minority_race)


# --------------
#Code starts here

senior_citizens = census[census[:,0]>60]
#print(senior_citizens)
working_hours_sum = np.sum(senior_citizens[:,6], axis=0)
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here

high = census[census[:,1]>10]
print(high)

low = census[census[:,1]<=10]
print(low)

avg_pay_high = round(np.mean(high[:,7]),2)
print(avg_pay_high)


avg_pay_low = round(np.mean(low[:,7]),2)
print(avg_pay_low)



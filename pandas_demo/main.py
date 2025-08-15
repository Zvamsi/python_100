# # # with open('weather-data.csv') as file:
# # #     data=file.readlines()
# # #     for d in data:
# # #         d=d.strip('\n')
# # #         print(d)
# #
# # # import csv
# # #
# # # with open('weather-data.csv') as file:
# # #     data=csv.reader(file)
# # #     temp=[]
# # #     for d in data:
# # #         if d[1]!='temp':
# # #             temp.append(int(d[1]))
# # #     print(temp)
# # #     for d in data:
# # #         print(d)
# # #     print(data)
# #
import pandas
#
read=pandas.read_csv('weather-data.csv')
print(type(read['temp']))
print(read['temp'])

data_dict=read.to_dict()
print(data_dict)
# # #
# # # data_list=read['temp'].to_list()
# # # print(data_list)
# # #
# # # print(read['temp'].median()
# # # print(read['temp'].max())
# #
# #
# # # Get the data in columns
# # # print(read['condition'])
# # # print(read.condition)
# #
# #
# # #Get data from rows
# # # print(read[read.day=='Monday'])
# # # print(read[read.temp==max(read['temp'])])
# #
# # # day=read[read.day=='Monday']['temp'].to_list()
# # # # celsius=day*32
# # # for d in day:
# # #     print((d-30)/2)
# #
# monday=read[read.day=='Monday']
# monday_temp=(read.temp[0] *9/5)+32
# print(monday_temp)
# print(monday_temp)
# #
# # #Create dataframe from scratch
# # data_dict={
# #     'students':['vamshi','rahul','Gandhi'],
# #     'scores':[10,20,30]
# # }
# # datas=pandas.DataFrame(data_dict)
# # datas.to_csv('is_it.csv')
# #
# # data=[1,2,3,4,5,6]
# # pandas.Series(data).to_csv('first.csv')
#
#
# # import pandas
#
#
# # data=pandas.read_csv('2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
# # fur_data=data['Primary Fur Color'].to_list()
# # gray=0
# # red=0
# # black=0
# # null_one=0
# # for s in fur_data:
# #     if s=='Gray':
# #         gray+=1
# #     elif s=='Cinnamon':
# #         red+=1
# #     elif s=='Black':
# #         black+=1
# #     else:
# #         null_one+=1
# # dict_squirrels={
# #     "Color":['Grey','Red','Black','Remaining'],
# #     "Count":[gray,red,black,null_one]
# # }
#
# # gray_squirrels=len(data[data['Primary Fur Color']=='Gray'])
# # print(gray_squirrels)
# # red_squirrels=len(data[data['Primary Fur Color']=='Cinnamon'])
# # print(red_squirrels)
# # black_squirrels=len(data[data['Primary Fur Color']=='Black'])
# # print(black_squirrels)
#
# # final_data=pandas.DataFrame(dict_squirrels)
# # final_data.to_csv('squirrel_count.csv')

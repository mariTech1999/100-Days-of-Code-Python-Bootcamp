import csv
import exemplos
from exemplos import Series

# with open("weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     tempetures= []
#     for row in data:
#         if row[1] != "temp":
#             tempetures.append(int(row[1]))
#
#     print(tempetures)

# data = pandas.read_csv('weather_data.csv')
# #
# # temp_list = data['temp'].to_list()
# # print(temp_list)
# # print(data[data['temp'] == data['temp'].max()])
#
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("data.csv")

import exemplos

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])



data_dict ={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count,cinnamon_count,black_count ]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
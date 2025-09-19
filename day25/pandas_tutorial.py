# import csv

# with open("weather_data.csv","r") as file:
#     data= csv.reader(file)
#     temperatures=[]
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
import pandas

data=pandas.read_csv("weather_data.csv")
# # print(type(data)) #data frames
# # print(type(data["temp"]))#series
# data_dict= data.to_dict()
# # print(data_dict)

# temp_list= data["temp"].to_list()
# # print(temp_list)

# # print(data["temp"].mean())
# # print(data["temp"].max())# data is a frame but data["temp"] is a series

# #Get Data in columns 
# # print(data["condition"])
# # print(data.condition)   same two things

#Get Data in Row
# print(data[data.day=="Monday"])
#Getting the max temp row    
# print(data[data.temp ==data["temp"].max()])

# monday=data[data.day=="Monday"]
# # print(monday.condition)
# monday_temp= monday.temp[0]
# monday_temp_F=monday_temp * 9/5 +32
# print(monday_temp_F)

#Create a dataframe from scratch
data_dict= {
    "students":["Amy","James","Angela"],
    "scores": [76,56,65]
}
new_data=pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
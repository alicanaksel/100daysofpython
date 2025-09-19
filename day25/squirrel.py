import pandas

data= pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#finding the right data
grey_squirrels= data[data["Primary Fur Color"] =="Gray"]
grey_squirrels_count=len(data[data["Primary Fur Color"] =="Gray"])
red_squirrels_count=len(data[data["Primary Fur Color"] =="Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"] =="Black"])
print(grey_squirrels_count, red_squirrels_count, black_squirrels_count)
# creating dict to print into csv
data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}
#printing dict to csv
df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
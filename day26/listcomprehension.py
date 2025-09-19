numbers= [1,2,3]
# new_list=[]
# for n in numbers:
#     add_1=n +1
#     new_list.append(add_1)
# instead of this much code we can do it with list comprehrension
#     new item  item    list
new_list=[n+1 for n in numbers]

name="Alican"
letters_list=[letter for letter in name]
range_list= [num*2 for num in range(1,5)]

#conditional list comprehension
# new_list= [new_item for item in list if test]
names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

short_names=[name for name in names if len(name)<=4]
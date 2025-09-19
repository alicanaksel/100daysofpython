with open("file1.txt", "r") as f1:
    data1 = [int(line.strip()) for line in f1]

with open("file2.txt", "r") as f2:
    data2 = {int(line.strip()) for line in f2}  

result = [num for num in data1 if num in data2]

print(result)

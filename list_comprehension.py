with open('file1.txt') as file1:
    data=list(file1)
    cleaned_data1=[int(d.strip('\n')) for d in data]
    print(cleaned_data1)
with open('file2.txt') as file2:
    data=list(file2)
    cleaned_data2=[int(d.strip('\n')) for d in data]
    print(cleaned_data2)

result=[i for i in cleaned_data1 if i in cleaned_data2]

print(result)

# Dictinoary Comprehension


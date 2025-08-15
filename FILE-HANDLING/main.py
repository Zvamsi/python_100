file=open('../../../Desktop/FILE1.txt')
contents=file.read()
print(contents)
file.close()

with open('FILE2.txt','w') as file:
    file.write(f"\nSomething")
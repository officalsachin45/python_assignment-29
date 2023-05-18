import keyword
filename= 'example.txt'
with open(filename,'r')as f:
    f1=f.read()
    keywords=keyword.kwlist()
    count=0
    
for file in f1.split():
    if file in keywords:
        keywords+=1
print("the number number of keword",count)
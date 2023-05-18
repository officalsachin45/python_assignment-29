filename=str(input("enter the number:"))
filename1=str(input("enter the number:"))
with open(filename,'rb') as f:
    with open(filename1,'wb')as f1:
      f1.write(f.read())
print("file copy is sucsfull")
def read(filename):
    f=open(filename,'r')
    text=f.read()
    print(text)
read('myfile.txt')
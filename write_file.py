def writing(filename,text):
    with open(filename,'w')as f:
        f.write(text)
writing('text.txt',"my name is sachin")

def append(filename,text):
    with open(filename,'a')as f:
        f.write(text)
append('text.txt',"it's my first file handling program so i am very happy")
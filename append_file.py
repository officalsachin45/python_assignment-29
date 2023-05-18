def append(filename,text):
    with open(filename,'w')as f:
        f.write(text)
append('test.txt',"it's my first file handling program so i am very happy")
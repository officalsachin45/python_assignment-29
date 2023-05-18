def writing(filename,text):
    with open(filename,'w')as f:
        f.write(text)

def append(filename,text):
    with open(filename,'a')as f:
        f.write(text)
def reading(filename):
 try:
    f=open('text.txt','r')
    text=f.read()
    print(text)
    f.close()
 except FileNotFoundError:
    print("not found")
 else:
    None
reading('text.txt')
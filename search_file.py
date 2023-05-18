def search(filename,word):
    try:
        f=open(filename,'r')
        line_count=0
        for line in f.readlines():
            line_count+=1
            strlist=line.split(' ')
            word_count=0
            for w in strlist:
                word_count+=1
                if w==word:
                    return(word_count,line_count)
        else:
            return("abe gadhe ye word hi nhi hain")
        f.close()
    except FileNotFoundError:
        print("file not found so sorry plese next try")
x=search('text.txt',"is")
print(x)            
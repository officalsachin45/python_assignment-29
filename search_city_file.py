city=str(input("enter your city name"))
with open('cities.txt','r')as f:
    citie=f.read().splitlines()
if city in citie:
    print("the city present in file")
else:
    print("the city not present in file")
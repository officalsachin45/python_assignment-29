cities = ['New York', 'Paris', 'Tokyo', 'London', 'Mumbai']
# def write(filename):
with open('cities.txt','w') as f:
       for city in cities:
           f.write(city+'\n')
# write('cities.txt')
print('City names have been stored in the file.')   
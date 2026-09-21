# with open("name.txt", "r")as f:
#     print(f.read())

# with open("name.txt", "w")as f:
#     print(f.write("anshul \n khushi \n ankush \n suryansh \n dev"))    
    
# with open("name.txt", "r")as f:
#     print(f.read())

#2
# list=[5,10,15,20,25]
# n=[i for i in list if i>15]
# print(n)

#3
import json

cities={
    "Delhi":20000,
    "Noida":15000,
    "Saharanpur":10000
}

with open("cities.json","w")as f:
    
#takes salary as input
# n=int(input("enter a salary"))

# if(n<=30000):
#     print("you have to pay 5%")
# elif(n<=70000):
#     print("you have to pay 15%")
# else:
#     print("you have to pay 25%")        

#all even number's functions
# def even_numbers(a,b):
#     for i in range(a,b+1):
#         if i%2==0:
#             print(i)

# even_numbers(10,31)

#3
# def print_digits(n):
#     while n>0:
#        digit=n%10
#        print(digit)
#        n=n//10

# print_digits(312) 

#4
# def count_digits(n):
    
#     count=0
#     while n>0:
#         count+=1
#         n = n//10

#     print(count)     

# count_digits(549)

#5
def sum_digits(n):
    sum=0
    while n>0:
     digit=n%10
     sum=sum+digit
     n=n//10

    return sum
    
print(sum_digits(328)) 








    
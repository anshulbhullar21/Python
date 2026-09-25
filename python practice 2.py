#1 if-else logic questions
# n=int(input("enter a number : "))

# if n%2==0:
#     print("the number is even")
# else:
#     print("the number is odd")

#2
# n=int(input("enter a age : "))

# if n>=18:
#     print("person is eligible for vote")
# else:
#     print("person is not eligible for vote")

#3
# n=int(input("enter a number : "))

# if n>0:
#     print(f"{n} is positive")
# elif n<0:
#       print("number is negative")
# else:
#      print("number is zero")

#4
# m=int(input("enter a first number : "))
# n=int(input("enter a second number : "))

# if m>n:
#     print("first number bda hai")
# elif n>m:
#     print("second number bda hai")
# else:
#     print("dono equal hai")

#5
# m=int(input("enter a number : "))
# n=int(input("enter a number : "))
# q=int(input("enter a number : "))

# if m>n and m>q:
#     print("first number bda hai")
# elif n>m and n>q:
#     print("second number bda hai")
# elif q>m and q>n:
#     print("third number bda hai")
# elif m==n and n==q:
#     print("teeno equal hai")
# else:
#     print("do numbers equal hai or yehi largest hai")

#6
# n=int(input("enter a marks : "))

# if n>=90:
#     print("Grade A")
# elif n>=80:
#     print("Grade B")
# elif n>=70:
#     print("Grade C")
# elif n>=60:
#     print("Grade D")
# else:
#     print("Grade F")

#7
n=int(input("enter a number : "))

if n%3==0 and n%5==0:
    print(f"{n} is divisible by both")

elif n%3==0:
    print(f"{n} is divisible by 3")
elif n%5==0:
    print(f"{n} is divisible by 5")
else:
    print(f"{n} is not divisible by 3 and 5 both") 

    










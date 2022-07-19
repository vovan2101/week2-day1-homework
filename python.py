#exersise1

 i = 1

 while i ** 3 <= 1000:   
     print(i ** 3, end=' ')
     i += 1
     if i == 1000:
         break
 print("End")


# # exersise 2

 a = int(input("pleasr put a number:"))
 k = 0
 for i in range(2, a // 2+1):
     if (a % i == 0):
         k = k+1
 if (k <= 0):
     print("Number is prime")
 else:
     print("Number is NOT a prime")


# exersise 3




a = int(input("please inter your age:"))
if a < 18:
    print("kids")
elif 18 < a <=65:
    print("adults")
else:
    Error
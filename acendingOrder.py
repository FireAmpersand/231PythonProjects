a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Eneter Third Number: "))
large = max(a,b,c) 
small = min(a,b,c)
sum = a+b+c
middle = sum - large -small
print(small,middle,large)

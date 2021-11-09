# num=int(input("enter a number"))
# sum=0
# number=num
# while num>0:
#     num2=num%10
#     sum=(num2**3)+sum
#     num=num//10
# if number==sum:
#     print("armstrong")
# else:
#     print("not armstrong")


# num = int(input("enter a number"))
# sum = 0
# digit = num
# while num > 0:
#     rev = num % 10
#     sum = (rev**3)+sum
#     num = num//10
# if digit == sum:
#     print("armstrong")
# else:
#     print("not armstrong")





x=1
while x<=500:
    n=x
    sum=0
    while n!=0:
        sum=sum+(n%10)**3
        n=n//10
    if sum==x:
        print("armstrog",x)
    x=x+1

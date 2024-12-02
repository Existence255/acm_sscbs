#q1
def q1(m,n):
    sum=0
    for i in range(m-1,n):
        sum+=i
    return sum

    
#q2
def q2(a,b):
    if a/b:
        return True
    else:
        return False

    

#q3

def q3(l,b):
    area=l*b
    perimeter=2*(l+b)
    return area,perimeter
    
#q4

def q4(f):
    if f==0:
        return 1
    else:
        return f*q3(f-1)

    
#q5
def q5():
    for i in range(1,6):
        for j in range(1,i+1):
          print(j,end=" ")
        print()

def main():
    m=int(input("Enter the lower limit:"))
    n=int(input("Enter the upper limit:"))
    sum=q1(m,n)
    print("Sum of numbers between",m,"and",n,"is:",sum)
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    if q2(a,b):
        print(a,"is divisible by",b)
    else:
        print(a,"is not divisible by",b)
    l=int(input("Enter the length of rectangle:"))
    b=int(input("Enter the breadth of rectangle:"))
    area,perimeter=q3(l,b)
    print("Area of rectangle is:",area)
    print("Perimeter of rectangle is:",perimeter)
    f=int(input("Enter the number:"))
    print("Factorial of",f,"is:",q3(f))
    q5()
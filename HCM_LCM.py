
def find_HCF(a,b):
    hcf = 1
    minimum=min(a,b)
    
    for i in range(1,minimum+1):
        if a % i == 0 and b%i ==0:
            hcf=i
    return hcf

def find_LCM(a,b):
    return (a*b)//(find_HCF(a,b))

a = int(input("Enter first number"))
b = int(input("Enter second number"))

print(f"The HCF is {find_HCF(a,b)}")
print(f"The LCM is {find_LCM(a,b)}")

                            

import math
def is_prime(num):
    non_prime= None
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i ==0:
            non_prime=True
            break
        else:
            non_prime= False
    if non_prime:
        return False    
    else:
        return True
        

is_prime(75)
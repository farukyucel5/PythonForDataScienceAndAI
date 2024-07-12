def my_pow(x, y):

    return x ** y

altın_oran = 6.18

my_pi = 3.14

def my_sqrt(x):

    return x ** 0.5

def dik_üçgen_alanı(x, y):

    return (x * y) / 2 


def isAsal(x):

    if x < 2:
        return False
    
    else:

        for i in range(2, x):

            if x % i == 0:
                return False
            
    return True


def isLasa(x):

    ters_sayı = int(str(x)[::-1])

    if isAsal(x) and isAsal(ters_sayı):

        return True
    
    else:
        return False
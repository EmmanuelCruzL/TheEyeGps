

def  esPar(cordenadax,cordenaday):
    cordenadax = ord(cordenadax)
    cordenadax =True if (cordenadax%2)==0 else False
    cordenaday =True if (cordenaday%2)==0 else False
    return cordenadax == cordenaday 

def main():
    cordenadax = input()
    cordenaday = int(input())
    print("NEGRA" if esPar(cordenadax,cordenaday) else "BLANCA")

main()

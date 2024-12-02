def main():
    n = pegar_numero()
    miar(n)
def miar(n):
        for _ in range(n):
            print("miau")

def pegar_numero():
                while True:
                    n = int(input("Quantas vezes o gato miar? "))
                    if n > 0:
                        return n
                    
main()
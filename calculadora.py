# Funções para cada operação
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."

# Função principal
def calculadora():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        # Entrada do usuário
        escolha = input("Digite o número da operação (1/2/3/4): ")

        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, insira números válidos.")
                continue

            # Realizando a operação escolhida
            if escolha == '1':
                print(f"{num1} + {num2} = {somar(num1, num2)}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")

        else:
            print("Opção inválida! Por favor, escolha um número entre 1 e 4.")

        continuar = input("Deseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por usar a calculadora!")
            break

# Chama a função da calculadora
calculadora()

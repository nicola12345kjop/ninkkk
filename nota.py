def calcular_nota(nota_numerica):
    """Função para converter a nota numérica para o sistema de notas americano."""
    
    if nota_numerica >= 90:
        return 'A'
    elif nota_numerica >= 80:
        return 'B'
    elif nota_numerica >= 70:
        return 'C'
    elif nota_numerica >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Entrada do usuário
    nota_numerica = float(input("Digite a sua nota numérica (0-100): "))
    
    # Verificação da validade da nota
    if nota_numerica < 0 or nota_numerica > 100:
        print("Nota inválida! A nota deve estar entre 0 e 100.")
    else:
        # Exibe a nota final
        letra_nota = calcular_nota(nota_numerica)
        print(f"A sua nota é: {letra_nota}")
    
if __name__ == "__main__":
    main()
 
def calculadora():
    print("Calculadora")
    print("Digite o valor entre 1 e 4 para a operação: ")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Escolha o número da operação: ")

    if escolha not in ['1', '2', '3', '4']:
        print("Número inválido!")

    try:
        num1 = int(input("Digite o primeiro número "))
        num2 = int(input("Digite o segundo número "))
    except ValueError:
        print("Digita certo ai, maluco!")
        return
    
    if escolha == '1':
        resultado = num1 + num2
        operador = '+'
    elif escolha == '2':
        resultado = num1 - num2
        operador = '-'
    elif escolha == '3':
        resultado = num1 * num2
        operador = '*'
    elif escolha == '4':
        if num2 == 0:
            print("Erro: divisão por zero não é permitida!")
            return
        resultado = num1 / num2
        operador = '/'

    print(f"{num1} {operador} {num2} = {resultado}")

if __name__ == "__main__":
    calculadora()
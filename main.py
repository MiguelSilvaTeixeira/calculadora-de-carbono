def Main():
    # Loop principal para permitir múltiplos cálculos
    while True:
        print("Calculadora de Créditos de Carbono")

        # Pergunta inicial para identificar o tipo de usuário
        while True:
            print("Você está utilizando esta calculadora como:")
            print("1. Indivíduo")
            print("2. Empresa")
            print("3. Cidade")
            # Recebe a escolha do usuário
            tipoUsuario = input("Digite o número correspondente à sua escolha: ")

            # Se a escolha for válida, sai do loop
            if tipoUsuario in ["1", "2", "3"]:
                break
            else:
                # Se a escolha for inválida, pede a entrada novamente
                print("Escolha inválida. Por favor, tente novamente.\n")

        # TODO: Implementar funcionalidades adicionais aqui.

# Executa o programa principal
if __name__ == "__main__":
    Main()
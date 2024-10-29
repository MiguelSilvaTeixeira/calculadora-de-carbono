from funcoes import CalcularPegadaCarbono

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

        # Condicional para a opção "Indivíduo"
        if tipoUsuario == '1':
            print("\nVocê escolheu: Indivíduo")
            # Coleta dados de consumo específicos para indivíduos
            consumoEletricidade = float(input("Consumo mensal de eletricidade (kWh): "))
            consumoGasolina = float(input("Consumo mensal de gasolina (litros): "))
            consumoDiesel = float(input("Consumo mensal de diesel (litros): "))
            distanciaVooDomestico = float(input("Distância percorrida em voos domésticos por mês (km): "))
            distanciaVooInternacional = float(input("Distância percorrida em voos internacionais por mês (km): "))

            # Armazena os dados em um dicionário
            dadosAtividade = {
                "eletricidade": consumoEletricidade,
                "gasolina": consumoGasolina,
                "diesel": consumoDiesel,
                "voo_domestico": distanciaVooDomestico,
                "voo_internacional": distanciaVooInternacional
            }
            # Define as opções de projeto de compensação disponíveis
            opcoesProjeto = ["florestamento", "energia_renovavel", "eficiencia_energetica"]

        # Condicional para a opção "Empresa"
        elif tipoUsuario == "2":
            print("\nVocê escolheu: Empresa")
            # Coleta dados de consumo específicos para empresas
            consumoEletricidade = float(input("Consumo mensal de eletricidade (kWh): "))
            consumoGasolina = float(input("Consumo mensal de gasolina (litros): "))
            consumoDiesel = float(input("Consumo mensal de diesel (litros): "))
            transportePublico = float(input("Distância percorrida por transporte público por mês (km): "))
            residuosSolidos = float(input("Quantidade de resíduos sólidos gerados por mês (kg): "))

            # Armazena os dados em um dicionário
            dadosAtividade = {
                "eletricidade": consumoEletricidade,
                "gasolina": consumoGasolina,
                "diesel": consumoDiesel,
                "transporte_publico": transportePublico,
                "residuos_solidos": residuosSolidos
            }
            # Define as opções de projeto de compensação disponíveis
            opcoesProjeto = ["florestamento", "energia_renovavel", "eficiencia_energetica", "projetos_sociais"]

        # Condicional para a opção "Cidade"
        elif tipoUsuario == "3":
            print("\nVocê escolheu: Cidade")
            # Coleta dados de consumo específicos para cidades
            consumoEletricidade = float(input("Consumo mensal de eletricidade (MWh): ")) * 1000  # Converte para kWh
            consumoGasolina = float(input("Consumo mensal de gasolina (litros): "))
            transportePublico = float(input("Distância total percorrida por transporte público por mês (km): "))
            residuosSolidos = float(input("Quantidade total de resíduos sólidos gerados por mês (toneladas): ")) * 1000  # Converte para kg

            # Armazena os dados em um dicionário
            dadosAtividade = {
                "eletricidade": consumoEletricidade,
                "gasolina": consumoGasolina,
                "transporte_publico": transportePublico,
                "residuos_solidos": residuosSolidos
            }
            # Define as opções de projeto de compensação disponíveis
            opcoesProjeto = ["florestamento", "energia_renovavel", "eficiencia_energetica", "projetos_sociais"]

        # Calcular a pegada de carbono total com base nos dados fornecidos
        pegadaCarbono = CalcularPegadaCarbono(dadosAtividade)
        print(f"\nSua pegada de carbono mensal é: {pegadaCarbono:.2f} kg de CO2")

        # Escolher o tipo de projeto de compensação
        while True:
            print("\nEscolha o tipo de projeto para compensar suas emissões:")
            # Exibe as opções de projetos disponíveis
            for i, projeto in enumerate(opcoesProjeto, 1):
                print(f"{i}. {projeto.replace("_", " ").capitalize()}")
            escolhaProjeto = input("Digite o número correspondente à sua escolha: ")

            # Verifica se a escolha do projeto é válida
            try:
                tipoProjeto = opcoesProjeto[int(escolhaProjeto) - 1]
                break
            except (IndexError, ValueError):
                # Se a escolha for inválida, pede a entrada novamente
                print("Escolha inválida. Por favor, tente novamente.\n")

        # TODO: Implementar funcionalidades adicionais aqui.

# Executa o programa principal
if __name__ == "__main__":
    Main()
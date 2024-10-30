# Definindo os fatores de emissão para diferentes atividades em kg de CO2 por unidade
fatoresEmissao = {
    "eletricidade": 0.233,  # kg CO2 por kWh
    "gasolina": 2.31,       # kg CO2 por litro de gasolina
    "diesel": 2.68,         # kg CO2 por litro de diesel
    "voo_domestico": 0.255, # kg CO2 por km em voo doméstico
    "voo_internacional": 0.150, # kg CO2 por km em voo internacional
    "transporte_publico": 0.105, # kg CO2 por km por pessoa (média)
    "residuos_solidos": 1.42      # kg CO2 por kg de resíduos sólidos (média)
}

# Preço dos créditos de carbono em USD por tonelada de CO2
precosCreditos = {
    "florestamento": 10,
    "energia_renovavel": 15,
    "eficiencia_energetica": 12,
    "projetos_sociais": 20
}

# Taxa de câmbio USD para BRL
taxaCambioUsdBrl = 5.50  # 1 USD = 5,50 BRL

# Função para calcular a pegada de carbono
def CalcularPegadaCarbono(dadosAtividade):
    # Inicializa a pegada de carbono total como zero
    pegadaTotal = 0
    # Itera sobre cada atividade e seu valor de consumo
    for atividade, valor in dadosAtividade.items():
        # Obtém o fator de emissão correspondente à atividade
        fator = fatoresEmissao.get(atividade, 0)
        # Calcula a emissão para a atividade e soma ao total
        pegadaTotal += valor * fator
    # Retorna a pegada de carbono total em kg de CO2
    return pegadaTotal

# TODO: Implementar funcionalidades adicionais aqui.
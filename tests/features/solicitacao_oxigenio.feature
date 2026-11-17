Feature: Solicitação e Consumo de Suprimentos de Oxigênio
  Como engenheiro do habitat de Marte
  Quero validar o consumo de oxigênio em operação normal e em crise
  Para garantir a sobrevivência da tripulação

  Scenario: Consumo de oxigênio dentro do limite seguro
    Given que o habitat possui 1000 litros de oxigênio em estoque
    When a tripulação consome 300 litros de oxigênio
    Then o estoque restante deve ser de 700 litros
    And nenhum alerta de crise deve ser disparado

  Scenario: Solicitação de oxigênio acima do estoque disponível em crise
    Given que o habitat possui 200 litros de oxigênio em estoque
    When a tripulação tenta consumir 500 litros de oxigênio
    Then o sistema deve bloquear a operação por oxigênio insuficiente
    And um alerta de crise deve ser enviado para a Terra
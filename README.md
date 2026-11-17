# Missão Marte: ECLSS - Automação de Testes Integrada

![Status da Pipeline](https://github.com/gubonaluno/projeto-missao-marte/actions/workflows/pipeline.yml/badge.svg)

Projeto de garantia de qualidade de software (QA) desenvolvido para validar o sistema **Environmental Control and Life Support System (ECLSS)** do Habitat de Marte[cite: 1].

## Tecnologias Utilizadas
* **Pytest** (Fixtures, Parametrização e Validação de Exceções)[cite: 1, 2]
* **Pytest-Mock** (Isolamento de dependências de telemetria)[cite: 2]
* **Selenium WebDriver** (Testes End-to-End em modo headless com esperas explícitas)[cite: 1, 2]
* **Pytest-BDD** (Especificação de cenários em Gherkin)[cite: 2, 3]
* **GitHub Actions** (Integração Contínua e relatório de cobertura via `pytest-cov`)[cite: 3]

## Como Executar Localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/gubonaluno/projeto-missao-marte.git
   cd projeto-missao-marte
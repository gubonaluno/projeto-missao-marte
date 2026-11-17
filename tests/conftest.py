import pytest
from unittest.mock import MagicMock
from src.gerenciador_recursos import GerenciadorRecursosMarte


@pytest.fixture(scope="module")
def parametros_iniciais_habitat():
    """Fixture de escopo de módulo com os parâmetros padrão do habitat."""
    return {
        "oxigenio_inicial": 1000.0,
        "agua_inicial": 2000.0
    }


@pytest.fixture(scope="function")
def mock_telemetria():
    """Fornece um dublê (mock) limpo do serviço de telemetria para cada teste."""
    return MagicMock()


@pytest.fixture(scope="function")
def gerenciador(parametros_iniciais_habitat, mock_telemetria):
    """Instancia um GerenciadorRecursosMarte limpo antes de cada teste e limpa após."""
    instancia = GerenciadorRecursosMarte(
        oxigenio_inicial=parametros_iniciais_habitat["oxigenio_inicial"],
        agua_inicial=parametros_iniciais_habitat["agua_inicial"],
        telemetria=mock_telemetria
    )
    yield instancia
    # Teardown / limpeza pós-teste
    del instancia
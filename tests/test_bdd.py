import pytest
from unittest.mock import MagicMock
from pytest_bdd import scenarios, given, when, then, parsers
from src.gerenciador_recursos import (
    GerenciadorRecursosMarte,
    OxigenioInsuficienteError,
)

scenarios("features/solicitacao_oxigenio.feature")


@pytest.fixture
def contexto_bdd():
    return {"telemetria": MagicMock(), "erro": None}


@given(parsers.parse("que o habitat possui {estoque:d} litros de oxigênio em estoque"))
def definir_estoque_inicial(contexto_bdd, estoque):
    contexto_bdd["gerenciador"] = GerenciadorRecursosMarte(
        oxigenio_inicial=float(estoque),
        agua_inicial=1000.0,
        telemetria=contexto_bdd["telemetria"],
    )


@when(parsers.parse("a tripulação consome {quantidade:d} litros de oxigênio"))
def consumir_oxigenio_normal(contexto_bdd, quantidade):
    contexto_bdd["gerenciador"].consumir_oxigenio(float(quantidade))


@when(parsers.parse("a tripulação tenta consumir {quantidade:d} litros de oxigênio"))
def tentar_consumir_oxigenio_crise(contexto_bdd, quantidade):
    try:
        contexto_bdd["gerenciador"].consumir_oxigenio(float(quantidade))
    except OxigenioInsuficienteError as exc:
        contexto_bdd["erro"] = exc


@then(parsers.parse("o estoque restante deve ser de {esperado:d} litros"))
def verificar_estoque_restante(contexto_bdd, esperado):
    assert contexto_bdd["gerenciador"].oxigenio == float(esperado)


@then("nenhum alerta de crise deve ser disparado")
def verificar_sem_alerta(contexto_bdd):
    contexto_bdd["telemetria"].disparar_alerta_crise.assert_not_called()


@then("o sistema deve bloquear a operação por oxigênio insuficiente")
def verificar_bloqueio_excecao(contexto_bdd):
    assert isinstance(contexto_bdd["erro"], OxigenioInsuficienteError)


@then("um alerta de crise deve ser enviado para a Terra")
def verificar_alerta_disparado(contexto_bdd):
    contexto_bdd["telemetria"].disparar_alerta_crise.assert_called_once()
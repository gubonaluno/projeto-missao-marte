import pytest
from src.gerenciador_recursos import (
    OxigenioInsuficienteError,
    NivelEmergenciaInvalidoError,
)


@pytest.mark.parametrize(
    "num_astronautas, consumo_base, nivel_emergencia, esperado",
    [
        (4, 20.0, "normal", 80.0),
        (4, 20.0, "alerta", 96.0),
        (4, 20.0, "critico", 120.0),
        (6, 25.0, "normal", 150.0),
    ],
)
def test_calcular_consumo_diario_parametrizado(
    gerenciador, num_astronautas, consumo_base, nivel_emergencia, esperado
):
    resultado = gerenciador.calcular_consumo_diario(
        num_astronautas=num_astronautas,
        consumo_base_o2=consumo_base,
        nivel_emergencia=nivel_emergencia,
    )
    assert resultado == esperado


def test_nivel_emergencia_invalido_lanca_excecao(gerenciador):
    with pytest.raises(NivelEmergenciaInvalidoError):
        gerenciador.calcular_consumo_diario(
            num_astronautas=3, nivel_emergencia="apocalipse"
        )


def test_consumo_oxigenio_insuficiente_dispara_alerta_e_excecao(
    gerenciador, mock_telemetria
):
    with pytest.raises(OxigenioInsuficienteError):
        gerenciador.consumir_oxigenio(1500.0)

    mock_telemetria.disparar_alerta_crise.assert_called_once_with(
        recurso="Oxigenio",
        nivel_atual=1000.0,
        mensagem="Tentativa de consumo superior ao estoque disponível.",
    )


def test_consumo_oxigenio_reserva_critica_dispara_alerta(
    gerenciador, mock_telemetria
):
    novo_estoque = gerenciador.consumir_oxigenio(850.0)
    assert novo_estoque == 150.0

    mock_telemetria.disparar_alerta_crise.assert_called_once_with(
        recurso="Oxigenio",
        nivel_atual=150.0,
        mensagem="Estoque de oxigênio entrou em reserva crítica.",
    )
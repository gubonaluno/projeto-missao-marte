class OxigenioInsuficienteError(Exception):
    """Exceção lançada quando o estoque de oxigênio não supre a demanda."""
    pass


class NivelEmergenciaInvalidoError(Exception):
    """Exceção lançada quando o nível de emergência informado é inválido."""
    pass


class GerenciadorRecursosMarte:
    TAXAS_EMERGENCIA = {
        "normal": 1.0,
        "alerta": 1.2,
        "critico": 1.5
    }

    def __init__(self, oxigenio_inicial: float, agua_inicial: float, telemetria):
        self.oxigenio = oxigenio_inicial
        self.agua = agua_inicial
        self.telemetria = telemetria

    def calcular_consumo_diario(self, num_astronautas: int, consumo_base_o2: float = 20.0, nivel_emergencia: str = "normal") -> float:
        if num_astronautas <= 0:
            raise ValueError("Número de astronautas deve ser maior que zero.")
        if nivel_emergencia not in self.TAXAS_EMERGENCIA:
            raise NivelEmergenciaInvalidoError(f"Nível '{nivel_emergencia}' não reconhecido.")
        
        taxa = self.TAXAS_EMERGENCIA[nivel_emergencia]
        return num_astronautas * consumo_base_o2 * taxa

    def consumir_oxigenio(self, quantidade: float) -> float:
        if quantidade > self.oxigenio:
            self.telemetria.disparar_alerta_crise(
                recurso="Oxigenio",
                nivel_atual=self.oxigenio,
                mensagem="Tentativa de consumo superior ao estoque disponível."
            )
            raise OxigenioInsuficienteError("Estoque de oxigênio insuficiente para esta operação.")
        
        self.oxigenio -= quantidade
        
        # Se ficar abaixo de 200L após o consumo, dispara alerta preventivo
        if self.oxigenio < 200.0:
            self.telemetria.disparar_alerta_crise(
                recurso="Oxigenio",
                nivel_atual=self.oxigenio,
                mensagem="Estoque de oxigênio entrou em reserva crítica."
            )
        return self.oxigenio

    def aplicar_cota_racionamento(self, percentual_reducao: float) -> float:
        if not (0 < percentual_reducao < 100):
            raise ValueError("Percentual de racionamento deve estar entre 0 e 100.")
        fator = 1 - (percentual_reducao / 100.0)
        self.oxigenio = round(self.oxigenio * fator, 2)
        return self.oxigenio
class ServicoTelemetriaEspacial:
    def enviar_relatorio_status(self, oxigenio: float, agua: float) -> bool:
        # Em produção faria uma requisição HTTP para a Terra
        print(f"Telemetria enviada: O2={oxigenio}L, Agua={agua}L")
        return True

    def disparar_alerta_crise(self, recurso: str, nivel_atual: float, mensagem: str) -> bool:
        # Dispara alerta crítico para a estação terrestre
        print(f"ALERTA DE CRISE [{recurso}]: {mensagem} (Nível: {nivel_atual})")
        return True
from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_VALVULA_MOTOR = "TVM", "Trocar válvula do  moto"
    TROCAR_OLEO = "TO", "Troca de oleo"
    BALANCEAMENTO = "B", "Balanceamento"
    LAVAGEM_NA_VALETA = "LNV", "Lavagem na valeta"
    LAVAGEM_SIMPES = "LS", "Lavagem simples"
    LAVAGEM_DETALHADA = "LD", "Lavagem detalhada"
    HIGIENIZACAO_SIMPLES = "HS", "Higienizacao simples"
    HIGIENIZACAO_COMPLETA = "HC", "Higienizacao completa"
    RENOVACAO_PINTURA = "RP", "Renovacao de pintura"
    REVISAO_COMPLETA = "RC", "Revisao"


# Módulo: Monitoramento
# Registra e consulta leituras de qualidade da água


from datetime import datetime

leituras = []


def avaliar_qualidade(ph, turbidez, cloro):
    """
    Avalia a qualidade da água com base nos parâmetros informados.
    Parâmetros:
        ph (float)       — potencial hidrogeniônico (6.5 a 8.5 = normal)
        turbidez (float) — turbidez em NTU (< 5 = normal)
        cloro (float)    — cloro residual em mg/L (0.2 a 2.0 = normal)
    Retorna: str — 'Aprovado' ou 'Reprovado'
    """
    ph_ok = 6.5 <= ph <= 8.5
    turbidez_ok = turbidez < 5.0
    cloro_ok = 0.2 <= cloro <= 2.0

    return "Aprovado" if (ph_ok and turbidez_ok and cloro_ok) else "Reprovado"


def registrar_leitura():
    
    """Solicita e registra uma nova leitura de qualidade da água
    para um módulo de purificação específico."""

    print("\n--- Registrar Leitura de Qualidade ---")
    print("Parâmetros: pH (6.5-8.5), Turbidez NTU (<5), Cloro mg/L (0.2-2.0)")

    id_modulo = input("ID do módulo: ").strip()

    # 1. Coleta as entradas como strings primeiro
    ph_str = input("pH: ").strip()
    turbidez_str = input("Turbidez (NTU): ").strip()
    cloro_str = input("Cloro residual (mg/L): ").strip()
    temperatura_str = input("Temperatura (°C): ").strip()

    # Helper function temporária para validar se a string pode virar um float
    # Ela substitui o primeiro ponto por nada e checa se o resto são apenas dígitos
    def eh_float(val):
        return val.replace('.', '', 1).isdigit()

    # 2. Valida todas as entradas antes de converter
    if not (eh_float(ph_str) and eh_float(turbidez_str) and eh_float(cloro_str) and eh_float(temperatura_str)):
        print("Erro: informe apenas números para os parâmetros.")
        return

    # 3. Agora que sabemos que são seguras, fazemos a conversão
    ph = float(ph_str)
    turbidez = float(turbidez_str)
    cloro = float(cloro_str)
    temperatura = float(temperatura_str)

    resultado = avaliar_qualidade(ph, turbidez, cloro)
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

    leitura = {
        "id": len(leituras) + 1,
        "id_modulo": id_modulo,
        "data_hora": data_hora,
        "ph": ph,
        "turbidez": turbidez,
        "cloro": cloro,
        "temperatura": temperatura,
        "resultado": resultado
    }

    leituras.append(leitura)

    icone = "Ok" if resultado == "Aprovado" else "Not Ok"
    print(f"\n{icone} Leitura registrada — Resultado: {resultado}")


def listar_leituras_modulo(id_modulo):
    """
    Lista todas as leituras de um módulo específico.
    Parâmetros: id_modulo (str) — ID do módulo a consultar
    Retorna: lista de leituras do módulo
    """
    resultado_lista = [l for l in leituras if l["id_modulo"] == id_modulo]

    if not resultado_lista:
        print(f"Nenhuma leitura encontrada para o módulo ID {id_modulo}.")
        return []

    print(f"\n--- Leituras do Módulo {id_modulo} ---")
    for l in resultado_lista:
        status = "Ok" if l["resultado"] == "Aprovado" else "Not Ok"
        print(f"\n  {status} Data/Hora: {l['data_hora']}")
        print(f"     pH: {l['ph']} | Turbidez: {l['turbidez']} NTU | "
              f"Cloro: {l['cloro']} mg/L | Temp: {l['temperatura']}°C")
        print(f"     Resultado: {l['resultado']}")

    return resultado_lista
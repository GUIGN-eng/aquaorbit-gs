
# Módulo: Equipamentos
# Gerencia os módulos de purificação instalados

equipamentos = []

TIPOS_MODULO = [
    "UV Compacto",
    "Multifiltro Gravitacional",
    "Eletroquímico Portátil",
    "Destilação Solar"
]


def cadastrar_equipamento():
    """
    Cadastra um novo módulo de purificação vinculado a uma comunidade.
    """
    print("\n--- Cadastro de Módulo de Purificação ---")

    numero_serie = input("Número de série do módulo: ").strip()
    if not numero_serie:
        print("Erro: número de série obrigatório.")
        return

    print("Tipos de módulo disponíveis:")
    for i, tipo in enumerate(TIPOS_MODULO, 1):
        print(f"  [{i}] {tipo}")

    while True:
        escolha = input("Escolha o tipo (número): ").strip()
    
        # 1. Verifica se o usuário digitou apenas números e se não está vazio
        if escolha.isdigit():
            idx = int(escolha) - 1
            
            # 2. Verifica se o índice existe na lista TIPOS_MODULO
            if 0 <= idx < len(TIPOS_MODULO):
                tipo_escolhido = TIPOS_MODULO[idx]
                break  # Sai do loop pois a escolha é válida
            else:
                print("Opção invalida. Número ou Modulo incoerentes")
        # Se falhar em qualquer uma das condições acima, exibe o erro e o loop continua
        else:
            print("Opção inválida.")

    id_comunidade = input("ID da comunidade onde será instalado: ").strip()
    capacidade = input("Capacidade (litros/dia): ").strip()

    id_modulo = len(equipamentos) + 1

    equipamento = {
        "id": id_modulo,
        "numero_serie": numero_serie,
        "tipo": tipo_escolhido,
        "id_comunidade": id_comunidade,
        "capacidade": capacidade,
        "status": "ativo"
    }

    equipamentos.append(equipamento)
    print(f"\nMódulo '{numero_serie}' cadastrado com ID {id_modulo}.")


def listar_equipamentos():
    """
    Lista todos os módulos de purificação cadastrados.
    Retorna a lista de equipamentos.
    """
    print("\n--- Módulos de Purificação ---")

    if not equipamentos:
        print("Nenhum módulo cadastrado ainda.")
        return []

    for eq in equipamentos:
        print(f"\n  ID: {eq['id']}")
        print(f"  Série: {eq['numero_serie']}")
        print(f"  Tipo: {eq['tipo']}")
        print(f"  Comunidade ID: {eq['id_comunidade']}")
        print(f"  Capacidade: {eq['capacidade']} L/dia")
        print(f"  Status: {eq['status']}")

    return equipamentos

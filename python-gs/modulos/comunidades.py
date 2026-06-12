
# Módulo: Comunidades
# Responsável pelo cadastro e consulta de comunidades

comunidades = []  # Lista que armazena dicionários de comunidades


def validar_populacao(valor):
    """Valida se o valor informado é um número inteiro positivo.
    Parâmetros: valor (str) — string a ser validada
    Retorna: int válido ou None se inválido"""

    # Verifica se a entrada é uma string e se contém apenas dígitos
    if isinstance(valor, str) and valor.isdigit():
        num = int(valor)
        if num > 0:
            return num
            
    return None


def cadastrar_comunidade():
    
    #Solicita dados ao usuário e cadastra uma nova comunidade na lista.
    
    print("\n--- Cadastro de Comunidade ---")

    nome = input("Nome da comunidade: ").strip()
    if not nome:
        print("Erro: nome não pode ser vazio.")
        return

    municipio = input("Município: ").strip()
    estado = input("Estado (sigla, ex: CE): ").strip().upper()

    while True:
        pop_str = input("População estimada: ").strip()
        populacao = validar_populacao(pop_str)
        if populacao:
            break
        print("Erro: informe um número inteiro positivo para a população.")

    id_comunidade = len(comunidades) + 1

    comunidade = {
        "id": id_comunidade,
        "nome": nome,
        "municipio": municipio,
        "estado": estado,
        "populacao": populacao,
        "modulos": 0
    }

    comunidades.append(comunidade)
    print(f"\nComunidade '{nome}' cadastrada com ID {id_comunidade}.")


def listar_comunidades():
    
    #Exibe todas as comunidades cadastradas no sistema.
    
    print("\n--- Lista de Comunidades ---")

    if not comunidades:
        print("Nenhuma comunidade cadastrada ainda.")
        return

    print(f"\n{'ID':<5} {'Nome':<30} {'Município':<20} {'UF':<5} {'Pop.':<10}")
    print("-" * 72)

    for c in comunidades:
        print(f"{c['id']:<5} {c['nome']:<30} {c['municipio']:<20} "
              f"{c['estado']:<5} {c['populacao']:<10}")

    print(f"\nTotal: {len(comunidades)} comunidade(s) cadastrada(s).")


def buscar_comunidade(nome):
    
    """Busca comunidades pelo nome (parcial, sem diferenciação de maiúsculas).
    Parâmetros: nome (str) — termo de busca
    Retorna: lista de comunidades encontradas"""

    encontradas = [c for c in comunidades
                   if nome.lower() in c['nome'].lower()]

    if not encontradas:
        print(f"Nenhuma comunidade encontrada com '{nome}'.")
        return []

    print(f"\nResultados para '{nome}':")
    for c in encontradas:
        print(f"  ID {c['id']} — {c['nome']} / {c['municipio']}-{c['estado']}")

    return encontradas
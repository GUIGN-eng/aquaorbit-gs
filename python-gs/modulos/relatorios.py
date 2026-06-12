
# Módulo: Relatórios
# Gera análises e relatórios consolidados do sistema


from modulos.comunidades import comunidades
from modulos.equipamentos import equipamentos
from modulos.monitoramento import leituras


def relatorio_comunidades():
    
    """Gera um relatório consolidado de todas as comunidades
    e seus respectivos módulos instalados."""

    print("\n" + "=" * 60)
    print("     RELATÓRIO — COMUNIDADES ATENDIDAS")
    print("=" * 60)

    if not comunidades:
        print("Nenhuma comunidade cadastrada.")
        return

    total_pop = sum(c["populacao"] for c in comunidades)
    modulos_por_comunidade = {}

    for eq in equipamentos:
        cid = eq["id_comunidade"]
        modulos_por_comunidade[cid] = modulos_por_comunidade.get(cid, 0) + 1

    for c in comunidades:
        qtd_modulos = modulos_por_comunidade.get(str(c["id"]), 0)
        print(f"\n  {c['nome']} — {c['municipio']}/{c['estado']}")
        print(f"  População: {c['populacao']:,} habitantes")
        print(f"  Módulos instalados: {qtd_modulos}")

    print(f"\n{'=' * 60}")
    print(f"  Total de comunidades: {len(comunidades)}")
    print(f"  Total de pessoas atendidas: {total_pop:,}")
    print(f"  Total de módulos: {len(equipamentos)}")
    print("=" * 60)


def relatorio_qualidade_agua():
    """
    Gera um relatório estatístico das leituras de qualidade da água,
    mostrando percentual de aprovação e parâmetros médios.
    """
    print("\n" + "=" * 60)
    print("     RELATÓRIO — QUALIDADE DA ÁGUA")
    print("=" * 60)

    if not leituras:
        print("Nenhuma leitura registrada.")
        return

    aprovadas = [l for l in leituras if l["resultado"] == "Aprovado"]
    reprovadas = [l for l in leituras if l["resultado"] == "Reprovado"]
    total = len(leituras)

    perc_aprovacao = (len(aprovadas) / total) * 100

    ph_medio = sum(l["ph"] for l in leituras) / total
    turbidez_media = sum(l["turbidez"] for l in leituras) / total

    print(f"\n  Total de leituras: {total}")
    print(f" Aprovadas: {len(aprovadas)} ({perc_aprovacao:.1f}%)")
    print(f" Reprovadas: {len(reprovadas)} ({100 - perc_aprovacao:.1f}%)")
    print(f"\n  pH médio: {ph_medio:.2f}")
    print(f"  Turbidez média: {turbidez_media:.2f} NTU")
    print("=" * 60)
# AquaOrbit - Sistema de Gestão de Purificação de Água
# Disciplina: Computational Thinking Using Python
# Global Solution 2026/1 - FIAP ADS


from modulos.comunidades import (
    cadastrar_comunidade,
    listar_comunidades,
    buscar_comunidade
)
from modulos.equipamentos import (
    cadastrar_equipamento,
    listar_equipamentos
)
from modulos.monitoramento import (
    registrar_leitura,
    listar_leituras_modulo
)
from modulos.relatorios import (
    relatorio_comunidades,
    relatorio_qualidade_agua
)


def exibir_descricao():
    
    #Exibe uma breve descrição textual da solução AquaOrbit.
    
    print("\n" + "=" * 60)
    print("  AQUAORBIT — Gestão de Purificação de Água e Ar")
    print("=" * 60)
    print("""
  A AquaOrbit é uma plataforma de gestão de módulos portáteis
  de purificação de água inspirados na tecnologia da ISS
  (Estação Espacial Internacional), implantados em comunidades
  com escassez hídrica no semiárido brasileiro.

  O sistema permite cadastrar comunidades, gerenciar
  equipamentos instalados, registrar leituras de qualidade
  da água e gerar relatórios de impacto.
    """)
    print("=" * 60)
    input("\nPressione ENTER para continuar...")


def exibir_menu():
    
    """Exibe o menu principal do sistema AquaOrbit.
    Retorna a opção escolhida pelo usuário."""

    print("\n" + "=" * 60)
    print("         AQUAORBIT — MENU PRINCIPAL")
    print("=" * 60)
    print("  [1] Sobre o sistema")
    print("  [2] Gerenciar Comunidades")
    print("  [3] Gerenciar Equipamentos")
    print("  [4] Monitoramento de Qualidade")
    print("  [5] Relatórios")
    print("  [0] Sair")
    print("=" * 60)
    opcao = input("  Escolha uma opção: ").strip()
    return opcao


def menu_comunidades():
    
    #Submenu para gerenciamento de comunidades.
    
    while True:
        print("\n--- COMUNIDADES ---")
        print("[1] Cadastrar comunidade")
        print("[2] Listar comunidades")
        print("[3] Buscar comunidade por nome")
        print("[0] Voltar")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            cadastrar_comunidade()
        elif opcao == "2":
            listar_comunidades()
        elif opcao == "3":
            nome = input("Nome para buscar: ").strip()
            buscar_comunidade(nome)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_equipamentos():
    
    #Submenu para gerenciamento de equipamentos (módulos de purificação).
    
    while True:
        print("\n--- EQUIPAMENTOS ---")
        print("[1] Cadastrar módulo de purificação")
        print("[2] Listar módulos instalados")
        print("[0] Voltar")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            cadastrar_equipamento()
        elif opcao == "2":
            listar_equipamentos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_monitoramento():
    
    #Submenu para registro e consulta de leituras de qualidade.
    
    while True:
        print("\n--- MONITORAMENTO ---")
        print("[1] Registrar leitura de qualidade")
        print("[2] Consultar leituras de um módulo")
        print("[0] Voltar")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            registrar_leitura()
        elif opcao == "2":
            id_modulo = input("ID do módulo: ").strip()
            listar_leituras_modulo(id_modulo)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_relatorios():
    
    #Submenu de relatórios e análises do sistema.
    
    while True:
        print("\n--- RELATÓRIOS ---")
        print("[1] Relatório geral de comunidades")
        print("[2] Relatório de qualidade da água")
        print("[0] Voltar")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            relatorio_comunidades()
        elif opcao == "2":
            relatorio_qualidade_agua()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


def main():
    
    #Função principal: inicializa o sistema e controla o fluxo do menu.
    
    print("\nBem-vindo ao AquaOrbit!")

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            exibir_descricao()
        elif opcao == "2":
            menu_comunidades()
        elif opcao == "3":
            menu_equipamentos()
        elif opcao == "4":
            menu_monitoramento()
        elif opcao == "5":
            menu_relatorios()
        elif opcao == "0":
            print("\nEncerrando o sistema AquaOrbit. Até logo!")
            break
        else:
            print("Opção inválida! Digite um número entre 0 e 5.")


if __name__ == "__main__":
    main()
package aquaorbit.main;

import aquaorbit.entidades.*;
import java.util.Scanner;

public class Main {

    public static void main(String[] academico) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("--- SISTEMA AQUAORBIT - STARTUP OPERACIONAL ---");

        // 1. Instanciação Dinâmica (Captação de Entradas do Usuário)
        System.out.print("Digite o nome da comunidade a ser atendida: ");
        String nomeCom = entrada.nextLine();

        System.out.print("Digite a localização/estado: ");
        String locCom = entrada.nextLine();

        System.out.print("Digite a população estimada: ");
        int popCom = entrada.nextInt();
        entrada.nextLine(); // Limpeza de buffer

        // Criação de objetos usando construtores parametrizados
        Comunidade comunidade = new Comunidade(nomeCom, locCom, popCom);

        // Criando purificadores associados à comunidade criada
        PurificadorUV purificadorUv = new PurificadorUV("EQ-UV01", "Ativo", comunidade, 15.5);
        PurificadorDestilacao purificadorDes = new PurificadorDestilacao("EQ-DS02", "Manutenção", comunidade, 45.0);

        System.out.println("\n--- REGISTRO DE TESTE FÍSICO-QUÍMICO ---");
        System.out.print("Informe o pH coletado na amostra: ");
        double ph = entrada.nextDouble();

        System.out.print("Informe o nível de turbidez (NTU): ");
        double turbidez = entrada.nextDouble();

        System.out.print("Informe o cloro residual (mg/L): ");
        double cloro = entrada.nextDouble();

        Monitoramento analise = new Monitoramento(ph, turbidez, cloro, purificadorUv);

        // --- EXECUÇÃO E EXIBIÇÃO COMPLETA DAS SAÍDAS ---
        System.out.println("\n=============================================");
        System.out.println("          RELATÓRIO CONSOLIDADO EM TEMPO REAL");
        System.out.println("=============================================");

        // Exibição do estado dos objetos através do toString()
        System.out.println(comunidade);
        System.out.println("\nInventário de Equipamentos:");
        System.out.println(" -> " + purificadorUv);
        System.out.println(" -> " + purificadorDes);

        System.out.println("\nResultado do Monitoramento:");
        System.out.println(" -> " + analise);

        // Uso dos Métodos Funcionais 1 e 2 (Inclusos na classe Monitoramento)
        System.out.println(" -> Status da Amostra: " + analise.obterResultadoFormatado());

        // Chamada dos Métodos Funcionais de Negócio 3 e 4 (Implementados abaixo)
        calcularTotalVidasImpactadas(comunidade);
        emitirAlertaSeguranca(analise);

        System.out.println("=============================================");
        entrada.close();
    }

    // --- MÉTODOS FUNCIONAIS ADICIONAIS NA CLASSE EXECUTÁVEL ---

    /**
     * Método Funcional 3: Consolida e exibe o impacto social com base na comunidade atendida.
     */
    public static void calcularTotalVidasImpactadas(Comunidade c) {
        System.out.println("\n[MÉTODO 3 - Métrica Social]");
        System.out.println(" >> Sucesso! Total de " + c.getPopulacaoAtendida() + " vidas positivamente impactadas pela iniciativa.");
    }

    /**
     * Método Funcional 4: Emite um alerta severo baseado no resultado operacional do teste.
     */
    public static void emitirAlertaSeguranca(Monitoramento m) {
        System.out.println("\n[MÉTODO 4 - Auditoria de Risco]");
        if (!m.avaliarQualidadeAgua()) {
            System.out.println(" >> ALERTA URGENTE: Desative o equipamento "
                    + m.getEquipamentoMonitorado().getCodigoIdentificacao()
                    + " imediatamente para triagem técnica!");
        } else {
            System.out.println(" >> Operação Estável. Parâmetros dentro das metas de qualidade.");
        }
    }
}
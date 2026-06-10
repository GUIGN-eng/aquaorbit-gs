package aquaorbit.entidades;

public class Monitoramento {
    private double ph;
    private double turbidez;
    private double cloroResidual;
    private Equipamentos equipamentoMonitorado;

    public Monitoramento() {}

    public Monitoramento(double ph, double turbidez, double cloroResidual, Equipamentos equipamentoMonitorado) {
        this.ph = ph;
        this.turbidez = turbidez;
        this.cloroResidual = cloroResidual;
        this.equipamentoMonitorado = equipamentoMonitorado;
    }

    // --- MÉTODOS FUNCIONAIS DE NEGÓCIO (Exigência: Mínimo 4 métodos no sistema) ---

    /**
     * Método Funcional 1: Avalia se a amostra de água está em conformidade.
     * Critérios: pH entre 6.0 e 9.5 | Turbidez menor que 5.0 NTU | Cloro entre 0.2 e 2.0 mg/L
     */
    public boolean avaliarQualidadeAgua() {
        return (this.ph >= 6.0 && this.ph <= 9.5) &&
                (this.turbidez <= 5.0) &&
                (this.cloroResidual >= 0.2 && this.cloroResidual <= 2.0);
    }

    /**
     * Método Funcional 2: Retorna uma String legível com o veredito do teste.
     */
    public String obterResultadoFormatado() {
        if (avaliarQualidadeAgua()) {
            return "APROVADA para consumo.";
        } else {
            return "REPROVADA - Risco à saúde pública.";
        }
    }

    public double getPh() { return ph; }
    public void setPh(double ph) { this.ph = ph; }

    public double getTurbidez() { return turbidez; }
    public void setTurbidez(double turbidez) { this.turbidez = turbidez; }

    public double getCloroResidual() { return cloroResidual; }
    public void setCloroResidual(double cloroResidual) { this.cloroResidual = cloroResidual; }

    public Equipamentos getEquipamentoMonitorado() { return equipamentoMonitorado; }
    public void setEquipamentoMonitorado(Equipamentos equipamentoMonitorado) { this.equipamentoMonitorado = equipamentoMonitorado; }

    @Override
    public String toString() {
        return "Análise -> pH: " + ph + ", Turbidez: " + turbidez + " NTU, Cloro: " + cloroResidual + " mg/L";
    }
}
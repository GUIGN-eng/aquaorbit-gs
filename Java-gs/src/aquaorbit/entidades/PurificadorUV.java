package aquaorbit.entidades;

public class PurificadorUV extends Equipamentos {
    private double potenciaLampadaWatts;

    public PurificadorUV() {}

    public PurificadorUV(String codigoIdentificacao, String status, Comunidade comunidadeVinculada, double potenciaLampadaWatts) {
        super(codigoIdentificacao, status, comunidadeVinculada);
        this.potenciaLampadaWatts = potenciaLampadaWatts;
    }

    public double getPotenciaLampadaWatts() { return potenciaLampadaWatts; }
    public void setPotenciaLampadaWatts(double potenciaLampadaWatts) { this.potenciaLampadaWatts = potenciaLampadaWatts; }

    @Override
    public String toString() {
        return super.toString() + " | Tipo: UV Compacto (Potência: " + potenciaLampadaWatts + "W)";
    }
}
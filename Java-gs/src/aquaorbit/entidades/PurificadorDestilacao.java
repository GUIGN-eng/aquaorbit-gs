package aquaorbit.entidades;

public class PurificadorDestilacao extends Equipamentos {
    private double capacidadeLitrosHora;

    public PurificadorDestilacao() {}

    public PurificadorDestilacao(String codigoIdentificacao, String status, Comunidade comunidadeVinculada, double capacidadeLitrosHora) {
        super(codigoIdentificacao, status, comunidadeVinculada);
        this.capacidadeLitrosHora = capacidadeLitrosHora;
    }

    public double getCapacidadeLitrosHora() { return capacidadeLitrosHora; }
    public void setCapacidadeLitrosHora(double capacidadeLitrosHora) { this.capacidadeLitrosHora = capacidadeLitrosHora; }

    @Override
    public String toString() {
        return super.toString() + " | Tipo: Destilação Solar (Capacidade: " + capacidadeLitrosHora + " L/h)";
    }
}
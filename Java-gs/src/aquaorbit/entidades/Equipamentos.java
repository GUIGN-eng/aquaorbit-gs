package aquaorbit.entidades;

public abstract class Equipamentos {
    private String codigoIdentificacao;
    private String status; // Ativo, Manutenção, Inativo
    private Comunidade comunidadeVinculada; // Atributo de Referência

    public Equipamentos() {}

    public Equipamentos(String codigoIdentificacao, String status, Comunidade comunidadeVinculada) {
        this.codigoIdentificacao = codigoIdentificacao;
        this.status = status;
        this.comunidadeVinculada = comunidadeVinculada;
    }

    public String getCodigoIdentificacao() { return codigoIdentificacao; }
    public void setCodigoIdentificacao(String codigoIdentificacao) { this.codigoIdentificacao = codigoIdentificacao; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }

    public Comunidade getComunidadeVinculada() { return comunidadeVinculada; }
    public void setComunidadeVinculada(Comunidade comunidadeVinculada) { this.comunidadeVinculada = comunidadeVinculada; }

    @Override
    public String toString() {
        return "Código: " + codigoIdentificacao + " | Status: " + status + " | " + (comunidadeVinculada != null ? comunidadeVinculada.getNome() : "Sem comunidade");
    }
}
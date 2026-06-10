package aquaorbit.entidades;

public class Comunidade {
    private String nome;
    private String localizacao;
    private int populacaoAtendida;

    public Comunidade() {}

    public Comunidade(String nome, String localizacao, int populacaoAtendida) {
        this.nome = nome;
        this.localizacao = localizacao;
        setPopulacaoAtendida(populacaoAtendida);
    }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public String getLocalizacao() { return localizacao; }
    public void setLocalizacao(String localizacao) { this.localizacao = localizacao; }

    public int getPopulacaoAtendida() { return populacaoAtendida; }

    // Validação estrita: garante população inteira positiva (requisito do PDF)
    public void setPopulacaoAtendida(int populacaoAtendida) {
        if (populacaoAtendida >= 0) {
            this.populacaoAtendida = populacaoAtendida;
        } else {
            this.populacaoAtendida = 0;
        }
    }

    @Override
    public String toString() {
        return "Comunidade: " + nome + " | Localização: " + localizacao + " | População: " + populacaoAtendida;
    }
}
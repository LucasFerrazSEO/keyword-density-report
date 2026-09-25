# keyword-density-report — ferramenta grátis e de código aberto de densidade de palavra-chave em pt-BR

`keyword-density-report` é uma ferramenta gratuita e de código aberto que
mede densidade e cobertura de uma palavra-chave em um texto pt-BR, e lista
os bigramas e trigramas mais frequentes (tirando stopwords) para ver do
que o texto realmente fala, além da keyword que você tinha em mente.

## Como funciona

**Densidade da keyword.** Para termos curtos (até 3 palavras), conta
ocorrência da frase exata dividida pelo total de palavras. Para termos
longos (4 palavras ou mais), usa cobertura por palavras — ocorrências
multiplicadas pelo número de termos da keyword, dividido pelo total —
porque uma frase longa exata é rara de se repetir literalmente, mas a
combinação de termos pode estar coberta de outros jeitos.

**Bigramas e trigramas.** Conta as combinações de 2 e 3 palavras mais
frequentes no texto, descartando qualquer n-grama que contenha stopword em
pt-BR, para não poluir o resultado com "de um", "para a" e afins.

## Instalação

Só biblioteca padrão do Python (3.9 ou mais recente). Sem dependência
externa.

```bash
git clone https://github.com/lucasferrazseo/keyword-density-report.git
cd keyword-density-report
```

## Como usar, passo a passo

**1. Passe o texto e a keyword-alvo.**

```bash
python keyword_density_report.py texto.txt --kw "consultoria de seo"
```

**2. Leia o relatório.** Exemplo real de saída:

```
=== keyword-density-report ===
75 palavra(s) no texto

Keyword "schema markup" (frase exata): 1 ocorrência(s), densidade 1.33%

-- Bigramas mais frequentes --
     1x  schema markup
     1x  preciso configurar
     1x  json ld
     1x  google entenda
     ...

-- Trigramas mais frequentes --
     1x  schema markup h2
     1x  json ld corretamente
     ...
```

**3. Ajuste quantos n-gramas mostrar** (padrão: 10):

```bash
python keyword_density_report.py texto.txt --kw "seo" --top 15
```

**4. Passe texto direto pelo pipe**, sem salvar arquivo antes:

```bash
cat texto.txt | python keyword_density_report.py - --kw "seo para ia"
```

**5. Rode sem `--kw`**, se só quiser ver os n-gramas mais frequentes, sem
calcular densidade de nenhuma keyword específica.

## Perguntas frequentes

**keyword-density-report é realmente grátis?**
Sim, código aberto sob licença MIT.

**Qual é a densidade ideal de keyword?**
Não existe um número mágico oficial. Densidade acima de 2-3% costuma
indicar texto forçado — trate como sinal de repetição mecânica a evitar,
não como meta a perseguir.

**A ferramenta funciona em inglês?**
A lista de stopwords é específica de português brasileiro; em outro
idioma, os bigramas/trigramas vão incluir palavras funcionais que
deveriam ser descartadas.

## Limitações

Densidade de keyword é, na melhor das hipóteses, um sinal fraco de
relevância — motores de busca modernos não rankeiam por essa métrica
isolada, e forçar uma densidade-alvo tende a produzir texto pior, não
melhor.

## Método e origem

Generalização do critério de densidade usado no processo editorial de
[lucasferrazseo.com](https://lucasferrazseo.com).

## Autor

[Lucas Ferraz](https://lucasferraz.com) — especialista em SEO, criação de
sites e SEO para IA, fundador da [Lucas Ferraz SEO](https://lucasferrazseo.com).

## Licença

MIT — ver [LICENSE](LICENSE).

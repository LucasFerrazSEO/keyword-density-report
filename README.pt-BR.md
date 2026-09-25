[English](README.md) · **Português (Brasil)**

# keyword-density-report

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)

`keyword-density-report` é uma ferramenta de linha de comando gratuita e de
código aberto que mede densidade e cobertura de uma palavra-chave em um
texto em português brasileiro. Também lista os bigramas e trigramas mais
frequentes (tirando stopwords), para ver do que o texto realmente fala,
além da keyword que você tinha em mente. Roda localmente, só com a
biblioteca padrão do Python.

## Sumário

- [Como funciona](#como-funciona)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Perguntas frequentes](#perguntas-frequentes)
- [Limitações](#limitações)
- [Método e origem](#método-e-origem)
- [Como contribuir](#como-contribuir)
- [Autor](#autor)
- [Licença](#licença)

## Como funciona

**Densidade da keyword.** Para termos curtos (até 3 palavras), conta as
ocorrências da frase exata e divide pelo total de palavras. Para termos
longos (4 palavras ou mais), usa cobertura por palavras: ocorrências da
frase exata multiplicadas pelo número de termos da keyword, divididas
pelo total de palavras. Densidade acima de 2% recebe um alerta no
relatório.

**Bigramas e trigramas.** Conta as combinações de 2 e 3 palavras mais
frequentes no texto, descartando qualquer n-grama que contenha stopword em
pt-BR, para não poluir o resultado com "de um", "para a" e afins.

## Requisitos

Python 3.9 ou mais recente. Só biblioteca padrão, sem dependência externa.

## Instalação

```bash
git clone https://github.com/LucasFerrazSEO/keyword-density-report.git
cd keyword-density-report
```

## Uso

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
Não existe um número mágico oficial. Densidade acima de 2 a 3% costuma
indicar texto forçado. Trate como sinal de repetição mecânica a evitar,
não como meta a perseguir.

**A ferramenta funciona em inglês?**
A lista de stopwords é específica de português brasileiro. Em outro
idioma, os bigramas e trigramas vão incluir palavras funcionais que
deveriam ser descartadas.

## Limitações

Densidade de keyword é, na melhor das hipóteses, um sinal fraco de
relevância. Motores de busca modernos não rankeiam por essa métrica
isolada, e forçar uma densidade-alvo tende a produzir texto pior, não
melhor.

## Método e origem

Generalização do critério de densidade usado no processo editorial de
[lucasferrazseo.com](https://lucasferrazseo.com).

## Como contribuir

Relatos de erro e sugestões são bem-vindos pelas [Issues do GitHub](https://github.com/LucasFerrazSEO/keyword-density-report/issues).

## Autor

[Lucas Ferraz](https://lucasferraz.com) é especialista em SEO, criação de sites e Generative Engine Optimization e fundador da [Lucas Ferraz SEO](https://lucasferrazseo.com).

## Licença

MIT. Veja o arquivo [LICENSE](LICENSE).

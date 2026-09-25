#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
keyword-density-report — mede densidade e cobertura de uma palavra-chave em
um texto pt-BR, e lista os bigramas e trigramas mais frequentes (tirando
stopwords) para ajudar a ver do que o texto realmente fala, além da
keyword que você tinha em mente.

O QUE FAZ
    1. Conta a densidade da keyword informada: ocorrências da frase exata
       dividido pelo total de palavras (para termos de 1-3 palavras) ou
       cobertura por palavras (ocorrências × nº de palavras da keyword,
       dividido pelo total) para termos de 4+ palavras — o mesmo critério
       de "termo longo conta por cobertura, termo curto por frase exata"
       usado em checagens editoriais.
    2. Lista os N bigramas e trigramas mais frequentes do texto, ignorando
       stopwords em pt-BR — útil para ver quais combinações de palavras
       dominam o texto de fato, não só a keyword-alvo.

USO
    python keyword_density_report.py texto.txt --kw "consultoria de seo"
    python keyword_density_report.py texto.txt --kw "seo" --top 15
    cat texto.txt | python keyword_density_report.py - --kw "seo para ia"

LIMITAÇÕES
    Densidade de keyword é, na melhor das hipóteses, um sinal fraco de
    relevância — motores de busca modernos não rankeiam por essa métrica
    isolada. Trate como diagnóstico de repetição mecânica (densidade acima
    de 2-3% costuma indicar texto forçado), não como meta a perseguir.

Autor: Lucas Ferraz (lucasferraz.com) — dependência zero, só biblioteca padrão.
Licença: MIT.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter

STOPWORDS_PT = set(
    "a o os as um uma uns umas de do da dos das em no na nos nas por para "
    "com sem que qual quais como quando onde quem e ou seu sua seus suas "
    "mais menos muito pouco sobre entre ser é são está estão foi eram era "
    "tem têm ter deve devem pode podem vai vão isso esse essa este esta "
    "isto aquilo aquele aquela ao aos à às pelo pela pelos pelas num numa "
    "se não sim já ainda muito também até só apenas mas porém".split()
)


def tokeniza(texto: str) -> list[str]:
    return re.findall(r"[a-zà-ÿ0-9]+", texto.lower())


def conta_ngramas(tokens: list[str], n: int) -> Counter:
    ngramas = Counter()
    for i in range(len(tokens) - n + 1):
        grupo = tokens[i:i + n]
        if any(t in STOPWORDS_PT for t in grupo):
            continue
        ngramas[" ".join(grupo)] += 1
    return ngramas


def main() -> None:
    ap = argparse.ArgumentParser(description="Densidade de keyword e n-gramas mais frequentes de um texto pt-BR.")
    ap.add_argument("arquivo", help="arquivo de texto, ou '-' para entrada padrão")
    ap.add_argument("--kw", default="", help="keyword para calcular densidade")
    ap.add_argument("--top", type=int, default=10, help="quantos bigramas/trigramas mostrar (padrão 10)")
    args = ap.parse_args()

    texto = sys.stdin.read() if args.arquivo == "-" else open(args.arquivo, encoding="utf-8").read()
    tokens = tokeniza(texto)
    total = len(tokens) or 1

    print(f"\n=== keyword-density-report ===")
    print(f"{total} palavra(s) no texto\n")

    if args.kw:
        kw = args.kw.lower().strip()
        kw_palavras = kw.split()
        baixo = texto.lower()
        if len(kw_palavras) >= 4:
            ocorrencias = len(re.findall(re.escape(kw), baixo))
            densidade = ocorrencias * len(kw_palavras) / total * 100
            metodo = "cobertura de palavras (keyword de 4+ termos)"
        else:
            ocorrencias = len(re.findall(re.escape(kw), baixo))
            densidade = ocorrencias / total * 100
            metodo = "frase exata"
        alerta = " — acima de 2%, considerar reduzir repetição" if densidade > 2 else ""
        print(f"Keyword \"{args.kw}\" ({metodo}): {ocorrencias} ocorrência(s), densidade {densidade:.2f}%{alerta}\n")

    for n, rotulo in ((2, "Bigramas"), (3, "Trigramas")):
        contagem = conta_ngramas(tokens, n)
        mais_comuns = contagem.most_common(args.top)
        print(f"-- {rotulo} mais frequentes --")
        if not mais_comuns:
            print("  (nenhum, texto curto demais)")
        for termo, freq in mais_comuns:
            print(f"  {freq:>4}x  {termo}")
        print()


if __name__ == "__main__":
    main()

**English** · [Português (Brasil)](README.pt-BR.md)

# keyword-density-report

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)

`keyword-density-report` is a free, open source command-line tool that
measures the density and coverage of a keyword in a Brazilian Portuguese
text. It also lists the most frequent bigrams and trigrams (stopwords
removed), so you can see what the text is actually about beyond the
keyword you had in mind. It runs locally with the Python standard library
only.

The stopword list is specific to Brazilian Portuguese (pt-BR). On texts in
other languages, the n-gram lists will include function words that should
have been filtered out.

## Contents

- [How it works](#how-it-works)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [FAQ](#faq)
- [Limitations](#limitations)
- [Methodology](#methodology)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## How it works

**Keyword density.** For short terms (up to 3 words), it counts
occurrences of the exact phrase and divides by the total word count. For
long terms (4 words or more), it uses word coverage: exact-phrase
occurrences multiplied by the number of words in the keyword, divided by
the total word count. Densities above 2% get a warning in the report.

**Bigrams and trigrams.** It counts the most frequent 2-word and 3-word
combinations in the text and discards any n-gram that contains a pt-BR
stopword, so results are not cluttered with pairs like "de um" or
"para a".

## Requirements

Python 3.9 or newer. Standard library only, no external dependencies.

## Installation

```bash
git clone https://github.com/LucasFerrazSEO/keyword-density-report.git
cd keyword-density-report
```

## Usage

The tool prints its report in Brazilian Portuguese.

**1. Pass the text file and the target keyword.**

```bash
python keyword_density_report.py texto.txt --kw "consultoria de seo"
```

**2. Read the report.** Real sample output:

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

**3. Set how many n-grams to show** (default: 10):

```bash
python keyword_density_report.py texto.txt --kw "seo" --top 15
```

**4. Pipe text in directly**, without saving a file first:

```bash
cat texto.txt | python keyword_density_report.py - --kw "seo para ia"
```

**5. Run without `--kw`** if you only want the most frequent n-grams and
no density calculation for a specific keyword.

## FAQ

**Is keyword-density-report really free?**
Yes. It is open source under the MIT license.

**What is the ideal keyword density?**
There is no official magic number. Density above 2 to 3% usually points to
forced text. Treat it as a sign of mechanical repetition to avoid, not as
a target to chase.

**Does the tool work in English?**
The stopword list is specific to Brazilian Portuguese. In other languages,
the bigrams and trigrams will include function words that should have been
discarded.

## Limitations

Keyword density is, at best, a weak relevance signal. Modern search
engines do not rank on this metric alone, and forcing a target density
tends to produce worse text, not better.

## Methodology

A generalization of the density criterion used in the editorial process
of [lucasferrazseo.com](https://lucasferrazseo.com).

## Contributing

Bug reports and suggestions are welcome through [GitHub Issues](https://github.com/LucasFerrazSEO/keyword-density-report/issues).

## Author

[Lucas Ferraz](https://lucasferraz.com) is an SEO, website development and Generative Engine Optimization specialist and the founder of [Lucas Ferraz SEO](https://lucasferrazseo.com).

## License

MIT. See [LICENSE](LICENSE).

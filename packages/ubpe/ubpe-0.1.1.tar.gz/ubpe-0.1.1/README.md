# UBPE Tokenizer

> UBPE -- Universal Byte-Pair Encoding. Universal means that it works not only with strings, but with general sequences too.

The package provides Universal Byte-Pair Encoding tokenizers:
 - `UBPEClassic` -- *optimized* version of classic BPE algorithm
 - `UBPE` -- novel approach to BPE tokenization which allows you to choose between multiple different variants of encodings according to scores of tf-idf metric or something else; the most optimal encoding from this implementation was *shorter* than the encoding from classic implementation

## Guides and theory
 - [Description of tokenizer fitting algorithms](https://scurrra.github.io/blog/ubpe-tokenizers-i/)
 - [Description of encoding and decoding algorithms for classic and novel approaches](https://scurrra.github.io/blog/ubpe-tokenizers-ii/)
  
## Installation

I am planning to deliver different implementations for the algorithm, so the package is divided into general import package (this one), and implementations (for now, only Python native). To install use:

```bash
pip install ubpe[native]
```

## Contribution

I am pretty sure, that it has not the most optimal native Python implementation, so feel free to propose optimizations and find bugs.

It's planned to add Cython implementation and Rust implementation with Python bindings (not to bite Hugging Face, just because).

P.S. if you are working at Hugging Face, you can write me and hire me. Please. 
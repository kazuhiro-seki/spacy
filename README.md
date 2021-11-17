# NER by SpaCy on M1 Mac

## Install

```sh
python3 -m venv venv
source venv/bin/activate
pip install spacy
```

### Install generic (small) model

```sh
python3 -m spacy download en_core_web_sm
```

### Install transformer-based model

```sh
brew install Rust
pip install https://huggingface.co/spacy/en_core_web_trf/resolve/main/en_core_web_trf-any-py3-none-any.whl
```

## Run

```sh
python test.py
```

## References

- https://spacy.io/usage/linguistic-features#named-entities
- https://github.com/explosion/spaCy/issues/9606
- https://huggingface.co/spacy/en_core_web_trf

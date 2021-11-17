# NER by SpaCy

## Virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
```

## Install

```sh
pip install spacy
```

### Install generic (small) model

```sh
python3 -m spacy download en_core_web_sm
```

### Install transformer-based model

#### For M1 Mac

```sh
brew install Rust
pip install https://huggingface.co/spacy/en_core_web_trf/resolve/main/en_core_web_trf-any-py3-none-any.whl
```

#### For others (tested on centos)

```sh
pip install https://huggingface.co/spacy/en_core_web_trf/resolve/main/en_core_web_trf-any-py3-none-any.whl
```


## Run

```sh
python test.py
```

## Note

SpaCy and SciSpaCy collide due to different version dependencies and should be installed separately.

## References

- https://spacy.io/usage/linguistic-features#named-entities
- https://github.com/explosion/spaCy/issues/9606
- https://huggingface.co/spacy/en_core_web_trf

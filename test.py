import spacy

#nlp = spacy.load("en_core_web_sm")

# For the non-transformer models, the ner component is independent, so
# you can disable everything

nlp = spacy.load("en_core_web_sm", disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])

#nlp = spacy.load("en_core_web_trf")

# In the transformer models, ner listens to the transformer component,
# so you can disable all components related tagging, parsing, and
# lemmatization.

#nlp = spacy.load("en_core_web_trf", disable=["tagger", "parser", "attribute_ruler", "lemmatizer"])


doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)


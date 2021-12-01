import spacy
from spacy import displacy

# For the non-transformer models, the ner component is independent, so
# you can disable everything

nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("en_core_web_sm", disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])

# In the transformer models, ner listens to the transformer component,
# so you can disable all components related tagging, parsing, and
# lemmatization.

#nlp = spacy.load("en_core_web_trf")
#nlp = spacy.load("en_core_web_trf", disable=["tagger", "parser", "attribute_ruler", "lemmatizer"])

lines = []
with open("transcript.txt") as f:
    for line in f:
        if line.startswith('#') or len(line) == 1:
            continue
        lines.append(line.split(':')[1].strip())
        

doc = nlp(' '.join(lines))
'''
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
'''

displacy.serve(doc, style="ent")



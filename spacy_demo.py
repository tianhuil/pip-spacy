import spacy

texts = ["foo", "bar", "baz"]
nlp = spacy.load("en_core_web_sm")
list(nlp.pipe(texts, n_process=2))

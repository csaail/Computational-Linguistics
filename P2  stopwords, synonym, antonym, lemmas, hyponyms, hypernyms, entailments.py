from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet, stopwords

print("Saail Chavan - KFPMSCCS016 CL_P2\n")
text = "Natural language processing, especially when Saail discusses it, is fascinating. It involves many tasks such as text classification, sentiment analysis, and more."

# Stop words removal
stop_words = set(stopwords.words('english'))
words = word_tokenize(text)
filtered_words = [word for word in words if word.casefold() not in stop_words]
print("Stopwords:\n", "original text:",text,"\nfiltered words:",filtered_words)

synonyms = []
antonyms = []
lemmas = []

# Synonyms and antonyms
for syn in wordnet.synsets("active"):   #synsets-syntax sets
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
        lemmas.append(l.name())

print("\nSynonyms of active:\n", set(synonyms))
print("\nAntonyms of active:\n", set(antonyms))

# Printing lemmas
print("\nLemmas of active:\n", set(lemmas))

# Hyponyms 
hypo = wordnet.synset('car.n.01').hyponyms()
print("\nHyponym of car:\n", hypo)

# Hypernyms
hyper = wordnet.synset('car.n.01').hypernyms()
print("\nHypernym of car:\n", hyper)

# Entailments
ent = wordnet.synset('snore.v.01').entailments()
print("\nEntailment of snore:\n", ent)

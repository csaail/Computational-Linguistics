#Code1:  Text preprocessing => removing stopwords and apply stemming, lemmitization

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
print("Saail Chavan - KFPMSCCS016 CL_P2\n")
text = "Natural language processing, especially when Saail discusses it, is
fascinating. It involves many tasks such as text classification, sentiment analysis,
and more."
stop_words = set(stopwords.words('english'))
words = word_tokenize(text)
filtered_words = [word for word in words if word.casefold() not in stop_words]
print("original text")
print(text)
print("after removing stopwords")
print(filtered_words)
porter_stemmer = PorterStemmer()
words = word_tokenize(text)
stemmed_words = [porter_stemmer.stem(word) for word in words]
print("after applying stemming")
print(stemmed_words)
lemmatizer = WordNetLemmatizer()
words = word_tokenize(text)
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print("after applying lemmitization")
print(lemmatized_words)



#Code 2: Semantic Relations: synonym, antonym, hyponyms, hypernyms and entailments.
from nltk.corpus import wordnet
synonyms = []
antonyms = []
for syn in wordnet.synsets("active"):
 for l in syn.lemmas():
 synonyms.append(l.name())
 if l.antonyms():
 antonyms.append(l.antonyms()[0].name())
print("Synonyms of active:",set(synonyms))
print("Antonyms of active:",set(antonyms))
hypo=wordnet.synset('car.n.01').hyponyms()
print("hyponym of car:",hypo)
hyper=wordnet.synset('car.n.01').hypernyms()
print("hypernym of car:",hyper)
ent=wordnet.synset('snore.v.01').entailments()
print("entailment of snore:",ent)

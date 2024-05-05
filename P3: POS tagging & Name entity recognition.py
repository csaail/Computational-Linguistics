#COde 1: POS TAGGING:
from nltk.tokenize import word_tokenize
from nltk import pos_tag
print("Saail Chavan - KFPMSCCS016 CL_P2\n")
text = input("Enter some text")
words = word_tokenize(text)
tagged_words = pos_tag(words)
print("tagged words:",tagged_words)

#COde 2: NER
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
text = input("enter some text")
words = word_tokenize(text)
tagged_words = pos_tag(words)
named_entities = ne_chunk(tagged_words)
print("Named Entities")
print(named_entities)

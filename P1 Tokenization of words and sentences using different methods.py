#Saail Chavan - KFPMSCCS016 CL_P1

import re  
from nltk.tokenize import word_tokenize , sent_tokenize
print("Saail Chavan - KFPMSCCS016 CL_P1")
text = "Hi this is Saail Chavan . This is an example of tokenization methods ."

tokens=text.split()
print("\noriginal text:", text)

print("\ntokenized using split()\n", tokens)

tokens = re.findall("[\w']+", text) 
print("\ntokenized using re.findall()\n", tokens)

tokens=word_tokenize(text)
print("\ntokenized using word_tokenize()\n",tokens)

print("\n\nsentence tokenization")

sents=text.split('.')
print("\noriginal text\n", text)

print("\ntokenized using split('.')\n", sents)

sents = re.compile('[.!?]').split(text)
print("\ntokenized using re.compile()\n",sents)

sents=sent_tokenize(text)
print("\ntokenized using sent_tokenize()\n",sents)


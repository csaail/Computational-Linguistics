import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

print("Saail Chavan - KFPMSCCS016 CL_P7")

# Sample text to summarize
text = """Humans communicate with each other using words and text.
The way that humans convey information to each other is called Natural Language.
Every day humans share a large quality of information with each other in various languages
as speech or text.
However, computers cannot interpret this data, which is in natural language,
as they communicate in 1s and 0s. The data produced is precious and can offer valuable insights.
Hence, you need computers to be able to understand, emulate and respond intelligently to human speech. 
Natural Language Processing or NLP refers to the branch of Artificial Intelligence
that gives the machines the ability to read, understand and derive meaning from human languages.
Natural language processing (NLP) is a machine learning technology that gives computers
the ability to interpret, manipulate, and comprehend human language.
Organizations today have large volumes of voice and text data from various
communication channels like emails, text messages, social media newsfeeds, video, audio, and more.
They use NLP software to automatically process this data, analyze the intent or
sentiment in the message, and respond in real time to human communication."""

stopWords = set(stopwords.words("english"))     
# Tokenizing the text into words
words = word_tokenize(text)

# Creating a frequency table to store word frequencies
freqTable = dict()

# Populating the frequency table with word frequencies
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

# Tokenizing the text into sentences
sentences = sent_tokenize(text)

# Calculating the value of each sentence based on word frequencies
sentenceValue = dict()
for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

# Calculating the average value of sentences
sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]
average = int(sumValues / len(sentenceValue))

# Generating the summary by selecting sentences with values greater than the average
summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (average)):
        summary += " " + sentence

# Printing the summary
print(summary)

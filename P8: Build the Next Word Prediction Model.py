import nltk
# Tokenize the text into words
words = nltk.word_tokenize(text)
# Preprocess the words (convert to lowercase, remove punctuation)
words = [word.lower() for word in words if word.isalnum()]
# Define the order of the N-gram model (N=2 for bigrams)
N = 2
# Create N-grams from the tokenized words
ngrams_list = list(ngrams(words, N))
# Create a defaultdict to store N-grams and their frequency
ngram_freq = defaultdict(int)
for ngram in ngrams_list:
 ngram_freq[ngram] += 1
# Define Function
def predict_next_word(prefix):
 # Filter N-grams that start with the given prefix
 matching_ngrams = [(ngram, freq) for ngram, freq in ngram_freq.items() if
ngram[:-1] == prefix]
 if not matching_ngrams:
 return "No prediction available."
 print(matching_ngrams)
 # Sort N-grams by frequency in descending order
 sorted_ngrams = sorted(matching_ngrams, key=lambda x: x[1], reverse=True)
 print(sorted_ngrams)
 # Select the N-gram with the highest frequency as the prediction
 prediction = sorted_ngrams[0][0][-1]
 return prediction
# You can use this code snippet to interactively test the model with user input
user_input = input("Enter a prefix for next-word prediction: ").lower().split()
if len(user_input) != N - 1:
 print("Please enter a valid prefix.")
else:
 prefix = tuple(user_input)
 prediction = predict_next_word(prefix)
 print(f"Next word prediction: {prediction}")

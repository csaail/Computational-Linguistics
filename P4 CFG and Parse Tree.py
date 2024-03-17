from nltk import CFG
from nltk.parse.generate import generate
from nltk.parse import RecursiveDescentParser
print("Saail Chavan - KFPMSCCS016 CL_P4\n")

# Define a context-free grammar
grammar = CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "admires" | "loves" | "hates"
    NP -> "Alice" | "Bob" | "Charlie" | Det N | Det N PP
    Det -> "the" | "a"
    N -> "cat" | "dog" | "rabbit"
    P -> "on" | "under" | "beside"
""")

# Generate and print example sentences based on the defined grammar
print("Generated sentences:")
for sentence in generate(grammar, n=10):
    print(' '.join(sentence))

# Parse a given sentence using the Recursive Descent Parser
rd_parser = RecursiveDescentParser(grammar)

# Input sentence
input_sentence = "Alice loves the cat".split()

# Parse the input sentence and print the parse trees
print("\nParse tree for the input sentence:")
for tree in rd_parser.parse(input_sentence):
    print(tree)


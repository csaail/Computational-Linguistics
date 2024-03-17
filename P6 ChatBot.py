import nltk
from nltk.chat.util import Chat, reflections

print("Saail Chavan - KFPMSCCS016 CL_P6")

pairs = [
    [r"my name is (.*)",
     ["Hello %1, How are you today?"]
    ],
    [r"hi|hey|hello",
     ["Hello", "Hey there"]
    ],
    [r"what is your name ?",
     ["I'm Sheldon, your friendly chatbot."]
    ],
    [r"how are you ?",
     ["I'm fine"]
    ],
    [r"sorry (.*)",
     ["Its alright", "Its OK, never mind"]
    ],
    [r"i am fine",
     ["Great to hear that", "Awesome!"]
    ],
    [r"what can you do ?",
     ["I can have a conversation with you. You can ask me about anything or just chat for fun!"]
    ],
    [r"tell me a joke",
     ["Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [r"how old are you ?",
     ["I don't have an age. I'm just a computer program."]
    ],
    [r"what is the weather today ?",
     ["I'm sorry, I don't have access to real-time data. You can check a weather website or app for that!"]
    ],
    [r"thanks|thank you",
     ["You're welcome!", "No problem!"]
    ],
    [r"bye|goodbye",
     ["Goodbye! Take care.", "Bye bye, have a great day!"]
    ],
    [r"quit",
     ["Bye bye, take care. See you soon :) "]
    ],
]

Chatbot = Chat(pairs, reflections)
Chatbot.converse()

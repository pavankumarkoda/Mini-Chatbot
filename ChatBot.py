
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chitti and I'm a chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ],
    [
        r"hi|hey|hello|namesthe|vanakam ",
        ["Hello", "Hey there", "Hi, how can I assist you today?, namesthe"]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program :)", "I'm ageless!"]
    ],
    [
        r"quit|end|bye|tata|end chat",
        ["Bye, take care. See you soon :) ", "It was nice talking to you. Goodbye!"]
    ],
    [
        r"(.*) (location|city) ?", 
        ["I'm a virtual assistant, so I don't have a physical location.",]
    ],
    [
        r"how old are you ?",
        ["I'm timeless, but thank you for asking!",]
    ],
    [
        r"tell me about yourself",
        ["I'm an AI chatbot created to assist you with queries. How can I help you today?",]
    ],
    [
        r"(.*) (weather|temperature) (.*)",
        ["I'm sorry, I don't have access to real-time weather information.",]
    ],
    [
        r"(.*) advice",
        ["Sure, my advice would be to stay curious and keep learning!",]
    ],
    [
        r"(.*) (movie|film) (.*)",
        ["I enjoy movies too! Do you have a favorite genre?",]
    ],
    [
        r"(.*) do you like (.*)",
        ["I'm a chatbot, so I don't have personal preferences. But tell me more about %2!",]
    ],
    [
        r"(.*) (food|cuisine) (.*)",
        ["I don't eat food, but I can help you find recipes or recommend restaurants!",]
    ],
    [
        r"(.*) (sport|game) (.*)",
        ["I'm more into chatting than sports or games, but I can chat about them!",]
    ],
    [
        r"who created you ?",
        ["I was created by developer pavan at Adroitec Information Systems Pvt. Ltd.",]
    ],
    [
        r"how can I contact you ?",
        ["You can contact my creators at contact@adroitecengg.com",]
    ],
    [
        r"(.*) (technology|programming) (.*)",
        ["I'm knowledgeable about various technologies and programming languages. What specifically are you interested in?",]
    ],
    [
        r"(have you had your) (lunch|dinner|breakfast|bf)",
        ["thaks for asking, as a chat bot we dont need food we only need battery"]
    ],
    [
        r"where you stay|live",
        ["i'll stay here only"]
    ],
    [
        r"are you a person",
        [" no im  a virtual machine"]
    ],
]

# Reflections for pronouns
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
  
}

# Create a chatbot function
def chatbot():
    print("Hi, I'm Chitti the Chatbot! How can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()

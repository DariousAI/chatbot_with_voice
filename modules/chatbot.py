import random

# A very simple response generation function
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I assist you?"],
    "how are you": ["I'm just a bot, but I'm doing great! How can I help you?"],
    "bye": ["Goodbye!", "See you soon!", "Take care!"],
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I don't understand that."
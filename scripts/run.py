import sys
import os

# Add the base project directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.speech import listen, speak
from modules.chatbot import get_response

def run_chatbot():
    while True:
        user_input = listen()
        if user_input == "":
            continue
        if "bye" in user_input.lower():
            speak("Goodbye! Talk to you soon!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")
        speak(response)

if __name__ == "__main__":
    print("Say 'hello' to start a conversation or 'bye' to end it.")
    run_chatbot()



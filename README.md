# Chatbot with Voice Interaction

This repository contains a simple chatbot with voice interaction capabilities. The chatbot uses Google's Text-to-Speech (gTTS) for responding verbally and SpeechRecognition to understand spoken input from the user.

## Features

- **Voice Input**: Listens to your voice input and converts it to text.
- **Voice Output**: Uses `gTTS` to generate a spoken response.
- **Basic Conversational Capabilities**: Responds to simple greetings and questions.

## Installation

To set up and run the project on your local machine, follow these steps:

### Step 1: Clone the Repository

```sh
git clone https://github.com/username/chatbot_with_voice.git
cd chatbot_with_voice
```

### Step 2: Create a Virtual Environment

Create a virtual environment to keep your dependencies organized:

```sh
python -m venv venv
```

### Step 3: Activate the Virtual Environment

- **Windows**:
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```sh
  source venv/bin/activate
  ```

### Step 4: Install the Required Packages

Install the dependencies using `pip`:

```sh
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, you can install the necessary packages individually:

```sh
pip install gtts SpeechRecognition pyaudio
```

## Running the Chatbot

To start the chatbot, ensure your virtual environment is active and run:

```sh
python scripts/run.py
```

The chatbot will listen to your voice and respond. You can say "bye" to end the conversation.

## Project Structure

```
chatbot_with_voice/
├── data/
├── modules/
│   ├── speech.py
│   └── chatbot.py
├── scripts/
│   └── run.py
├── venv/
├── response.mp3
├── .gitignore
└── README.md
```

## Requirements

- Python 3.6+
- Libraries:
  - `gTTS`
  - `SpeechRecognition`
  - `PyAudio`

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.


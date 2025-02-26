# Jarvis AI Assistant

Jarvis is a personal AI assistant that can open websites, fetch news, play music, and respond to user commands using voice recognition.

## Features
- Voice-controlled virtual assistant
- Opens popular websites (Google, YouTube, LinkedIn, Facebook)
- Fetches news headlines from NewsAPI
- Plays music using a predefined library
- AI-powered responses via Cohere API
- Text-to-speech using gTTS and pygame

## Installation

### **Step 1: Clone the Repository**
```sh
git clone https://github.com/sagarc2426/Jravis-AI-assistance-using-python.git
cd Jravis-AI-assistance-using-python
```

### **Step 2: Create a Virtual Environment (Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### **Step 3: Install Dependencies**
```sh
pip install -r requirements.txt
```

If `requirements.txt` is missing, manually install the required libraries:
```sh
pip install speechrecognition webbrowser pyttsx3 requests gtts pygame cohere
```

## Configuration
1. **API Keys**:
   - Update `newsapi` variable in `main.py` with your NewsAPI key.
   - Update the Cohere API key in `aicommnad()` function.

2. **Music Library**:
   - Ensure `musicLibrary.py` exists and contains a dictionary with song names mapped to URLs.

## Usage
Run the assistant with:
```sh
python main.py
```
It will listen for the wake word **"Jarvis"** before processing commands.

## Commands Supported
- "Open Google"
- "Open YouTube"
- "Open LinkedIn"
- "Open Facebook"
- "Play [song_name]"
- "News"
- "How are you?"
- "Who are you?"
- "What can you do?"
- "Exit" or "Stop" to quit

## License
This project is licensed under the MIT License.

---

### Notes
- Ensure your microphone is working properly.
- This project requires an internet connection for news fetching and AI responses.

Happy Coding! 🚀


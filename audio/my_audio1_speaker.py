#  Audio AI
# source .venv/bin/activate && pip install pyttsx3

import pyttsx3

def hello_harry():
    engine = pyttsx3.init()
    text = "Hello Martin. How are you? What is your hobby? I'm a Star Wars fan."

    # Set Bahh voice (sheep-like sound)
    #engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Bahh')
    #engine.setProperty('voice', 'com.apple.speech.synthesis.voice.BadNews')
    #engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Bells')
    #engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Bubbles')
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Trinoids')

    # Make it sound more dog-like by adjusting properties
    #engine.setProperty('rate', 400)  # Faster speech (default is ~200)
    #engine.setProperty('pitch', 0.5)  # Lower pitch (if supported)
    #engine.setProperty('volume', 1.0)  # Max volume

    engine.say(text)
    #engine.save_to_file(text, "./hello_harry.mp3", name="Test")
    engine.runAndWait()

hello_harry()

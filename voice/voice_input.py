# voice/voice_input.py

import speech_recognition as sr

def listen_to_user():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎤 Listening... Speak now!")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return "Sorry, I didn't understand that."
    except sr.RequestError:
        return "Sorry, there was a problem with the recognition service."

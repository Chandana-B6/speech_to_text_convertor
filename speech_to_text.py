import SpeechRecognition as sr   # REASON: Provides easy-to-use methods for speech-to-text

# Create a recognizer instance
recognizer = sr.Recognizer()  # REASON: Required to process and understand audio input

# Load audio file
with sr.AudioFile("sample.wav") as source:  # REASON: Reads the .wav file
    print("Listening to audio...")
    audio = recognizer.record(source)  # REASON: Records the full audio content into memory

    try:
        # Recognize speech using Google python Web API (no key needed)
        text = recognizer.recognize_google(audio)  # REASON: Uses a free pre-trained model from Google to convert speech to text
        print("Transcribed Text:")
        print(text)
    except sr.UnknownValueError:
        print("Speech not recognized.")  # REASON: Error handling for unclear or empty audio
    except sr.RequestError as e:
        print(f"API error: {e}")  
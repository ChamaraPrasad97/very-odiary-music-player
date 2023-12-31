import speech_recognition as sr
import keyboard

recognizer = sr.Recognizer()

def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening for keyword...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=10)
    return audio

def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        print("Error; {0}".format(e))
        return ""

def process_voice_command(text):
    if "turn on" in text.lower():
        print("Keyword detected! Simulating key press.")
        keyboard.press_and_release('a')
    else:
        print("Keyword not detected.")

def main():
    while True:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        process_voice_command(text)

if __name__ == "__main__":
    main()


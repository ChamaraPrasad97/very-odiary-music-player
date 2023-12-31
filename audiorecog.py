import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Say something (say 'stop' to end):")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)

        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            
            # Check for the stop command
            if "stop" in text.lower():
                print("Stopping the program.")
                break

        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print("Error; {0}".format(e))

if __name__ == "__main__":
    recognize_speech()

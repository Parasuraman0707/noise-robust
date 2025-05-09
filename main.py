import speech_recognition as sr
import time

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("recognizer must be Recognizer instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("microphone must be Microphone instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Say something!")
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

if _name_ == "_main_":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    for i in range(3):
        print(f"Attempt {i+1}...")
        time.sleep(0.1)
        response = recognize_speech_from_mic(recognizer, microphone)
        if response["success"]:
            print("You said: {}".format(response["transcription"]))
            break
        else:
            print("Error: {}".format(response["error"]))
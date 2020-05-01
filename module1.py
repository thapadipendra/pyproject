import speech_recognition as sr
 
 
sound="speech.wav"
 
def main():
    global sound  
 
    r = sr.Recognizer()
 
 
    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)
 
 
        print("Converting Audio To Text ..... ")
 
 
        audio = r.listen(source)
 
 
 
    try:
        print("Converted Audio Is : \n" + r.recognize_google(audio))
        return(r.recognize_google(audio))
 
 
    except Exception as e:
        print("Error {} : ".format(e) )
 
 
 
if __name__ == "__main__":
    main()
#using version 3.10

import speech_recognition as sr
import translatee as tr
import languag

r = sr.Recognizer()

def transPrompt(lang, wordss):
    if 'en' not in lang:
        transAsk = input('Do you want to translate to english? y or n \n')
        if transAsk == 'y':
            print('translating')
            tr.main(wordss)
        elif transAsk == 'n':
            return
    else:
        return

def listenMic():
    #get audio from the microphone
    with sr.Microphone() as source:
        print("Speak")
        audio = r.listen(source, 10, 10)
    printText(audio)

def wavFile():
    #get audio from wav file
    filename = input("input the .wav filename and its path and remove quotes \n")
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
    printText(audio_data)

def printText(audio):
    lang = input("Please specify the language as shown below \n " + languag.langua + "\n and others not included \n for english type en-US \n Please input --> ")
    wordss = r.recognize_google(audio, language=lang)
    try:
        print("You said '" + wordss + "'")

    except sr.UnknownValueError as e:
        print("could not understand audio; {0}".format(e))

    except sr.RequestError as e:
        print("could not request results; {0}".format(e))

    #prompt for translating language to english
    transPrompt(lang, wordss)
    #to reask   
    choose()

    
#ask if the user wants to input file or talk to the mic or quit

def choose():
    choice = input("""type 'm' if you want to talk to the mic \n or 'n' if you want to input an audio file \n or q if you want to quit \n""")

    if choice == 'm':
        listenMic()
    elif choice == 'n':
        wavFile()
    elif choice == 'q':
        quit()
choose()

#goals

#make it to be able to listen in other languages and ask if you want to translate
#to english
    

    

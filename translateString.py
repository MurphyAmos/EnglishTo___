import pyaudio
import speech_recognition as sr
from deep_translator import GoogleTranslator

class multiWordTranslate:
    def listen():
        def findLanguage():
            #making global variables to access language variables 
            global lanDictIndex    
            global Language
            global lanDictIndex            
            #get language to translate to 
            Language = input("Translate To: ").lower()
            #language dict to look through for translation
            langDict = {"english":"en", "hindi":"hi", "spanish":"es", "dutch":"de", "french": "fr", "russian":"ru", "polish":"pl", "chinese":"zh"}
            #for loop to look through the langDict for language
            for x in langDict:
                #while we look through if index match language landictIndex  = langDict[of full language name to return dict value]
                if x == Language:
                    lanDictIndex = langDict[Language]               
                    return lanDictIndex
        global stringOfVoice
        UserVoiceHolder= sr.Recognizer()
        with sr.Microphone() as source:
            audioHolder = UserVoiceHolder.listen(source)
            try:
                stringOfVoice = UserVoiceHolder.recognize_sphinx(audioHolder)
            except UserVoiceHolder.UnknownValueError:
                print("No input received")
            finally:
                if bool(stringOfVoice) != None:
                    print("Translate: " , stringOfVoice)
                    findLanguage()
                    return stringOfVoice
                else:
                    print("No input Was Found")

    def returnTranslateString(string):
        global translatedString        
        translatedString = GoogleTranslator(source='auto',target = lanDictIndex).translate(string)
        print(f"Translated to {Language.title()}: {translatedString}")
        return translatedString

    returnTranslateString(listen())

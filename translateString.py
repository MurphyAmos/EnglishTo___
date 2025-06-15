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
        #making a string of what was said 
        global stringOfVoice
        #creating voice holder on the mic, taking that an putting it into a audioholder... then turning audio into text and holding it into the stringOfVoice 
        UserVoiceHolder= sr.Recognizer()
        with sr.Microphone() as source:
            audioHolder = UserVoiceHolder.listen(source)
            try:
                ##tryging to put the audio into the string if there is some 
                stringOfVoice = UserVoiceHolder.recognize_sphinx(audioHolder)
            except UserVoiceHolder.UnknownValueError:
                #if not say so
                print("No input received")
            finally:
                #if there is a string at the end return the string!
                if bool(stringOfVoice) != None:
                    print("Translate: " , stringOfVoice)
                    findLanguage()
                    return stringOfVoice
                else:
                    print("No input Was Found")
    
    def returnTranslateString(string):
        #translated string holder
        global translatedString       
        #use googlesTramlater to translate my Userpicked language and return the string
        translatedString = GoogleTranslator(source='auto',target = lanDictIndex).translate(string)
        print(f"Translated to {Language.title()}: {translatedString}")
        return translatedString

    #run Return and use the output of multiwordString as the input of it
    returnTranslateString(listen())

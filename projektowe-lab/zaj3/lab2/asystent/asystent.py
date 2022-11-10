#!/usr/bin/python3
# -*- coding: utf-8 -*-

end = None

import pyttsx3 as tts
import speech_recognition as sr
import time


################################################################################

def asystent(pytanie):
  if pytanie in ['godzina','która godzina','która jest godzina','jaki jest czas']:
    return f'Jest godzina {time.ctime()[11:16]}'
  end
  return 'Niestety nie znam odpowiedzi'
end


################################################################################

def main():

  TTS = tts.init()
  TTS.setProperty('volume',0.7)
  TTS.setProperty('rate',190)

  STT = sr.Recognizer()


  while True:
    tekst = input(">>")
    if len(tekst)>0:
      odp = asystent(tekst)
      TTS.say(odp)
      TTS.runAndWait()

    else:
      with sr.Microphone() as source:
        print("slucham ...")
        audio = STT.listen(source)
        try:
          tekst = STT.recognize_google(audio, language='pl_PL')
          print(tekst)
          odp = asystent(tekst)
          TTS.say(odp)
          TTS.runAndWait()

        except sr.UnknownValueError:
          print('nie rozumiem')
        except sr.RequestError as e:
          print('error:',e)

  end
end

################################################################################

main()

################################################################################

from speech_recognition import Recognizer, AudioFile
import os

root_dir = 'files'
filenames = os.listdir(root_dir)

# No need to initialize on every iteration
recognizer = Recognizer()

for filename in filenames:

  with AudioFile(f'{root_dir}/{filename}') as audio_file:
    audio = recognizer.record(audio_file)

    text = recognizer.recognize_google(audio)
    if 'cable' in text:
      print(filename)

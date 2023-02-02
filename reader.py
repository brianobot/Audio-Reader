"""
Reader Class to generate reader instances, capable of reading different text file format in customizable speech rate and tones

Copyright @2023 Brian Obot <brianobot9@gmail.com>
"""
import sys
import pyttsx3
import PyPDF2
import random


READER_NAMES = ['David', 'Okon', 'Akpan', 'Paul']


class Reader:
    def __init__(self, file=None, name=None, *args, rate=165, **kwargs):
        self.file = file
        self.name = name or random.choice(READER_NAMES)
        self.speaker = pyttsx3.init()
        for (attr, value) in kwargs:
            self.speaker.setProperty(attr, value)
            print(f"{attr} = {value}")
        self.introduce_self()

    def introduce_self(self):
        intro = f"""Hello there! I am {self.name}.
             Software Audio Reader to enable you to listen to your favourite books.

            I was created and maintained by Brian Obot <brianobot9@gmail.com>"""

        self.speaker.say(intro)
        self.speaker.runAndWait()

    def set_file(self, file):
        self.file = file
        self.process_file()

    def read(self):
        if self.file.endswith('.pdf'):
            pdfReader = PyPDF2.PdfFileReader(open(self.file, 'rb'))
            for page_num in range(pdfReader.numPages):
                try:
                    data = pdfReader.getPage(page_num).extractText()
                    self.speaker.say(data)
                    self.speaker.runAndWait()
                except KeyboardInterrupt:
                    self.speaker.say("Ending Reader")
                    self.skeaper.runAndWait()
                    sys.exit()    
        else:
            with open(self.file, encoding="utf-8") as data:
                for line in data:
                    try:
                        self.speaker.say(line)
                        self.speaker.runAndWait()
                    except KeyboardInterrupt:
                        self.speaker.say("Ending Reader")
                        self.skeaper.runAndWait()
                        sys.exit()    

        # Stop the speaker when reading is completed
        self.speaker.stop()
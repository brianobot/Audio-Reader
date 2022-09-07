import pyttsx3
import PyPDF2
import sys

speaker = pyttsx3.init()
rate = speaker.setProperty('rate', 165)


introduction = 'Hello there! I am David. A Software Reader to enable you to listen to your favourite books, Written and owned by Brian'
speaker.say(introduction)
speaker.runAndWait()

def main(file_name):
    if file_name.endswith('.pdf'):
        pdfReader = PyPDF2.PdfFileReader(open(file_name, 'rb'))
        for page_num in range(pdfReader.numPages):
            data = pdfReader.getPage(page_num).extractText()
            speaker.say(data)
            speaker.runAndWait()
    else:
        with open(file_name) as file:
            data = file.readlines()
            for line in data:
                speaker.say(line)
                speaker.runAndWait()
    speaker.stop()

if __name__ == "__main__":
    file_name = sys.argv[1]
    main(file_name)

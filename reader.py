import pyttsx3
import PyPDF2
import sys
import yaml

speaker = pyttsx3.init()
rate = speaker.setProperty('rate', 165)

#to create a sensation of relation, the user can change the reader's name 
reader_name = "David"

introduction = f"""Hello there! I am {reader_name}.
    A Software Reader to enable you to listen to your favourite books,
    Written and Maintained by Brian Obot <brianobot9@gmail.com>"""

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
        with open(file_name, encoding="utf-8") as file:
            data = file.readlines()
            for line in data:
                speaker.say(line)
                speaker.runAndWait()
    speaker.stop()

if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except:
        file_name = input("Enter Complete path to File to be read: ")
        
    print("_____________________________")
    print(f"starting {file_name}")
    print("_____________________________")
    main(file_name)

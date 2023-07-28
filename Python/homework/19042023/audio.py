import pyttsx3
import pyPDF2
from tkinter.filedialog import *

book=askopenfilename()
pdfreader=pyPDF2.PdfFilrReader(book)
pages=pdfreader.numpages

for num in range(0,pages):
    page=pdfreader.getPage(num)
    text=page.extractText()
    player=pyttsx3.init
    player.say(text)
    player.runAndWait()
                           



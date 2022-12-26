# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from   PyQt5.QtWidgets import *
from   PyQt5.QtGui     import *
from   PyQt5.QtCore    import *
from PyQt5.QtMultimedia import *

import random

import PyPDF2

import speech_recognition as sr
import time
import pyaudio
from translate import Translator

import googletrans

from gtts import gTTS
import os


import nltk
import random
import string 
import wikipedia
# from termcolor import colored
import warnings
from textblob import TextBlob
import textblob

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity




s="BOT:Hello,choose languages and hit record for topic...\n"
a="KANNADA"
o="HINDI"

f=""
raw=""
file=""

topic=""
que=""
flag=False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 720)
        MainWindow.setStyleSheet("#centralwidget{background-color:black;}\n"
".QLabel{color:White;}\n"
"#pushButton{background-color:rgba(0, 175, 250, 1);border-radius:30}\n"
"\n"
"#pushButton:hover{background-color:rgba(0, 175, 250, 0.5);border-radius:30}\n"
"\n"
"#pushButton_2{background-color:rgba(0, 175, 250, 1);border-radius:20;}\n"
"\n"
"#pushButton_2:hover{background-color:rgba(0, 175, 250, 0.5);border-radius:30}\n"
"\n"
"#pushButton_3{background-color:rgba(0, 175, 250, 1);border-radius:20;}\n"
"\n"
"#pushButton_3:hover{background-color:rgba(0, 175, 250, 0.5);border-radius:30}\n"
"\n"


"#pushButton_5{background-color:rgba(0, 175, 250, 1);border-radius:30}\n"
"\n"
"#pushButton_5:hover{background-color:rgba(0, 175, 250, 0.5);border-radius:30}\n"
"\n"
".QComboBox{border-radius:10}\n"
"\n"
".QTextEdit{background-color:rgba(0, 0, 255, 0.3);color:white;}\n"
"\n"
".comboBox{color:red}")
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
        #=------background gif---
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(0, -230, 0, 0))
        self.label2.setMinimumSize(QtCore.QSize(1280,1280))
        self.label2.setMaximumSize(QtCore.QSize(1280,1280))
        self.label2.setObjectName("label2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        

        self.movie1 = QMovie(r"C:\Users\AASHISH\Desktop\Project Demo\wallpaper.gif")
        self.movie1.setScaledSize(QSize().scaled(1100,1100, Qt.KeepAspectRatio))
        self.label2.setMovie(self.movie1)
        self.movie1.start()
        #=---------
        
        
        
        
        
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 580, 121, 101))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/feather/mic.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 20, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 110, 1041, 441))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(font)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 580, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
                
                
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(760, 580, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        
        
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 20, 151, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1145, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)
        
        
        
        #=---------GIF robot:
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(970, 50, 0, 0))
        self.label1.setMinimumSize(QtCore.QSize(170, 170))
        self.label1.setMaximumSize(QtCore.QSize(170, 170))
        self.label1.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        

        self.movie2 = QMovie(r"C:\Users\AASHISH\Desktop\Project Demo\chatbot-marketing.gif")
        self.movie2.setScaledSize(QSize().scaled(150, 150, Qt.KeepAspectRatio))
        self.label1.setMovie(self.movie2)
        self.movie2.start()
        #=---------
        
        
        
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        global s
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "REC"))
        self.pushButton_2.setText(_translate("MainWindow", "Input language"))
        self.pushButton_3.setText(_translate("MainWindow", "Output language"))
        self.label.setText(_translate("MainWindow", "WELCOME USER!"))
        self.textEdit.setText(s)

        
        self.textEdit.setText(s)
        
        
        self.pushButton.clicked.connect(self.record)
        self.pushButton_2.clicked.connect(self.chooseinplang)
        self.pushButton_3.clicked.connect(self.chooseoutlang)
        self.pushButton_5.setText(_translate("MainWindow", "UPLOAD FILE"))
        self.pushButton_5.clicked.connect(self.pdf)


    def pdf(self):
        
        global s
        global o 
        
        file , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                                    "", "All Files (*);;pdf Files (*.pdf)")
        if check:
                file=open(file,'rb')
                reader = PyPDF2.PdfFileReader(file)
                page1 = reader.getPage(0)
                print(reader.numPages)
                print(page1.extractText())
                f = open('test1.txt', 'a')
                f.write(page1.extractText())
                for i in range(0,reader.numPages-1):
                    page = reader.getPage(i)
                    f.write(page.extractText())
                f.close()
                g = open('test1.txt','r')
                text = g.read(10000)
                # l1 = []
                # for i in text.split('\n\n'):
                #     l1.append(i)
                # print(l1)
                
                dicti={'ASSAMESE':'as',
                'BENGALI':'bn',
                'BODO':'brx',
                'DOGRI':'doi',
                'GUJARATI':'gu',
                'HINDI':'hi',
                'KANNADA':'kn',
                'KASHMIRI':'ks',
                'KONKANI':'gom',
                'MAITHILI':'mai',
                'MALAYALAM':'ml',
                'MANIPURI':'mni',
                'MARATHI':'mr',
                'NEPALI':'ne',
                'ORIYA':'or',
                'PUNJABI':'pa',
                'SANSKRIT':'sa',
                'SANTALI':'sat',
                'SINDHI':'sd',
                'TAMIL':'ta',
                'TELEGU':'te',
                'URDU':'ur',
                'ENGLISH':'en'}   


                x=TextBlob(text)
                
                o=o.upper()
                x= x.translate(from_lang='en',to=dicti[o])
                # translation = translator.translate(l1[i])
                print("The translated langtext is:",x)
                s=s+"\n"+str(x)
                self.textEdit.setText(s)

                        
                
        
        

    def chooseinplang(self):    
        
        global s
        global a
        r = sr.Recognizer()

        print("\nStart speaking:\n")

        start=time.time()
        with sr.Microphone() as source:
                # read the audio data from the default microphone
                audio_data = r.record(source, duration=3)
                print("Recognizing...:")
                # convert speech to langtext
                
                try:
                    langtext = r.recognize_google(audio_data,language='en-in')
                    print("You said:",langtext)
                    
                    s=s+"\nBOT:you have choosen "+langtext+" as your input language"
                    self.textEdit.setText(s)
                    a=langtext
                except:
                    s=s+"\nBOT:sorry could you repeat?"
                    self.textEdit.setText(s)
                    print("sorry couldnt hear your voice")
                    
                    
    def chooseoutlang(self):    
        
        global s
        global o
        r = sr.Recognizer()

        print("\nStart speaking:\n")

        start=time.time()
        with sr.Microphone() as source:
                # read the audio data from the default microphone
                audio_data = r.record(source, duration=3)
                print("Recognizing...:")
                # convert speech to langtext
                
                try:
                    langtext = r.recognize_google(audio_data,language='en-in')
                    print("You said:",langtext)
                    
                    s=s+"\nBOT:you have choosen "+langtext+" as your output language"
                    self.textEdit.setText(s)
                    o=langtext
                except:
                    s=s+"\nBOT:sorry could you repeat?"
                    self.textEdit.setText(s)
                    print("sorry couldnt hear your voice")               
                    
                    
    def record(self):
        global s
        global a
        global o
                
        if(os.path.exists('hello.mp3')):
            os.remove('hello.mp3')

        
        a=a.upper()
        o=o.upper()
        
        self.textEdit.setText(s)
        
        
        self.label1.setGeometry(QtCore.QRect(955, 35, 0, 0))

        n=random.randint(2,4)
        
        self.movie2 = QMovie("robot"+str(n)+".gif")
        self.movie2.setScaledSize(QSize().scaled(190, 190, Qt.KeepAspectRatio))
        self.label1.setMovie(self.movie2)
        self.movie2.start()
        

        langtext=""
        lan={'ASSAMESE':'as-IN',
                'BENGALI':'bn-IN',
                'BODO':'brx-IN',
                'DOGRI':'doi-IN',
                'GUJARATI':'gu-IN',
                'HINDI':'hi-IN',
                'KANNADA':'kn-IN',
                'KASHMIRI':'ks-IN',
                'KONKANI':'gom-IN',
                'MAITHILI':'mai-IN',
                'MALAYALAM':'ml-IN',
                'MANIPURI':'mni-IN',
                'MARATHI':'mr-IN',
                'NEPALI':'ne-IN',
                'ORIYA':'or-IN',
                'PUNJABI':'pa-IN',
                'SANSKRIT':'sa-IN',
                'SANTALI':'sat-IN',
                'SINDHI':'sd-IN',
                'TAMIL':'ta-IN',
                'TELEGU':'te-IN',
                'URDU':'ur-IN',
                'ENGLISH':'en-IN'}
            
            
            # user_input=input("enter the language you are going to speak in: ")
            # a=user_input.upper()
            
            #a=input("SELECT LANGUAGE: ")
            # if(a not in lan.keys()):
            #     print("sorry not available")
            # else:
        r = sr.Recognizer()

                # Reading Microphone as source
                # listening the speech and store in audio_langtext variable
        print("\nStart speaking:\n")

        start=time.time()
        with sr.Microphone() as source:
                # read the audio data from the default microphone
                audio_data = r.record(source, duration=5)
                print("Recognizing...:")
                # convert speech to langtext
                
                try:
                    langtext = r.recognize_google(audio_data,language=lan[a])
                    print("You said:",langtext)
                    
                    # if(topic==""):
                    #     topic=langtext
                    #     s=s+"\nBot:The topic you selected:"+topic
                    #     self.textEdit.setText(s)
                     
                except:
                    s=s+"\nBOT:sorry could you repeat?"
                    self.textEdit.setText(s)
                    print("sorry couldnt hear your voice")
                
               
            #TRANSLATION:--------------------------------


        dicti={'ASSAMESE':'as',
                'BENGALI':'bn',
                'BODO':'brx',
                'DOGRI':'doi',
                'GUJARATI':'gu',
                'HINDI':'hi',
                'KANNADA':'kn',
                'KASHMIRI':'ks',
                'KONKANI':'gom',
                'MAITHILI':'mai',
                'MALAYALAM':'ml',
                'MANIPURI':'mni',
                'MARATHI':'mr',
                'NEPALI':'ne',
                'ORIYA':'or',
                'PUNJABI':'pa',
                'SANSKRIT':'sa',
                'SANTALI':'sat',
                'SINDHI':'sd',
                'TAMIL':'ta',
                'TELEGU':'te',
                'URDU':'ur',
                'ENGLISH':'en'}

        for i in dicti:
                    if i in dicti:
                        # user_input=input("enter the language you are going to speak in: ")
                        # capital=user_input.upper()


                        # translator= Translator(from_lang=dicti[a],to_lang='en')
                
                        # # langtext=input("Enter your langtext in your language: ")
                        # translation = translator.translate(langtext)
                        # print("The translated langtext is:",translation)
                        
                        
                        x=TextBlob(langtext)
                        x= x.translate(from_lang=dicti[a],to='en')
                        # translation = translator.translate(l1[i])
                        print("The translated langtext is:",x)
                        s=s+"\n"+str(x)
                        self.textEdit.setText(s)
                            
                        
                        
                        s=s+"\nBOT:in "+o+":"+str(x)
                        self.textEdit.setText(s)
                        
                        


                        warnings.filterwarnings('ignore')

                        
                        ip=str(x.correct())

                      

                        wikipedia.set_lang("en")
                        f=str(wikipedia.summary(ip,sentences=1))
                        raw=f.lower()
                        print(f)
                        
                        s=s+"\n"+f  
                        
                        # translator= Translator(from_lang='en',to_lang=dicti[o])
                        # translation = translator.translate(raw)
                        # print("The translated langtext is:",translation)
                        
                        
                        x=TextBlob(raw)
                        x= x.translate(from_lang='en',to=dicti[o])
                        # translation = translator.translate(l1[i])
                        print("The translated langtext is:",x)
                        s=s+"\n"+str(x)
                        self.textEdit.setText(s)
                        
                        
                        # s=s+"\n"+
                        # self.textEdit.setText(s)

                        
                        # nltk.download('punkt')                # first-time use only
                        # nltk.download('wordnet')              # first-time use only
                        # sent_tokens = nltk.sent_tokenize(raw)        # converts to list of sentences 
                        # word_tokens = nltk.word_tokenize(raw)        # converts to list of words


                        # lemmer = nltk.stem.WordNetLemmatizer()
                        # def LemTokens(tokens):                #Lemmatizing
                        #     return [lemmer.lemmatize(token) for token in tokens]
                        # remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
                        # def LemNormalize(text):               #Tokenizing
                        #     return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


                        # def response(user_response):#User-Response function
                            
                        #     global s
                            
                        #     wiki_response=''
                        #     sent_tokens.append(user_response)
                        #     TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
                        #     tfidf = TfidfVec.fit_transform(sent_tokens)
                        #     vals = cosine_similarity(tfidf[-1], tfidf)
                        #     idx=vals.argsort()[0][-2]
                        #     flat = vals.flatten()
                        #     flat.sort()
                        #     req_tfidf = flat[-2]
                            
                        #     if(req_tfidf==0):
                        #         wiki_response=wiki_response+"I am sorry! I don't understand you"
                        #         return wiki_response
                        #     else:
                        #         wiki_response = wiki_response+sent_tokens[idx]
                        #         return wiki_response


                        # flag=True
                        
                        # user_response = translation
                        # user_response=user_response.lower()
                        # user_response=str(TextBlob(user_response).correct())

                        #if(user_response!='bye'):
                                # if(user_response=='thanks' or user_response=='thank you' ):
                                #     # flag=False
                                #     print(colored("WIKI-BOT: You are welcome..",'cyan'))
                                # else:
                        # print("this is the output:\n"+response(user_response))
                        # self.textEdit.setText(s)
                        # sent_tokens.remove(user_response)


                        print(str(x))
                        
                        tts = gTTS(str(x), lang=dicti[o],tld='co.in', slow=False )
                        tts.save('hello.mp3')


                        full_file_path = os.path.join(os.getcwd(), 'hello.mp3')
                        url = QUrl.fromLocalFile(full_file_path)
                        content = QMediaContent(url)

                        self.player = QMediaPlayer()
                        self.player.setMedia(content)
                        self.player.play()

                        

                        
                        break
                    else:
                        print("Speak in a different language please")
                        continue
        
                




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

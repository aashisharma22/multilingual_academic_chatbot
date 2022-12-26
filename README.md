# multilingual_academic_chatbot
A chatbot or chatterbot is a software application used to conduct an on-line chat conversation via text or text-to-speech, in lieu of providing direct contact with a live human agent.

We have created a voice-based chatbot that aides students in their day-to-day educational activities; mainly academic doubts in the language of their preference. This uses Machine Learning Algorithms, Natural Langugage Processing, PyQT5 GUI and Python Object Oriented Programming. 

This Chatbot has three major functions:

**i) For Students not proficient in English**:

We all know that majority of educational websites support English and Hindi as their main languages. But what if a student who doesn't know the mainstream languages want to clarify a doubt!! That's where this Chatbot helps in. Since it is completely voice-based, the student need not know the text written on the screen. The student has to say the input language(the language in which they'll ask the doubt) of their preference. The Chatterbot will then ask the student to say the output language(the language that the chatterbot will use to converse) of their preference. Then they can enter their doubt in text form of their native language. The chatterbot translates the language into English, scrapes the web for all information(using WIKIPEDIA API) regarding the question(using keywords extraction and Natural Language Processing) and again translates back to the output language preferred. It displays the answer as well as speaks-out the answer back to the user. 

The sub-part of this use is the AI model training of our bot. For ex:, if a student asks about chess, the bot would display information about chess from Wikipedia. Then the student wishes to know more about chess(like no of pieces, no of players etc). This is where the Machine Learning would come into play. The bot will get trained about Chess and is now able to answer any generic question about it.The more questions are asked, the more our bot gets trained.

**ii) For people wanting to learn new languages**: 

Those who want to transalte their languages into English or Hindi, this Chatterbot is a useful tool. Just say any sentence in your language and it will be converted to English, as well as be spoken out with the correct pronounciation.

**iii) PDF Analysis:** 

The third and final major use of out chatterbot is the PDF scraping feature. You can upload your homework pdf(any language) to our bot. The bot would then scrape through the entire pdf, summarize it and display it in the translated language. 

**Languages Used:** Python


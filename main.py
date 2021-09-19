



import  pyttsx3
engine=pyttsx3.init()
engine.setProperty('rate',125)









knowledge_base = {
    "hello": engine.say("Hi sir how are you"),

    "what is your name": "My name is Bot . I am ur virtual assistant",

}
class Bot(object):
    def respond(self, msg):
     return knowledge_base[msg]

bot = Bot()
msg = input("You :")
resp = bot.respond(msg)
print("Bot :" ,resp)
engine.runAndWait()
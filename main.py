knowledge_base = {
    "hello": "Hai sir,",

    "what is your name": "My name is Bot . I am ur virtual assistant",

}
class Bot(object):
    def respond(self, msg):
     return knowledge_base[msg]

bot = Bot()
msg = input("You :")
resp = bot.respond(msg)
print("Bot :" , resp)

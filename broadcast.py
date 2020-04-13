import telegram

token = 'YOUR_TOKEN'
chat_id = YOUR_CHAT_ID

#For Telegram Broadcast
def sendToTelegram(msg):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)

#For testing only
def main():
    #sends your message to a telegram chat
    sendToTelegram(str(input("Messege : ")))

if __name__ == "__main__":
    main()

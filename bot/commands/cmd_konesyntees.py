from gtts import gTTS

def cmd_konesyntees(bot, update, args):
    """Use superior estonian technology to express your feelings like you've never before!"""
    chatid = update.message.chat_id

    text = ''
    for x in args:
        text += f'{x} '
    try:
        tts = gTTS(text=text, lang='et')
        tts.save('bot/konesyntees/konesyntees.mp3')

        with open('bot/konesyntees/konesyntees.mp3', 'rb') as file:
            bot.send_document(chatid, file)

    except AttributeError:
        return update.message.reply_text('The Konesyntees TTS API seems to be offline at the moment. Please try again later.')
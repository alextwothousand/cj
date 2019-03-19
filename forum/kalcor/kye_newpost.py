from .kye_scrape import kalcor_scrape

from time import sleep
import _thread

previous_count = kalcor_scrape()

def kalcor_newpost_thread(bot, job):
    while True:
        global previous_count

        current_count = kalcor_scrape()
        samp_telegram = -1001484204664 # id of the channel, in this case its the 'SA-MP Telegram' supergroup.

        if current_count > previous_count:
            bot.send_message(chat_id=samp_telegram, text='New Kalcor Post: http://forum.sa-mp.com/search.php?do=finduser&u=3')
            previous_count = current_count

        sleep(10)

def kalcor_newpost(bot, job):
    _thread.start_new_thread(kalcor_newpost_thread(bot, job))
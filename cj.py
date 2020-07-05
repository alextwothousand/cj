#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""CJ Telegram Bot, by Bork. Thank go to python-telegram-bot team for 'Advanced Echo' base script!.
CJ Bot originally by Southclaws, https://github.com/Southclaws/cj"""

# credits for cj's logo goes to its respective author (assumingly southclaws)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
import asyncio

import _thread

from bot.commands import *
from bot.autoresponses import *

from storage import *
from forum.kalcor import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def error(_bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main(): #
    """Start the bot."""
    print('Bot online!')

    # Create the EventHandler and pass it your bot's token so that the API can communicate with Telegram.
    updater = Updater("YOUR-BOT-TOKEN-HERE")
    j = updater.job_queue

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("konesyntees", cmd_konesyntees, pass_args=True))
    dp.add_handler(CommandHandler("wiki", cmd_wiki, pass_args=True))
    
    #dp.add_handler(CommandHandler("verify", cmd_verify, pass_args=True))
    dp.add_handler(CommandHandler("help", cmd_help))

    # on noncommand i.e message, used for auto responses.
    dp.add_handler(MessageHandler(Filters.text, logging_chat))
    #dp.add_handler(MessageHandler(Filters.text, kye_timer), 1)

    dp.add_handler(MessageHandler(Filters.text, auto_cj), 2)
    dp.add_handler(MessageHandler(Filters.text, auto_gmname), 3)

    dp.add_handler(MessageHandler(Filters.text, auto_mpname), 4)
    dp.add_handler(MessageHandler(Filters.text, auto_dynamic), 5)

    dp.add_handler(MessageHandler(Filters.text, auto_rpname), 6)
    dp.add_handler(MessageHandler(Filters.text, auto_mapname), 7)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Initialize SQLite Database
    _thread.start_new_thread(create_conn())

    # Start the Kalcor Post Checker loop.
    j.run_once(kalcor_newpost, 0)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
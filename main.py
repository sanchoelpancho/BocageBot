# -*- coding: utf-8 -*-

from telegram.ext import *
import requests
import re
import configparser as cfg
import wikisource as wiki

def read_token_from_config_file(config):
    parser = cfg.ConfigParser()
    parser.read(config)
    return parser.get('creds', 'token')

def poem(update, context):
    received = context.args
    print(type(context.args))
    print(context.args)
    if not received:
        msg = wiki.getPoemsList()
    else: 
        try:
            msg = wiki.getPoem(received[0])
        except:
            msg = "Ãhn?? Não comprendi..."
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Fazei o obséquio de repetir, não entendi merda nenhuma.")

def main():
    token = read_token_from_config_file('config.cfg')
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('poem',poem))
    dp.add_handler(MessageHandler(Filters.command, unknown))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
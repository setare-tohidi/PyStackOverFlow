import emoji
from loguru import logger
from telebot import custom_filters

from src.bot import bot
from src.constants import keyboards, keys, states
from src.filters import IsAdmin
from src.db import db
from src.utils.io import read_file
from src.data import DATA_DIR



class Bot:
    """
    Template for telegram bot.
    """
    def __init__(self, telebot, mongodb):
        self.bot = telebot
        self.db = mongodb

        # add custom filters
        self.bot.add_custom_filter(IsAdmin())
        self.bot.add_custom_filter(custom_filters.TextMatchFilter())
        self.bot.add_custom_filter(custom_filters.TextStartsFilter())

        # register handlers
        self.handlers()

        # run bot
        logger.info('Bot is running...')
        self.bot.infinity_polling()




    def handlers(self):
        
        
        @self.mesagge_handler(test=keys.ask_question)
        def ask_questions(message):
            self.update_state(message.chat.id, states.ask_question)
            self.bot.send_message(
                message.chat.id, 
                read_file(DATA_DIR / 'guide.html')
                reply_markup=keyboards.main
            )
        
        
        @self.bot.message_handler(text=[keys.cancel])
        def exit(message):
            pass

        @self.bot.message_handler(text=[keys.settings])
        def settings(message):
            pass

        @self.bot.message_handler(is_admin=True)
        def admin_of_group(message):
            self.send_message(message.chat.id, '<strong>You are admin of this group!</strong>')

        @self.bot.message_handler(func=lambda ـ: True)
        def echo(message):
            self.send_message(
                message.chat.id, message.text,
                reply_markup=keyboards.main
            )

    def send_message(self, chat_id, text, reply_markup=None, emojize=True):
        """
        Send message to telegram bot.
        """
        if emojize:
            text = emoji.emojize(text, use_aliases=True)

        self.bot.send_message(chat_id, text, reply_markup=reply_markup)
        
        
    def update_state(self, state):
        self.db.users.update_one(
            {'chat.id': chat_id}, 
            {'$set' : {'state': state}}
        )

if __name__ == '__main__':
    logger.info('Bot started')
    nashenas_bot = Bot(telebot=bot, mongodb=db)
    nashenas_bot.run()

from telegram.ext import CommandHandler, Updater
import os
from random import randint
import requests

PORT = int(os.environ.get('PORT', 5000))
TOKEN = 'TELEGRAMTOKEN' #Enter your token which is generated from Telegram

def get_question(i, j):
    content = requests.get(
        "https://leetcode.com/api/problems/algorithms/").json()
    question_list = []
    for question in content['stat_status_pairs']:
        if question['paid_only'] == False and question['difficulty']['level'] >= i and question['difficulty']['level'] <= j:
            question_list.append({
                "name": question['stat']['question__title'],
                "slug": question['stat']['question__title_slug']
            })
    return question_list[randint(0, len(question_list)-1)]


def easy(update, context):
    question = get_question(1, 1)
    msg = f"{question['name']}\n\nhttps://leetcode.com/problems/{question['slug']}/\n\n"
    msg += "Click on the /commands to get list of all available commands\n"
    print(f"Easy: {question['name']}")
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)


def medium(update, context):
    question = get_question(2, 2)
    msg = f"{question['name']}\n\nhttps://leetcode.com/problems/{question['slug']}/\n\n"
    msg += "Click on the /commands to get list of all available commands\n"
    print(f"Medium: {question['name']}")
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)


def hard(update, context):
    question = get_question(3, 3)
    msg = f"{question['name']}\n\nhttps://leetcode.com/problems/{question['slug']}/\n\n"
    msg += "Click on the /commands to get list of all available commands\n"
    print(f"Hard: {question['name']}")
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)


def random(update, context):
    question = get_question(1, 3)
    msg = f"{question['name']}\n\nhttps://leetcode.com/problems/{question['slug']}/\n\n"
    msg += "Click on the /commands to get list of all available commands\n"
    print(f"Random: {question['name']}")
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)


def commands(update, context):
    msg = f"List of all available commands: \n\n"
    msg += "/easy - Click on this to get any random easy question from leetcode\n\n"
    msg += "/medium - Click on this to get any random medium question from leetcode\n\n"
    msg += "/hard - Click on this to get any random hard question from leetcode\n\n"
    msg += "/random - Click on this to get any random question from leetcode"
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)


def start(update, context):
    print("BOT STARTED!!")
    msg = f"Welcome to the LeetCode DSA Practice BOT\n\n"
    msg += "Click on the /commands to get list of all available commands"
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('commands', commands))
    dp.add_handler(CommandHandler('random', random))
    dp.add_handler(CommandHandler('easy', easy))
    dp.add_handler(CommandHandler('medium', medium))
    dp.add_handler(CommandHandler('hard', hard))
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://cryptic-sea-73497.herokuapp.com/'+TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()

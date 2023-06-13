import requests
import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from aiogram.utils import executor



random_token = "https://api.adviceslip.com/advice"
bot_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


bot = Bot(bot_token)  # Use the bot_token from the config.py file
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text="Random advice")
keyboard.add(button_1)


@dp.message_handler(commands=["start"])
async def cmd_start(message: Message):
    await message.answer("Hi!\nI can generate some random advice for you!\n", reply_markup=keyboard)


def get_fact(random_token):
    try:
        r = requests.get(random_token)
        data = r.json()
        
        adv = data['slip']["advice"]
        
        return adv
        
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)


@dp.message_handler(text=["Random advice"])
async def randfact(message: Message):
    fact = get_fact(random_token)
    await message.answer(f"Your advice: {fact}")




if __name__ == "__main__":
    executor.start_polling(dp)

import os

import config
import logging
from pynput.keyboard import Key, Controller
from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# bot init, create config.py and put there bot token (example: TOKEN = "1971411111:AAE...")
bot = Bot(config.TOKEN)
dp = Dispatcher(bot)
keyboard = Controller()


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Пробел", "Выключить компьютер", "Отменить выключение", "Кнопка вверх", "Кнопка вниз", "Кнопка влево",
               "Кнопка вправо"]
    kb.add(*buttons)
    await message.answer("что делаем?", reply_markup=kb)


@dp.message_handler(lambda message: message.text == "Пробел")
async def btn_space(message: types.Message):
    keyboard.press(Key.space)


@dp.message_handler(lambda message: message.text == "Выключить компьютер")
async def btn_turnoff(message: types.Message):
    os.system("shutdown /s /t 60")


@dp.message_handler(lambda message: message.text == "Отменить выключение")
async def btn_cancel(message: types.Message):
    os.system("shutdown /a")


@dp.message_handler(lambda message: message.text == "Кнопка вверх")
async def btn_arrow_up(message: types.Message):
    keyboard.press(Key.up)


@dp.message_handler(lambda message: message.text == "Кнопка вниз")
async def btn_arrow_down(message: types.Message):
    keyboard.press(Key.down)


@dp.message_handler(lambda message: message.text == "Кнопка влево")
async def btn_arrow_left(message: types.Message):
    keyboard.press(Key.left)


@dp.message_handler(lambda message: message.text == "Кнопка вправо")
async def btn_arrow_right(message: types.Message):
    keyboard.press(Key.right)


# long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



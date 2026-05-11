import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

BOT_TOKEN = "8628782532:AAFF_v36PSyYfRTDcIt9KXbfa0WQqa8kwmo"
CHILD_ID = 8442186405

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    if message.chat.id == CHILD_ID:
        await message.answer("Привет! Бот работает!")

@dp.message(Command("task"))
async def task_command(message: Message):
    if message.chat.id == CHILD_ID:
        await message.answer("Задание: What is 2+2? Напиши ответ числом.")

@dp.message()
async def answer_handler(message: Message):
    if message.chat.id == CHILD_ID:
        if message.text == "4":
            await message.answer("✅ Правильно!")
        else:
            await message.answer("❌ Неправильно. Попробуй еще раз.")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

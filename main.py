import asyncio

import config
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
import keyboard as kb
import function as fun
import psutil

dp = Dispatcher()




@dp.message(CommandStart())
async def comand_start_handler(message: Message) -> None:
    if message.chat.id == config.user_id:
	    await message.answer("Главное меню:", reply_markup=kb.mainkeyboard)

@dp.message()
async def media_menu(message: Message) -> None:
    if message.chat.id == config.user_id:
        if message.text == "🔈":
            fun.volume_down()

        if message.text == "🔇":
            fun.mute()

        if message.text == "🔊":
            fun.vloume_up()

        if message.text == "⏪":
            fun.back()

        if message.text == "⏯️":
            fun.pause()

        if message.text == "⏩":
            fun.forward()

        if message.text == "⏮️":
            fun.back_video()
        
        if message.text == "субтитры":
            fun.subtiters()

        if message.text == "⏭️":
            fun.forward_video()

        if message.text == "Выключить":
            fun.shutdown()
        
        if message.text == "Перезагрузить":
            fun.reboot()
        
        if message.text == "Гибернация":
            fun.hypernation()
        
        if message.text == "🔅":
            fun.brightness_minus()

        if message.text == "🔆":
            fun.brightness_plus()

        if message.text == "🗑":
            fun.clear_bin
        
        if message.text == "🖥 Сделать скриношот":
            fun.screen_shot()

        if message.text == "🔒 Заблокировать":
            fun.block_pc()
        
        if message.text == "📊 статистика пк":
            memory = psutil.virtual_memory()
            memoryp = memory.percent
            cpu =  psutil.cpu_percent(interval=1)
            await message.answer(f"Загрузка пк:\nЦп: {cpu}%\nОзу: {memoryp}%")
        
        if message.text =="колесо вверх":
            fun.mouse_wheel_up()
        
        if message.text == "лкм":
            fun.mouse_left_click()

        if message.text == "скм":
            fun.mouse_midle_click()

        if message.text == "пкм":
            fun.mouse_right_click() 

        if message.text == "🔼":
            fun.mouse_up()

        if message.text == "win":
            fun.win()
        
        if message.text == "◀️":
            fun.mouse_left()
        
        if message.text == "▶️":
            fun.mouse_right()
        
        if message.text == "колесо вниз":
            fun.mouse_wheel_down()

        if message.text == "🔽":
            fun.mouse_down()
        
        if message.text == "смена языка":
            fun.switch_language()


    if message.text == "Назад":
        await message.answer("Главное меню:", reply_markup=kb.mainkeyboard)
        await message.delete()
        
    if message.text == "⏸️Медиа":
        await message.answer("⏸️Медиа:",reply_markup=kb.mediakeyboard)

    if message.text == "🔈" or message.text == "🔇" or message.text == "🔊" or message.text == "⏪" or message.text == "⏯️" or message.text == "⏩" or message.text == "⏮️" or message.text == "субтитры" or message.text == "⏭️":
        await message.delete()


    if message.text == "🔋Питание":
        await message.answer("🔋Питание:",reply_markup=kb.powerkeyboard)

    if message.text == "Выключить" or message.text == "Перезагрузить" or message.text == "Гибернация":
         await message.delete()


    if message.text == "💻ПК":
        await message.answer("💻ПК:",reply_markup=kb.pckeyboard)
    
    if message.text == "🔅" or  message.text == "🔆" or  message.text == "🗑" or  message.text == "🖥 Сделать скриношот" or message.text == "🖥 Сделать скриношот" or message.text == "🔒 Заблокировать" or message.text == "📊 статистика пк":
         await message.delete()


    if message.text == "⌨️ Устройства":
        await message.answer("⌨️ Устройства:",reply_markup=kb.inputkeyboard)
    
    if message.text == "колесо вверх" or message.text == "лкм" or message.text == "скм" or message.text == "пкм" or message.text == "🔼" or message.text == "win" or message.text == "◀️" or message.text == "▶️" or message.text == "колесо вниз" or message.text == "🔽" or message.text == "смена языка":
         await message.delete()
    

async def main() -> None:
    bot = Bot(token=config.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

try:
    if __name__ == "__main__":
        asyncio.run(main())
except KeyboardInterrupt:
      print("stop")
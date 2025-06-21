
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainkeyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
       [KeyboardButton(text="⏸️Медиа"),KeyboardButton(text="🔋Питание")],
       [KeyboardButton(text="💻ПК"),KeyboardButton(text="⌨️ Устройства")]
])

mediakeyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="🔈"), KeyboardButton(text="🔇"), KeyboardButton(text="🔊")],
    [KeyboardButton(text="⏪"),KeyboardButton(text="⏯️"), KeyboardButton(text="⏩")],
    [KeyboardButton(text="⏮️"),KeyboardButton(text="субтитры"),KeyboardButton(text="⏭️")],
    [KeyboardButton(text="Назад")]
])
powerkeyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="🔋выключить"), KeyboardButton(text="Перезагрузить"), KeyboardButton(text="Гибернация")],
    [KeyboardButton(text="Назад")]
])
powerkeyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="Выключить"), KeyboardButton(text="Перезагрузить"), KeyboardButton(text="Гибернация")],
    [KeyboardButton(text="Назад")]
])
pckeyboard = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[
    [KeyboardButton(text="🔅"),KeyboardButton(text="🔆"),KeyboardButton(text="🗑")],
    [KeyboardButton(text="🖥 Сделать скриношот"),KeyboardButton(text="🔒 Заблокировать")],
    [KeyboardButton(text="📊 статистика пк")],
    [KeyboardButton(text="Назад")]
])
inputkeyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="лкм"),KeyboardButton(text="скм"), KeyboardButton(text="пкм")],
    [KeyboardButton(text="колесо вверх"), KeyboardButton(text="🔼"), KeyboardButton(text="win")],
    [KeyboardButton(text="◀️"), KeyboardButton(text=" "), KeyboardButton(text="▶️")],
    [KeyboardButton(text="колесо вниз"), KeyboardButton(text="🔽"), KeyboardButton(text="смена языка")],
    [KeyboardButton(text="Назад")]

])

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import settings


import some_aditional_func
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import subprocess
#dadsa
data = MemoryStorage()
class LogInStates(StatesGroup):
    api_key = State()
    secret_key = State()
    logged_in = State()

flag = 50
bot = Bot(token='6234279060:AAFx1KgWvVNg1prHpQfvlS203nZaOt4IH5U')
dp = Dispatcher(bot, storage=MemoryStorage())
coins = ['BTC', 'ETH', 'BNB', 'BCC', 'NEO', 'LTC', 'QTUM', 'ADA', 'XRP', 'EOS', 'TUSD', 'IOTA', 'XLM', 'ONT', 'TRX',
         'ETC', 'ICX', 'VEN', 'NULS', 'VET', 'PAX', 'BCHABC', 'BCHSV', 'USDC', 'LINK', 'WAVES', 'BTT', 'USDS', 'ONG',
         'HOT', 'ZIL', 'ZRX', 'FET', 'BAT', 'XMR', 'ZEC', 'IOST', 'CELR', 'DASH', 'NANO', 'OMG', 'THETA', 'ENJ', 'MITH',
         'MATIC', 'ATOM', 'TFUEL', 'ONE', 'FTM', 'ALGO', 'USDSB', 'GTO', 'ERD', 'DOGE', 'DUSK', 'ANKR', 'WIN', 'COS',
         'NPXS', 'COCOS', 'MTL', 'TOMO', 'PERL', 'DENT', 'MFT', 'KEY', 'STORM', 'DOCK', 'WAN', 'FUN', 'CVC', 'CHZ',
         'BAND', 'BUSD', 'BEAM', 'XTZ', 'REN', 'RVN', 'HC', 'HBAR', 'NKN', 'STX', 'KAVA', 'ARPA', 'IOTX', 'RLC', 'MCO',
         'CTXC', 'BCH', 'TROY', 'VITE', 'FTT', 'EUR', 'OGN', 'DREP', 'BULL', 'BEAR', 'ETHBULL', 'ETHBEAR', 'TCT', 'WRX',
         'BTS', 'LSK', 'BNT', 'LTO', 'EOSBULL', 'EOSBEAR', 'XRPBULL', 'XRPBEAR', 'STRAT', 'AION', 'MBL', 'COTI',
         'BNBBULL', 'BNBBEAR', 'STPT', 'WTC', 'DATA', 'XZC', 'SOL', 'CTSI', 'HIVE', 'CHR', 'BTCUP', 'BTCDOWN', 'GXS',
         'ARDR', 'LEND', 'MDT', 'STMX', 'KNC', 'REP', 'LRC', 'PNT', 'COMP', 'BKRW', 'SC', 'ZEN', 'SNX', 'ETHUP',
         'ETHDOWN', 'ADAUP', 'ADADOWN', 'LINKUP', 'LINKDOWN', 'VTHO', 'DGB', 'GBP', 'SXP', 'MKR', 'DAI', 'DCR', 'STORJ',
         'BNBUP', 'BNBDOWN', 'XTZUP', 'XTZDOWN', 'MANA', 'AUD', 'YFI', 'BAL', 'BLZ', 'IRIS', 'KMD', 'JST', 'SRM', 'ANT',
         'CRV', 'SAND', 'OCEAN', 'NMR', 'DOT', 'LUNA', 'RSR', 'PAXG', 'WNXM', 'TRB', 'BZRX', 'SUSHI', 'YFII', 'KSM',
         'EGLD', 'DIA', 'RUNE', 'FIO', 'UMA', 'EOSUP', 'EOSDOWN', 'TRXUP', 'TRXDOWN', 'XRPUP', 'XRPDOWN', 'DOTUP',
         'DOTDOWN', 'BEL', 'WING', 'LTCUP', 'LTCDOWN', 'UNI', 'NBS', 'OXT', 'SUN', 'AVAX', 'HNT', 'FLM', 'UNIUP',
         'UNIDOWN', 'ORN', 'UTK', 'XVS', 'ALPHA', 'AAVE', 'NEAR', 'SXPUP', 'SXPDOWN', 'FIL', 'FILUP', 'FILDOWN',
         'YFIUP', 'YFIDOWN', 'INJ', 'AUDIO', 'CTK', 'BCHUP', 'BCHDOWN', 'AKRO', 'AXS', 'HARD', 'DNT', 'STRAX', 'UNFI',
         'ROSE', 'AVA', 'XEM', 'AAVEUP', 'AAVEDOWN', 'SKL', 'SUSD', 'SUSHIUP', 'SUSHIDOWN', 'XLMUP', 'XLMDOWN', 'GRT',
         'JUV', 'PSG', '1INCH', 'REEF', 'OG', 'ATM', 'ASR', 'CELO', 'RIF', 'BTCST', 'TRU', 'CKB', 'TWT', 'FIRO', 'LIT',
         'SFP', 'DODO', 'CAKE', 'ACM', 'BADGER', 'FIS', 'OM', 'POND', 'DEGO', 'ALICE', 'LINA', 'PERP', 'RAMP', 'SUPER',
         'CFX', 'EPS', 'AUTO', 'TKO', 'PUNDIX', 'TLM', '1INCHUP', '1INCHDOWN', 'BTG', 'MIR', 'BAR', 'FORTH', 'BAKE',
         'BURGER', 'SLP', 'SHIB', 'ICP', 'AR', 'POLS', 'MDX', 'MASK', 'LPT', 'NU', 'XVG', 'ATA', 'GTC', 'TORN', 'KEEP',
         'ERN', 'KLAY', 'PHA', 'BOND', 'MLN', 'DEXE', 'C98', 'CLV', 'QNT', 'FLOW', 'TVK', 'MINA', 'RAY', 'FARM',
         'ALPACA', 'QUICK', 'MBOX', 'FOR', 'REQ', 'GHST', 'WAXP', 'TRIBE', 'GNO', 'XEC', 'ELF', 'DYDX', 'POLY', 'IDEX',
         'VIDT', 'USDP', 'GALA', 'ILV', 'YGG', 'SYS', 'DF', 'FIDA', 'FRONT', 'CVP', 'AGLD', 'RAD', 'BETA', 'RARE',
         'LAZIO', 'CHESS', 'ADX', 'AUCTION', 'DAR', 'BNX', 'RGT', 'MOVR', 'CITY', 'ENS', 'KP3R', 'QI', 'PORTO', 'POWR',
         'VGX', 'JASMY', 'AMP', 'PLA', 'PYR', 'RNDR', 'ALCX', 'SANTOS', 'MC', 'ANY', 'BICO', 'FLUX', 'FXS', 'VOXEL',
         'HIGH', 'CVX', 'PEOPLE', 'OOKI', 'SPELL', 'UST', 'JOE', 'ACH', 'IMX', 'GLMR', 'LOKA', 'SCRT', 'API3', 'BTTC',
         'ACA', 'ANC', 'XNO', 'WOO', 'ALPINE', 'T', 'ASTR', 'NBT', 'GMT', 'KDA', 'APE', 'BSW', 'BIFI', 'MULTI', 'STEEM',
         'MOB', 'NEXO', 'REI', 'GAL', 'LDO', 'EPX', 'OP', 'LEVER', 'STG', 'LUNC', 'GMX', 'NEBL', 'POLYX', 'APT', 'OSMO',
         'HFT', 'PHB', 'HOOK', 'MAGIC', 'HIFI', 'RPL', 'PROS', 'AGIX', 'GNS', 'SYN', 'VIB', 'SSV', 'LQTY', 'AMB',
         'BETH', 'USTC', 'GAS', 'GLM', 'PROM', 'QKC', 'UFT', 'ID', 'ARB', 'LOOM', 'OAX', 'RDNT', 'WBTC', 'EDU', 'SUI',
         'AERGO', 'PEPE', 'FLOKI', 'AST', 'SNT', 'COMBO', 'MAV', 'PENDLE']

## Keyboard
button_authorization = KeyboardButton('Log in 🤳')
first_kb_no_admins = ReplyKeyboardMarkup(resize_keyboard=True).add(button_authorization)


def get_inline_kb(i: int):
    inline_keyboard = InlineKeyboardMarkup(row_width=5)
    buttons = []

    for coin in coins[i - 50:i]:
        buttons.append(InlineKeyboardButton(coin, callback_data=coin))

    inline_keyboard.add(*buttons)

    if i >= 400:
        inline_keyboard.row(InlineKeyboardButton('Prev', callback_data='prev'))
    elif i <= 50:
        inline_keyboard.row(InlineKeyboardButton('Next', callback_data='next'))
    else:
        inline_keyboard.row(
            InlineKeyboardButton('Prev', callback_data='prev'),
            InlineKeyboardButton('Next', callback_data='next')
        )

    return inline_keyboard


@dp.callback_query_handler(text='next')
async def get_further_kb(query: types.CallbackQuery):
    global flag
    flag += 50
    await query.message.edit_reply_markup(reply_markup=get_inline_kb(flag))


@dp.callback_query_handler(text='prev')
async def get_prev_kb(query: types.CallbackQuery):
    global flag
    flag -= 50
    await query.message.edit_reply_markup(reply_markup=get_inline_kb(flag))



## Keyboard
button_authorization = KeyboardButton('Log in 🤳')
first_kb_no_admins = ReplyKeyboardMarkup(resize_keyboard=True).add(button_authorization)


def get_start_kb():
    button_client_work = KeyboardButton('Add an account to work 🚜')
    button_statistics = KeyboardButton('Prices 💰')

    first_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_client_work).add(button_statistics)

    return first_kb

@dp.message_handler(text='Prices 💰')
async def process_statistics_command(message: types.Message):
    global flag
    flag = 50
    await message.reply("Choose the coin:", reply_markup=get_inline_kb(flag))
@dp.callback_query_handler(lambda query: query.data in coins)
async def handle_coin_button(query: types.CallbackQuery):
    selected_coin = query.data
    # Handle the selected coin
    await query.answer()
    ans = some_aditional_func.answer(selected_coin)
    await query.message.answer(ans)

def get_final_kb():
    button_back = KeyboardButton('Back 🔙')
    button_back_to_main = KeyboardButton('Back to main menu 🔙')
    button_start = KeyboardButton('Start 🚀')
    final_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back).add(button_back_to_main).add(button_start)

    return final_kb


def get_debug_kb():
    button_back = KeyboardButton('Back 🔙')
    button_back_to_main = KeyboardButton('Back to main menu 🔙')

    debug_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back).add(button_back_to_main)

    return debug_kb


## Admins
admins = [682751445, 1992272849]


@dp.message_handler(commands=['start'])
async def alarm(message: types.Message):
    if message.from_user.id in admins:
        settings.USER_ID = message.from_user.id
        await message.answer(f"Greetings, {message.from_user.username}", reply_markup=get_start_kb())
    else:
        await message.answer(f"Greetings, {message.from_user.username}, log in!", reply_markup=first_kb_no_admins)


@dp.message_handler(state=LogInStates.api_key)
async def return_from_api_state(message: types.Message, state: FSMContext):
    if message.from_user.id in admins:
        if message.text == 'Back 🔙':
            await message.reply("Main menu", reply_markup=get_start_kb())
            await state.finish()

        elif message.text == 'Back to main menu 🔙':
            await message.reply("Main menu", reply_markup=get_start_kb())
            await state.finish()

        else:
            async with state.proxy() as data:
                data['api_key'] = message.text

            await message.reply("Enter SECRET_KEY which is tied to the work account:", reply_markup=get_debug_kb())
            await LogInStates.secret_key.set()


@dp.message_handler(state=LogInStates.secret_key)
async def return_from_secret_state(message: types.Message, state: FSMContext):
    if message.from_user.id in admins:
        if message.text == 'Back 🔙':
            await message.reply("Add account section.\n"
                                "\n"
                                "Enter API_KEY which is tied to the work account:", reply_markup=get_debug_kb())
            await LogInStates.api_key.set()

        elif message.text == 'Back to main menu 🔙':
            await message.reply("Main menu", reply_markup=get_start_kb())
            await state.finish()

        else:
            async with state.proxy() as data:
                data['secret_key'] = message.text

            await message.reply(f"Your API_KEY: {data['api_key']}\nYour SECRET_KEY: {data['secret_key']}",
                                reply_markup=get_final_kb())

            global API_KEY, SECRET_KEY
            settings.API_KEY = data.get("api_key")
            settings.SECRET_KEY = data.get("secret_key")
            await LogInStates.logged_in.set()


@dp.message_handler(state=LogInStates.logged_in)
async def return_from_loggedin_state(message: types.Message, state: FSMContext):
    if message.from_user.id in admins:
        if message.text == 'Back 🔙':
            await message.reply("Enter SECRET_KEY which is tied to the work account:", reply_markup=get_debug_kb())
            await LogInStates.secret_key.set()

        elif message.text == 'Back to main menu 🔙':
            await message.reply("Main menu", reply_markup=get_start_kb())
            await state.finish()

        elif message.text == 'Start 🚀':
            try:
                output = subprocess.check_output("python main.py",
                                                 stderr=subprocess.STDOUT,
                                                 universal_newlines=True)
                print(output)
            except subprocess.CalledProcessError as error:
                print(error.output)
            await message.reply("Started torgovlya")


@dp.message_handler(text=['Add an account to work 🚜'])
async def process_client_work_command(message: types.Message):
    if message.from_user.id in admins:
        await message.reply("Add account section.\n"
                            "\n"
                            "Enter API_KEY which is tied to the work account:", reply_markup=get_debug_kb())
        await LogInStates.api_key.set()


@dp.message_handler(text=['Statistics 💻'])
async def process_statistics_command(message: types.Message):
    if message.from_user.id in admins:
        await message.reply("TO be procecced")


@dp.message_handler()
async def echo(message: types.Message):
    if message.from_user.id in admins:
        await message.answer("I don't understand you, try again", reply_markup=get_start_kb())


async def notify_user(message: str, bot, userid):
    print(userid)
    await bot.send_message(chat_id=userid, text=message)


if __name__ == '__main__':
    executor.start_polling(dp)

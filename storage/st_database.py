import time
import datetime

import aiosqlite3
import asyncio

import _thread

table_chatlogs = '`chatlogs`'
logloop = asyncio.get_event_loop()

def create_conn():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_conn_thread())

async def create_conn_thread():
    global conn
    global cur

    conn = await aiosqlite3.connect('storage/db/cj_db.db')
    cur = await conn.cursor()

    await cur.execute(f"CREATE TABLE IF NOT EXISTS {table_chatlogs} (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `timestamp` TEXT, `user` TEXT, `message` TEXT);")

def logging_chat(_bot, update):
    if update.message.from_user.is_bot is True: return

    global conn
    global cur

    logloop.run_until_complete(append_log(update.message.from_user.username, update.message.text))

async def append_log(username, text):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y %H:%M:%S')

    query = f"INSERT INTO {table_chatlogs} (`timestamp`, `user`, `message`) VALUES (?, ?, ?);"

    await cur.execute(query, (timestamp, username, text))
    await conn.commit()

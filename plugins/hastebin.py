from pyrogram import Client, filters
from pyrogram.types import Message
from config import prefix
from utils import http


@Client.on_message(filters.command("hastebin", prefix))
async def hastebin(c: Client, m: Message):
    if m.reply_to_message:
        if m.reply_to_message.document:
            tfile = m.reply_to_message
            to_file = await tfile.download()
            with open(to_file, 'rb') as fd:
                mean = fd.read().decode('UTF-8')
        if m.reply_to_message.text:
            mean = m.reply_to_message.text

        url = "https://hastebin.com/documents"
        r = await http.post(url, data=mean.encode('UTF-8'))
        url = f"https://hastebin.com/{r.json()['key']}"
        await m.reply_text(url, disable_web_page_preview=True)
    else:
        await m.reply_text("reply_to_document_or_text")

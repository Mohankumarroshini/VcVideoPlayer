from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**Hey, I'm a VC Video Player developed by Developers of** @Athena_proBot \n\n**To use it:-** __ \n1) Add this Bot to your Group and Make it Admin \n2) Add__ @Eagle_probotz  __to your Group__ \n3) **Commands** : \n`/stream` (IN REPLY TO A VIDEO) \n`/stop`",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "Support", url="t.me/my_dear_brightlight")
                                    ]]
                            ))
   else:
      await m.reply("**Vc Video player is Alive! ✨**")

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "ðð¼ð ð¦ðð®ð¿ðð²ð± ð£ð¹ð²ð®ðð² ð¦ðð¯ðð°ð¿ð¶ð¯ð² ð¢ð½ððð§ð²ð°ðµð",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

CHAT_ID=int(os.environ.get("CHAT_ID", -1001899905385))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button=[[
      InlineKeyboardButton("â Aá´á´ Má´ Tá´ Yá´á´Ê GÊá´á´á´ â", url=f"http://t.me/AutoApproveJoinRequestsBot?startgroup=true")
      ],[
      InlineKeyboardButton("ð¤ ðð¿ð³ð°ðð´ð ð¤", url="https://t.me/MX_Networks"),
      InlineKeyboardButton("â¤ï¸ ð¼ð¾ðð¸ð´ð â¤ï¸", url="https://t.me/+3JlUG6DklkIzNThh")
      ],[
      InlineKeyboardButton("ð  ð¶ðð¾ðð¿ ð ", url=f"https://MX_Movie_Request"),
      InlineKeyboardButton("â¡ ððð¿ð¿ð¾ðð â¡", url=f"https://t.me/MX_Support_Bot")
      ]]
    await message.reply_text(text="**ð·ð´ð»ð»ð¾...â¡\n\nð¸ð°ð¼ ð° ðð¸ð¼ð¿ð»ð´ ðð´ð»ð´ð¶ðð°ð¼ ð°ððð¾ ðð´ððð´ðð ð°ð²ð²ð´ð¿ð ð±ð¾ð.\nðµð¾ð ðð¾ðð ð²ð·ð°ðð...")

@pr0fess0r_99.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} ð¹ð¾ð¸ð½ð´ð³ â¡") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))       

print("ðð¼ð ð¦ðð®ð¿ðð²ð± ð£ð¹ð²ð®ðð² ðð¼ð¶ð» ð ð« ð¡ð²ððð¼ð¿ð¸ð")
pr0fess0r_99.run()

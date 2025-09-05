# Place all handler definitions after all imports

from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

@Client.on_message(filters.command("hyperlinkdemo") & filters.private)
async def hyperlink_demo(client, message):
    # Demonstrate a working Telegram hyperlink using HTML
    text = 'Visit <a href="https://www.google.com">Google</a> for search.'
    await client.send_message(
        chat_id=message.chat.id,
        text=text,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
@Client.on_message(filters.command("hyperlinkdemo") & filters.private)
async def hyperlink_demo(client, message):
    # Demonstrate a working Telegram hyperlink using HTML
    text = 'Visit <a href="https://www.google.com">Google</a> for search.'
    await client.send_message(
        chat_id=message.chat.id,
        text=text,
        parse_mode="HTML",
        disable_web_page_preview=True
    )

# ...existing code...

# Place all handler definitions after all imports
from pyrogram import Client, filters


# Test various hyperlink methods with /testhyper

# ...existing code...


# ...existing code...

# Place all handler definitions after all imports
from pyrogram import Client, filters

@Client.on_message(filters.command("testhyper") & filters.private)
async def test_hyperlink(client, message):
    print("/testhyper handler triggered!")  # Debug print
    await client.send_message(
        chat_id=message.chat.id,
        text="/testhyper handler triggered! (debug)",
        disable_web_page_preview=True
    )
    # Method 1: HTML with quotes
    html1 = '<a href="https://t.me/dreamxbotz">HTML Link with quotes</a>'
    await client.send_message(
        chat_id=message.chat.id,
        text=html1,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
    # Method 2: HTML without quotes (not recommended, but for test)
    html2 = '<a href=https://t.me/dreamxbotz>HTML Link no quotes</a>'
    await client.send_message(
        chat_id=message.chat.id,
        text=html2,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
    # Method 3: Markdown (should not work for inline links in Telegram, but for test)
    md1 = '[Markdown Link](https://t.me/dreamxbotz)'
    await client.send_message(
        chat_id=message.chat.id,
        text=md1,
        parse_mode="Markdown",
        disable_web_page_preview=True
    )
    # Method 4: HTML with bold inside
    html3 = '<a href="https://t.me/dreamxbotz"><b>HTML Bold Link</b></a>'
    await client.send_message(
        chat_id=message.chat.id,
        text=html3,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
    # Method 5: HTML with code inside
    html4 = '<a href="https://t.me/dreamxbotz"><code>HTML Code Link</code></a>'
    await client.send_message(
        chat_id=message.chat.id,
        text=html4,
        parse_mode="HTML",
        disable_web_page_preview=True
    )

@Client.on_message(filters.command("hyperlinktest") & filters.private)
async def hyperlink_test(client, message):
    # Use the same technique as Script.py
    link = '<a href="https://www.google.com">Google</a>'
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Here is a hyperlink: {link}",
        parse_mode="HTML",
        disable_web_page_preview=True
    )

@Client.on_message(filters.command("hyperlinkdemo") & filters.private)
async def hyperlink_demo(client, message):
    # Demonstrate a working Telegram hyperlink using HTML
    text = 'Visit <a href="https://www.google.com">Google</a> for search.'
    await client.send_message(
        chat_id=message.chat.id,
        text=text,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
BATCH_FILES = {}

# /explore command: send 20 popular movies as IMDB links for Telegram link preview
POPULAR_MOVIES = [
    {"title": "The Shawshank Redemption", "year": "1994", "url": "https://www.imdb.com/title/tt0111161/"},
    {"title": "The Godfather", "year": "1972", "url": "https://www.imdb.com/title/tt0068646/"},
    {"title": "The Dark Knight", "year": "2008", "url": "https://www.imdb.com/title/tt0468569/"},
    {"title": "Pulp Fiction", "year": "1994", "url": "https://www.imdb.com/title/tt0110912/"},
    {"title": "Forrest Gump", "year": "1994", "url": "https://www.imdb.com/title/tt0109830/"},
    {"title": "Inception", "year": "2010", "url": "https://www.imdb.com/title/tt1375666/"},
    {"title": "Fight Club", "year": "1999", "url": "https://www.imdb.com/title/tt0137523/"},
    {"title": "The Matrix", "year": "1999", "url": "https://www.imdb.com/title/tt0133093/"},
    {"title": "Goodfellas", "year": "1990", "url": "https://www.imdb.com/title/tt0099685/"},
    {"title": "The Lord of the Rings: The Return of the King", "year": "2003", "url": "https://www.imdb.com/title/tt0167260/"},
    {"title": "Interstellar", "year": "2014", "url": "https://www.imdb.com/title/tt0816692/"},
    {"title": "Parasite", "year": "2019", "url": "https://www.imdb.com/title/tt6751668/"},
    {"title": "Joker", "year": "2019", "url": "https://www.imdb.com/title/tt7286456/"},
    {"title": "Avengers: Endgame", "year": "2019", "url": "https://www.imdb.com/title/tt4154796/"},
    {"title": "Gladiator", "year": "2000", "url": "https://www.imdb.com/title/tt0172495/"},
    {"title": "Titanic", "year": "1997", "url": "https://www.imdb.com/title/tt0120338/"},
    {"title": "The Lion King", "year": "1994", "url": "https://www.imdb.com/title/tt0110357/"},
    {"title": "Schindler's List", "year": "1993", "url": "https://www.imdb.com/title/tt0108052/"},
    {"title": "The Silence of the Lambs", "year": "1991", "url": "https://www.imdb.com/title/tt0102926/"},
    {"title": "Saving Private Ryan", "year": "1998", "url": "https://www.imdb.com/title/tt0120815/"}
]

from pyrogram import Client, filters



# Move /explore command handler to the end to ensure registration

@Client.on_message(filters.command("explore") & filters.private)
async def explore_movies(client, message):
    """Command to explore top IMDB movies with deep link buttons to search"""
    # First, let's send a welcome message
    await message.reply("🎬 **Top IMDB Movies** 🎬\n\nHere are some of the highest-rated movies on IMDB:")
    
    # Only show first 10 movies to avoid flooding
    top_movies = [
        {"title": "The Shawshank Redemption", "year": "1994", "url": "https://www.imdb.com/title/tt0111161/", "poster": "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIwLTljNTEtNWYzODZhYzU3N2NhXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_.jpg", "desc": "Two imprisoned men bond over years, finding redemption through acts of decency."},
        {"title": "The Godfather", "year": "1972", "url": "https://www.imdb.com/title/tt0068646/", "poster": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmYtYTAwMC00ZjQ5LWFmNTEtODM1ZmRlY2RhYjA2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg", "desc": "The aging patriarch of an organized crime dynasty transfers control to his reluctant son."},
        {"title": "The Dark Knight", "year": "2008", "url": "https://www.imdb.com/title/tt0468569/", "poster": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg", "desc": "Batman faces his greatest challenge as the Joker wreaks havoc on Gotham City."},
        {"title": "The Godfather Part II", "year": "1974", "url": "https://www.imdb.com/title/tt0071562/", "poster": "https://m.media-amazon.com/images/M/MV5BMWMwMGQzZTItY2JlNC00OWZiLWIyMDctNDk2ZDQ2YjRjMWQ0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg", "desc": "The early life of Vito Corleone while his son expands the family crime syndicate."},
        {"title": "12 Angry Men", "year": "1957", "url": "https://www.imdb.com/title/tt0050083/", "poster": "https://m.media-amazon.com/images/M/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhNGUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_.jpg", "desc": "A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence."},
        {"title": "Schindler's List", "year": "1993", "url": "https://www.imdb.com/title/tt0108052/", "poster": "https://m.media-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg", "desc": "A businessman saves over a thousand Jews from the Holocaust by employing them in his factories."},
        {"title": "The Lord of the Rings: The Return of the King", "year": "2003", "url": "https://www.imdb.com/title/tt0167260/", "poster": "https://m.media-amazon.com/images/M/MV5BNzA5ZDNlZWMtM2NhNS00NDJjLTk4NDItYTRmY2EwMWZlMTY3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg", "desc": "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam."},
        {"title": "Pulp Fiction", "year": "1994", "url": "https://www.imdb.com/title/tt0110912/", "poster": "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg", "desc": "The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption."},
        {"title": "The Lord of the Rings: The Fellowship of the Ring", "year": "2001", "url": "https://www.imdb.com/title/tt0120737/", "poster": "https://m.media-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_.jpg", "desc": "A meek Hobbit and eight companions set out on a journey to destroy the One Ring and the Dark Lord Sauron."},
        {"title": "The Good, the Bad and the Ugly", "year": "1966", "url": "https://www.imdb.com/title/tt0060196/", "poster": "https://m.media-amazon.com/images/M/MV5BNjJlYmNkZGItM2NhYy00MjlmLTk5NmQtNjg1NmM2ODU4OTMwXkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg", "desc": "Three gunslingers compete to find fortune in a buried cache of Confederate gold amid the violent chaos of the Civil War."}
    ]
    
    # Process each movie one by one
    for m in top_movies:
        try:
            # Format movie name for the deep link exactly like the example (replace spaces with hyphens)
            formatted_name = m['title'].replace(' ', '-')
            
            # Create deep link URL in the format https://t.me/BotUsername?start=getfile-MovieName
            deep_link = f"https://t.me/{temp.U_NAME}?start=getfile-{formatted_name}"
            
            # Create button with the deep link URL and download emoji
            buttons = [[InlineKeyboardButton("⬇️ Get This Movie", url=deep_link)]]
            reply_markup = InlineKeyboardMarkup(buttons)
            
            # Create caption with movie title as a hyperlink and description
            caption = f"🎬 <a href='{m['url']}'><b>{m['title']}</b></a> ({m['year']})\n\n{m['desc']}"
            
            try:
                # Try to send with photo
                if 'poster' in m and m['poster']:
                    await message.reply_photo(
                        photo=m['poster'],
                        caption=caption,
                        reply_markup=reply_markup,
                        parse_mode=enums.ParseMode.HTML
                    )
                else:
                    # Fallback to text only if no poster
                    await message.reply(
                        text=caption,
                        reply_markup=reply_markup,
                        parse_mode=enums.ParseMode.HTML
                    )
            except Exception as img_error:
                print(f"Image error: {img_error}")
                # If photo fails, send as text
                await message.reply(
                    text=caption,
                    reply_markup=reply_markup,
                    parse_mode=enums.ParseMode.HTML
                )
                
            # Add a small delay to avoid flooding
            await asyncio.sleep(0.5)
            
        except Exception as e:
            print(f"Error sending movie {m['title']}: {e}")
            # Try a simplified version if regular send fails
            try:
                # Simplified version with movie title as hyperlink and description
                simple_caption = f"<a href='{m['url']}'>{m['title']}</a> ({m['year']})\n\n{m['desc']}"
                await message.reply(simple_caption, parse_mode=enums.ParseMode.HTML)
            except:
                pass

# Removed the callback handler since we're now using direct deep links
# with the URL parameter in the format:
# https://t.me/bot_username?start=getfile-MovieName

# Add a simple test button command
@Client.on_message(filters.command("testbutton") & filters.private)
async def test_button_cmd(client, message):
    """Simple command to test if buttons are working correctly"""
    buttons = [[InlineKeyboardButton("Test Button", callback_data="test_button_click")]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    # Use a default image URL - replace with any image URL you prefer
    image_url = "https://i.imgur.com/gxbTvQS.jpeg"
    
    try:
        await message.reply_photo(
            photo=image_url,
            caption="This is a test button. Click it to verify buttons are working.",
            reply_markup=reply_markup
        )
    except Exception as e:
        # Fallback to text if image fails
        print(f"Image error: {e}")
        await message.reply(
            text="This is a test button. Click it to verify buttons are working.",
            reply_markup=reply_markup
        )

@Client.on_callback_query(filters.regex(r"^test_button_click"))
async def handle_test_button(client, callback_query):
    """Handle the test button click"""
    await callback_query.answer("Button is working! ✅", show_alert=True)
    await callback_query.message.reply("Button click received successfully! The button system is working correctly.")

import os
import re, sys
import json
import base64
import logging
import random
import asyncio
import string
import pytz
from .pmfilter import auto_filter 
from Script import script
from datetime import datetime
from database.refer import referdb
from database.config_db import mdb
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait, ChatAdminRequired, UserNotParticipant
from database.ia_filterdb import Media, Media2, get_file_details, unpack_new_file_id, get_bad_files
from database.users_chats_db import db
from info import *
from utils import get_settings, save_group_settings, is_subscribed, is_req_subscribed, get_size, get_shortlink, is_check_admin, temp, get_readable_time, get_time, generate_settings_text, log_error, clean_filename



logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

TIMEZONE = "Asia/Kolkata"
BATCH_FILES = {}

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    if EMOJI_MODE:
        try:
            await message.react(emoji=random.choice(REACTIONS), big=True)
        except Exception:
            await message.react(emoji="⚡️", big=True)
    m = message
    if len(m.command) == 2 and m.command[1].startswith(('notcopy', 'sendall')):
        _, userid, verify_id, file_id = m.command[1].split("_", 3)
        user_id = int(userid)
        grp_id = temp.VERIFICATIONS.get(user_id, 0)
        settings = await get_settings(grp_id)         
        verify_id_info = await db.get_verify_id_info(user_id, verify_id)
        if not verify_id_info or verify_id_info["verified"]:
            return await message.reply("<b>ʟɪɴᴋ ᴇxᴘɪʀᴇᴅ ᴛʀʏ ᴀɢᴀɪɴ...</b>")  
        
        ist_timezone = pytz.timezone('Asia/Kolkata')
        if await db.user_verified(user_id):
            key = "third_time_verified"
        else:
            key = "second_time_verified" if await db.is_user_verified(user_id) else "last_verified"
        current_time = datetime.now(tz=ist_timezone)
        result = await db.update_notcopy_user(user_id, {key:current_time})
        await db.update_verify_id_info(user_id, verify_id, {"verified":True})
        if key == "third_time_verified": 
            num = 3 
        else: 
            num =  2 if key == "second_time_verified" else 1 
        if key == "third_time_verified": 
            msg = script.THIRDT_VERIFY_COMPLETE_TEXT
        else:
            msg = script.SECOND_VERIFY_COMPLETE_TEXT if key == "second_time_verified" else script.VERIFY_COMPLETE_TEXT
        if message.command[1].startswith('sendall'):
            verifiedfiles = f"https://telegram.me/{temp.U_NAME}?start=allfiles_{grp_id}_{file_id}"
        else:
            verifiedfiles = f"https://telegram.me/{temp.U_NAME}?start=file_{grp_id}_{file_id}"
        await client.send_message(settings['log'], script.VERIFIED_LOG_TEXT.format(m.from_user.mention, user_id, datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d %B %Y'), num))
        btn = [[
            InlineKeyboardButton("✅ ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ɢᴇᴛ ꜰɪʟᴇ ✅", url=verifiedfiles),
        ]]
        reply_markup=InlineKeyboardMarkup(btn)
        dlt=await m.reply_photo(
            photo=(VERIFY_IMG),
            caption=msg.format(message.from_user.mention, get_readable_time(TWO_VERIFY_GAP)),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await asyncio.sleep(300)
        await dlt.delete()
        return         
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        buttons = [[
                    InlineKeyboardButton('❤️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❤️', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
                ],[
                    InlineKeyboardButton('🍁 Update Channel 🍁', url=UPDATE_CHNL_LNK)
                  ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(script.GSTART_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup, disable_web_page_preview=True)
        await asyncio.sleep(2) 
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        buttons = [[
                    InlineKeyboardButton('🔰 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🔰', url=f'http://telegram.me/{temp.U_NAME}?startgroup=true')
                ],[
                    InlineKeyboardButton(' ʜᴇʟᴘ 📢', callback_data='help'),
                    InlineKeyboardButton(' ᴀʙᴏᴜᴛ 📖', callback_data='about')
                ],[
                    InlineKeyboardButton('ᴛᴏᴘ sᴇᴀʀᴄʜɪɴɢ ⭐', callback_data="topsearch"),
                    InlineKeyboardButton('ᴜᴘɢʀᴀᴅᴇ 🎟', callback_data="premium_info"),
                ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        current_time = datetime.now(pytz.timezone(TIMEZONE))
        curr_time = current_time.hour        
        if curr_time < 12:
            gtxt = "ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 🌞" 
        elif curr_time < 17:
            gtxt = "ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ 🌓" 
        elif curr_time < 21:
            gtxt = "ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ 🌘"
        else:
            gtxt = "ɢᴏᴏᴅ ɴɪɡʜᴛ 🌑"
        m=await message.reply_text("⏳")
        await asyncio.sleep(0.4)
        await m.delete()        
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, gtxt, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return

    if len(message.command) == 2 and message.command[1] in ["subscribe", "error", "okay", "help"]:
        buttons = [[
                    InlineKeyboardButton('🔰 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🔰', url=f'http://telegram.me/{temp.U_NAME}?startgroup=true')
                ],[
                    InlineKeyboardButton(' ʜᴇʟᴘ 📢', callback_data='help'),
                    InlineKeyboardButton(' ᴀʙᴏᴜᴛ 📖', callback_data='about')
                ],[
                    InlineKeyboardButton('ᴛᴏᴘ sᴇᴀʀᴄʜɪɴɢ ⭐', callback_data="topsearch"),
                    InlineKeyboardButton('ᴜᴘɢʀᴀᴅᴇ 🎟', callback_data="premium_info"),
                ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        current_time = datetime.now(pytz.timezone(TIMEZONE))
        curr_time = current_time.hour        
        if curr_time < 12:
            gtxt = "ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 🌞" 
        elif curr_time < 17:
            gtxt = "ɢᴏᴏᴅ ᴀғᴛᴇʀɴᴏᴏɴ 🌓" 
        elif curr_time < 21:
            gtxt = "ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ 🌘"
        else:
            gtxt = "ɢᴏᴏᴅ ɴɪɡʜᴛ 🌑"
        m=await message.reply_text("⏳")
        await asyncio.sleep(0.4)
        await m.delete()        
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, gtxt, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return
    if message.command[1].startswith("reff_"):
        try:
            user_id = int(message.command[1].split("_")[1])
        except ValueError:
            await message.reply_text("Invalid refer!")
            return
        if user_id == message.from_user.id:
            await message.reply_text("Hᴇʏ Dᴜᴅᴇ, Yᴏᴜ Cᴀɴ'ᴛ Rᴇғᴇʀ Yᴏᴜʀsᴇʟғ 🤣!\n\nsʜᴀʀᴇ ʟɪɴᴋ ʏᴏᴜʀ ғʀɪᴇɴᴅ ᴀɴᴅ ɢᴇᴛ 10 ʀᴇғᴇʀʀᴀʟ ᴘᴏɪɴᴛ ɪғ ʏᴏᴜ ᴀʀᴇ ᴄᴏʟʟᴇᴄᴛɪɴɢ 100 ʀᴇғᴇʀʀᴀʟ ᴘᴏɪɴᴛs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ 1 ᴍᴏɴᴛʜ ғʀᴇᴇ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀsʜɪᴘ.")
            return
        if referdb.is_user_in_list(message.from_user.id):
            await message.reply_text("Yᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴀʟʀᴇᴀᴅʏ ɪɴᴠɪᴛᴇᴅ ❗")
            return
        if await db.is_user_exist(message.from_user.id): 
            await message.reply_text("‼️ Yᴏᴜ Hᴀᴠᴇ Bᴇᴇɴ Aʟʀᴇᴀᴅʏ Iɴᴠɪᴛᴇᴅ ᴏʀ Jᴏɪɴᴇᴅ")
            return 
        try:
            uss = await client.get_users(user_id)
        except Exception:
            return 	    
        referdb.add_user(message.from_user.id)
        fromuse = referdb.get_refer_points(user_id) + 10
        if fromuse == 100:
            referdb.add_refer_points(user_id, 0) 
            await message.reply_text(f"🎉 𝗖𝗼𝗻𝗴𝗿𝗮𝘁𝘂𝗹𝗮𝘁𝗶𝗼𝗻𝘀! 𝗬𝗼𝘂 𝘄𝗼𝗻 𝟭𝟬 𝗥𝗲𝗳𝗲𝗿𝗿𝗮𝗹 𝗽𝗼𝗶𝗻𝘁 𝗯𝗲𝗰𝗮𝘂𝘀𝗲 𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝗯𝗲𝗲𝗻 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗜𝗻𝘃𝗶𝘁𝗲𝗱 ☞ {uss.mention}!")		    
            await message.reply_text(user_id, f"You have been successfully invited by {message.from_user.mention}!") 	
            seconds = 2592000
            if seconds > 0:
                expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
                user_data = {"id": user_id, "expiry_time": expiry_time}  # Using "id" instead of "user_id"  
                await db.update_user(user_data)  # Use the update_user method to update or insert user data		    
                await client.send_message(
                chat_id=user_id,
                text=f"<b>Hᴇʏ {uss.mention}\n\nYᴏᴜ ɢᴏᴛ 1 ᴍᴏɴᴛʜ ᴘʀᴇᴍɪᴜᴍ sᴜʙsᴄʀɪᴘᴛɪᴏɴ ʙʏ ɪɴᴠɪᴛɪɴɢ 10 ᴜsᴇʀs ❗", disable_web_page_preview=True              
                )
            for admin in ADMINS:
                await client.send_message(chat_id=admin, text=f"Sᴜᴄᴄᴇss ғᴜʟʟʏ ᴛᴀsᴋ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ʙʏ ᴛʜɪs ᴜsᴇʀ:\n\nuser Nᴀᴍᴇ: {uss.mention}\n\nUsᴇʀ ɪᴅ: {uss.id}!")	
        else:
            referdb.add_refer_points(user_id, fromuse)
            await message.reply_text(f"You have been successfully invited by {uss.mention}!")
            await client.send_message(user_id, f"𝗖𝗼𝗻𝗴𝗿𝗮𝘁𝘂𝗹𝗮𝘁𝗶𝗼𝗻𝘀! 𝗬𝗼𝘂 𝘄𝗼𝗻 𝟭𝟬 𝗥𝗲𝗳𝗲𝗿𝗿𝗮𝗹 𝗽𝗼𝗶𝗻𝘁 𝗯𝗲𝗰𝗮𝘂𝘀𝗲 𝗬𝗼𝘂 𝗵𝗮𝘃𝗲 𝗯𝗲𝗲𝗻 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗜𝗻𝘃𝗶𝘁𝗲𝗱 ☞{message.from_user.mention}!")
        return
        
    if len(message.command) == 2 and message.command[1] in ["premium"]:
        buttons = [[
                    InlineKeyboardButton('📲 ꜱᴇɴᴅ ᴘᴀʏᴍᴇɴᴛ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ', url=OWNER_LNK)
                  ],[
                    InlineKeyboardButton('❌ ᴄʟᴏꜱᴇ ❌', callback_data='close_data')
                  ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=(SUBSCRIPTION),
            caption=script.PREPLANS_TXT.format(message.from_user.mention, OWNER_UPI_ID, QR_CODE),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return  
    
    if len(message.command) == 2 and message.command[1].startswith('getfile'):
        movies = message.command[1].split("-", 1)[1] 
        movie = movies.replace('-',' ')
        message.text = movie 
        await auto_filter(client, message) 
        return
    
    data = message.command[1]
    try:
        _, grp_id, file_id = data.split("_", 2)
        grp_id = int(grp_id)
    except:
        _, grp_id, file_id = "", 0, data

    if not await db.has_premium_access(message.from_user.id): 
        try:
            btn = []
            chat = int(data.split("_", 2)[1])
            settings      = await get_settings(chat)
            fsub_channels = list(dict.fromkeys((settings.get('fsub', []) if settings else [])+ AUTH_CHANNELS)) 

            if fsub_channels:
                btn += await is_subscribed(client, message.from_user.id, fsub_channels)
            if AUTH_REQ_CHANNELS:
                btn += await is_req_subscribed(client, message.from_user.id, AUTH_REQ_CHANNELS)
            if btn:
                if len(message.command) > 1 and "_" in message.command[1]:
                    kk, file_id = message.command[1].split("_", 1)
                    btn.append([
                        InlineKeyboardButton("♻️ ᴛʀʏ ᴀɡᴀɪɴ ♻️", callback_data=f"checksub#{kk}#{file_id}")
                    ])
                    reply_markup = InlineKeyboardMarkup(btn)
                photo = random.choice(FSUB_PICS) if FSUB_PICS else "https://graph.org/file/7478ff3eac37f4329c3d8.jpg"
                caption = (
                    f"👋 ʜᴇʟʟᴏ {message.from_user.mention}\n\n"
                    "🛑 ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ ᴛʜᴇ ʀᴇǫᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟs ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.\n"
                    "👉 ᴊᴏɪɴ ᴀʟʟ ᴛʜᴇ ʙᴇʟᴏᴡ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɡᴀɪɴ."
                )
                await message.reply_photo(
                    photo=photo,
                    caption=caption,
                    reply_markup=reply_markup,
                    parse_mode=enums.ParseMode.HTML
                )
                return

        except Exception as e:
            await log_error(client, f"❗️ Force Sub Error:\n\n{repr(e)}")
            logger.error(f"❗️ Force Sub Error:\n\n{repr(e)}")


    user_id = m.from_user.id
    if not await db.has_premium_access(user_id):
        try:
            grp_id = int(grp_id)
            user_verified = await db.is_user_verified(user_id)
            settings = await get_settings(grp_id)
            is_second_shortener = await db.use_second_shortener(user_id, settings.get('verify_time', TWO_VERIFY_GAP)) 
            is_third_shortener = await db.use_third_shortener(user_id, settings.get('third_verify_time', THREE_VERIFY_GAP))
            if settings.get("is_verify", IS_VERIFY) and (not user_verified or is_second_shortener or is_third_shortener):
                verify_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
                await db.create_verify_id(user_id, verify_id)
                temp.VERIFICATIONS[user_id] = grp_id
                if message.command[1].startswith('allfiles'):
                    verify = await get_shortlink(f"https://telegram.me/{temp.U_NAME}?start=sendall_{user_id}_{verify_id}_{file_id}", grp_id, is_second_shortener, is_third_shortener)
                else:
                    verify = await get_shortlink(f"https://telegram.me/{temp.U_NAME}?start=notcopy_{user_id}_{verify_id}_{file_id}", grp_id, is_second_shortener, is_third_shortener)
                if is_third_shortener:
                    howtodownload = settings.get('tutorial_3', TUTORIAL_3)
                else:
                    howtodownload = settings.get('tutorial_2', TUTORIAL_2) if is_second_shortener else settings.get('tutorial', TUTORIAL)
                buttons = [[
                    InlineKeyboardButton(text="♻️ ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴠᴇʀɪꜰʏ ♻️", url=verify)
                ],[
                    InlineKeyboardButton(text="⁉️ ʜᴏᴡ ᴛᴏ ᴠᴇʀɪꜰʏ ⁉️", url=howtodownload)
                ]]
                reply_markup=InlineKeyboardMarkup(buttons)
                if await db.user_verified(user_id): 
                    msg = script.THIRDT_VERIFICATION_TEXT
                else:            
                    msg = script.SECOND_VERIFICATION_TEXT if is_second_shortener else script.VERIFICATION_TEXT
                n=await m.reply_text(
                    text=msg.format(message.from_user.mention),
                    protect_content = True,
                    reply_markup=reply_markup,
                    parse_mode=enums.ParseMode.HTML
                )
                await asyncio.sleep(300) 
                await n.delete()
                await m.delete()
                return
        except Exception as e:
            print(f"Error In Verification - {e}")
            pass

    if data.startswith("allfiles"):
        try:
            files = temp.GETALL.get(file_id)
            if not files:
                return await message.reply('<b><i>ɴᴏ ꜱᴜᴄʜ ꜰɪʟᴇ ᴇxɪꜱᴛꜱ !</b></i>')
            filesarr = []
            for file in files:
                file_id = file.file_id
                files_ = await get_file_details(file_id)
                files1 = files_[0]
                title = clean_filename(files1.file_name)
                size = get_size(files1.file_size)
                f_caption = files1.caption
                settings = await get_settings(int(grp_id))
                DREAMX_CAPTION = settings.get('caption', CUSTOM_FILE_CAPTION)
                if DREAMX_CAPTION:
                    try:
                        f_caption=DREAMX_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
                    except Exception as e:
                        logger.exception(e)
                        f_caption = f_caption
                if f_caption is None:
                    f_caption = f"{clean_filename(files1.file_name)}"
                
                if STREAM_MODE and not PREMIUM_STREAM_MODE:
                    
                    btn = [
                        [InlineKeyboardButton('🚀 ꜰᴀꜱᴛ ᴅᴏᴡɴʟᴏᴀᴅ / ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 🖥️', callback_data=f'generate_stream_link:{file_id}')],
                        [InlineKeyboardButton('📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌', url=UPDATE_CHNL_LNK)]  # Keep this line unchanged  
                    ]
                elif STREAM_MODE and PREMIUM_STREAM_MODE:
                    
                    if not await db.has_premium_access(message.from_user.id):
                        
                        btn = [
                            [InlineKeyboardButton('🚀 ꜰᴀꜱᴛ ᴅᴏᴡɴʟᴏᴀᴅ / ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 🖥️', callback_data=f'prestream')],
                            [InlineKeyboardButton('📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌', url=UPDATE_CHNL_LNK)]  # Keep this line unchanged  
                        ]
                    else:
                        
                        btn = [
                            [InlineKeyboardButton('🚀 ꜰᴀꜱᴛ ᴅᴏᴡɴʟᴏᴀᴅ / ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 🖥️', callback_data=f'generate_stream_link:{file_id}')],
                            [InlineKeyboardButton('📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌', url=UPDATE_CHNL_LNK)]  # Keep this line unchanged  
                        ]
                else:
                    btn = [[InlineKeyboardButton('📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌', url=UPDATE_CHNL_LNK)]]
                msg = await client.send_cached_media(
                    chat_id=message.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    protect_content=settings.get('file_secure', PROTECT_CONTENT),
                    reply_markup=InlineKeyboardMarkup(btn)
                )
                filesarr.append(msg)
            k = await client.send_message(chat_id=message.from_user.id, text=f"<b><u>❗️❗️❗️IMPORTANT❗️️❗️❗️</u></b>\n\nᴛʜɪꜱ ᴍᴏᴠɪᴇ ꜰɪʟᴇ/ᴠɪᴅᴇᴏ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ɪɴ <b><u><code>{get_time(DELETE_TIME)}</code></u> 🫥 <i></b>(ᴅᴜᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ)</i>.\n\n<b><i>ᴘʟᴇᴀꜱᴇ ꜰᴏʀᴡᴀʀᴅ ᴛʜɪꜱ ꜰɪʟᴇ ᴛᴏ ꜱᴏᴍᴇᴡʜᴇʀᴇ ᴇʟꜱᴇ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇʀᴇ</i></b>")
            await asyncio.sleep(DELETE_TIME)
            for x in filesarr:
                await x.delete()
            await k.edit_text("<b>ʏᴏᴜʀ ᴀʟʟ ᴠɪᴅᴇᴏꜱ/ꜰɪʟᴇꜱ ᴀʀᴇ ᴅᴇʟᴇᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ !\nᴋɪɴᴅʟʏ ꜱᴇᴀʀᴄʜ ᴀɡᴀɪɴ</b>")
            return
        except Exception as e:
            logger.exception(e)
            return

    user = message.from_user.id
    files_ = await get_file_details(file_id)
    settings = await get_settings(int(grp_id))
    if not files_:
        pre, file_id = ((base64.urlsafe_b64decode(data + "=" * (-len(data) % 4))).decode("ascii")).split("_", 1)
        try:
            if STREAM_MODE and not PREMIUM_STREAM_MODE:
                btn = [
                    [InlineKeyboardButton('🚀 ꜰᴀꜱᴛ ᴅᴏᴡɴʟᴏᡟ / ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 🖥️', callback_data=f'generate_stream_link:{file_id}')],
                    [InlineKeyboardButton('📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌', url=UPDATE_CHNL_LNK)]  # Keep this line unchanged  
                ]
            elif STREAM_MODE and PREMIUM_STREAM_MODE:
                if not await db.has_premium_access(message.from_user.id):
                   btn = [
                        [InlineKeyboardButton('🚀 ꜰᴀꜱᴛ ᴅᴏᴡɴʟᴏᡟ / ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 🖥️', callback_data=f'prestream')],
                        [InlineKeyboardButton('📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌', url=UPDATE_CHNL_LNK)]  # Keep this line unchanged  
                    ]
                else:
                    btn = [
                        [InlineKeyboardButton('🚀 ꜰᴀꜱᴛ ᴅᴏᴡɴʟᴏᡟ / ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 🖥️', callback_data=f'generate_stream_link:{file_id}')],
                        [InlineKeyboardButton('📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌', url=UPDATE_CHNL_LNK)]  # Keep this line unchanged  
                    ]
            else:
                btn = [[InlineKeyboardButton('📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌', url=UPDATE_CHNL_LNK)]] 
            msg = await client.send_cached_media(
                chat_id=message.from_user.id,
                file_id=file_id,
                protect_content=settings.get('file_secure', PROTECT_CONTENT),
                reply_markup=InlineKeyboardMarkup(btn))

            filetype = msg.media
            file = getattr(msg, filetype.value)
            title = clean_filename(file.file_name)
            size=get_size(file.file_size)
            f_caption = f"<code>{title}</code>"
            settings = await get_settings(int(grp_id))
            DREAMX_CAPTION = settings.get('caption', CUSTOM_FILE_CAPTION)
            if DREAMX_CAPTION:
                try:
                    f_caption=DREAMX_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='')
                except:
                    return
            await msg.edit_caption(
                f_caption,
                reply_markup=InlineKeyboardMarkup(btn)
            )
            k = await msg.reply(
                f"<b><u>❗️❗️❗️IMPORTANT❗️️❗️❗️</u></b>\n\n"
                f"ᴛʜɪꜱ ᴍᴏᴠɪᴇ ꜰɪʟᴇ/ᴠɪᴅᴇᴏ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ɪɴ <b><u><code>{get_time(DELETE_TIME)}</code></u> 🫥 <i></b>"
                "(ᴅᴜᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ)</i>.\n\n"
                "<b><i>ᴘʟᴇᴀꜱᴇ ꜰᴏʀᴡᴀʀᴅ ᴛʜɪꜱ ꜰɪʟᴇ ᴛᴏ ꜱᴏᴍᴇᴡʜᴇʀᴇ ᴇʟꜱᴇ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇʀᴇ</i></b>",
                quote=True
            )
            await asyncio.sleep(DELETE_TIME)
            await msg.delete()
            await k.edit_text("<b>ʏᴏᴜʀ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ ɪꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ !!</b>")
            return
        except Exception as e:
            logger.exception(e)
            pass
        return await message.reply('ɴᴏ ꜱᴜᴄʜ ꜰɪʟᴇ ᴇxɪꜱᴛꜱ !')
    
    files = files_[0]
    title = clean_filename(files.file_name)
    size = get_size(files.file_size)
    f_caption = files.caption
    settings = await get_settings(int(grp_id))            
    DREAMX_CAPTION = settings.get('caption', CUSTOM_FILE_CAPTION)
    if DREAMX_CAPTION:
        try:
            f_caption=DREAMX_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
        except Exception as e:
            logger.exception(e)
            f_caption = f_caption

    if f_caption is None:
        f_caption = clean_filename(files.file_name)
    
    if STREAM_MODE and not PREMIUM_STREAM_MODE:
        btn = [
            [InlineKeyboardButton('🚀 ꜰᴀꜱᴛ ᴅᴏᴡɴʟᴏᡟ / ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 🖥️', callback_data=f'generate_stream_link:{file_id}')],
            [InlineKeyboardButton('📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌', url=UPDATE_CHNL_LNK)]  # Keep this line unchanged  
        ]
    elif STREAM_MODE and PREMIUM_STREAM_MODE:
        if not await db.has_premium_access(message.from_user.id):
            btn = [
                [InlineKeyboardButton('🚀 ꜰᴀꜱᴛ ᴅᴏᴡɴʟᴏᡟ / ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 🖥️', callback_data=f'prestream')],
                [InlineKeyboardButton('📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌', url=UPDATE_CHNL_LNK)]  # Keep this line unchanged  
            ]
        else:
            btn = [
                [InlineKeyboardButton('🚀 ꜰᴀꜱᴛ ᴅᴏᴡɴʟᴏᡟ / ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 🖥️', callback_data=f'generate_stream_link:{file_id}')],
                [InlineKeyboardButton('📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌', url=UPDATE_CHNL_LNK)]  # Keep this line unchanged  
            ]
    else:
        btn = [[InlineKeyboardButton('📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌', url=UPDATE_CHNL_LNK)]]
    msg = await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        protect_content=settings.get('file_secure', PROTECT_CONTENT),
        reply_markup=InlineKeyboardMarkup(btn)
    )
    k = await msg.reply(
        f"<b><u>❗️❗️❗️IMPORTANT❗️️❗️❗️</u></b>\n\n"
        f"ᴛʜɪꜱ ᴍᴏᴠɪᴇ ꜰɪʟᴇ/ᴠɪᴅᴇᴏ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ɪɴ <b><u><code>{get_time(DELETE_TIME)}</code></u> 🫥 <i></b>"
        "(ᴅᴜᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ)</i>.\n\n"
        "<b><i>ᴘʟᴇᴀꜱᴇ ꜰᴏʀᴡᴀʀᴅ ᴛʜɪꜱ ꜰɪʟᴇ ᴛᴏ ꜱᴏᴍᴇᴡʜᴇʀᴇ ᴇʟꜱᴇ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇʀᴇ</i></b>",
        quote=True
    )     
    await asyncio.sleep(DELETE_TIME)
    await msg.delete()
    await k.edit_text("<b>ʏᴏᴜʀ ᴠɪᴅᴇᴏ / ꜰɪʟᴇ ɪꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ !!</b>")
    return

@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('DreamXlogs.txt', caption="📑 **ʟᴏɢꜱ**")
    except Exception as e:
        await message.reply(str(e))
        return
async def settings(client, message):
    user_id = message.from_user.id if message.from_user else None
    if not user_id:
        return await message.reply(f"ʏᴏᴜ'ʀᴇ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ.")
    chat_type = message.chat.type
    if chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grp_id = message.chat.id
        if not await is_check_admin(client, grp_id, message.from_user.id):
            return await message.reply_text(script.NT_ADMIN_ALRT_TXT)
        await db.connect_group(grp_id, user_id)
        btn = [[
                InlineKeyboardButton("👤 ᴏᴘᴇɴ ɪɴ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ 👤", callback_data=f"opnsetpm#{grp_id}")
              ],[
                InlineKeyboardButton("👥 ᴏᴘᴇɴ ʜᴇʀᴇ 👥", callback_data=f"opnsetgrp#{grp_id}")
              ]]
        await message.reply_text(
                text="<b>ᴡʜᴇʀᴇ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴏᴘᴇɴ ꜱᴇᴛᴛɪɴɢꜱ ᴍᴇɴᴜ ? ⚙️</b>",
                reply_markup=InlineKeyboardMarkup(btn),
                disable_web_page_preview=True,
                parse_mode=enums.ParseMode.HTML,
                reply_to_message_id=message.id
        )
    elif chat_type == enums.ChatType.PRIVATE:
        connected_groups = await db.get_connected_grps(user_id)
        if not connected_groups:
            return await message.reply_text("Nᴏ Cᴏɴɴᴇᴄᴛᴇᴅ Gʀᴏᴜᴘs Fᴏᴜɴᴅ .")
        group_list = []
        for group in connected_groups:
            try:
                Chat = await client.get_chat(group)
                group_list.append([ InlineKeyboardButton(text=Chat.title, callback_data=f"grp_pm#{Chat.id}") ])
            except Exception as e:
                print(f"Error In PM Settings Button - {e}")
                pass
        await message.reply_text(
                    "⚠️ ꜱᴇʟᴇᴄᴛ ᴛʜᴇ ɢʀᴏᴜᴘ ᴡʜᴏꜱᴇ ꜱᴇᴛᴛɪɴɢꜱ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴀɴɢᴇ.\n\n"
                    "ɪꜰ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪꜱ ɴᴏᴛ ꜱʜᴏᴡɪɴɢ ʜʏʀᴇ,\n"
                    "ᴜꜱᴇ /reload ɪɴ ᴛʜᴀᴛ ɢʀᴏᴜᴘ ᴀɴᴅ ɪᴛ ᴡɪʟʟ ᴀᴘᴘᴇᴀʀ ʜᴇʀᴇ.",
                    reply_markup=InlineKeyboardMarkup(group_list)
                )
        
@Client.on_message(filters.command('reload'))
async def connect_group(client, message):
    user_id = message.from_user.id
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        await db.connect_group(message.chat.id, user_id)
        await message.reply_text("Gʀᴏᴜᴘ Rᴇʟᴏᴀᴅᴇᴅ ✅ Nᴏᴡ Yᴏᴜ Cᴀɴ Mᴀɴᴀɡᴇ Tʜɪs Gʀᴏᴜᴘ Fʀᴏᴍ PM.")
    elif message.chat.type == enums.ChatType.PRIVATE:
        if len(message.command) < 2:
            await message.reply_text("Example: /reload 123456789")
            return
        try:
            group_id = int(message.command[1])
            if not await is_check_admin(client, group_id, user_id):
                await message.reply_text(script.NT_ADMIN_ALRT_TXT)
                return
            chat = await client.get_chat(group_id)
            await db.connect_group(group_id, user_id)
            await message.reply_text(f"Lɪɴᴋᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅ {chat.title} ᴛᴏ PM.")
        except:
            await message.reply_text("Invalid group ID or error occurred.")
            
@Client.on_message(filters.command('set_template'))
async def save_template(client, message):
    sts = await message.reply("ᴄʜᴇᴄᴋɪɴɢ ᴛᴇᴍᴘʟᴀᴛᴇ...")
    user_id = message.from_user.id if message.from_user else None
    if not user_id:
        return await message.reply("ʏᴏᴜ'ʀᴇ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ.")
    
    if message.chat.type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await sts.edit("⚠️ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ.")
    
    group_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, group_id, user_id):
        await message.reply_text(script.NT_ADMIN_ALRT_TXT)
        return
    if len(message.command) < 2:
        return await sts.edit("⚠️ ɴᴏ ᴛᴇᴍᴘʟᴀᴛᴇ ᴘʀᴏᴠɪᴅᴇᴅ!")
    
    template = message.text.split(" ", 1)[1]
    await save_group_settings(group_id, 'template', template)
    await sts.edit(
        f"✅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ᴛᴇᴍᴘʟᴀᴛᴇ ꜰᴏʀ <code>{title}</code> ᴛᴏ:\n\n{template}"
    )


# Must add REQST_CHANNEL and SUPPORT_CHAT_ID to use this feature 
@Client.on_message((filters.command(["request", "Request"]) | filters.regex("#request") | filters.regex("#Request")) & filters.group)
async def requests(bot, message):
    if REQST_CHANNEL is None or SUPPORT_CHAT_ID is None: return 
    if message.reply_to_message and SUPPORT_CHAT_ID == message.chat.id:
        chat_id = message.chat.id
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        success = True
        content = message.reply_to_message.text
        try:
            if REQST_CHANNEL is not None:
                btn = [[
                        InlineKeyboardButton('ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ', url=f"{message.reply_to_message.link}"),
                        InlineKeyboardButton('ꜱʜᴏᴡ ᴏᴘᴛɪᴏɴꜱ', callback_data=f'show_option#{reporter}')
                      ]]
                reported_post = await bot.send_message(chat_id=REQST_CHANNEL, text=f"<b>📝 ʀᴇǫᴜᴇꜱᴛ : <u>{content}</u>\n\n📚 ʀᴇᴘᴏʀᴛᴇᴅ ʙʏ : {mention}\n📖 ʀᴇᴘᴏʀᴛᴇʀ ɪᴅ : {reporter}\n\n</b>", reply_markup=InlineKeyboardMarkup(btn))
                success = True
            elif len(content) >= 3:
                for admin in ADMINS:
                    btn = [[
                        InlineKeyboardButton('ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ', url=f"{message.reply_to_message.link}"),
                        InlineKeyboardButton('ꜱʜᴏᴡ ᴏᴘᴛɪᴏɴꜱ', callback_data=f'show_option#{reporter}')
                      ]]
                    reported_post = await bot.send_message(chat_id=admin, text=f"<b>📝 ʀᴇǫᴜᴇꜱᴛ : <u>{content}</u>\n\n📚 ʀᴇᴘᴏʀᴛᴇᴅ ʙʏ : {mention}\n📖 ʀᴇᴘᴏʀᴛᴇʀ ɪᴅ : {reporter}\n\n</b>", reply_markup=InlineKeyboardMarkup(btn))
                    success = True
            else:
                if len(content) < 3:
                    await message.reply_text("<b>ʏᴏᴜ ᴍᴜꜱᴛ ᴛʏᴘᴇ ᴀʙᴏᴜᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ [ᴍɪɴɪᴍᴜᴍ 3 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ]. ʀᴇǫᴜᴇꜱᴛꜱ ᴄᴀɴ'ᴛ ʙᴇ ᴇᴍᴘᴛʏ.</b>")
            if len(content) < 3:
                success = False
        except Exception as e:
            await message.reply_text(f"Error: {e}")
            pass
    elif SUPPORT_CHAT_ID == message.chat.id:
        chat_id = message.chat.id
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        success = True
        content = message.text
        keywords = ["#request", "/request", "#Request", "/Request"]
        for keyword in keywords:
            if keyword in content:
                content = content.replace(keyword, "")
        try:
            if REQST_CHANNEL is not None and len(content) >= 3:
                btn = [[
                        InlineKeyboardButton('ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ', url=f"{message.link}"),
                        InlineKeyboardButton('ꜱʜᴏᴡ ᴏᴘᴛɪᴏɴꜱ', callback_data=f'show_option#{reporter}')
                      ]]
                reported_post = await bot.send_message(chat_id=REQST_CHANNEL, text=f"<b>📝 ʀᴇǫᴜᴇꜱᴛ : <u>{content}</u>\n\n📚 ʀᴇᴘᴏʀᴛᴇᴅ ʙʏ : {mention}\n📖 ʀᴇᴘᴏʀᴛᴇʀ ɪᴅ : {reporter}\n\n</b>", reply_markup=InlineKeyboardMarkup(btn))
                success = True
            elif len(content) >= 3:
                for admin in ADMINS:
                    btn = [[
                        InlineKeyboardButton('ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ', url=f"{message.link}"),
                        InlineKeyboardButton('ꜱʜᴏᴡ ᴏᴘᴛɪᴏɴꜱ', callback_data=f'show_option#{reporter}')
                      ]]
                    reported_post = await bot.send_message(chat_id=admin, text=f"<b>📝 ʀᴇǫᴜᴇꜱᴛ : <u>{content}</u>\n\n📚 ʀᴇᴘᴏʀᴛᴇᴅ ʙʏ : {mention}\n📖 ʀᴇᴘᴏʀᴛᴇʀ ɪᴅ : {reporter}\n\n</b>", reply_markup=InlineKeyboardMarkup(btn))
                    success = True
            else:
                if len(content) < 3:
                    await message.reply_text("<b>ʏᴏᴜ ᴍᴜꜱᴛ ᴛʏᴘᴇ ᴀʙᴏᴜᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ [ᴍɪɴɪᴍᴜᴍ 3 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ]. ʀᴇǫᴜᴇꜱᴛꜱ ᴄᴀɴ'ᴛ ʙᴇ ᴇᴍᴘᴛʏ.</b>")
            if len(content) < 3:
                success = False
        except Exception as e:
            await message.reply_text(f"Error: {e}")
            pass
    elif SUPPORT_CHAT_ID == message.chat.id:
        chat_id = message.chat.id
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        success = True
        content = message.text
        keywords = ["#request", "/request", "#Request", "/Request"]
        for keyword in keywords:
            if keyword in content:
                content = content.replace(keyword, "")
        try:
            if REQST_CHANNEL is not None and len(content) >= 3:
                btn = [[
                        InlineKeyboardButton('ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ', url=f"{message.link}"),
                        InlineKeyboardButton('ꜱʜᴏᴡ ᴏᴘᴛɪᴏɴꜱ', callback_data=f'show_option#{reporter}')
                      ]]
                reported_post = await bot.send_message(chat_id=REQST_CHANNEL, text=f"<b>📝 ʀᴇǫᴜᴇꜱᴛ : <u>{content}</u>\n\n📚 ʀᴇᴘᴏʀᴛᴇᴅ ʙʏ : {mention}\n📖 ʀᴇᴘᴏʀᴛᴇʀ ɪᴅ : {reporter}\n\n</b>", reply_markup=InlineKeyboardMarkup(btn))
                success = True
            elif len(content) >= 3:
                for admin in ADMINS:
                    btn = [[
                        InlineKeyboardButton('ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ', url=f"{message.link}"),
                        InlineKeyboardButton('ꜱʜᴏᴡ ᴏᴘᴛɪᴏɴꜱ', callback_data=f'show_option#{reporter}')
                      ]]
                    reported_post = await bot.send_message(chat_id=admin, text=f"<b>📝 ʀᴇǫᴜᴇꜱᴛ : <u>{content}</u>\n\n📚 ʀᴇᴘᴏʀᴛᴇᴅ ʙʏ : {mention}\n📖 ʀᴇᴘᴏʀᴛᴇʀ ɪᴅ : {reporter}\n\n</b>", reply_markup=InlineKeyboardMarkup(btn))
                    success = True
            else:
                if len(content) < 3:
                    await message.reply_text("<b>ʏᴏᴜ ᴍᴜꜱᴛ ᴛʏᴘᴇ ᴀʙᴏᴜᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ [ᴍɪɴɪᴍᴜᴍ 3 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ]. ʀᴇǫᴜᴇꜱᴛꜱ ᴄᴀɴ'ᴛ ʙᴇ ᴇᴍᴘᴛʏ.</b>")
            if len(content) < 3:
                success = False
        except Exception as e:
            await message.reply_text(f"Error: {e}")
            pass
    else:
        success = False
    if success:
        '''if isinstance(REQST_CHANNEL, (int, str)):
            channels = [REQST_CHANNEL]
        elif isinstance(REQST_CHANNEL, list):
            channels = REQST_CHANNEL
        for channel in channels:
            chat = await bot.get_chat(channel)
        #chat = int(chat)'''
        link = await bot.create_chat_invite_link(int(REQST_CHANNEL))
        btn = [[
                InlineKeyboardButton('ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ', url=link.invite_link),
                InlineKeyboardButton('ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ', url=f"{reported_post.link}")
              ]]
        await message.reply_text("<b>ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ᴀᴅᴅᴇᴅ! ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ꜰᴏʀ ꜱᴏᴍᴇ ᴛɪᴍᴇ.\n\nᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ꜰɪʀꜱᴛ & ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ.</b>", reply_markup=InlineKeyboardMarkup(btn))
    
@Client.on_message(filters.command("send") & filters.user(ADMINS))
async def send_msg(bot, message):
    if message.reply_to_message:
        target_id = message.text.split(" ", 1)[1]
        out = "Users Saved In DB Are:\n\n"
        success = False
        try:
            user = await bot.get_users(target_id)
            users = await db.get_all_users()
            async for usr in users:
                out += f"{usr['id']}"
                out += '\n'
            if str(user.id) in str(out):
                await message.reply_to_message.copy(int(user.id))
                success = True
            else:
                success = False
            if success:
                await message.reply_text(f"<b>ʏᴏᴜʀ ᴍᴇꜱꜱᴀɢᴇ ʜᴀꜱ ʙᴇᴇɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴇɴᴛ ᴛᴏ {user.mention}.</b>")
            else:
                await message.reply_text("<b>ᴛʜɪꜱ ᴜꜱᴇʀ ᴅɪᴅɴ'ᴛ ꜱᴀʀᴛᴇᴅ ᴛʜɪꜱ ʙᴏᴛ ʏᴇᴛ !</b>")
        except Exception as e:
            await message.reply_text(f"<b>Error: {e}</b>")
    else:
        await message.reply_text("<b>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴀꜱ ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ ᴜꜱɪɴɢ ᴛʜᴇ ᴛᴀʀɡᴇᴛ ᴄʜᴀᴛ ɪᴅ. ꜰᴏʀ ᴇɡ:  /send ᴜꜱᴇʀɪᴅ</b>")

@Client.on_message(filters.command("deletefiles") & filters.user(ADMINS))
async def deletemultiplefiles(bot, message):
    confirm_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton("Yes", callback_data="confirm_del_yes"),
        InlineKeyboardButton("No", callback_data="confirm_del_no")
    ]])
    sent_message = await message.reply_text(
        "⚠️ Aʀᴇ ʏᴏᴜ sᴜʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʟᴇᴀʀ ᴛʜᴇ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ʟɪsᴛ ?\n\n ᴅᴏ ʏᴏᴜ ꜱᴛɪʟʟ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ ?",
        reply_markup=confirm_markup
    )
    await asyncio.sleep(60)
    try:
        await sent_message.delete()
    except Exception as e:
        print(f"Error deleting the message: {e}")

@Client.on_callback_query(filters.regex('^confirm_del_'))
async def confirmation_handler(client, callback_query):
    action = callback_query.data.split("_")[-1] 
    if action == "yes":
        await db.delete_all_msg()  
        await callback_query.message.edit_text('🧹 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ ʟɪsᴛ ʜᴀs ʙᴇᴇɴ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅')
    elif action == "no":
        await callback_query.message.delete()  
    await callback_query.answer()

@Client.on_message(filters.command('set_caption'))
async def save_caption(client, message):
    grp_id = message.chat.id
    title = message.chat.title
    invite_link = await client.export_chat_invite_link(grp_id)
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text(script.NT_ADMIN_ALRT_TXT)
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("<b>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ...</b>")
    try:
        caption = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("<code>ɢɪᴠᴇ ᴍᴇ ᴀ ᴄᴀᴘᴛɪᴏɴ ᴀʟᴏɴɢ ᴡɪᴛʜ ɪᴛ.\n\nᴇxᴀᴍᴘʟᴇ -\n\nꜰᴏʀ ꜰɪʟᴇ ɴᴀᴍᴇ ꜱᴇɴᴅ <code>{file_name}</code>\nꜰᴏʀ ꜰɪʟᴇ ꜱɪᴢᴇ ꜱᴇɴᴅ <code>{file_size}</code>\n\n<code>/set_caption {file_name}</code></code>")
    await save_group_settings(grp_id, 'caption', caption)
    await message.reply_text(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ᴄᴀᴘᴛɪᴏɴ ꜰᴏʀ {title}\n\nᴄᴀᴘᴛɪᴏɴ - {caption}", disable_web_page_preview=True)
    await client.send_message(LOG_API_CHANNEL, f"#Set_Caption\n\nɢʀᴏᴜᴘ ɴᴀᴍᴇ : {title}\n\nɢʀᴏᴜᴘ ɪᴅ: {grp_id}\nɪɴᴠɪᴛᴇ ʟɪɴᴋ : {invite_link}\n\nᴜᴘᴅᴀᴛᴇᴅ ʙʏ : {message.from_user.username}")


@Client.on_message(filters.command(["set_tutorial", "set_tutorial_2", "set_tutorial_3"]))
async def set_tutorial(client, message: Message):
    grp_id = message.chat.id
    title = message.chat.title
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text(
            f"<b>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ...\n\nGroup Name: {title}\nGroup ID: {grp_id}</b>"
        )
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text(script.NT_ADMIN_ALRT_TXT)

    try:
        tutorial_link = message.text.split(" ", 1)[1]
    except IndexError:
        return await message.reply_text(
            f"<b>ᴄᴏᴍᴍᴀɴᴅ ɪɴᴄᴏᴍᴘʟᴇᴛᴇ !!\n\nᴜsᴇ ʟɪᴋᴇ ᴛʜɪs -</b>\n\n"
            f"<code>/{message.command[0]} https://t.me/dreamxbotz</code>"
        )
    if message.command[0] == "set_tutorial":
        tutorial_key = "tutorial"
    else:
        tutorial_key = f"tutorial_{message.command[0].split('_', 2)[2]}"

    await save_group_settings(grp_id, tutorial_key, tutorial_link)
    invite_link = await client.export_chat_invite_link(grp_id)
    await message.reply_text(
        f"<b>ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ {tutorial_key.replace('_', ' ').title()} ꜰᴏʀ {title}</b>\n\n"
        f"ʟɪɴᴋ - {tutorial_link}",
        disable_web_page_preview=True
    )
    await client.send_message(
        LOG_API_CHANNEL,
        f"#Set_{tutorial_key.title()}_Video\n\n"
        f"ɢʀᴏᴜᴘ ɴᴀᴍᴇ : {title}\n"
        f"ɢʀᴏᴜᴘ ɪᴅ : {grp_id}\n"
        f"ɪɴᴠɪᴛᴇ ʟɪɴᴋ : {invite_link}\n"
        f"ᴜᴘᴅᴀᴛᴇᴅ ʙʏ : {message.from_user.mention()}"
    )


async def handle_shortner_command(c, m, shortner_key, api_key, log_prefix, fallback_url, fallback_api):
    grp_id = m.chat.id
    if not await is_check_admin(c, grp_id, m.from_user.id):
        return await m.reply_text(script.NT_ADMIN_ALRT_TXT)
    if len(m.command) != 3:
        return await m.reply(
            f"<b>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʟɪᴋᴇ -\n\n`/{m.command[0]} omegalinks.in your_api_key_here`</b>"
        )
    sts = await m.reply("<b>♻️ ᴄʜᴇᴄᴋɪɴɢ...</b>")
    await asyncio.sleep(1.2)
    await sts.delete()
    if m.chat.type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await m.reply_text("<b>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ...</b>")
    try:
        URL = m.command[1]
        API = m.command[2]
        await save_group_settings(grp_id, shortner_key, URL)
        await save_group_settings(grp_id, api_key, API)
        await m.reply_text(f"<b><u>✅ sʜᴏʀᴛɴᴇʀ ᴀᴅᴅᴇᴅ</u>\n\nꜱɪᴛᴇ - `{URL}`\nᴀᴘɪ - `{API}`</b>")
        user_id = m.from_user.id
        user_info = f"@{m.from_user.username}" if m.from_user.username else f"{m.from_user.mention}"
        link = (await c.get_chat(m.chat.id)).invite_link
        grp_link = f"[{m.chat.title}]({link})"
        log_message = (
            f"#{log_prefix}\n\nɴᴀᴍᴇ - {user_info}\n\nɪᴅ - `{user_id}`"
            f"\n\nꜱɪᴛᴇ - {URL}\n\nᴀᴘɪ - `{API}`"
            f"\n\nɢʀᴏᴜᴘ - {grp_link}\nɢʀᴏᴜᴘ ɪᴅ - `{grp_id}`"
        )
        await c.send_message(LOG_API_CHANNEL, log_message, disable_web_page_preview=True)
    except Exception as e:
        await save_group_settings(grp_id, shortner_key, fallback_url)
        await save_group_settings(grp_id, api_key, fallback_api)
        await m.reply_text(
            f"<b><u>💢 ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ!</u>\n\n"
            f"ᴅᴇꜰᴀʊʟᴛ ꜱʜᴏʀᴛɴᴇʀ ᴀᴘᴘʟɪᴇᴅ\n"
            f"ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴀɴɢᴇ ᴀ ᴠᴀʟɪᴅ ꜱɪᴛᴇ ᴀɴᴅ ᴀᴘɪ ᴋᴇʏ.\n\n"
            f"ʟɪᴋᴇ:\n\n`/{m.command[0]} mdiskshortner.link your_api_key_here`\n\n"
            f"💔 ᴇʀʀᴏʀ - <code>{e}</code></b>"
        )

@Client.on_message(filters.command('set_log_channel'))
async def set_log(client, message):
    grp_id = message.chat.id
    title = message.chat.title
    invite_link = await client.export_chat_invite_link(grp_id)
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text(script.NT_ADMIN_ALRT_TXT)
    if len(message.text.split()) == 1:
        await message.reply("<b>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʟɪᴋᴇ ᴛʜɪꜱ - \n\n`/set_log_channel -100******`</b>")
        return
    sts = await message.reply("<b>♻️ ᴄʜᴇᴄᴋɪɴɢ...</b>")
    await asyncio.sleep(1.2)
    await sts.delete()
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("<b>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ...</b>")
    try:
        log = int(message.text.split(" ", 1)[1])
    except IndexError:
        return await message.reply_text("<b><u>ɪɴᴠᴀʟɪᴅ ꜰᴏʀᴍᴀᴛ!!</u>\n\nᴜsᴇ ʟɪᴋᴇ ᴛʜɪs - `/set_log_channel -100xxxxxxxx`</b>")
    except ValueError:
        return await message.reply_text('<b>ᴍᴀᴋᴇ sᴜʀᴇ ɪᴅ ɪs ɪɴᴛᴇɡᴇʀ...</b>')
    try:
        t = await client.send_message(chat_id=log, text="<b>ʜᴇʏ ᴡʜᴀᴛ's ᴜᴘ!!</b>")
        await asyncio.sleep(3)
        await t.delete()
    except Exception as e:
        return await message.reply_text(f'<b><u>😐 ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜɪs ʙᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ...</u>\n\n💔 ᴇʀʀᴏʀ - <code>{e}</code></b>')
    await save_group_settings(grp_id, 'log', log)
    await message.reply_text(f"<b>✅ sᴜᴄᴄᴇssꜰᴜʟʟʏ sᴇᴛ ʏᴏᴜʀ ʟᴏɡ ᴄʜᴀɴɴᴇʟ ꜰᴏʀ {title}\n\nɪᴅ - `{log}`</b>", disable_web_page_preview=True)
    user_id = message.from_user.id
    user_info = f"@{message.from_user.username}" if message.from_user.username else f"{message.from_user.mention}"
    link = (await client.get_chat(message.chat.id)).invite_link
    grp_link = f"[{message.chat.title}]({link})"
    log_message = f"#New_Log_Channel_Set\n\nɴᴀᴍᴇ - {user_info}\n\nɪᴅ - `{user_id}`\n\nʟᴏɡ ᴄʜᴀɴɴᴇʟ ɪᴅ - `{log}`\nɢʀᴏᴜᴘ ʟɪɴᴋ - `{grp_link}`\n\nɢʀᴏᴜᴘ ɪᴅ : `{grp_id}`"
    await client.send_message(LOG_API_CHANNEL, log_message, disable_web_page_preview=True) 


@Client.on_message(filters.command('set_time'))
async def set_time(client, message):
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("<b>ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ...</b>")       
    grp_id = message.chat.id
    title = message.chat.title
    invite_link = await client.export_chat_invite_link(grp_id)
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text(script.NT_ADMIN_ALRT_TXT)
    try:
        time = int(message.text.split(" ", 1)[1])
    except:
        return await message.reply_text("<b>ᴄᴏᴍᴍᴀɴᴅ ɪɴᴄᴏᴍᴘʟᴇᴛᴇ\n\nᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʟɪᴋᴇ ᴛʜɪꜱ - <code>/set_time 600</code> [ ᴛɪᴍᴇ ᴍᴜꜱᴛ ʙᴇ ɪɴ ꜱᴇᴄᴏɴᴅꜱ ]</b>")   
    await save_group_settings(grp_id, 'verify_time', time)
    await message.reply_text(f"<b>✅️ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴇᴛ 2ɴᴅ ᴠᴇʀɪꜰʏ ᴛɪᴍᴇ ꜰᴏʀ {title}\n\nᴛɪᴍᴇ - <code>{time}</code></b>")
    await client.send_message(LOG_API_CHANNEL, f"#Set_2nd_Verify_Time\n\nɢʀᴏᴜᴘ ɴᴀᴍᴇ : {title}\n\nɢʀᴏᴜᴘ ɪᴅ : {grp_id}\n\nɪɴᴠɪᴛᴇ ʟɪɴᴋ : {invite_link}\n\nᴜᴘᴅᴀᴛᴇᴅ ʙʏ : {message.from_user.username}")

@Client.on_message(filters.command('set_time_2'))
async def set_time_2(client, message):
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("<b>ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ...</b>")       
    grp_id = message.chat.id
    title = message.chat.title
    invite_link = await client.export_chat_invite_link(grp_id)
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text(script.NT_ADMIN_ALRT_TXT)
    try:
        time = int(message.text.split(" ", 1)[1])
    except:
        return await message.reply_text("<b>ᴄᴏᴍᴍᴀɴᴅ ɪɴᴄᴏᴍᴘʟᴇᴛᴇ\n\nᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʟɪᴋᴇ ᴛʜɪꜱ - <code>/set_time 3600</code> [ ᴛɪᴍᴇ ᴍᴜꜱᴛ ʙᴇ ɪɴ ꜱᴇᴄᴏɴᴅꜱ ]</b>")   
    await save_group_settings(grp_id, 'third_verify_time', time)
    await message.reply_text(f"<b>✅️ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴇᴛ 3ʀᴅ ᴠᴇʀɪꜰʏ ᴛɪᴍᴇ ꜰᴏʀ {title}\n\nᴛɪᴍᴇ - <code>{time}</code></b>")
    await client.send_message(LOG_API_CHANNEL, f"#Set_3rd_Verify_Time\n\nɢʀᴏᴜᴘ ɴᴀᴍᴇ : {title}\n\nɢʀᴏᴜᴘ ɪᴅ : {grp_id}\n\nɪɴᴠɪᴛᴇ ʟɪɴᴋ : {invite_link}\n\nᴜᴘᴅᴀᴛᴇᴅ ʙʏ : {message.from_user.username}")


@Client.on_message(filters.command('details'))
async def all_settings(client, message):
    if message.chat.type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("<b>ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ...</b>")
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text(script.NT_ADMIN_ALRT_TXT)
    try:
        settings = await get_settings(grp_id)
    except Exception as e:
        return await message.reply_text(f"<b>⚠️ ᴇʀʀᴏʀ ꜰᴇᴛᴄʜɪɴɢ ꜱᴇᴛᴛɪɴɢꜱ:</b>\n<code>{e}</code>")
    text = generate_settings_text(settings, title)
    btn = [
        [InlineKeyboardButton("♻️ ʀᴇꜱᴇᴛ ꜱᴇᴛᴛɪɴɢꜱ", callback_data=f"reset_group_{grp_id}")],
        [InlineKeyboardButton("🚫 ᴄʟᴏꜱᴇ", callback_data="close_data")]
    ]
    dlt = await message.reply_text(text, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)
    await asyncio.sleep(300)
    await dlt.delete()

@Client.on_callback_query(filters.regex(r"^reset_group_(\-\d+)$"))
async def reset_group_callback(client, callback_query):
    grp_id = int(callback_query.matches[0].group(1))
    user_id = callback_query.from_user.id
    if not await is_check_admin(client, grp_id, user_id):
        return await callback_query.answer(script.NT_ADMIN_ALRT_TXT, show_alert=True)
    await callback_query.answer("♻️ ʀᴇꜱᴇᴛᴛɪɴɢ ꜱᴇᴛᴛɪɴɢꜱ...")
    defaults = {
        'shortner': SHORTENER_WEBSITE,
        'api': SHORTENER_API,
        'shortner_two': SHORTENER_WEBSITE2,
        'api_two': SHORTENER_API2,
        'shortner_three': SHORTENER_WEBSITE3,
        'api_three': SHORTENER_API3,
        'verify_time': TWO_VERIFY_GAP,
        'third_verify_time': THREE_VERIFY_GAP,
        'template': IMDB_TEMPLATE,
        'tutorial': TUTORIAL,
        'tutorial_2': TUTORIAL_2,
        'tutorial_3': TUTORIAL_3,
        'caption': CUSTOM_FILE_CAPTION,
        'log': LOG_CHANNEL,
        'is_verify': IS_VERIFY,
        'fsub': AUTH_CHANNELS
    }
    current = await get_settings(grp_id)
    if current == defaults:
        return await callback_query.answer("✅ ꜱᴇᴛᴛɪɴɢꜱ ᴀʟʀᴇᴀᴅʏ ᴅᴇꜰᴀᴜʟᴛ.", show_alert=True)
    for key, value in defaults.items():
        await save_group_settings(grp_id, key, value)
    updated = await get_settings(grp_id)
    title = callback_query.message.chat.title
    text = generate_settings_text(updated, title, reset_done=True)
    buttons = [
        [InlineKeyboardButton("♻️ ʀᴇꜱᴇᴛ ꜱᴇᴛᴛɪɴɢꜱ", callback_data=f"reset_group_{grp_id}")],
        [InlineKeyboardButton("🚫 ᴄʟᴏꜱᴇ", callback_data="close_data")]
    ]
    await callback_query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

@Client.on_message(filters.command("verify") & filters.user(ADMINS))
async def verify(bot, message):
    try:
        chat_type = message.chat.type
        if chat_type == enums.ChatType.PRIVATE:
            return await message.reply_text("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋs ᴏɴʟʏ ɪɴ ɢʀᴏᴜᴘs!")
        if chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            grpid = message.chat.id
            title = message.chat.title
            command_text = message.text.split(' ')[1] if len(message.text.split(' ')) > 1 else None
            if command_text == "off":
                await save_group_settings(grpid, 'is_verify', False)
                return await message.reply_text("✓ ᴠᴇʀɪꜰʏ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅɪsᴀʙʟᴇᴅ.")
            elif command_text == "on":
                await save_group_settings(grpid, 'is_verify', True)
                return await message.reply_text("✗ ᴠᴇʀɪꜰʏ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ.")
            else:
                return await message.reply_text("ʜɪ, ᴛᴏ ᴇɴᴀʙʟᴇ ᴠᴇʀɪꜰʏ, ᴜsᴇ <code>/verify on</code> ᴀɴᴅ ᴛᴏ ᴅɪsᴀʙʟᴇ ᴠᴇʀɪꜰʏ, ᴜsᴇ <code>/verify off</code>.")
    except Exception as e:
        print(f"Error: {e}")
        await message.reply_text(f"Error: {e}")

@Client.on_message(filters.command('set_fsub'))
async def set_fsub(client, message):
    try:
        userid = message.from_user.id if message.from_user else None
        if not userid:
            return await message.reply("<b>You are Anonymous admin you can't use this command !</b>")
        if message.chat.type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            return await message.reply_text("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs")
        grp_id = message.chat.id
        title = message.chat.title
        if not await is_check_admin(client, grp_id, userid):
            return await message.reply_text(script.NT_ADMIN_ALRT_TXT)
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            return await message.reply_text(
                "ᴄᴏᴍᴍᴀɴᴅ ɪɴᴄᴏᴍᴘʟᴇᴛᴇ!\n\n"
                "ᴄᴀɴ ᴀᴅᴅ ᴍᴜʟᴛɪᴘʟᴇ ᴄʜᴀɴɴᴇʟs sᴇᴘᴀʀᴀᴛᴇᴅ ʙʏ sᴘᴀᴄᴇs. ʟɪᴋᴇ: /sᴇᴛ_ғsᴜʙ ɪᴅ1 ɪᴅ2 ɪᴅ3\n"
            )
        option = args[1].strip()
        try:
            fsub_ids = [int(x) for x in option.split()]
        except ValueError:
            return await message.reply_text('ᴍᴀᴋᴇ sᴜʀᴇ ᴀʟʟ ɪᴅs ᴀʀᴇ ɪɴᴛᴇɡᴇʀs.')
        if len(fsub_ids) > 5:
            return await message.reply_text("ᴍᴀxɪᴍᴜᴍ 5 ᴄʜᴀɴɴᴇʟs ᴀʟʟᴏᴡᴇᴅ.")
        channels = "ᴄʜᴀɴɴᴇʟs:\n"
        channel_titles = []
        for id in fsub_ids:
            try:
                chat = await client.get_chat(id)
            except Exception as e:
                return await message.reply_text(
                    f"{id} ɪs ɪɴᴠᴀʟɪᴅ!\nᴍᴀᴋᴇ sᴜʀᴇ ᴛʜɪs ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ.\n\nError - {e}"
                )
            if chat.type != enums.ChatType.CHANNEL:
                return await message.reply_text(f"{id} ɪs ɴᴏᴛ ᴀ ᴄʜᴀɴɴᴇʟ.")
            channel_titles.append(f"{chat.title} (`{id}`)")
            channels += f'{chat.title}\n'
        await save_group_settings(grp_id, 'fsub', fsub_ids)
        await message.reply_text(f"sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ sᴇᴛ ꜰꜱᴜʙ ᴄʜᴀɴɴᴇʟ(ꜱ) ғᴏʀ {title} ᴛᴏ\n\n{channels}")
        mention = message.from_user.mention if message.from_user else "Unknown"
        await client.send_message(
            LOG_API_CHANNEL,
            f"#Fsub_Channel_set\n\n"
            f"ᴜꜱᴇʀ - {mention} ꜱᴇᴛ ᴛʜᴇ ꜰᴏʀᴄᴇ ᴄʜᴀɴɴᴇʟ(ꜱ) ꜰᴏʀ {title}:\n\n"
            f"ꜰꜱᴜʙ ᴄʜᴀɴɴᴇʟ(ꜱ):\n" + '\n'.join(channel_titles)
        )
    except Exception as e:
        err_text = f"⚠️ Error in set_fSub :\n{e}"
        logger.error(err_text)
        await client.send_message(LOG_API_CHANNEL, err_text)

@Client.on_message(filters.private & filters.command("resetallgroup") & filters.user(ADMINS))
async def reset_all_settings(client, message):
    try:
        reset_count = await db.dreamx_reset_settings()
        await message.reply_text(
            f"<b>ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ꜱᴇᴛᴛɪɴɢꜱ ꜰᴏʀ  <code>{reset_count}</code> ɢʀᴏᴜᴘꜱ. ᴅᴇꜰᴀᴜʟᴛ ᴠᴀʟᴜᴇꜱ ᴡɪʟʟ ʙᴇ ᴜꜱᴇᴅ ✅</b>",
            quote=True
        )
    except Exception as e:
        print(f"Error: {e}")
        await message.reply_text(
            "<b>🚫 An error occurred while resetting group settings.\nPlease try again later.</b>",
            quote=True
        )

@Client.on_message(filters.command("trial_reset"))
async def reset_trial(client, message):
    user_id = message.from_user.id
    if user_id not in ADMINS:
        await message.reply("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
        return
    try:
        if len(message.command) > 1:
            target_user_id = int(message.command[1])
            updated_count = await db.reset_free_trial(target_user_id)
            message_text = f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʀᴇꜱᴇᴛ ꜰʀᴇᴇ ᴛʀᴀɪʟ ꜰᴏʀ ᴜꜱᴇʀꜱ {target_user_id}." if updated_count else f"ᴜꜱᴇʀ {target_user_id} ɴᴏᴛ ꜰᴏᴜɴᴅ ᴏʀ ᴅᴏɴ'ᴛ ᴄʟᴀɪᴍ ꜰʀᴇᴇ ᴛʀᴀɪʟ ʏᴇᴛ."
        else:
            updated_count = await db.reset_free_trial()
            message_text = f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʀᴇꜱᴇᴛ ꜰʀᴇᴇ ᴛʀᴀɪʟ ꜰᴏʀ {updated_count} ᴜꜱᴇʀꜱ."
        await message.reply_text(message_text)
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")

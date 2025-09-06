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
    html1 = '<a href="https://example.com">HTML Link with quotes</a>'
    await client.send_message(
        chat_id=message.chat.id,
        text=html1,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
    # Method 2: HTML without quotes (not recommended, but for test)
    html2 = '<a href=https://example.com>HTML Link no quotes</a>'
    await client.send_message(
        chat_id=message.chat.id,
        text=html2,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
    # Method 3: Markdown (should not work for inline links in Telegram, but for test)
    md1 = '[Markdown Link](https://example.com)'
    await client.send_message(
        chat_id=message.chat.id,
        text=md1,
        parse_mode="Markdown",
        disable_web_page_preview=True
    )
    # Method 4: HTML with bold inside
    html3 = '<a href="https://example.com"><b>HTML Bold Link</b></a>'
    await client.send_message(
        chat_id=message.chat.id,
        text=html3,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
    # Method 5: HTML with code inside
    html4 = '<a href="https://example.com"><code>HTML Code Link</code></a>'
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
        try:
            dlt=await m.reply_photo(
                photo=(VERIFY_IMG),
                caption=msg.format(message.from_user.mention, get_readable_time(TWO_VERIFY_GAP)),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
        except Exception as e:
            await message.reply_text(f"Error: {e}")
            return

        await asyncio.sleep(300)
        await dlt.delete()
        return         
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        # Do nothing when /start is used in groups/chats
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        # Do nothing when someone just uses /start
        return

    if len(message.command) == 2 and message.command[1] in ["subscribe", "error", "okay", "help"]:
        # Do nothing for these specific parameters too
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
                    "🛑 ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ ᴛʜᴇ ʀᴇǫᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟs ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ғɪʟᴇs.\n"
                    "👉 ᴊᴏɪɴ ᴀʟʟ ᴛʜᴇ ʙᴇʟᴏᴡ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴄʟɪᴄᴋ '♻️ ᴛʀʏ ᴀɡᴀɪɴ' ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇ."
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
            # NEW: Always send credit / count messages before batch
            try:
                await client.send_message(message.from_user.id, "😊 Your credit is 0")
                await client.send_message(message.from_user.id, f"😊 You will receive 😊 {len(files)} Movie files.")
            except Exception:
                pass
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
                    # Remove buttons - no buttons when sending files
                    btn = []
                elif STREAM_MODE and PREMIUM_STREAM_MODE:
                    
                    if not await db.has_premium_access(message.from_user.id):
                        # Remove buttons - no buttons when sending files
                        btn = []
                    else:
                        # Remove buttons - no buttons when sending files
                        btn = []
                else:
                    # Remove buttons - no buttons when sending files
                    btn = []
                msg = await client.send_cached_media(
                    chat_id=message.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    protect_content=settings.get('file_secure', PROTECT_CONTENT),
                    reply_markup=InlineKeyboardMarkup(btn) if btn else None
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
                # Remove buttons - no buttons when sending files
                btn = []
            elif STREAM_MODE and PREMIUM_STREAM_MODE:
                if not await db.has_premium_access(message.from_user.id):
                   # Remove buttons - no buttons when sending files
                   btn = []
                else:
                    # Remove buttons - no buttons when sending files
                    btn = []
            else:
                # Remove buttons - no buttons when sending files
                btn = [] 
            # Pre-file static messages (single file path)
            try:
                await client.send_message(message.from_user.id, "😊 Your credit is 0")
                await client.send_message(message.from_user.id, "😊 You will receive 😊 1 Movie file.")
            except Exception:
                pass
            msg = await client.send_cached_media(
                chat_id=message.from_user.id,
                file_id=file_id,
                protect_content=settings.get('file_secure', PROTECT_CONTENT),
                reply_markup=InlineKeyboardMarkup(btn) if btn else None)

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
                reply_markup=InlineKeyboardMarkup(btn) if btn else None
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


# Clean implementation of request forwarding (support group only)
@Client.on_message((filters.command(["request", "Request"]) | filters.regex("(?i)#request")) & filters.group)
async def requests(client, message):
    if REQST_CHANNEL is None or SUPPORT_CHAT_ID is None:
        return
    if message.chat.id != SUPPORT_CHAT_ID:
        return
    if message.reply_to_message and message.reply_to_message.text:
        content = message.reply_to_message.text
        origin_link = message.reply_to_message.link
    else:
        content = message.text or ""
        origin_link = message.link
    for kw in ("#request", "/request", "#Request", "/Request"):
        content = content.replace(kw, "")
    content = content.strip()
    if len(content) < 3:
        await message.reply_text("<b>Request too short (min 3 chars)</b>")
        return
    reporter_id = message.from_user.id if message.from_user else 0
    reporter_mention = message.from_user.mention if message.from_user else "User"
    btn = [[InlineKeyboardButton('View request', url=origin_link)]]
    text = (f"<b>📝 Request:</b> <u>{content}</u>\n\n"
            f"👤 {reporter_mention} | <code>{reporter_id}</code>")
    try:
        if REQST_CHANNEL:
            await client.send_message(REQST_CHANNEL, text, reply_markup=InlineKeyboardMarkup(btn))
        else:
            for admin in ADMINS:
                await client.send_message(admin, text, reply_markup=InlineKeyboardMarkup(btn))
        await message.reply_text("✅ Forwarded")
    except Exception as e:
        await message.reply_text(f"Error: {e}")
    return

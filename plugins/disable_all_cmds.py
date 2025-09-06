from pyrogram import Client, filters, enums

# High-priority catch-all for commands to disable them.
# This should load before other command handlers (Pyrogram processes in added order; ensure filename alphabetically early if needed).

@Client.on_message(filters.command([]))
async def _noop(client, message):
    # Pyrogram needs at least one command string; instead intercept by checking message via custom condition below.
    pass

@Client.on_message(filters.create(lambda _, __, m: bool(m.text) and m.text.startswith('/')))
async def block_all_commands(client, message):
    if message.chat.type == enums.ChatType.PRIVATE and message.text.startswith('/start') and len(message.command) == 2:
        payload = message.command[1]
        # Allow only expected deep link prefixes
        if payload.startswith(('file_', 'allfiles_', 'notcopy_', 'sendall_')):
            return  # permit
    # Allow nothing else: just silently ignore.
    return

# Block bot replies in private chats for non deep-link messages (except file delivery triggers via /start handled elsewhere)
@Client.on_message(filters.private & ~filters.command('start'))
async def block_private_everything(client, message):
    # If user sends anything in PM (command or text) that's not a deep-link /start, ignore.
    return

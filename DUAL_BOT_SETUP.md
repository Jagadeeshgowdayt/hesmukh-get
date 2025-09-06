# Dual Bot Setup Guide

This bot now supports running two identical instances simultaneously with different bot tokens.

## Configuration

### Environment Variables

You can set these environment variables or modify the defaults in `info.py`:

**For First Bot (Primary):**
- `BOT_TOKEN` - Your first bot token from @BotFather
- `SESSION` - Session name for first bot (default: 'X_ploreFlix_1080_search')

**For Second Bot:**
- `BOT_TOKEN2` - Your second bot token from @BotFather  
- `SESSION2` - Session name for second bot (default: 'X_ploreFlix_1080_search_2')
- `DUAL_BOT_MODE` - Set to "True" to enable dual bot mode (default: True)

### Bot Tokens

**Current Configuration:**
- Primary Bot Token: `8251332933:AAHgs4HjXc8tsx1jsiWsgW_ZGdydkIE_PUc`
- Secondary Bot Token: `8251332933:AAHgs4HjXc8tsx1jsiWsgW_ZGdydkIE_PUc` (same as primary)

⚠️ **Important:** Currently both bots are using the same token. You need to create a second bot with @BotFather and update `BOT_TOKEN2` for proper dual bot functionality.

## How to Create a Second Bot

1. Go to @BotFather on Telegram
2. Send `/newbot`
3. Follow the instructions to create a new bot
4. Copy the bot token
5. Update the `BOT_TOKEN2` variable with your new token

## Features

When dual bot mode is enabled:

✅ Both bots will start simultaneously
✅ Both bots will receive all plugins and commands  
✅ Both bots will share the same database
✅ Both bots will send startup notifications to the log channel
✅ Load balancing across two bot instances
✅ Backup functionality if one bot goes down

## Disable Dual Bot Mode

To run only one bot, set `DUAL_BOT_MODE=False` in your environment variables.

## Testing

After setup, both bots should respond to commands and function identically. Check the log channel for startup messages from both bots.

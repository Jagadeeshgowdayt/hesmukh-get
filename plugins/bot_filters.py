"""
Bot-specific filters for dual bot mode
This module provides filters to control which bot responds in which context
"""

from pyrogram import filters
from info import DUAL_BOT_MODE, SESSION, SESSION2

def bot1_no_groups_filter():
    """
    Custom filter that blocks bot1 from responding in groups/chats
    but allows normal operation in private messages
    """
    async def func(flt, client, message):
        # If dual bot mode is disabled, allow all messages
        if not DUAL_BOT_MODE:
            return True
            
        # Check if this is bot1 by session name
        if hasattr(client, 'name') and client.name == SESSION:
            # This is bot1 - block group messages
            if message.chat.type.name in ['GROUP', 'SUPERGROUP']:
                return False
            
        # Allow all other scenarios (bot2 or private messages)
        return True
    
    return filters.create(func)

def bot2_only_filter():
    """
    Filter to block bot2 from private messages
    """
    async def func(flt, client, message):
        if not DUAL_BOT_MODE:
            return True
            
        # Check if this is bot2 by session name
        if hasattr(client, 'name') and client.name == SESSION2:
            # This is bot2 - block private messages
            if message.chat.type.name == 'PRIVATE':
                return False
            
        # Allow all other scenarios (bot1 or group messages)
        return True
    
    return filters.create(func)

# Create the filter instances
bot1_filter = bot1_no_groups_filter()
bot2_filter = bot2_only_filter()

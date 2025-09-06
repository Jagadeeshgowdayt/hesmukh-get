#!/usr/bin/env python3
# Index Test Script

import sys
import asyncio
import logging
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

async def test_index_imports():
    """Test if all indexing-related imports work correctly"""
    try:
        print("🔍 Testing index.py imports...")
        
        # Test basic imports
        from pyrogram import Client, filters, enums
        from pyrogram.errors import FloodWait
        print("✅ Pyrogram imports successful")
        
        # Test project-specific imports
        from info import ADMINS, INDEX_REQ_CHANNEL
        print("✅ Info imports successful")
        print(f"   INDEX_REQ_CHANNEL: {INDEX_REQ_CHANNEL}")
        print(f"   ADMINS: {len(ADMINS) if ADMINS else 'None'} admin(s)")
        
        # Test database imports
        from database.ia_filterdb import save_file
        print("✅ Database imports successful")
        
        # Test utils imports
        from utils import temp, get_readable_time
        print("✅ Utils imports successful")
        print(f"   temp.CURRENT: {getattr(temp, 'CURRENT', 'Not defined')}")
        print(f"   temp.CANCEL: {getattr(temp, 'CANCEL', 'Not defined')}")
        
        # Test if index.py loads without errors
        import plugins.index
        print("✅ Index plugin loaded successfully")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        return False

async def test_index_functions():
    """Test if index functions are available"""
    try:
        from plugins.index import index_files_to_db, get_progress_bar
        print("✅ Index functions imported successfully")
        
        # Test progress bar function
        progress = get_progress_bar(50)
        print(f"   Progress bar test (50%): {progress}")
        
        return True
    except Exception as e:
        print(f"❌ Function test failed: {e}")
        return False

async def main():
    print("🚀 Starting Index Functionality Test\n")
    
    # Test imports
    import_success = await test_index_imports()
    print()
    
    # Test functions
    if import_success:
        function_success = await test_index_functions()
        print()
        
        if import_success and function_success:
            print("✅ All index tests passed!")
            print("\n📋 Index functionality should be working.")
            print("   To use indexing:")
            print("   1. Forward a message from a channel to the bot")
            print("   2. Or send a channel message link to the bot")
            print("   3. Use /setskip command to set skip number")
        else:
            print("❌ Some tests failed. Check the errors above.")
    else:
        print("❌ Import tests failed. Cannot proceed with function tests.")

if __name__ == "__main__":
    asyncio.run(main())

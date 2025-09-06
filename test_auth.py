#!/usr/bin/env python3

# Test script to verify AUTH_CHANNELS configuration
import sys
import os
sys.path.append(os.path.dirname(__file__))

try:
    from info import AUTH_CHANNELS, auth_channels, id_pattern, AUTH_REQ_CHANNELS
    
    print("=== AUTH_CHANNELS Configuration Test ===")
    print(f"Raw auth_channels value: {auth_channels}")
    print(f"Parsed AUTH_CHANNELS: {AUTH_CHANNELS}")
    print(f"AUTH_CHANNELS type: {type(AUTH_CHANNELS)}")
    print(f"AUTH_CHANNELS length: {len(AUTH_CHANNELS)}")
    
    if AUTH_CHANNELS:
        print("✅ AUTH_CHANNELS is properly configured!")
        for i, channel in enumerate(AUTH_CHANNELS):
            print(f"  Channel {i+1}: {channel}")
    else:
        print("❌ AUTH_CHANNELS is empty or not configured properly")
    
    print(f"\nAUTH_REQ_CHANNELS: {AUTH_REQ_CHANNELS}")
    
    # Test regex pattern
    test_id = "-1002723371583"
    match = id_pattern.search(test_id)
    print(f"\nRegex test for '{test_id}': {match}")
    if match:
        print("✅ ID pattern regex is working correctly")
    else:
        print("❌ ID pattern regex failed")
        
    print("\n=== Force Subscription Logic Test ===")
    if AUTH_CHANNELS:
        print("Force subscription is ENABLED")
        print("Users will need to join these channels to search movies:")
        for channel in AUTH_CHANNELS:
            print(f"  - Channel ID: {channel}")
    else:
        print("Force subscription is DISABLED")
        
except Exception as e:
    print(f"❌ Error loading configuration: {e}")
    import traceback
    traceback.print_exc()

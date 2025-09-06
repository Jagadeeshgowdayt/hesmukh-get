#!/usr/bin/env python3
# Simple script to check force subscription configuration

def check_force_subscription():
    try:
        from info import AUTH_CHANNELS, auth_channels, id_pattern
        from utils import is_subscribed
        
        print("=== Force Subscription Check ===")
        print(f"Raw auth_channels value: '{auth_channels}'")
        print(f"Parsed AUTH_CHANNELS: {AUTH_CHANNELS}")
        print(f"AUTH_CHANNELS type: {type(AUTH_CHANNELS)}")
        print(f"AUTH_CHANNELS length: {len(AUTH_CHANNELS)}")
        
        if AUTH_CHANNELS:
            print("✅ AUTH_CHANNELS is properly configured!")
            for i, channel in enumerate(AUTH_CHANNELS):
                print(f"  Channel {i+1}: {channel}")
            
            print("\n=== Configuration Summary ===")
            print("✅ Force subscription is ENABLED")
            print("✅ Users will need to join these channels to search movies:")
            for channel in AUTH_CHANNELS:
                print(f"   📢 Channel ID: {channel}")
                
            print("\n=== How Force Subscription Works ===")
            print("1. When user searches for a movie")
            print("2. Bot checks if user has joined AUTH_CHANNELS")
            print("3. If not joined, shows subscription prompt with join buttons")
            print("4. User must join all channels to access files")
            print("5. Premium users bypass force subscription")
            
        else:
            print("❌ AUTH_CHANNELS is empty or not configured properly")
            
    except ImportError as e:
        print(f"❌ Import error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    check_force_subscription()

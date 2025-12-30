#!/usr/bin/env python3
"""API Version Ouija Board - When documentation is a ghost town."""

import random
import sys
from datetime import datetime

class APIOuija:
    """Spiritual guidance for your API integration woes."""
    
    def __init__(self):
        self.versions = ['v1', 'v2', 'v2.1', 'v3', 'v3.5', 'vNext', 'beta', 'legacy']
        self.responses = [
            "The spirits say: 'Just use v2, everyone else does'",
            "Ectoplasmic reading: Try the deprecated one - it still works!",
            "Ghostly whisper: 'Check Stack Overflow from 2017'",
            "Ouija says: v3, but prepare for breaking changes tomorrow",
            "Spirit guide suggests: Use whatever the CEO demoed last week",
            "Phantom advice: 'Copy-paste from that old project'"
        ]
    
    def divine_version(self):
        """Channel the API spirits for guidance."""
        print("\n🔮 Contacting the API spirits...\n")
        
        # Mystical algorithm (patent pending)
        random.seed(datetime.now().microsecond)
        version = random.choice(self.versions)
        advice = random.choice(self.responses)
        
        # Add some dramatic delay for authenticity
        import time
        for _ in range(3):
            print(".", end='', flush=True)
            time.sleep(0.5)
        
        print(f"\n\n✨ Version: {version}")
        print(f"💡 Advice: {advice}")
        
        # Bonus: The ghost in the machine
        if random.random() > 0.7:
            print("👻 Bonus: Also try adding '?format=json' to the URL")
        
        return version
    
    def test_endpoint(self, version):
        """Simulate what happens when you actually try it."""
        outcomes = [
            f"{version} works! (for now)",
            f"{version} returns 200 but wrong data structure",
            f"{version} deprecated - use {random.choice(self.versions)} instead",
            f"{version} requires authentication we don't have",
            "Rate limited. Try again in 24 hours."
        ]
        return random.choice(outcomes)


def main():
    """Main séance."""
    print("=== API VERSION OUIJA BOARD ===")
    print("When documentation fails, consult the spirits!\n")
    
    board = APIOuija()
    
    while True:
        print("\n1. Divine which version to use")
        print("2. Test the chosen version")
        print("3. Exit (and probably use v2 anyway)")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "1":
            version = board.divine_version()
        elif choice == "2":
            if 'version' not in locals():
                print("\n⚠️  You need to divine a version first!")
                continue
            result = board.test_endpoint(version)
            print(f"\n🔧 Test result: {result}")
        elif choice == "3":
            print("\n👋 May your API calls be ever successful!")
            break
        else:
            print("\n❌ Invalid choice. The spirits are confused.")

if __name__ == "__main__":
    main()

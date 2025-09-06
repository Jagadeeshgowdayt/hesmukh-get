#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# Read the file
with open('c:/Users/jagad/Downloads/hesmukh-get/plugins/pmfilter.py', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Replace all instances of corrupted emoji after "Download now"
# Pattern 1: Find lines with "Download now" followed by corrupted characters
content = re.sub(r'(Download now\s*)[^\<\>]*(<)', r'\1👈👈\2', content)

# Pattern 2: Direct replacement of common corruption patterns
content = content.replace('Download now ��', 'Download now 👈👈')
content = content.replace('Download now �', 'Download now 👈👈')

# Pattern 3: Fix any remaining issues with specific line patterns
content = re.sub(r'f"<a href=\\"[^"]*\\">👉👉 Download now[^<]*</a>"', 
                 'f"<a href=\\"{deep_link}\\">👉👉 Download now 👈👈</a>"', content)

# Write back to file
with open('c:/Users/jagad/Downloads/hesmukh-get/plugins/pmfilter.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ All emoji issues have been fixed successfully!")
print("Now the bot should show: 👉👉 Download now 👈👈")

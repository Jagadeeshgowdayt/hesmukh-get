#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read the file
with open('c:/Users/jagad/Downloads/hesmukh-get/plugins/pmfilter.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the problematic line
# Look for the specific pattern around line 1997
old_line = 'f"<a href=\\"{deep_link}\\">👉👉 Download now 👈👈</a>"'
new_line = 'f\'<a href="{deep_link}">👉👉 Download now 👈👈</a>\''

# Replace with the correct version
content = content.replace(old_line, new_line)

# Also try replacing any variation with corrupted emoji
import re
pattern = r'f"<a href=\\".*?\\">👉👉 Download now 👈👈</a>"'
replacement = 'f\'<a href="{deep_link}">👉👉 Download now 👈👈</a>\''
content = re.sub(pattern, replacement, content)

# Write back
with open('c:/Users/jagad/Downloads/hesmukh-get/plugins/pmfilter.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed the emoji and HTML formatting!")

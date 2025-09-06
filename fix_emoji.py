import re

# Read the file
with open('c:/Users/jagad/Downloads/hesmukh-get/plugins/pmfilter.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the problematic line
# Look for the pattern and replace with correct emoji
pattern = r'(f"<a href=\\"{deep_link}\\">👉👉 Download now )[^<]+(</a>")'
replacement = r'\g<1>👈👈\g<2>'

content = re.sub(pattern, replacement, content)

# Write back
with open('c:/Users/jagad/Downloads/hesmukh-get/plugins/pmfilter.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Emoji replacement completed!")

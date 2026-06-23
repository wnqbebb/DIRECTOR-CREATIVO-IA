import re

with open('biblioteca-de-prompts.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find every occurrence of class="copy-btn" or class='copy-btn'
# and extract about 500 characters around it to see the structure.
pos = 0
count = 0
for m in re.finditer(r'class=["\']copy-btn', content):
    count += 1
    start = max(0, m.start() - 250)
    end = min(len(content), m.end() + 250)
    print(f"=== OCCURRENCE {count} ===")
    print(content[start:end])
    print("=" * 30)

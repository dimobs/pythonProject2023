# +359 2 222 2222
# +359-2-2
import re
line = input.split(', ')
pattern = r'[\+359]{4}[\s-]{1}[2]{1}[\s-]{1}[\d]{3}[ -]{1}[\d]{4}\b'

print(re.find(pattern, line))

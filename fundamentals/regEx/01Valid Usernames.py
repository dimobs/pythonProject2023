import re


line = input().split(', ')

pattern = r"\([A-Za-z_-]{3,16}\S)"


for str in line:
    result = re.match(pattern, str);
    print(result)
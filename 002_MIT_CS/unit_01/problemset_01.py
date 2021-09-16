s = 'azcbobobegghakl'

char_count = 0
s = s.lower()

for char in s:
    if char in 'aeiou':
        char_count += 1

print("Number of vowels: " + str(char_count))

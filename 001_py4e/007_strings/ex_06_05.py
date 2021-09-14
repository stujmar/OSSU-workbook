# String Exercise 6-5
print("Exercise 6-5")

str = 'X-DSPAM-Confidence: 0.8475 '

position = str.find(':')
str = str[str.find(':')+1:].strip()

print(float(str))
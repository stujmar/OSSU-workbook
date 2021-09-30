# non numeric recursion.
# able was I ere I saw elba
# are we not drawn onward we few drawn onward to new era

def is_palindrome(string_param):
    def toChars(string):
        string = string.lower()
        ans = ''
        for char in string:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                ans += char 
        return ans
    def is_pal(string):
        if len(string) <= 1:
            return True
        else:
            return string[0] == string[-1] and is_pal(string[1:-1])
    return is_pal(toChars(string_param))

print(is_palindrome('otto'))
print(is_palindrome('motto'))
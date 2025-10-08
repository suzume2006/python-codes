def palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(palindrome("Racecar"))
print(palindrome("Python"))

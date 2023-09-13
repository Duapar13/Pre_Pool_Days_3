palindrome = "racecarbananaappleleveldeifiedcivicnoonradarrotorreferkayakmadamtenetwowbobpoppeepredderrepaperrotatorlevelerreviverredividerdetartratedmalayalam"

palindromes = []
length = len(palindrome)

for i in range(length):
    for j in range(i + 2, length + 1):
        word = palindrome[i:j]
        if word == word[::-1]:
            palindromes.append(word)
palindromes.sort()
sorted_palindromes = " ".join(palindromes)
print(sorted_palindromes)

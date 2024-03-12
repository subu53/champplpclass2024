 #program that uses list comprehension to find words with odd characters
words = ["hello", "world", "this", "is", "a", "list", "of", "words"]
len_words = [word for word in words if len(word) %2 != 0]

print("List with words of odd length:", len_words)
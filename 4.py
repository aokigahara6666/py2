text = input("Введите строку: ").lower()
words = text.split()
unique_words = set(words)

for word in unique_words:
    print(f"{word}: {words.count(word)}")
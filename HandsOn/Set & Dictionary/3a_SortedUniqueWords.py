text=input("Enter the sentence:")
words=text.split()
words=[word.lower() for word in words]
unique_words=set(words)
unique_list=sorted(unique_words)
print(unique_list)
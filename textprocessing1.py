import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
text="Hello, How are you?"
words=word_tokenize(text)
print(words)
sentence=sent_tokenize(text)
print(sentence)
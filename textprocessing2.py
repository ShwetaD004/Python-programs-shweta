import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
nltk.download('stopwords')
#stopwords.words("english")

text="This is a simple sentence,showing off the stop words filtration."
words=word_tokenize(text)
filtered_words=[]
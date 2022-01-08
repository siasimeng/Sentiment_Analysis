import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize, RegexpTokenizer # tokenize words
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import re

class preprocess:
    def sentiment_preprocess(text):
        stopWords = set(stopwords.words('english'))
    # remove single quote and dashes
    #   text = text.replace("'", "").replace("-", "").lower()

    #   # split on words only
    #   tk = nltk.tokenize.RegexpTokenizer(r'\w+')
    #   tokens = tk.tokenize(text)
        alphaPattern = '[^a-zA-Z]'
        text = re.sub(alphaPattern, " ", text) # Replace all non alphabets.
        text = nltk.word_tokenize(text) # tokenize
    #     text = [word for word in text if word.isalnum()] # check characters are alphanumeric
        text = [lemmatizer.lemmatize(word.lower()) for word in text] # lemmas - convert a word to its base form and each text 
                                                             # is converted to lowercase
    
    # remove stop words
        list_word = []
        #words = [w for w in text if not w in stopWords]
        for w in text:
            if not w in stopWords:
                if len(w) > 1: # the word such as "u" will be eliminate
                    words = w
                    list_word.append(words)
            
        return list_word


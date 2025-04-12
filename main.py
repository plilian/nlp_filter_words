import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Just one time download - then read from the file
nltk.download('punkt')
nltk.download('stopwords')

# Instantiate the stopwords set
stop_words = set(stopwords.words('english'))

# file path / table / variable
file_path = 'your/output/file/path.csv'
data = pd.read_csv(file_path)

# function to check the word numbers
def is_number(word):
    number_words = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"}
    return word.lower() in number_words

# function to extract keywords and keep 5 of them
common_words = {"hi", "hello", "hey", "answer", "question", "think", "well", "yes", "no", "maybe", "please", "thanks",
                "thank", "you", "goodbye", "questions", "guys", "friends", "friend", "talk", "tell"}

def extract_keywords(question):
    common_words_lower = set(word.lower() for word in common_words)

    word_tokens = word_tokenize(question.lower())
    filtered_words = [word for word in word_tokens if
                      word not in common_words_lower and word.isalpha() and word not in stop_words and not is_number(word)]
    # Return a list of length 5 with empty strings if there are fewer than 5 keywords
    return filtered_words[:4] + [''] * (4 - len(filtered_words))


keyword_columns = ['context2', 'context3', 'context4', 'context5']

for i, col in enumerate(keyword_columns):
    data[col] = data['question'].apply(lambda x: extract_keywords(x)[i] if len(extract_keywords(x)) > i else '')

file_path2 = 'your/output/file/path.csv'

# write back to the main datasource - table
data.to_csv(file_path2, index=False)

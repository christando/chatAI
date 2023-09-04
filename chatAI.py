import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Baca data dari file CSV
try:
    data = pd.read_csv('data.csv')
except FileNotFoundError:
    print("File CSV tidak ditemukan. Pastikan nama file dan path-nya sudah benar.")
    exit()
except Exception as e:
    print("Terjadi kesalahan saat membaca file CSV:", str(e))
    exit()
    
# Preprocessing teks
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]
    return ' '.join(tokens)

data['processed_question'] = data['question'].apply(preprocess_text)

# Buat vektor TF-IDF dari pertanyaan yang telah diproses
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(data['processed_question'])

# Fungsi untuk mendapatkan jawaban terbaik berdasarkan cosine similarity
def get_best_answer(user_input):
    user_input = preprocess_text(user_input)
    user_tfidf = tfidf_vectorizer.transform([user_input])
    
    similarities = cosine_similarity(user_tfidf, tfidf_matrix)[0]
    best_index = similarities.argmax()
    best_answer = data['answer'][best_index]
    
    return best_answer

# Interaksi dengan user
print("Chatbot: Halo! Silakan bertanya atau ketik 'exit' untuk mengakhiri.")
while True:
    user_input = input("Anda: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Sampai jumpa!")
        break
    else:
        response = get_best_answer(user_input)
        print("Chatbot:", response)

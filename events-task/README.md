# Krakowski Asystent Kultury 🎭
## Building Blocks dla Hackathonu AI Krak Hack

### 🎯 Cel Wyzwania

Stwórz inteligentny system kulturalny wykorzystujący:
- System rekomendacji dopasowany do użytkownika
- Zaawansowaną personalizację i profiling
- Inteligentne powiadomienia i engagement
- Nowoczesny interfejs użytkownika

### 📁 Co Dostajesz

```
events-task/
├── code/
│   ├── data_loader.py         # Funkcje do ładowania/filtrowania danych  
│   ├── main.py               # Demo i eksploracja możliwości
│   ├── config.ini            # Konfiguracja
│   └── requirements.txt      # Podstawowe zależności
├── events-data/              # 558+ wydarzeń kulturalnych z Krakowa
└── README.md
```

### 🚀 Szybki Start

```bash
cd events-task/code
pip install -r requirements.txt
python main.py
```

### 📊 Dane do Wykorzystania

**558+ rzeczywistych wydarzeń** kulturalnych z Krakowa:
- Spektakle teatralne, koncerty, wystawy, festiwale
- Daty, lokalizacje, szczegółowe opisy, kategorie
- Format CSV/JSON/SQLite - łatwy do rozszerzenia

### 🛠️ Dostępne Building Blocks

```python
# Podstawowe funkcje do rozbudowy
from data_loader import load_events_data, filter_events_by_category, simple_text_search

events_df = load_events_data()                    # Załaduj wszystkie dane
music_events = filter_events_by_category(df, cat) # Filtruj po kategorii  
results = simple_text_search(df, "teatr")         # Proste wyszukiwanie
```

### 💡 Kierunki Projektów

#### 🧠 System Rekomendacji
- **Profil użytkownika**: preferencje, historia, demografia
- **Content-based filtering**: embeddingi opisów wydarzeń
- **Collaborative filtering**: podobni użytkownicy, podobne gusty
- **Hybrydowe podejścia**: łączenie różnych metod
- **Ciągłe uczenie**: adaptacja na podstawie feedbacku

#### 🎯 Personalizacja i Dopasowanie  
- **Kontekstowe rekomendacje**: pora dnia, pogoda, sezon
- **Analiza nastrojów**: social media, previous ratings
- **Grupowe sugestie**: wydarzenia dla par/grup znajomych
- **Lokalizacja**: dystans, transport publiczny, parkingi
- **Budżet i preferencje**: cenowe filtry, accessibility

#### 📱 Interfejsy i UX
- **Web app**: interaktywna mapa, filtry, kalendarz
- **Mobile app**: geolokalizacja, push notifications
- **Chatboty**: Telegram, Discord, WhatsApp
- **Voice assistants**: Alexa, Google Assistant
- **AR experiences**: wydarzenia w pobliżu przez kamerę

#### 🔔 Engagement i Powiadomienia
- **Smart notifications**: optymalne czasowanie
- **Personalized digest**: cotygodniowe podsumowania
- **Event reminders**: przypomnienia przed wydarzeniem
- **Social features**: znajomi, wspólne wydarzenia
- **Gamification**: punkty, odznaki, wyzwania

#### ⭐ Ocenianie i Feedback
- **Rating system**: oceny wydarzeń po uczestnictwie
- **Review analysis**: sentiment analysis komentarzy
- **Popularity prediction**: przewidywanie trendów
- **Quality scoring**: algorytmy oceny jakości
- **Recommendation loops**: uczenie z ocen użytkowników

### 🔧 Implementacja - Przykłady

#### System Rekomendacji z Embeddingami
```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Model dla polskich tekstów
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# 2. Embeddingi wydarzeń
event_descriptions = events_df['description'].tolist()
event_embeddings = model.encode(event_descriptions)

# 3. Profil użytkownika jako embedding
user_preferences = "Lubię muzykę klasyczną i teatr alternatywny"
user_embedding = model.encode([user_preferences])

# 4. Znajdź najbardziej pasujące wydarzenia
similarities = cosine_similarity(user_embedding, event_embeddings)
top_events = similarities[0].argsort()[-10:][::-1]
```

#### Web App z Flask
```python
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    user_profile = request.json['profile']
    # Twój algorytm rekomendacji tutaj
    recommendations = recommend_events(user_profile)
    return jsonify(recommendations)

@app.route('/api/rate', methods=['POST'])  
def rate_event():
    # System ocen wydarzeń
    rating_data = request.json
    update_user_profile(rating_data)
    return jsonify({'status': 'success'})
```

#### Chatbot Framework
```python
# Telegram bot example
import telebot
from telebot import types

bot = telebot.TeleBot("YOUR_BOT_TOKEN")

@bot.message_handler(commands=['recommend'])
def recommend_handler(message):
    user_id = message.from_user.id
    user_profile = get_user_profile(user_id)
    recommendations = get_recommendations(user_profile)
    
    for event in recommendations:
        bot.send_message(message.chat.id, format_event(event))
```

### 📈 Zaawansowane Kierunki

#### ML i AI
- **Deep Learning**: neural collaborative filtering
- **NLP**: analiza opisów, sentiment analysis, intent recognition  
- **Computer Vision**: analiza zdjęć wydarzeń, face recognition
- **Time Series**: przewidywanie popularności, seasonal trends
- **Reinforcement Learning**: optymalizacja timing'u powiadomień

#### Big Data i Real-time
- **Streaming data**: real-time social media analysis
- **Event sourcing**: tracking wszystkich interakcji użytkowników
- **A/B testing**: optymalizacja algorytmów rekomendacji
- **Analytics dashboard**: metryki biznesowe, user behavior
- **Scalability**: Redis, microservices, cloud deployment

### 🏆 Kluczowe Zagadnienia z Wyzwania

1. **Analiza profilu użytkownika** - jak modelować preferencje?
2. **Reprezentacja wydarzeń** - embeddingi vs. features vs. graph
3. **Podobieństwo i ranking** - metryki, scoring, diversity
4. **Feedback loops** - jak uczyć się z interakcji użytkowników?
5. **Cold start problem** - nowi użytkownicy, nowe wydarzenia
6. **Explainable AI** - dlaczego polecamy konkretne wydarzenie?

### 🔗 Przydatne Biblioteki

```bash
# ML i embeddingi
pip install sentence-transformers scikit-learn faiss-cpu

# NLP polskie modele  
pip install spacy
python -m spacy download pl_core_news_sm

# Web development
pip install flask fastapi streamlit

# Chatboty
pip install python-telegram-bot discord.py

# Data processing
pip install requests beautifulsoup4 pandas numpy
```

---

**🚀 Powodzenia w budowaniu systemu przyszłości!**

*Wykorzystaj te building blocks do stworzenia czegoś niesamowitego!* 
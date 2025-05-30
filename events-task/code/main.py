#!/usr/bin/env python3
"""
Krakowski Asystent Kultury - Starter Demo

Podstawowe funkcje do ładowania i filtrowania danych o wydarzeniach kulturalnych.
Uczestnicy mogą używać tych funkcji jako building blocks do stworzenia
zaawansowanego systemu rekomendacji i interfejsu użytkownika.

Uruchom: python main.py
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from data_loader import (
    load_events_data, 
    filter_events_by_category,
    simple_text_search,
    get_unique_categories,
    get_unique_locations
)

def demo_basic_functions():
    """Demo podstawowych funkcji do manipulacji danych."""
    print("=== DEMO: Podstawowe funkcje do rozszerzenia ===")
    
    # Załaduj dane
    events_df = load_events_data()
    
    if events_df.empty:
        print("❌ Brak danych. Sprawdź konfigurację.")
        return
    
    print(f"✅ Załadowano {len(events_df)} wydarzeń")
    print(f"📂 Kategorie: {len(get_unique_categories(events_df))}")
    print(f"📍 Lokalizacje: {len(get_unique_locations(events_df))}")
    
    # Przykłady filtrowania
    music_events = filter_events_by_category(events_df, "Muzyka klasyczna")
    print(f"🎵 Wydarzenia muzyczne: {len(music_events)}")
    
    theater_results = simple_text_search(events_df, "teatr")
    print(f"🎭 Wyniki dla 'teatr': {len(theater_results)}")
    
    # Pokaż próbkę danych
    if len(events_df) > 0:
        print(f"\n📄 Przykład wydarzenia:")
        event = events_df.iloc[0]
        print(f"   Tytuł: {event['title']}")
        print(f"   Kategoria: {event['category']}")
        print(f"   Lokalizacja: {event['location']}")
        print(f"   Data: {event['date']}")

def show_project_ideas():
    """Pokazuje konkretne pomysły na projekty finałowe."""
    print("\n=== 🚀 POMYSŁY NA PROJEKTY FINAŁOWE ===")
    print("""
💡 SYSTEM REKOMENDACJI:
- Profil użytkownika z preferencjami (gatunki, lokalizacje, budżet)
- Content-based filtering z embeddingami tekstów
- Collaborative filtering na podstawie ocen innych użytkowników
- Hybrydowy system łączący różne podejścia
- Ciągłe uczenie się z feedbacku użytkownika

🎯 PERSONALIZACJA I DOPASOWANIE:
- Algorytm analizujący historię uczestnictwa
- Dopasowanie na podstawie pory dnia/tygodnia
- Uwzględnienie pogody i sezonu
- Analiza nastrojów z social media
- Grupowe rekomendacje dla znajomych

📱 INTERFEJSY UŻYTKOWNIKA:
- Aplikacja webowa z mapą wydarzeń
- Chatbot (Telegram/Discord/WhatsApp)
- Aplikacja mobilna z geolokalizacją
- Voice assistant (Alexa/Google)
- AR app pokazująca wydarzenia w pobliżu

🔔 POWIADOMIENIA I ENGAGEMENT:
- Smart notifications w optymalnym czasie
- Przypomnienia o zbliżających się wydarzeniach
- Powiadomienia o nowych wydarzeniach w ulubionych kategoriach
- Weekly digest z personalizowanymi sugestiami
- Social sharing i znajomi o podobnych gustach

⭐ OCENIANIE I FEEDBACK:
- System ocen i recenzji wydarzeń
- Sentiment analysis komentarzy
- Predykcja popularności wydarzeń
- Ranking wydarzeń na podstawie opinii
- Machine learning z historii ocen użytkowników

🌐 INTEGRACJE I DANE:
- Web scraping nowych źródeł wydarzeń
- Integracja z Facebook Events, Eventbrite
- API do social media platforms
- Real-time updates i synchronizacja
- Export do kalendarzy (Google, Outlook)

🧠 ZAAWANSOWANE AI:
- NLP do analizy opisów wydarzeń
- Computer vision do analizy zdjęć
- Embeddingi do semantic search
- LLM do generowania opisów i odpowiedzi
- Analiza trendów i przewidywanie przyszłych wydarzeń
    """)

def show_technical_directions():
    """Pokazuje kierunki techniczne do eksploracji."""
    print("\n=== 🔧 KIERUNKI TECHNICZNE ===")
    print("""
📊 MACHINE LEARNING:
- sentence-transformers dla embeddingów polskich tekstów
- scikit-learn dla klasycznych algorytmów ML
- TensorFlow/PyTorch dla deep learning
- FAISS lub Pinecone dla wektorowych baz danych

🤖 NATURAL LANGUAGE PROCESSING:
- spaCy z modelem polskim (pl_core_news_sm)
- Hugging Face transformers (herbert, allegro)
- OpenAI API dla generatywnego AI
- Rasa dla chatbotów z NLU

🌐 WEB DEVELOPMENT:
- Flask/FastAPI dla backend API
- React/Vue.js dla frontend
- Streamlit dla szybkich prototypów
- PostgreSQL/MongoDB dla bazy danych

📱 MOBILE & DESKTOP:
- React Native / Flutter dla mobile
- Electron dla desktop apps
- Progressive Web Apps (PWA)
- Telegram Bot API dla chatbotów

☁️ CLOUD & DEPLOYMENT:
- Docker dla konteneryzacji
- AWS/GCP/Azure dla hostingu
- GitHub Actions dla CI/CD
- Redis dla cache'owania
    """)

def explore_data():
    """Pozwala uczestnikowi eksplorować dane interaktywnie."""
    print("\n=== 🔍 EKSPLORACJA DANYCH ===")
    
    events_df = load_events_data()
    if events_df.empty:
        print("❌ Brak danych.")
        return
    
    categories = get_unique_categories(events_df)
    locations = get_unique_locations(events_df)
    
    print(f"📋 Dostępne kategorie ({len(categories)}):")
    for i, cat in enumerate(categories[:10], 1):
        count = len(filter_events_by_category(events_df, cat))
        print(f"  {i}. {cat} ({count} wydarzeń)")
    
    if len(categories) > 10:
        print(f"  ... i {len(categories) - 10} więcej")
    
    print(f"\n📍 Najpopularniejsze lokalizacje:")
    location_counts = {}
    for loc in locations:
        location_counts[loc] = len(events_df[events_df['location'].str.contains(loc, case=False, na=False)])
    
    sorted_locations = sorted(location_counts.items(), key=lambda x: x[1], reverse=True)
    for i, (loc, count) in enumerate(sorted_locations[:10], 1):
        print(f"  {i}. {loc[:50]}... ({count} wydarzeń)")

def main():
    """Główna funkcja demo."""
    print("🎭 KRAKOWSKI ASYSTENT KULTURY - BUILDING BLOCKS")
    print("=" * 55)
    print("Podstawowe narzędzia do budowy systemu rekomendacji")
    print("=" * 55)
    
    while True:
        print("\n📋 WYBIERZ:")
        print("1. Demo podstawowych funkcji")
        print("2. Eksploruj dane")
        print("3. Pomysły na projekty finałowe")
        print("4. Kierunki techniczne")
        print("5. Wyjście")
        
        choice = input("\nWybór (1-5): ").strip()
        
        if choice == "1":
            demo_basic_functions()
        elif choice == "2":
            explore_data()
        elif choice == "3":
            show_project_ideas()
        elif choice == "4":
            show_technical_directions()
        elif choice == "5":
            print("\n🚀 Powodzenia w tworzeniu systemu!")
            break
        else:
            print("❌ Nieprawidłowy wybór.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Do widzenia!")
    except Exception as e:
        print(f"❌ Błąd: {e}") 
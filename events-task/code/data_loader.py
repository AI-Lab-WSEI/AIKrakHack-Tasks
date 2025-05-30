import configparser
import logging
import json
import sqlite3
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime, date
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config() -> configparser.ConfigParser:
    """Loads configuration from config.ini file."""
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config

def load_events_data() -> pd.DataFrame:
    """
    Basic function to load events data from CSV file.
    
    Returns:
        pd.DataFrame: Raw events data
        
    TODO for participants:
    - Add data validation
    - Handle different file formats (JSON, SQLite)
    - Add error handling
    """
    config = load_config()
    csv_path = Path(config['DATA']['CSV_PATH'])
    
    try:
        df = pd.read_csv(csv_path)
        logger.info(f"Loaded {len(df)} events from {csv_path}")
        return df
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        return pd.DataFrame()

def basic_text_preprocessing(text: str) -> str:
    """
    Very basic text preprocessing.
    
    TODO for participants:
    - Add advanced text cleaning
    - Implement lemmatization
    - Remove stop words
    - Handle Polish language specifics
    """
    if pd.isna(text):
        return ""
    return str(text).lower().strip()

def filter_events_by_category(events_df: pd.DataFrame, category: str) -> pd.DataFrame:
    """Simple category filtering function."""
    if events_df.empty:
        return pd.DataFrame()
    return events_df[events_df['category'] == category].copy()

def filter_events_by_date_range(events_df: pd.DataFrame, start_date: str, end_date: str) -> pd.DataFrame:
    """Simple date range filtering function."""
    if events_df.empty:
        return pd.DataFrame()
    
    events_df['date'] = pd.to_datetime(events_df['date'], errors='coerce')
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)
    
    mask = (events_df['date'] >= start) & (events_df['date'] <= end)
    return events_df[mask].copy()

def simple_text_search(events_df: pd.DataFrame, query: str) -> pd.DataFrame:
    """
    Basic text search in title and description.
    
    TODO for participants:
    - Replace with embedding-based semantic search
    - Add TF-IDF scoring
    - Implement fuzzy matching
    - Use external search engines (Elasticsearch, etc.)
    """
    if events_df.empty:
        return pd.DataFrame()
    
    query_lower = query.lower()
    mask = (
        events_df['title'].fillna('').str.lower().str.contains(query_lower, regex=False) |
        events_df['description'].fillna('').str.lower().str.contains(query_lower, regex=False)
    )
    
    return events_df[mask].copy()

def get_unique_categories(events_df: pd.DataFrame) -> List[str]:
    """Get list of unique event categories."""
    if events_df.empty:
        return []
    return sorted(events_df['category'].dropna().unique().tolist())

def get_unique_locations(events_df: pd.DataFrame) -> List[str]:
    """Get list of unique event locations.""" 
    if events_df.empty:
        return []
    return sorted(events_df['location'].dropna().unique().tolist())

# TODO for participants: Add functions for:
# - generate_text_embeddings(texts: List[str]) -> np.ndarray
# - calculate_similarity(embedding1, embedding2) -> float
# - load_user_profile(user_id: str) -> Dict
# - save_user_profile(user_id: str, profile: Dict) -> None
# - connect_to_external_api(api_name: str) -> Any
# - scrape_additional_events(source_url: str) -> pd.DataFrame

if __name__ == "__main__":
    # Basic demo
    events_df = load_events_data()
    
    if not events_df.empty:
        print(f"Loaded {len(events_df)} events")
        print(f"Categories: {len(get_unique_categories(events_df))}")
        print(f"Locations: {len(get_unique_locations(events_df))}")
        
        # Example usage
        music_events = filter_events_by_category(events_df, "Muzyka klasyczna")
        print(f"Music events: {len(music_events)}")
        
        search_results = simple_text_search(events_df, "teatr")
        print(f"Theater search results: {len(search_results)}") 
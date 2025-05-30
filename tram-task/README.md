# Optymalizacja Infrastruktury Miejskiej 🚋
## Building Blocks dla Hackathonu AI Krak Hack

### 🎯 Cel Wyzwania

Stwórz system optymalizacji transportu publicznego w Krakowie wykorzystujący:
- Rzeczywiste dane MPK Kraków (przystanki, linie, rozkłady)
- Dane geograficzne OpenStreetMap (budynki, ulice)
- Algorytmy optymalizacji tras i logistyki
- AI do przewidywania popytu i ruchu

### 📁 Struktura Projektu

```
tram-task/
├── code/
│   ├── sourcing_data.py          # Główne klasy do pobierania danych
│   ├── mpk_lines_modeling.ipynb  # Notebook z przykładami analizy
│   ├── config.ini               # Konfiguracja API MPK
│   └── requirements.txt         # Zależności Python
├── Tram Optimisation Wyzwanie.pdf     # Opis wyzwania
├── Tram Optimisation PrepSet.pdf      # Materiały przygotowawcze
└── README.md                           # Ten plik
```

### 🚀 Szybki Start

```bash
cd tram-task/code
pip install -r requirements.txt
python -c "from sourcing_data import TramData; data = TramData()"
```

### 📊 Dostępne Dane

#### 1. **Dane MPK Kraków (Real-time)**
- **Przystanki**: lokalizacja, kategoria, liczba linii
- **Linie tramwajowe**: trasy, przystanki, współrzędne
- **Rozkłady**: czasy odjazdów, częstotliwość kursów
- **API**: aktualne informacje o kursach

#### 2. **Dane OpenStreetMap**
- **Budynki**: geometrie, centroidy, lokalizacje
- **Ulice**: sieć dróg, segmenty, topologia
- **Geografia**: kompletna mapa Krakowa

### 🛠️ Główne Komponenty

#### TramData - Główna Klasa
```python
from sourcing_data import TramData

# Inicjalizacja pobiera wszystkie dane
tram_data = TramData()

# DataFrame z przystankami
stops_df = tram_data.stops_df
print(f"Przystanki: {len(stops_df)}")
print(stops_df.columns)
# Index: nazwa_przystanku
# Kolumny: category, latitude, longitude, number_of_lines, 
#          lines, min/max/avg_time_between_trams

# DataFrame z liniami
lines_df = tram_data.lines_df  
print(f"Linie: {len(lines_df)}")
print(lines_df.columns)
# Index: numer_linii
# Kolumny: stops (lista przystanków), coordinates (trasa)
```

#### MpkSourcing - API MPK
```python
from sourcing_data import MpkSourcing

mpk = MpkSourcing()
mpk.fetch_and_process()

# Dostęp do surowych danych
stops_data = mpk.stops_data          # Lista przystanków
passages_data = mpk.passages_data    # Rozkłady na przystankach
lines_to_stops = mpk.lines_to_stops  # Mapowanie linia -> przystanki
coordinates = mpk.lines_stops_coordinates  # Współrzędne tras
```

#### OpenStreetMapData - Dane Geograficzne
```python
from sourcing_data import OpenStreetMapData

osm_data = OpenStreetMapData(place="Kraków, Poland")

# GeoDataFrame z budynkami
buildings = osm_data.buildings_df
print(f"Budynki: {len(buildings)}")
print(buildings.columns)
# Kolumny: geometry, lat, lng (centroidy budynków)

# GeoDataFrame z ulicami  
streets = osm_data.streets_df
print(f"Segmenty ulic: {len(streets)}")
# Geometrie ulic i dróg
```

### 💡 Kierunki Projektów

#### 🚌 Optymalizacja Tras i Rozkładów
- **Analiza popytu**: gdzie ludzie jeżdżą, kiedy, jak często
- **Optymalizacja częstotliwości**: algorytmy dostosowania rozkładów
- **Nowe linie**: proponowanie tras na podstawie analizy ruchu
- **Transfer optimization**: optymalne przesiadki między liniami
- **Przewidywanie opóźnień**: ML modele czasów przejazdu

#### 🏙️ Analiza Przestrzenna
- **Dostępność transportu**: analiza pokrycia obszarów miasta
- **Planowanie przystanków**: optymalne lokalizacje nowych przystanków
- **Analiza gęstości**: korelacja budynków z użytkowaniem transportu
- **Heatmapy popytu**: wizualizacja popularności tras
- **Accessibility analysis**: dostęp dla osób niepełnosprawnych

#### 📈 Przewidywanie i Demand Forecasting
- **Time series analysis**: przewidywanie popytu na transport
- **Weather impact**: wpływ pogody na wykorzystanie tramwajów
- **Event analysis**: jak wydarzenia miejskie wpływają na ruch
- **Seasonal patterns**: wzorce sezonowe w transporcie
- **Real-time demand**: dynamiczne dostosowanie do aktualnego popytu

#### 🤖 AI i Machine Learning
- **Route recommendation**: AI dla pasażerów - najlepsze trasy
- **Predictive maintenance**: przewidywanie awarii infrastruktury
- **Dynamic pricing**: optymalizacja cen biletów
- **Crowd management**: zarządzanie tłumami w godzinach szczytu
- **Anomaly detection**: wykrywanie nietypowych sytuacji

### 🔧 Przykłady Implementacji

#### Analiza Najpopularniejszych Przystanków
```python
from sourcing_data import TramData
import pandas as pd

tram_data = TramData()

# Sortuj przystanki według liczby linii
popular_stops = tram_data.stops_df.sort_values('number_of_lines', ascending=False)
print("Najbardziej uczęszczane przystanki:")
print(popular_stops[['number_of_lines', 'lines']].head(10))

# Analiza częstotliwości kursów
frequent_stops = tram_data.stops_df.sort_values('avg_time_between_trams')
print("\nPrzystanki z najczęstszymi kursami:")
print(frequent_stops[['avg_time_between_trams', 'number_of_lines']].head(10))
```

#### Wizualizacja Sieci Tramwajowej
```python
import folium
import pandas as pd

# Stwórz mapę Krakowa
map_krakow = folium.Map(location=[50.0647, 19.9450], zoom_start=12)

# Dodaj przystanki
for stop_name, stop_data in tram_data.stops_df.iterrows():
    folium.CircleMarker(
        location=[stop_data['latitude'], stop_data['longitude']],
        radius=stop_data['number_of_lines'] * 2,
        popup=f"{stop_name}: {stop_data['number_of_lines']} linii",
        color='blue'
    ).add_to(map_krakow)

# Dodaj trasy linii
for line_num, line_data in tram_data.lines_df.iterrows():
    coordinates = line_data['coordinates']
    folium.PolyLine(
        locations=coordinates,
        color='red',
        weight=3,
        popup=f"Linia {line_num}"
    ).add_to(map_krakow)

map_krakow.save('krakow_tram_network.html')
```

#### Optymalizacja Tras z NetworkX
```python
import networkx as nx
from geopy.distance import distance

# Stwórz graf sieci tramwajowej
G = nx.Graph()

# Dodaj przystanki jako węzły
for stop_name, stop_data in tram_data.stops_df.iterrows():
    G.add_node(stop_name, 
               pos=(stop_data['latitude'], stop_data['longitude']),
               lines=stop_data['lines'])

# Dodaj połączenia między przystankami na tej samej linii
for line_num, line_data in tram_data.lines_df.iterrows():
    stops = line_data['stops']
    for i in range(len(stops) - 1):
        stop1, stop2 = stops[i], stops[i+1]
        if stop1 in G.nodes and stop2 in G.nodes:
            # Oblicz dystans jako wagę krawędzi
            pos1 = G.nodes[stop1]['pos']
            pos2 = G.nodes[stop2]['pos']
            dist = distance(pos1, pos2).kilometers
            G.add_edge(stop1, stop2, weight=dist, line=line_num)

# Znajdź najkrótszą trasę
start_stop = "Główny Dworzec"
end_stop = "Nowy Kleparz"
try:
    shortest_path = nx.shortest_path(G, start_stop, end_stop, weight='weight')
    print(f"Najkrótsza trasa z {start_stop} do {end_stop}:")
    print(" -> ".join(shortest_path))
except nx.NetworkXNoPath:
    print("Brak bezpośredniego połączenia")
```

#### Analiza Gęstości Zabudowy vs Transport
```python
from sourcing_data import TramData, OpenStreetMapData
import geopandas as gpd
from shapely.geometry import Point

tram_data = TramData()
osm_data = OpenStreetMapData()

# Stwórz bufor wokół przystanków (500m)
stops_gdf = gpd.GeoDataFrame(
    tram_data.stops_df,
    geometry=[Point(lon, lat) for lat, lon in 
              zip(tram_data.stops_df['latitude'], tram_data.stops_df['longitude'])]
)
stops_gdf = stops_gdf.set_crs('EPSG:4326').to_crs('EPSG:2180')  # Polska projekcja
stops_buffers = stops_gdf.geometry.buffer(500)  # 500m bufor

# Policz budynki w każdym buforze
buildings_gdf = osm_data.buildings_df.set_crs('EPSG:4326').to_crs('EPSG:2180')

for idx, buffer in enumerate(stops_buffers):
    buildings_in_buffer = buildings_gdf[buildings_gdf.geometry.within(buffer)]
    stop_name = stops_gdf.index[idx]
    print(f"{stop_name}: {len(buildings_in_buffer)} budynków w promieniu 500m")
```

### 📈 Zaawansowane Kierunki

#### Optimization Algorithms
- **Genetic algorithms**: optymalizacja rozkładów jazdy
- **Simulated annealing**: problem komiwojażera dla tras
- **Linear programming**: optymalizacja alokacji zasobów
- **Multi-objective optimization**: balans między kosztami a jakością
- **Reinforcement learning**: adaptacyjne zarządzanie ruchem

#### Big Data i Real-time
- **Stream processing**: analiza danych w czasie rzeczywistym
- **IoT integration**: sensory ruchu, liczniki pasażerów
- **Mobile data**: anonimowe dane lokalizacyjne z telefonów
- **Social media**: analiza wydarzeń wpływających na transport
- **Weather API**: integracja z prognozami pogody

#### Advanced Analytics
- **Clustering analysis**: segmentacja pasażerów i tras
- **Graph algorithms**: centrality, community detection
- **Time series forecasting**: ARIMA, LSTM dla popytu
- **Spatial statistics**: autokorelacja przestrzenna
- **Network flow optimization**: maksymalizacja przepustowości

### 🔗 Przydatne Biblioteki

```bash
# Już zainstalowane
pip install geopandas geopy networkx osmnx folium matplotlib

# Dodatkowe dla zaawansowanych analiz
pip install scikit-learn tensorflow keras
pip install plotly dash streamlit        # Wizualizacje
pip install pulp cvxpy                   # Optymalizacja
pip install prophet fbprophet           # Forecasting
pip install clustergram hdbscan         # Clustering
```

### 🏆 Kluczowe Wyzwania

1. **Multi-modal optimization** - integracja tramwajów z autobusami, metrem
2. **Real-time adaptation** - dynamiczne dostosowanie do zmieniających się warunków
3. **Sustainability** - minimalizacja wpływu na środowisko
4. **Social equity** - sprawiedliwy dostęp do transportu dla wszystkich grup
5. **Scalability** - rozwiązania działające dla całej aglomeracji
6. **Cost-benefit analysis** - ekonomiczna opłacalność optymalizacji

---

**🚀 Powodzenia w optymalizacji transportu przyszłości!**

*Wykorzystaj te narzędzia do stworzenia inteligentnej infrastruktury miejskiej!* 
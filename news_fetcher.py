import feedparser
import requests

# Fuentes globales y en español enfocadas en economía y finanzas
RSS_FEEDS = [
    "https://e00-expansion.uecdn.es/rss/economia.xml",     # Expansión (Economía - ES)
    "https://e00-expansion.uecdn.es/rss/mercados.xml",     # Expansión (Mercados - ES)
    "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/section/economia/portada", # El País (Economía - ES)
    "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000664", # CNBC Finance (Global - EN)
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=^GSPC,^DJI,^IXIC,EURUSD=X,BTC-USD", # Yahoo Finance (Global - EN)
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL,MSFT,NVDA,TSLA", # Yahoo Finance Tech (Global - EN)
    "https://www.investing.com/rss/news_25.rss", # Investing.com (Global - EN)
    "https://www.ft.com/?format=rss", # Financial Times (Global - EN)
    "https://cincodias.elpais.com/rss/cincodias/portada.xml", # Cinco Días (ES)
    "https://www.eleconomista.es/rss/flash", # El Economista (ES)
    "https://cointelegraph.com/rss" # Cointelegraph Crypto (Global)
]

def get_latest_news(limit_per_feed=8):
    """
    Descarga los títulos y resúmenes más recientes desde los RSS configurados.
    """
    all_news = []
    
    for url in RSS_FEEDS:
        try:
            feed = feedparser.parse(url)
            # Solo tomamos las primeras N noticias para no saturar al LLM
            for entry in feed.entries[:limit_per_feed]:
                title = entry.title
                summary = getattr(entry, 'summary', 'Sin resumen.')
                link = getattr(entry, 'link', 'Sin URL explícita.')
                all_news.append(f"- NOTICIA: {title}\n  RESUMEN: {summary}\n  URL: {link}")
        except Exception as e:
            print(f"[!] Error leyendo el portal {url}: {e}")
            
    # Compilamos las noticias en un solo texto a inyectar al prompt
    return "\n\n".join(all_news)

def get_cnn_fear_and_greed():
    """
    Intenta extraer el índice de miedo y codicia duro desde el API de CNN.
    Falla elegantemente entregando '50' (Neutral) en caso de bloqueos.
    """
    try:
        url = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://edition.cnn.com/"
        }
        res = requests.get(url, headers=headers, timeout=5)
        if res.status_code == 200:
            data = res.json()
            score = data.get("fear_and_greed", {}).get("score", 50)
            return int(score)
    except:
        pass
    return 50 # Default Neutral

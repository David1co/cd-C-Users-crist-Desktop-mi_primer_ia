import json
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from news_fetcher import get_latest_news
from analyzer import analyze_news
import os

app = FastAPI()

# Mount the static directory to serve HTML/CSS/JS frontend
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def read_root():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

@app.get("/api/analyze")
def api_analyze():
    # Attempt to fetch news
    news = get_latest_news(limit_per_feed=5)
    if not news or not news.strip():
        news = "No se establecieron feeds o hay problemas de red."
    
    # Get JSON format analysis from Gemini/Mock
    report_json_str = analyze_news(news)
    
    # Clean possible markdown block formatting
    cleaned = report_json_str.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
    cleaned = cleaned.strip()
    
    try:
        data = json.loads(cleaned)
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(
            content={"error": f"Error parsing JSON respones: {str(e)}", "raw": report_json_str}, 
            status_code=500
        )

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)

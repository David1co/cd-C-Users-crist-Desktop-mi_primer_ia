import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from news_fetcher import get_latest_news
from analyzer import analyze_news

def main():
    print("=========================================================")
    print("      🤖 BOT DE ANÁLISIS DE INVERSIONES CON IA        ")
    print("=========================================================\n")
    
    print("[*] Leyendo e interpretando feeds de noticias económicas globales...")
    news = get_latest_news(limit_per_feed=5)
    
    if not news.strip():
        print("[!] No se detectaron noticias legibles. Verifica conexión a internet o los RSS.")
        sys.exit(1)
        
    print(f"[*] ¡Noticias recopiladas exitosamente! Consultando analista virtual...\n")
    
    # El analista hace su magia
    report = analyze_news(news)
    
    print("\n" + "="*57)
    print("  RESULTADO DEL ANÁLISIS DE MERCADO  ".center(57, "="))
    print("="*57 + "\n")
    
    print(report)
    
    print("\n" + "="*57)
    
    # Archivar el reporte generado para el usuario
    report_filename = "proyeccion_diaria.md"
    try:
        with open(report_filename, "w", encoding="utf-8") as file:
            file.write("# REPORTE DIARIO DE CORTA\n\n")
            file.write(report)
        print(f"\n[✔] El reporte final fue guardado localmente en la carpeta de tu proyecto como '{report_filename}'")
    except Exception as e:
        print(f"\n[!] Hubo un error guardando el reporte: {e}")

if __name__ == '__main__':
    main()

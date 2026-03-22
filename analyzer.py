import os
import datetime
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def analyze_news(news_text):
    api_key = os.environ.get("GEMINI_API_KEY")
    
    from news_fetcher import get_cnn_fear_and_greed
    cnn_fg_score = get_cnn_fear_and_greed()
    
    if not api_key:
        print("\n[!] AVISO: No se encontró GEMINI_API_KEY. Ejecutando simulación JSON de nivel EXHAUSTIVO.")
        return get_mock_analysis(cnn_fg_score)
        
    try:
        genai.configure(api_key=api_key)
        
        current_date_str = datetime.datetime.now().strftime("%d de %B de %Y")
        
        prompt = f"""
Actúa como el estratega macroeconómico jefe de un fondo de inversión top del mundo (Bridgewater, BlackRock).
Analiza las noticias globales a continuación y genera un reporte EXHAUSTIVO en formato JSON estricto (no utilices backticks tipo ```json).
TODA LA RESPUESTA DEBE ESTAR EXCLUSIVAMENTE EN ESPAÑOL, sin importar el idioma de origen de las noticias. Incluye citas y enlaces a las fuentes originales en cada sección.

El JSON debe cumplir matemáticamente con la siguiente estructura:
{{
  "fecha": "{current_date_str}",
  "noticias_clave": [
     {{"titulo": "Titular impactante", "resumen": "Resumen ejecutivo", "url_referencia": "URL original de la noticia", "urgencia": "Alta/Media/Baja"}}
  ],
  "resumen_ejecutivo": [
     "Conclusión macro 1 con su respectiva cita y contexto"
  ],
  "bancos_centrales_monetaria": [
      {{"entidad": "Ej: FED o BCE", "decisiones": "El Termómetro: ¿Suben o bajan tasas?", "impacto_mercado": "Lógica de decisión (Ej: Tasas suben -> acciones tech caen).", "url_referencia": "Enlace verificable gubernamental o noticia"}}
  ],
  "geopolitica_seguridad": [
      {{"evento": "Ej: Conflicto o Elecciones", "impacto_mercado": "Ej: Redes logísticas cortadas", "activos_refugio": "Donde huir (Ej: GLD, Bonos cortos)", "url_referencia": "URL"}}
  ],
  "salud_economica_macro": [
      {{"indicador": "Ej: Crecimiento PIB o IPC inflacionario", "estado": "Creciendo / Estresado", "impacto_mercado": "Cómo afecta el consumo y la bolsa", "url_referencia": "URL"}}
  ],
  "guia_reaccion_rapida": [
      {{"noticia_hipotetica": "Ej: Inflación sube más de lo esperado", "contraste_realidad": "Aunque el gobierno diga X, el pánico hará Y", "accion_tomar": "Vender parte de tech, comprar TIPS"}}
  ],
  "calendario_economico": [
      {{"evento": "Ej: Reporte NFP Empleo", "fecha_estimada": "Este Viernes", "impacto_esperado": "Extremo"}}
  ],
  "escenarios_probables": [
      {{"escenario": "Qué puede suceder globalmente", "probabilidad_exito": "Ej: 65%", "efecto": "Efectos en la bolsa", "accion_recomendada": "Comprar X / Vender Y", "url_referencia": "URL relacionada"}}
  ],
  "analisis_divisas": [
      {{"moneda": "Dólar (USD)", "recomendacion": "Comprar/Vender", "probabilidad_exito": "80%", "accion_inmediata": "Acumular sobre X precio", "niveles_clave": "Comprar si baja a X nivel", "justificacion": "Por qué tomar esta acción.", "url_referencia": "URL oficial o noticia"}},
      {{"moneda": "Euro (EUR)", "recomendacion": "Vender", "probabilidad_exito": "90%", "accion_inmediata": "Shortear", "niveles_clave": "Mantener cortos", "justificacion": "Explicación detallada.", "url_referencia": "URL BC"}},
      {{"moneda": "Peso Colombiano (COP) o local de LATAM", "recomendacion": "Comprar/Vender/Mantener", "probabilidad_exito": "75%", "accion_inmediata": "Esperar caída", "niveles_clave": "Comprar gradualmente", "justificacion": "Impacto de políticas locales.", "url_referencia": "URL"}}
  ],
  "estrategia_sectores_estrategicos": [
      {{
         "sector": "Nombre del Sector (Ej: Financiero, Energía, Defensa, Tecnología, Salud, Consumo Básico, Criptomonedas, Nuevas Promesas)",
         "veredicto_boton_sector": "Escribe literalmente COMPRAR, VENDER o MANTENER",
         "activos_clave": "Empresas principales que cubran este sector (Ej: JP Morgan, Exxon, Lockheed, Apple... EXPANDE MÁS ALLÁ DE LO OBVIO)",
         "disparador_compra": "Si sucede X macroeconómico -> Comprar inmediato",
         "disparador_venta": "Si sucede Y geopolítico/económico -> Vender o Reducir",
         "horizonte_corto": "Estrategia para 3-12 meses.",
         "horizonte_largo": "Tesis para 1-3+ años.",
         "escenario_si_entonces": "Si tomo la decisión bajo la precondición X, pasaría esto o esto en un plazo Z.",
         "probabilidad_estadistica": "Ej: 65% probabilidad de éxito matemático",
         "consideracion_meta_60_anual": "El usuario busca un 60% de rendimiento anual global. Qué consideraciones puntuales de ALTO RIESGO y apalancamiento requiere este sector para acercarse a la meta, o si sirve como ancla.",
         "url_referencia": "URL exhaustiva sobre este sector (ETF, noticia top o reporte)"
      }}
  ],
  "analisis_colombia": {{
      "tasas_de_interes": "Proyección y estado actual de las tasas del Banco de la República.",
      "sector_inmobiliario": {{
          "momento_compra": "Bueno / Malo / Esperar",
          "zonas_recomendadas": "Zonas o regiones concretas (Ej: Sabana de Bogotá, Norte de Barranquilla)",
          "justificacion": "Por qué invertir ahí",
          "probabilidad_exito_estimada": "Ej: 85%",
          "url_referencia": "URL del DANE o BanRep"
      }}
  }},
  "portafolio_detallado": [
      {{
         "activo": "Ej: BND, VOO, QQQM, KO, JNJ, AAPL, MSFT, AMZN, NVDA, TSLA, PLTR, BTD, etc...",
         "tipo": "Acción / Cripto / ETF / Otro",
         "sector": "Consumo Discrecional / Tecnología (etc.)",
         "perfil_riesgo": "Conservador / Moderado / Agresivo",
         "porcentaje": "Porcentaje sugerido (para balanceo interno)",
         "probabilidad_exito_estimada": "Ej: 90%",
         "veredicto_boton": "Escribe literalmente COMPRAR, VENDER o MANTENER",
         "accion_inmediata": "Breve frase",
         "rentabilidad_1_mes": "Proyección % corto plazo",
         "rentabilidad_1_ano": "Proyección % anual",
         "impacto_noticias": "Explicación breve de qué noticia causó este veredicto.",
         "condicion_salida_venta": "Regla estricta: Vender si baja de $X o pasa Y.",
         "tesis_exhaustiva": "Justificación profunda por la que el porcentaje o veredicto. DEBE NOMBRAR TEXTUALMENTE UNA NOTICIA INCLUIDA EN EL CONTEXTO.",
         "url_analisis_detallado": "URL oficial de la empresa, ticket en Yahoo o noticia"
      }}
  ],
  "matrices_graficos": {{
     "fear_and_greed_index": {cnn_fg_score},
     "perfiles_distribucion": [
        {{ "perfil": "Conservador", "distribucion": [{{"clase": "Renta Fija / Bonos", "porcentaje": 70}}, {{"clase": "Acciones Dividendos", "porcentaje": 20}}, {{"clase": "Liquidez Fuerte", "porcentaje": 10}}] }},
        {{ "perfil": "Moderado", "distribucion": [{{"clase": "Acciones/ETFs", "porcentaje": 50}}, {{"clase": "Bonos / CDTs", "porcentaje": 30}}, {{"clase": "Cripto / Oro", "porcentaje": 10}}, {{"clase": "Liquidez / Divisas", "porcentaje": 10}}] }},
        {{ "perfil": "Alto Riesgo", "distribucion": [{{"clase": "Criptos/Derivados", "porcentaje": 50}}, {{"clase": "Tech Stocks Beta Alto", "porcentaje": 30}}, {{"clase": "Oro/Materias Primas", "porcentaje": 15}}, {{"clase": "Liquidez", "porcentaje": 5}}] }},
        {{ "perfil": "Mixto (Global)", "distribucion": [{{"clase": "RV Global", "porcentaje": 40}}, {{"clase": "RF Emergente", "porcentaje": 25}}, {{"clase": "Metales/Oro", "porcentaje": 15}}, {{"clase": "Liquidez", "porcentaje": 20}}] }}
     ]
  }},
  "factores_extra_decision": [
     {{"titulo": "Consideración de Impuestos", "consejo": "Recuerda declarar anualmente las utilidades..."}},
     {{"titulo": "Psicología Trading", "consejo": "Comprar con miedo en el mercado, vender con euforia."}}
  ]
}}
IMPORTANTE: La suma de porcentajes en cada array de 'distribucion' DEBE ser exactamente 100.
IMPORTANTE: 'portafolio_detallado' DEBE tener obligatoriamente MÍNIMO 25 ACTIVOS diferentes que cubran TODOS los sectores (Tecnología, Energía, Salud, Financiero, Consumo, REITs, Oro, Bonos, etc). DEBES FORZAR LA INCLUSIÓN de BND, VOO, QQQM, KO, JNJ, AAPL, MSFT, AMZN, NVDA, TSLA, PLTR y EFTs.
IMPORTANTE: El array 'estrategia_sectores_estrategicos' DEBE contemplar obligatoriamente mínimo 8 sectores: Financiero, Energía, Defensa, Tecnología, Salud, Consumo Básico, Criptomonedas y Nuevas Promesas. Expande buscando mucha más información.
IMPORTANTE: Absolutamente TODOS los ítems de todos los arrays deben incluir obligatoriamente el campo 'url_referencia' con un hipervínculo real o de noticia/entidad oficial para citación directa.
IMPORTANTE: En 'analisis_divisas' ESTÁS OBLIGADO a proveer siempre el análisis simultáneo de Dólar (USD), Euro (EUR) y Peso Colombiano (COP).
IMPORTANTE: Recuerda constantemente la meta del 60% anual del usuario en cada sector, advirtiendo claramente el gigantesco nivel de apalancamiento/riesgo y timing perfecto que eso requiere.
IMPORTANTE: El índice de Fear and Greed de CNN Business ha sido extraído duro como {cnn_fg_score}. Acata las reglas de oro de ejecución frente a este número estático.
IMPORTANTE: La salida final debe omitir el bloque markdown de json y empezar con {{ y terminar con }}.

Noticias crudas globales (PUEDEN ESTAR EN OTRO IDIOMA, TRADUCE AL ESPAÑOL Y USA SUS URLS):
{news_text}
"""
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return '{{"error": "{}"}}'.format(str(e).replace('"', "'"))


def get_mock_analysis(cnn_fg_score=50):
    current_date_str = datetime.datetime.now().strftime("%d de %B de %Y")
    return '''
    {
      "fecha": "''' + current_date_str + '''",
      "noticias_clave": [
         {
            "titulo": "Resurgimiento de tensiones en Medio Oriente catapulta petroleras",
            "resumen": "Ataques simétricos en puertos claves disparan el precio del crudo WTI superando USD 85 por barril.",
            "url_referencia": "https://www.reuters.com",
            "urgencia": "Alta"
         },
         {
            "titulo": "NVIDIA rompe estimaciones Q1 y promete revolución AI sostenida",
            "resumen": "El gigante tecnológico superó proyecciones marcando ingresos récord, impulsando activos de riesgo.",
            "url_referencia": "https://finance.yahoo.com/news/nvidia",
            "urgencia": "Media"
         }
      ],
      "resumen_ejecutivo": [
         "Las tensiones globales empujan el petróleo, limitando la capacidad de los Bancos Centrales de ceder en tasas."
      ],
      "bancos_centrales_monetaria": [
         {
            "entidad": "Reserva Federal EE.UU. (FED)",
            "decisiones": "El Termómetro: Posible congelamiento de recortes de tasas",
            "impacto_mercado": "Si las tasas suben o se mantienen altas (Higher for Longer), el dinero es caro. Las tecnológicas caen, los bonos y el USD se vuelven muy atractivos.",
            "url_referencia": "https://www.federalreserve.gov/"
         }
      ],
      "geopolitica_seguridad": [
         {
            "evento": "Conflicto escalado transoceánico",
            "impacto_mercado": "Encadena cuellos de botella marítimos; petróleo repunta sobre $90.",
            "activos_refugio": "Capital huye a Oro (GLD) y Bonos del Tesoro (SGOV).",
            "url_referencia": "https://www.wsj.com/"
         }
      ],
      "salud_economica_macro": [
         {
            "indicador": "Inflación (IPC) Global",
            "estado": "Estresado / Pegajoso",
            "impacto_mercado": "Poder de compra se erosiona. Obliga a mantener Bienes Raíces (REITs) y Commodities que fluyen con ella.",
            "url_referencia": "https://www.bloomberg.com"
         }
      ],
      "guia_reaccion_rapida": [
         {
            "noticia_hipotetica": "La inflación en EE.UU. sale más alta de lo esperado",
            "contraste_realidad": "El gobierno dirá que es temporal, pero el mercado entrará en pánico por futuras subidas.",
            "accion_tomar": "Vender tecnológicas vulnerables y rotar hacia Bonos protegidos (TIPS) inmediatamente.",
            "url_referencia": "https://www.bls.gov/cpi/"
         },
         {
            "noticia_hipotetica": "Banco Central anuncia pausa explícita",
            "contraste_realidad": "Ahorradores pierden, pero corporativos toman deuda barata.",
            "accion_tomar": "Modo agresivo: Rotar cash hacia S&P 500 y NASDAQ (AI tech).",
            "url_referencia": "https://www.federalreserve.gov/"
         }
      ],
      "calendario_economico": [
         {
            "evento": "Reporte de Empleo No Agrícola (NFP) EE.UU.",
            "fecha_estimada": "Próximo Viernes 08:30 AM EST",
            "impacto_esperado": "Alta Volatilidad",
            "url_referencia": "https://es.investing.com/economic-calendar/"
         }
      ],
      "escenarios_probables": [
         {
            "escenario": "Cierre prolongado de puertos petroleros",
            "probabilidad_exito": "65%",
            "efecto": "Auge acelerado de índices Commodities.",
            "accion_recomendada": "Comprar XOM y GLD urgente.",
            "url_referencia": "https://www.wsj.com"
         }
      ],
      "analisis_divisas": [
         {
            "moneda": "Dólar Estadounidense (USD)",
            "recomendacion": "Mantener / Comprar",
            "probabilidad_exito": "85%",
            "accion_inmediata": "Acumular sobre debilidad de COP",
            "niveles_clave": "Comprar bajo 4000 COP.",
            "justificacion": "Refugio por tasas altas garantizadas en EEUU.",
            "url_referencia": "https://www.federalreserve.gov/"
         },
         {
            "moneda": "Euro (EUR)",
            "recomendacion": "Vender escalonado",
            "probabilidad_exito": "80%",
            "accion_inmediata": "Shortear frente al USD",
            "niveles_clave": "Vender cerca a 1.08 USD/EUR.",
            "justificacion": "Estancamiento económico en Alemania y el BCE proyectando recortes agresivos.",
            "url_referencia": "https://www.ecb.europa.eu/home/html/index.en.html"
         },
         {
            "moneda": "Peso Colombiano (COP)",
            "recomendacion": "Vender escalonado",
            "probabilidad_exito": "75%",
            "accion_inmediata": "Aprovechar alzas temporales para salir a USD",
            "niveles_clave": "Soportes en 3850",
            "justificacion": "Presión macroeconómica interna.",
            "url_referencia": "https://www.banrep.gov.co/"
         }
      ],
      "estrategia_sectores_estrategicos": [
         {
            "sector": "Financiero Institucional",
            "veredicto_boton_sector": "COMPRAR",
            "activos_clave": "JP Morgan (JPM), Goldman Sachs (GS), Bancolombia (CIB), Berkshire Hathaway (BRK.B)",
            "disparador_compra": "Si el Banco Central enfría la inflación y anuncia recortes fuertes de tasas.",
            "disparador_venta": "Si se reporta morosidad masiva en créditos comerciales y tasas suben >6%.",
            "horizonte_corto": "Aprovechar hasta 6 meses el diferencial de tasas altas antes de recortes.",
            "horizonte_largo": "Mantener 1-3 años a medida que el ciclo de expansión de crédito reinicie.",
            "escenario_si_entonces": "Si compro hoy banco ante expectativas de recorte y cortan 50 puntos base, el sector sube 15% rápido. Si no cortan, cae 8% por reprecio de bonos basuras.",
            "probabilidad_estadistica": "65% éxito matemático a favor de compras",
            "consideracion_meta_60_anual": "Los bancos rinden 10-15% al año. Para arrimarte al 60% anual necesitarías apalancamiento 3x en ETFs de la industria financiera (FAS), asumiendo riesgo de liquidación severo.",
            "url_referencia": "https://es.investing.com/indices/s-p-500-financials"
         },
         {
            "sector": "Energía Convencional y Fósil",
            "veredicto_boton_sector": "MANTENER",
            "activos_clave": "ExxonMobil (XOM), Chevron (CVX), Ecopetrol (EC), NextEra Energy (NEE)",
            "disparador_compra": "Si barril WTI sube >5% semanal o se escalan cuellos marítimos Bálticos/Medio Oriente.",
            "disparador_venta": "Si OPEP incrementa flujo drásticamente o se instauran controles de precios gubernamentales.",
            "horizonte_corto": "Swing Trading aprovechando volatilidad mensual de inventarios (EIA).",
            "horizonte_largo": "Mantener rezagados value durante el superciclo de transición (Cash flow cows).",
            "escenario_si_entonces": "Si mantengo Ecopetrol por su spread dividend y gobierno impone nuevas regalías, el dividendo se pulveriza, afectando la acción -20%.",
            "probabilidad_estadistica": "72% éxito estadístico por falta de Capex petrolero reciente.",
            "consideracion_meta_60_anual": "Energía es defensivo. No da 60% rápido a menos que operes contratos de Opciones (Calls) directamente sobre crudo frente a picos de guerra.",
            "url_referencia": "https://www.eia.gov/"
         },
         {
            "sector": "Defensa Aeroespacial",
            "veredicto_boton_sector": "COMPRAR",
            "activos_clave": "Lockheed Martin (LMT), Northrop Grumman (NOC), RTX Corp (RTX), Palantir (PLTR)",
            "disparador_compra": "Al anunciarse megapresupuestos de rearme OTAN o picos de escalada misilística.",
            "disparador_venta": "Tratados reales y sostenidos de armisticio global. Austeridad fiscal demócrata/republicana en USA.",
            "horizonte_corto": "6-9 meses especulativos al son de titulares geopolíticos diarios.",
            "horizonte_largo": "Perpetuo mientras el cambio hegemónico mundial EE.UU-China no se defina.",
            "escenario_si_entonces": "Si estalla otro proxy-war en el Pacífico y tienes LMT, el salto inmediato es +12% al abrir mercado. Riesgo de estancamiento en paz global (-5%).",
            "probabilidad_estadistica": "85% con el mundo dividido.",
            "consideracion_meta_60_anual": "Este sector estabiliza tu cartera y distribuye riesgo. Para buscar el 60%, deberías mezclarlo fuertemente con acciones de Defensa que tengan IA (PLTR) que poseen betas locos.",
            "url_referencia": "https://www.sipri.org/"
         },
         {
            "sector": "Tecnología de Punta (Chips, IA)",
            "veredicto_boton_sector": "COMPRAR",
            "activos_clave": "NVIDIA (NVDA), Apple (AAPL), TSMC (TSM), Microsoft (MSFT), ASML",
            "disparador_compra": "Lanzamientos revolucionarios de nuevos LLM, reportes de DataCenters rebasados y guías altas.",
            "disparador_venta": "Bloqueos masivos anti-monopolio (DOJ), aranceles de silicio o guerra estructural de Taiwán.",
            "horizonte_corto": "Tomar momentum pre-earnings (hasta 6 meses).",
            "horizonte_largo": "Mantener agresivo 5+ años. La Cuarta Revolución Industrial es imparable.",
            "escenario_si_entonces": "Si compro NVDA pre-ganancias, y el Forward P/E (proyección futura) cae frente a altas tasas, la corrección arrastrará -15% en una tarde. La estadística macro avala a la tecnología en el largo plazo.",
            "probabilidad_estadistica": "80% de victoria reteniendo monopolios puros.",
            "consideracion_meta_60_anual": "Aquí ESTÁ la clave para tu 60% anual. Requerirías ponderar (sobreasignar) un 35% a 45% de tu capital directamente al Nasdaq-100 (QQQM) cruzado con Opciones Leaps a 1 año.",
            "url_referencia": "https://finance.yahoo.com/sector/Technology"
         },
         {
            "sector": "Salud Farmacéutica (BioTech)",
            "veredicto_boton_sector": "MANTENER",
            "activos_clave": "Pfizer (PFE), Johnson & Johnson (JNJ), Moderna (MRNA), Novo Nordisk (NVO)",
            "disparador_compra": "Aprobaciones FDA sorpresivas o reactivación de miedo endémico mundial.",
            "disparador_venta": "Fallas fase 3 brutales de desarrollo, litigios de patentes masivos o recorte insulinar.",
            "horizonte_corto": "Especulativo a 12 meses apostando a resoluciones orgánicas en tribunales FDA.",
            "horizonte_largo": "Inclusión demográfica mundial base (envejecimiento global es garantía de compra en bajas).",
            "escenario_si_entonces": "Si la FED rompe su política monetaria, consumo básico e industrial sufren, pero los abuelos europeos seguirán comprando aspirinas y diabetes care. Hedge perfecto.",
            "probabilidad_estadistica": "75% estadístico anti-cíclico.",
            "consideracion_meta_60_anual": "No debes buscar 60% anual en Salud estándar. Síguele el paso a los ETFs de Biotecnología tipo XBI, que sí entregan volatilidades extremas buscando el siguiente super medicamento antiobesidad.",
            "url_referencia": "https://www.fda.gov/"
         },
         {
            "sector": "Consumo Básico Inelástico",
            "veredicto_boton_sector": "VENDER",
            "activos_clave": "Coca-Cola (KO), P&G (PG), Unilever (UL), Grupo Nutresa",
            "disparador_compra": "Recesiones profundas asoman. La curva invertida es oficial.",
            "disparador_venta": "Nunca. Se asume reducción marginal si el mercado se torna ultra Riesgo Enérgico (Risk On).",
            "horizonte_corto": "Rotación al volar el pánico. Retiene valor como refugio con dividendos.",
            "horizonte_largo": "Hold eterno. Compuesto sobre dividendos en un plan de retiro (DRIP).",
            "escenario_si_entonces": "Si se reporta 0 crecimiento y recesión fuerte con deflación, Consumo Básico apenas pestañea frente a bancos colapsando o tech implosionando.",
            "probabilidad_estadistica": "95% tasa de supervivencia corporativa a largo plazo.",
            "consideracion_meta_60_anual": "Peligro: Este sector deprime radicalmente la consecución del 60% anual. Te dará 6-9% y seguridad con bajo stress. Es tu freno de auto.",
            "url_referencia": "https://es.investing.com/indices/s-p-500-consumer-staples"
         },
         {
            "sector": "Criptomonedas / Infraestructura Web3",
            "veredicto_boton_sector": "COMPRAR",
            "activos_clave": "Bitcoin (BTC), Ethereum (ETH), Solana (SOL), MicroStrategy (MSTR)",
            "disparador_compra": "Bancos perdiendo encaje, devaluación fiat (impresoras), o ETF aprobaciones en jurisdicciones asiáticas.",
            "disparador_venta": "Prohibiciones criminales de G7 centralizado, fallos criptográficos del Core Bitcoin, o subida de tasas al 8% ahogando riesgo.",
            "horizonte_corto": "Jugar impulsos de Halving a 3 meses. Extremadamente sobrecolapsado emocionalmente.",
            "horizonte_largo": "Mantener BTC/ETH absoluto como reserva dorada extra-sistema financiero y apolítico.",
            "escenario_si_entonces": "Si un fondo de pensiones europeo asigna el 2% a BTC spot, el shock de escasez manda el precio un 40% arriba. Es un vector asimétrico inaudito.",
            "probabilidad_estadistica": "45-55% (probabilidad binaria, sube brutalmente o se regula radicalmente).",
            "consideracion_meta_60_anual": "Este sector fue literalmente diseñado para rebasar márgenes del 60% al >200% interanual. El precio a pagar son los horribles drawdowns de -70% en osos brutales. Manejo exigente intra-ciclo.",
            "url_referencia": "https://coinmarketcap.com/"
         },
         {
            "sector": "Nuevas Promesas y Vanguardia",
            "veredicto_boton_sector": "MANTENER",
            "activos_clave": "CRISPR Therapeutics (CRSP), Plug Power (PLUG), QuantumSpace (QS), Nu (NU Holdings)",
            "disparador_compra": "Inversión de capital de Riesgo anunciada, avance de regulaciones NetZero globales 2030, Latam bancarización masiva.",
            "disparador_venta": "Tipos altos de interés sostenido (les seca el flujo a las compañías sin rentabilidad aún).",
            "horizonte_corto": "Swing táctico de alta especulación pre-anuncios de alianzas estratégicas corporativas (3-6 m).",
            "horizonte_largo": "Riesgo de insolvencia a cambio de encontrar 'El Siguiente Amazon'. Exige paciencia de 7 años.",
            "escenario_si_entonces": "Si inviertes hoy en biotecnología CRISPR sin ingresos pero se prueba exitosos sus test CRISPR contra Anemia, el retorno salta >400%.",
            "probabilidad_estadistica": "15% probabilidad de acierto individual, pero si acierta, paga todo.",
            "consideracion_meta_60_anual": "Dedica un máximo del 10%-15% estructural hacia estas promesas. Proyectarán ese componente multiplicador para promediar la cartera por encima del 50-60% si dos de ellas estallan arriba.",
            "url_referencia": "https://pitchbook.com/"
         }
      ],
      "analisis_colombia": {
         "tasas_de_interes": "Desestabilización inflacionaria local dificulta rebajas al 8.5% este trimestre.",
         "sector_inmobiliario": {
            "momento_compra": "Esperar caída de tasas (Q4)",
            "zonas_recomendadas": "Norte de Barranquilla y Sabana de Bogotá",
            "justificacion": "Bajo las altas tasas actuales hipotecarias (14%+), compras de usado destruyen rentabilidad patrimonial.",
            "probabilidad_exito_estimada": "90%",
            "url_referencia": "https://www.dane.gov.co"
         }
      },
      "portafolio_detallado": [
         {
            "activo": "Vanguard Total Stock ETF (VOO)", "tipo": "ETF", "sector": "Índices / Multi-Sectorial",
            "perfil_riesgo": "Conservador", "porcentaje": "25%", "probabilidad_exito_estimada": "90%", "veredicto_boton": "MANTENER",
            "accion_inmediata": "Comprar más en caídas.", "rentabilidad_1_mes": "1%", "rentabilidad_1_ano": "10%",
            "impacto_noticias": "Alta inflación reduce velocidad de crecimiento.", "condicion_salida_venta": "Nunca vender, es el núcleo.",
            "tesis_exhaustiva": "Apuesta infalible a la hegemonía estadounidense a largo plazo (Decisión FED).",
            "url_analisis_detallado": "https://investor.vanguard.com/investment-products/etfs/profile/voo"
         },
         {
            "activo": "Invesco QQQ Trust (QQQM)", "tipo": "ETF", "sector": "Tecnología",
            "perfil_riesgo": "Moderado", "porcentaje": "20%", "probabilidad_exito_estimada": "85%", "veredicto_boton": "COMPRAR",
            "accion_inmediata": "Asignar capital este mes.", "rentabilidad_1_mes": "2%", "rentabilidad_1_ano": "15%",
            "impacto_noticias": "Boom de IA sostiene métricas de crecimiento.", "condicion_salida_venta": "Si NASDAQ cae > 20% estructuralmente.",
            "tesis_exhaustiva": "Concentración en la vanguardia tech como solución a crisis de escasez laboral.",
            "url_analisis_detallado": "https://www.invesco.com/us/financial-products/etfs/product-detail?audienceType=Investor&productId=ETF-QQQM"
         },
         {
            "activo": "Vanguard Total Bond Market (BND)", "tipo": "Bono ETF", "sector": "Renta Fija / Bonos",
            "perfil_riesgo": "Conservador", "porcentaje": "15%", "probabilidad_exito_estimada": "95%", "veredicto_boton": "COMPRAR",
            "accion_inmediata": "Asegurar Yields actuales.", "rentabilidad_1_mes": "0.5%", "rentabilidad_1_ano": "5%",
            "impacto_noticias": "Pivote de tasas de interés los beneficia.", "condicion_salida_venta": "Si la inflación se dispara de vuelta arriba del 5%.",
            "tesis_exhaustiva": "El seguro del carro ante accidentes macroeconómicos y protección contra volatilidad.",
            "url_analisis_detallado": "https://investor.vanguard.com/investment-products/etfs/profile/bnd"
         },
         {
            "activo": "Bitcoin (BTC)", "tipo": "Criptomoneda", "sector": "Criptomonedas / Infraestructura Web3",
            "perfil_riesgo": "Agresivo", "porcentaje": "10%", "probabilidad_exito_estimada": "60%", "veredicto_boton": "COMPRAR",
            "accion_inmediata": "Agresivo post-caída de ETF.", "rentabilidad_1_mes": "10%", "rentabilidad_1_ano": "80%",
            "impacto_noticias": "Aprobaciones institucionales globales lideran el precio.", "condicion_salida_venta": "Rompe soporte crítico de 50K con volumen.",
            "tesis_exhaustiva": "Oro digital como seguro asimétrico contra la impresión infinita de deuda fiat de EE.UU.",
            "url_analisis_detallado": "https://bitcoin.org/"
         },
         {
            "activo": "Nvidia (NVDA)", "tipo": "Acción", "sector": "Tecnología de Punta (Chips, IA)",
            "perfil_riesgo": "Agresivo", "porcentaje": "10%", "probabilidad_exito_estimada": "70%", "veredicto_boton": "MANTENER",
            "accion_inmediata": "Hold.", "rentabilidad_1_mes": "5%", "rentabilidad_1_ano": "40%",
            "impacto_noticias": "Demanda de chips de IA supera la oferta.", "condicion_salida_venta": "Guerra abierta en Taiwán.",
            "tesis_exhaustiva": "Monopolio temporal en GPUs para entrenar los LLMs del planeta.",
            "url_analisis_detallado": "https://investor.nvidia.com/"
         },
         {
            "activo": "Apple Inc. (AAPL)", "tipo": "Acción", "sector": "Tecnología de Punta (Chips, IA)",
            "perfil_riesgo": "Moderado", "porcentaje": "5%", "probabilidad_exito_estimada": "85%", "veredicto_boton": "MANTENER",
            "accion_inmediata": "Acumular bajo $160.", "rentabilidad_1_mes": "2%", "rentabilidad_1_ano": "12%",
            "impacto_noticias": "Inmigración a Apple Intelligence ralentizada.", "condicion_salida_venta": "Pérdida de márgenes base del iPhone.",
            "tesis_exhaustiva": "Flujo de caja libre masivo, recompra indetenible.",
            "url_analisis_detallado": "https://investor.apple.com/"
         },
         {
            "activo": "Microsoft (MSFT)", "tipo": "Acción", "sector": "Tecnología de Punta (Chips, IA)",
            "perfil_riesgo": "Conservador", "porcentaje": "5%", "probabilidad_exito_estimada": "85%", "veredicto_boton": "COMPRAR",
            "accion_inmediata": "Ignorar ruido de mercado.", "rentabilidad_1_mes": "2%", "rentabilidad_1_ano": "18%",
            "impacto_noticias": "Integración Copilot asegura B2B.", "condicion_salida_venta": "CEO Nadella abandona Azure.",
            "tesis_exhaustiva": "Diversificación perfecta B2B y dueños de facto de OpenAI.",
            "url_analisis_detallado": "https://www.microsoft.com/en-us/investor"
         },
         {
            "activo": "Coca-Cola (KO)", "tipo": "Acción", "sector": "Consumo Básico Inelástico",
            "perfil_riesgo": "Conservador", "porcentaje": "2.5%", "probabilidad_exito_estimada": "90%", "veredicto_boton": "MANTENER",
            "accion_inmediata": "DRIP (Reinvertir dividendos).", "rentabilidad_1_mes": "0.5%", "rentabilidad_1_ano": "6%",
            "impacto_noticias": "Inflación alta frena consumo, pero es precio-fijador.", "condicion_salida_venta": "Reducción del dividendo.",
            "tesis_exhaustiva": "Rey del Value Investing y dividend aristocrat absoluto.",
            "url_analisis_detallado": "https://investors.coca-colacompany.com/"
         },
         {
            "activo": "Johnson & Johnson (JNJ)", "tipo": "Acción", "sector": "Salud Farmacéutica (BioTech)",
            "perfil_riesgo": "Conservador", "porcentaje": "2.5%", "probabilidad_exito_estimada": "85%", "veredicto_boton": "MANTENER",
            "accion_inmediata": "Aprovechar litigios de Talco para compras.", "rentabilidad_1_mes": "1%", "rentabilidad_1_ano": "8%",
            "impacto_noticias": "Espin-off de Kenvue.", "condicion_salida_venta": "Quiebra masiva por pleitos legales.",
            "tesis_exhaustiva": "Líder de med-tech y farmacéuticas con rating AAA.",
            "url_analisis_detallado": "https://investor.jnj.com/"
         },
         {
            "activo": "Amazon (AMZN)", "tipo": "Acción", "sector": "Consumo Discrecional / Tech",
            "perfil_riesgo": "Moderado", "porcentaje": "5%", "probabilidad_exito_estimada": "80%", "veredicto_boton": "COMPRAR",
            "accion_inmediata": "Toma posiciones estructurales.", "rentabilidad_1_mes": "3%", "rentabilidad_1_ano": "25%",
            "impacto_noticias": "AWS re-acelera contra Azure en nube.", "condicion_salida_venta": "Margen de AWS colapsa por guerra.",
            "tesis_exhaustiva": "Dominio logístico global y dueño de la infraestructura cloud moderna (AWS).",
            "url_analisis_detallado": "https://ir.aboutamazon.com/"
         }
      ],
      "matrices_graficos": {
         "fear_and_greed_index": ''' + str(cnn_fg_score) + ''',
         "perfiles_distribucion": [
            { "perfil": "Conservador", "distribucion": [{"clase": "Renta Fija / Bonos", "porcentaje": 70}, {"clase": "Acciones Dividendos", "porcentaje": 20}, {"clase": "Liquidez Fuerte", "porcentaje": 10}] },
            { "perfil": "Moderado", "distribucion": [{"clase": "Acciones/ETFs", "porcentaje": 50}, {"clase": "Bonos / CDTs", "porcentaje": 30}, {"clase": "Cripto / Oro", "porcentaje": 10}, {"clase": "Liquidez / Divisas", "porcentaje": 10}] },
            { "perfil": "Alto Riesgo", "distribucion": [{"clase": "Criptos/Derivados", "porcentaje": 50}, {"clase": "Tech Stocks Beta Alto", "porcentaje": 30}, {"clase": "Oro/Materias Primas", "porcentaje": 15}, {"clase": "Liquidez", "porcentaje": 5}] },
            { "perfil": "Mixto (Global)", "distribucion": [{"clase": "RV Global", "porcentaje": 40}, {"clase": "RF Emergente", "porcentaje": 25}, {"clase": "Metales/Oro", "porcentaje": 15}, {"clase": "Liquidez", "porcentaje": 20}] }
         ]
      },
      "factores_extra_decision": [
         {"titulo": "Protección Patrimonial vs Inflación local", "consejo": "Nunca evalúes rendimientos nominales. Si generas 10% pero tu país deprecia 12%, perdiste 2%. Opera globales en divisas fuertes."},
         {"titulo": "Inteligencia Emocional", "consejo": "La regla #1 de Warren Buffet es 'No pierdas dinero'. Revisa frenéticamente tus condiciones de salida (Stop-loss)."}
      ]
    }
    '''

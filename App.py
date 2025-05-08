import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Cargar modelo
modelo = joblib.load("stacking_rain_final.pkl")

# -----------------------------
# Configuración de página
st.set_page_config(page_title="🌧️ Predicción de Lluvia", page_icon="🌦️", layout="centered")

# -----------------------------
# Diccionario de textos por idioma
TEXTOS = {
    "es": {
        # Títulos y pestañas
        "titulo_app": "🌦️ Modelo Predictor de Lluvia",
        "descripcion": "Ingresa valores para hacer una predicción rápida.",
        "pestaña_modelo": "🧠 Acerca del Modelo",
        "pestaña_prediccion": "🌦️ Predicción",
        "boton_predecir": "🔍 Predecir",

        # Resultados
        "resultado_lluvia": "🌧️ ¡Probabilidad alta de lluvia!",
        "resultado_seco": "☀️ No se espera lluvia.",

        # Sección modelo
        "titulo_seccion_modelo": " Arquitectura del Modelo",
        "texto_seccion_modelo": """
            Este es un **modelo de ensamble tipo Stacking**, compuesto por los siguientes modelos base:
            - **XGBoost**
            - **LightGBM**
            - **Random Forest**

            Los resultados de estos modelos son combinados mediante una **Regresión Logística**, que actúa como meta-modelo final.

            El sistema también incluye un paso previo de **escalado automático de características**.
        """,

        # Sección Kaggle
        "titulo_seccion_kaggle": " Competición en Kaggle",
        "texto_seccion_kaggle": """
            Este modelo fue desarrollado como parte de una competición orientada a predecir si lloverá al día siguiente basándose en datos históricos de clima.

            🎯 **Primer clasificado:**  
            Accuracy de **0.90654**

            ✅ **Mi resultado obtenido:**  
            Accuracy de **0.88885**

            💡 Este desempeño demuestra un buen equilibrio entre complejidad y precisión del modelo.
        """,

        # Inputs
        "day": "📅 Día del año",
        "pressure": "🌬️ Presión atmosférica (hPa)",
        "maxtemp": "🔥 Temperatura máxima (°C)",
        "temparature": "🌡️ Temperatura actual (°C)",
        "mintemp": "❄️ Temperatura mínima (°C)",
        "dewpoint": "💧 Punto de rocío (°C)",
        "humidity": "💦 Humedad (%)",
        "cloud": "☁️ Nubosidad (%)",
        "sunshine": "☀️ Horas de sol",
        "winddirection": "🧭 Dirección del viento (grados)",
        "windspeed": "🌪️ Velocidad del viento (km/h)"
    },
    "en": {
        # Títulos y pestañas
        "titulo_app": "🌦️ Rain Forecast Model",
        "descripcion": "Enter values to make a quick prediction.",
        "pestaña_modelo": "🧠 About the Model",
        "pestaña_prediccion": "🌦️ Prediction",
        "boton_predecir": "🔍 Predict",

        # Resultados
        "resultado_lluvia": "🌧️ High probability of rain!",
        "resultado_seco": "☀️ No rain expected.",

        # Sección modelo
        "titulo_seccion_modelo": " Model Architecture",
        "texto_seccion_modelo": """
            This is a **Stacking ensemble model**, composed of the following base models:
            - **XGBoost**
            - **LightGBM**
            - **Random Forest**

            The results from these models are combined using **Logistic Regression** as the final meta-model.

            The system also includes an automatic feature scaling step.
        """,

        # Sección Kaggle
        "titulo_seccion_kaggle": " Kaggle Competition",
        "texto_seccion_kaggle": """
            This model was developed as part of a competition aimed at predicting whether it will rain the next day based on historical weather data.

            🎯 **Top-ranked participant:**  
            Accuracy of **0.90654**

            ✅ **My achieved result:**  
            Accuracy of **0.88885**

            💡 This performance demonstrates a good balance between model complexity and accuracy.
        """,

        # Inputs
        "day": "📅 Day of year",
        "pressure": "🌬️ Atmospheric pressure (hPa)",
        "maxtemp": "🔥 Max temperature (°C)",
        "temparature": "🌡️ Current temperature (°C)",
        "mintemp": "❄️ Min temperature (°C)",
        "dewpoint": "💧 Dew point (°C)",
        "humidity": "💦 Humidity (%)",
        "cloud": "☁️ Cloud cover (%)",
        "sunshine": "☀️ Hours of sun",
        "winddirection": "🧭 Wind direction (degrees)",
        "windspeed": "🌪️ Wind speed (km/h)"
    }
}

# -----------------------------
# Función para obtener texto según idioma
def t(clave):
    return TEXTOS[lang][clave]

# -----------------------------
# Selector de idioma
lang = st.selectbox("🌐 Idioma / Language", options=["es", "en"], format_func=lambda x: "Español" if x == "es" else "English")

# -----------------------------
# Estilos personalizados con CSS (con animaciones e iconos)
st.markdown("""
    <style>
        .main {
            background-color: #f5f9ff;
            color: #333;
            font-family: Arial, sans-serif;
            font-size: 17px;
        }
        h1, h2, h3 {
            color: #1e3a8a;
            font-size: 26px;
        }
        .section-title {
            font-size: 26px;
            font-weight: bold;
            margin-top: 20px;
            color: #1e3a8a;
        }
        .animated-icon {
            display: inline-block;
            animation: float 2s ease-in-out infinite;
            font-size: 1.5em;
            vertical-align: middle;
            margin-right: 10px;
        }
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-5px); }
            100% { transform: translateY(0px); }
        }
        .stButton button {
            background-color: #1e3a8a;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .result-box {
            padding: 20px;
            margin-top: 20px;
            border-radius: 10px;
            font-size: 1.2em;
            text-align: center;
            animation: fadeIn 0.5s ease;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.95); }
            to { opacity: 1; transform: scale(1); }
        }
        .rainy {
            background-color: #bee3f8;
            color: #1e40af;
        }
        .sunny {
            background-color: #fef9c3;
            color: #856404;
        }
        .section-model {
            background-color: #e0f2fe;
            padding: 15px;
            border-left: 5px solid #0369a1;
            margin-bottom: 20px;
            font-size: 16px;
        }
        .section-kaggle {
            background-color: #f8fafc;
            padding: 15px;
            border-left: 5px solid #7c3aed;
            margin-bottom: 20px;
            font-size: 16px;
        }
        .footer {
            margin-top: 50px;
            padding: 20px;
            text-align: center;
            font-size: 0.9em;
            color: #555;
        }
        .footer a {
            margin: 0 10px;
            text-decoration: none;
            color: #1e3a8a;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Crear las pestañas
tab1, tab2 = st.tabs([t("pestaña_modelo"), t("pestaña_prediccion")])

# -----------------------------
# Pestaña 1: Acerca del Modelo
with tab1:
 
    st.markdown(f'<span class="animated-icon">🧩</span><span class="section-title">{t("titulo_seccion_modelo")}</span>', unsafe_allow_html=True)
    st.markdown(t("texto_seccion_modelo"))
    st.markdown('</div>', unsafe_allow_html=True)


    st.markdown(f'<span class="animated-icon">🏆</span><span class="section-title">{t("titulo_seccion_kaggle")}</span>', unsafe_allow_html=True)
    st.markdown(t("texto_seccion_kaggle"))
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Pestaña 2: Interfaz de Predicción
with tab2:
    st.title(t("titulo_app"))
    st.write(t("descripcion"))

    col1, col2 = st.columns(2)

    with col1:
        day = st.number_input(t("day"), min_value=1, max_value=365, value=15)
        pressure = st.number_input(t("pressure"), value=1010.0)
        maxtemp = st.number_input(t("maxtemp"), value=30.0)
        temparature = st.number_input(t("temparature"), value=25.0)
        mintemp = st.number_input(t("mintemp"), value=15.0)
        dewpoint = st.number_input(t("dewpoint"), value=20.0)

    with col2:
        humidity = st.number_input(t("humidity"), value=60.0)
        cloud = st.number_input(t("cloud"), value=50.0)

        st.markdown(t("sunshine"))
        col_hora, col_minuto = st.columns(2)
        with col_hora:
            horas = st.number_input("Horas", min_value=0, max_value=24, value=5, step=1, label_visibility="collapsed")
        with col_minuto:
            minutos = st.number_input("Minutos", min_value=0, max_value=59, value=0, step=1, label_visibility="collapsed")
        sunshine = float(horas) + float(minutos)/60

        winddirection = st.number_input(t("winddirection"), value=180.0)
        windspeed = st.number_input(t("windspeed"), value=10.0)

    st.markdown('<div style="display: flex; justify-content: center; margin-top: 20px;">', unsafe_allow_html=True)
    if st.button(t("boton_predecir")):
        nuevos_datos_df = pd.DataFrame({
            'day': [day],
            'pressure': [pressure],
            'maxtemp': [maxtemp],
            'temparature': [temparature],
            'mintemp': [mintemp],
            'dewpoint': [dewpoint],
            'humidity': [humidity],
            'cloud': [cloud],
            'sunshine': [sunshine],
            'winddirection': [winddirection],
            'windspeed': [windspeed],
        })

        for col in nuevos_datos_df.columns:
            nuevos_datos_df[col] = pd.to_numeric(nuevos_datos_df[col], errors='coerce')

        probabilidad = modelo.predict_proba(nuevos_datos_df)[:, 1][0]
        prediccion = modelo.predict(nuevos_datos_df)[0]

        if prediccion == 1:
            st.markdown(f"""
                <div class="result-box rainy">
                    {t("resultado_lluvia")}<br>
                    <strong>{probabilidad:.2%}</strong>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="result-box sunny">
                    {t("resultado_seco")}<br>
                    <strong>{probabilidad:.2%}</strong>
                </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Footer con tus datos personales 👇👇👇
nombre = "Adrián Alonso Pérez"
correo = "adrian95oza@gmail.com"
github = "https://github.com/adrian-aperez "
linkedin = "https://www.linkedin.com/in/adrian-alonso-perez/ "

st.markdown(f"""
    <div class="footer">
        <strong>{nombre}</strong><br>
        📧 {correo} | 
        🐱 <a href="{github}" target="_blank">GitHub</a> | 
        🔗 <a href="{linkedin}" target="_blank">LinkedIn</a><br>
        © 2025 - Aplicación de Predicción de Lluvia usando Machine Learning
    </div>
""", unsafe_allow_html=True)
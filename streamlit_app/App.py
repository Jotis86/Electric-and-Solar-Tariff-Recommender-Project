import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt


# Configuración de la página
st.set_page_config(
    page_title="Recomendador Energético",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados globales (parte del código existente)
st.markdown("""
<style>
    /* Estilos globales */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Estilo para el banner principal */
    .banner {
        background: linear-gradient(135deg, #1e5799 0%, #207cca 51%, #2989d8 100%);
        color: white;
        padding: 2rem 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Estilos para el sidebar */
    [data-testid=stSidebar] {
        background-image: linear-gradient(135deg, #1e5799 0%, #207cca 51%, #2989d8 100%);
    }
    
    [data-testid=stSidebar] [data-testid=stMarkdown] {
        color: white;
    }
    
    [data-testid=stSidebar] .stRadio label {
        color: white;
        font-weight: 500;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 8px;
        transition: all 0.3s;
    }
    
    [data-testid=stSidebar] .stRadio label:hover {
        background-color: rgba(255, 255, 255, 0.2);
        transform: translateX(5px);
    }
    
    [data-testid=stSidebar] [data-testid=stImage]{
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Estilo para el botón de GitHub */
    .github-button {
        display: inline-block;
        padding: 10px 15px;
        background-color: #333;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        font-weight: 500;
        margin-top: 15px;
        text-align: center;
        transition: all 0.3s;
        width: 100%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    
    .github-button:hover {
        background-color: #2b2b2b;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        transform: translateY(-2px);
    }
    
    .github-icon {
        margin-right: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Banner personalizado en lugar de imagen 
st.markdown("""
<div class="banner">
    <h1>⚡ Recomendador de Tarifas de Luz y Placas Solares ☀️</h1>
    <p>Ahorra energía y dinero con recomendaciones personalizadas basadas en tus necesidades</p>
</div>
""", unsafe_allow_html=True)

# Contenido del sidebar mejorado
with st.sidebar:
    # Logo en la parte superior del sidebar
    st.image(os.path.join(current_dir, "octocat.jpg"), use_container_width=True)
    
    # Título del sidebar con icono
    st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 20px; text-shadow: 1px 1px 3px rgba(0,0,0,0.2);'>🌟 Navegación</h1>", unsafe_allow_html=True)
    
    # Separador visual
    st.markdown("<hr style='margin: 15px 0; border: 0; height: 1px; background: rgba(255,255,255,0.3);'>", unsafe_allow_html=True)
    
    # Opciones de navegación con iconos
    opciones = {
        "🏠 Inicio": "Inicio",
        "📈 Visualizaciones": "Visualizaciones",
        "💡 Recomendador Tarifas": "Recomendador Tarifas Eléctricas",
        "☀️ Recomendador Solar": "Recomendador Placas Solares"
    }

    seccion = st.radio("", list(opciones.keys()), key="nav")
    seccion_seleccionada = opciones[seccion]
    
    # Separador visual
    st.markdown("<hr style='margin: 15px 0; border: 0; height: 1px; background: rgba(255,255,255,0.3);'>", unsafe_allow_html=True)
    
    # Información adicional
    st.markdown("<div style='padding: 10px; background-color: rgba(255,255,255,0.1); border-radius: 5px;'><p style='color: white; margin: 0;'>Desarrollado con ❤️ usando Streamlit</p></div>", unsafe_allow_html=True)
    
    # Botón de GitHub
    github_repo_url = "https://github.com/Jotis86/Electric-and-Solar-Tariff-Recommender-Project"
    st.markdown(f"""
    <a href="{github_repo_url}" target="_blank" class="github-button">
        <span class="github-icon">⭐</span> Ver en GitHub
    </a>
    """, unsafe_allow_html=True)

# Sección de Introducción
if seccion_seleccionada == "Inicio":
    # CSS personalizado para tarjetas y diseño
    st.markdown("""
    <style>
        .card {
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            background: white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
            color: #333; /* Color oscuro para el texto en tarjetas con fondo blanco */
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .card-icon {
            font-size: 2.5rem;
            margin-bottom: 15px;
            text-align: center;
        }
        .card-title {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 10px;
            color: #2989d8;
        }
        .card p, .card ul, .card li {
            color: #333; /* Asegura que todo texto en las tarjetas sea oscuro */
        }
        .step-box {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 8px;
            padding: 15px;
            margin: 10px 0;
            display: flex;
            align-items: center;
            color: #333; /* Texto oscuro para contraste */
        }
        .step-number {
            background: #2989d8;
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 15px;
            font-weight: bold;
        }
        .highlight-section {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 10px;
            padding: 25px;
            margin: 20px 0;
            color: #333; /* Texto oscuro para contraste */
        }
        h2 {
            color: #1e5799;
            border-bottom: 2px solid #2989d8;
            padding-bottom: 8px;
            margin-bottom: 20px;
        }
        /* Asegurando que el texto en el sidebar sea visible */
        [data-testid=stSidebar] [data-testid=stMarkdown] {
            color: white !important;
        }
        /* Ajustar color de texto en secciones específicas */
        .stApp p, .stApp ul, .stApp li {
            color: #333;
        }
    </style>
    """, unsafe_allow_html=True)

    # Encabezado principal
    #st.markdown("<h2>⚡ Recomendador de Tarifas de Luz y Placas Solares</h2>", unsafe_allow_html=True)
    
    # Descripción breve
    st.markdown("""
    <div class="highlight-section">
        <p>Hemos desarrollado esta herramienta para ayudarte a <b>ahorrar dinero</b> y contribuir a un <b>futuro sostenible</b> 
        mediante recomendaciones personalizadas de tarifas eléctricas y placas solares basadas en tus necesidades específicas.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beneficios en 3 columnas
    st.markdown("<h3>🌟 Beneficios</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-icon">💰</div>
            <div class="card-title">Ahorro Económico</div>
            <p>Reduce tus facturas de luz eligiendo la tarifa más económica según tu perfil de consumo.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-icon">🌍</div>
            <div class="card-title">Sostenibilidad</div>
            <p>Disminuye tu huella de carbono utilizando energía solar y optimizando tu consumo energético.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-icon">☀️</div>
            <div class="card-title">Independencia</div>
            <p>Genera tu propia energía y reduce la dependencia de compañías eléctricas con placas solares.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Cómo funciona - Metodología simplificada
    st.markdown("<h3>🔍 Cómo Funciona</h3>", unsafe_allow_html=True)
    
    # Metodología en pasos
    st.markdown("""
    <div class="step-box">
        <div class="step-number">1</div>
        <div>Recopilamos datos actualizados de tarifas eléctricas y eficiencia de placas solares.</div>
    </div>
    <div class="step-box">
        <div class="step-number">2</div>
        <div>Analizamos los datos para encontrar las opciones más eficientes y económicas.</div>
    </div>
    <div class="step-box">
        <div class="step-number">3</div>
        <div>Personalizamos las recomendaciones según tu consumo, ubicación y necesidades.</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Cómo usar la aplicación
    st.markdown("<h3>🚀 Cómo Usar la Aplicación</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">🔌 Para Tarifas Eléctricas</div>
            <ul>
                <li>Proporciona tu consumo mensual, o la app te calcula el promedio</li>
                <li>Indica tu potencia contratada actual</li>
                <li>Recibe recomendaciones de tarifas que mejor se ajusten a tu perfil</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">☀️ Para Placas Solares</div>
            <ul>
                <li>Indica el espacio disponible para instalación</li>
                <li>Proporciona tu ubicación para calcular las horas de sol</li>
                <li>Descubre qué placas solares maximizarán tu ahorro</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Llamada a la acción
    st.markdown("""
    <div class="highlight-section" style="text-align: center; margin-top: 30px;">
        <h3 style="color: #1e5799;">¡Comienza a ahorrar ahora!</h3>
        <p>Navega a las secciones de recomendadores usando el menú lateral para obtener tus recomendaciones personalizadas.</p>
    </div>
    """, unsafe_allow_html=True)

# Sección de Visualizaciones
elif seccion_seleccionada == "Visualizaciones":
    # CSS adicional para la sección de visualizaciones - Corrigiendo problemas de contraste
    st.markdown("""
    <style>
        /* Estilos para los selectores - asegurando contraste */
        .stSelectbox label {
            color: #333 !important; /* Color oscuro para el texto del label */
        }
        
        .stSelectbox div[data-baseweb="select"] span {
            color: #333 !important; /* Color oscuro para el texto seleccionado */
        }
        
        .stSelectbox div[data-baseweb="select"] {
            background-color: white !important; /* Fondo blanco para el selector */
            border: 1px solid #2989d8 !important; /* Borde para mejor visibilidad */
        }
        
        .stSelectbox div[data-baseweb="select"]:hover {
            border: 1px solid #1e5799 !important; /* Borde más oscuro al hover */
        }
        
        /* Estilos para los elementos del menú desplegable */
        div[role="listbox"] li {
            color: #333 !important; /* Color oscuro para opciones del menú */
        }
        
        div[role="listbox"] li:hover {
            background-color: #f0f7ff !important; /* Fondo claro al hover */
        }
        
        /* Estilos para categorías con botones en lugar de tarjetas */
        .category-button {
            display: inline-block;
            background-color: #f0f7ff;
            color: #333;
            border: 1px solid #2989d8;
            border-radius: 5px;
            padding: 10px 15px;
            margin-right: 10px;
            margin-bottom: 10px;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .category-button:hover {
            background-color: #2989d8;
            color: white;
        }
        
        .category-button.active {
            background-color: #2989d8;
            color: white;
            font-weight: bold;
        }
        
        /* Resto de los estilos... */
        .graph-container {
            background: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
            margin: 20px 0;
            border: 1px solid #eaeaea;
        }
        
        .graph-explanation {
            background: #f8f9fa;
            border-left: 4px solid #2989d8;
            padding: 15px;
            border-radius: 0 8px 8px 0;
            margin: 15px 0;
            color: #333;
        }
        
        .graph-category {
            display: inline-block;
            background: #2989d8;
            color: white;
            padding: 5px 10px;
            border-radius: 30px;
            font-size: 0.8em;
            margin-right: 10px;
            margin-bottom: 10px;
        }
        
        .vis-header {
            background: linear-gradient(135deg, #1e5799 0%, #207cca 51%, #2989d8 100%);
            color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    # Título con estilo
    #st.markdown('<div class="vis-header"><h2>📊 Visualizaciones Interactivas 📊</h2></div>', unsafe_allow_html=True)
    
    # Introducción
    st.markdown("""
    <div class="graph-explanation" style="background: #e8f4fc; border-left: 4px solid #2989d8;">
        <h3 style="color: #1e5799;">Explora Nuestros Datos</h3>
        <p>Descubre insights valiosos a través de nuestras visualizaciones interactivas. Estos gráficos te ayudarán a 
        entender mejor las tarifas eléctricas y la energía solar en diferentes contextos.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Categorizar los gráficos
    categorias = {
        "Tarifas Eléctricas": ["Punta por Empresa", "Punta por Tarifa", "Llano por Empresa", "Llano por Tarifa", 
                              "Valle por Empresa", "Valle por Tarifa", "Dashboard Tarifas", "Potencia por Empresas"],
        "Energía Solar": ["Top Sol Ciudades", "Bottom Sol Ciudades"]
    }
    
    # Selección de categoría con botones en lugar de tarjetas
    st.markdown('<h3 style="color: white;">Selecciona una Categoría</h3>', unsafe_allow_html=True)
    
    # Inicializar estado de sesión para categoría seleccionada
    if 'categoria_seleccionada' not in st.session_state:
        st.session_state.categoria_seleccionada = list(categorias.keys())[0]
    
    # Botones para seleccionar categoría
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Tarifas Eléctricas", key="btn_tarifas", 
                    help="Ver gráficos relacionados con tarifas eléctricas"):
            st.session_state.categoria_seleccionada = "Tarifas Eléctricas"
    
    with col2:
        if st.button("☀️ Energía Solar", key="btn_solar",
                    help="Ver gráficos relacionados con energía solar"):
            st.session_state.categoria_seleccionada = "Energía Solar"
    
    # Mostrar categoría seleccionada
    st.markdown(f"""
    <div style="padding: 10px; background-color: #f0f7ff; border-radius: 5px; margin: 10px 0; border-left: 4px solid #2989d8;">
        <p style="margin: 0; color: #333;"><b>Categoría seleccionada:</b> {st.session_state.categoria_seleccionada}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Selección de gráfico con un estilo mejorado
    st.subheader("Selecciona un Gráfico")

    # Primero añadir este estilo CSS específico para el selector
    st.markdown("""
    <style>
        /* Estilo específico para el label del selector de gráficos */
        [data-testid="stSelectbox"] label {
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)

    
    # Selector de gráfico con estilo corregido
    grafico_seleccionado = st.selectbox(
        "Elige un gráfico para visualizar:", 
        categorias[st.session_state.categoria_seleccionada],
        key="grafico_selector"
    )
    
    # Contenedor para el gráfico con estilo mejorado
    #st.markdown('<div class="graph-container" style="background-color: white; color: #333;">', unsafe_allow_html=True)
    
    # Categoría del gráfico como etiqueta
    st.markdown(f'<span class="graph-category">{st.session_state.categoria_seleccionada}</span>', unsafe_allow_html=True)
    
    # Título del gráfico seleccionado
    st.markdown(f'<h3 style="color: #1e5799; margin-top: 5px;">{grafico_seleccionado}</h3>', unsafe_allow_html=True)
    
    # Mostrar el gráfico seleccionado
    if grafico_seleccionado == "Punta por Empresa":
        st.image(os.path.join(current_dir, "punta_por_empresa.png"), use_container_width=True)
        explicacion = "Este gráfico muestra la tarifa de punta (P1) por empresa. La tarifa de punta se aplica durante las horas de mayor demanda de energía, generalmente durante el día."
    
    elif grafico_seleccionado == "Punta por Tarifa":
        st.image(os.path.join(current_dir, "punta_por_tarifa.png"), use_container_width=True)
        explicacion = "Este gráfico muestra la tarifa de punta (P1) por tarifa. Permite comparar las diferentes tarifas de punta disponibles en el mercado."
    
    elif grafico_seleccionado == "Llano por Empresa":
        st.image(os.path.join(current_dir, "llano_por_empresa.png"), use_container_width=True)
        explicacion = "Este gráfico muestra la tarifa de llano (P2) por empresa. La tarifa de llano se aplica durante las horas de demanda moderada de energía."
    
    elif grafico_seleccionado == "Llano por Tarifa":
        st.image(os.path.join(current_dir, "llano_por_tarifa.png"), use_container_width=True)
        explicacion = "Este gráfico muestra la tarifa de llano (P2) por tarifa. Permite comparar las diferentes tarifas de llano disponibles en el mercado."
    
    elif grafico_seleccionado == "Valle por Empresa":
        st.image(os.path.join(current_dir, "valle_por_empresa.png"), use_container_width=True)
        explicacion = "Este gráfico muestra la tarifa de valle (P3) por empresa. La tarifa de valle se aplica durante las horas de menor demanda de energía, generalmente durante la noche."
    
    elif grafico_seleccionado == "Valle por Tarifa":
        st.image(os.path.join(current_dir, "valle_por_tarifa.png"), use_container_width=True)
        explicacion = "Este gráfico muestra la tarifa de valle (P3) por tarifa. Permite comparar las diferentes tarifas de valle disponibles en el mercado."
    
    elif grafico_seleccionado == "Dashboard Tarifas":
        st.image(os.path.join(current_dir, "dashboard_tarifas.png"), use_container_width=True)
        explicacion = "Este dashboard muestra una visión general de las tarifas de luz, incluyendo las tarifas de punta, llano y valle por diferentes empresas y tarifas."
    
    elif grafico_seleccionado == "Potencia por Empresas":
        st.image(os.path.join(current_dir, "potencia_por_empresas.png"), use_container_width=True)
        explicacion = "Este gráfico muestra la potencia contratada por diferentes empresas. La potencia contratada es la cantidad de energía que una empresa puede suministrar a sus clientes."
    
    elif grafico_seleccionado == "Top Sol Ciudades":
        st.image(os.path.join(current_dir, "top_sol_ciudades.png"), use_container_width=True)
        explicacion = "Este gráfico muestra las ciudades con más horas de sol al año. Las horas de sol son un factor importante a considerar al instalar placas solares, ya que determinan la cantidad de energía que se puede generar."
    
    elif grafico_seleccionado == "Bottom Sol Ciudades":
        st.image(os.path.join(current_dir, "bottom_sol_ciudades.png"), use_container_width=True)
        explicacion = "Este gráfico muestra las ciudades con menos horas de sol al año. Esto te permite identificar las ciudades menos favorables para la instalación de placas solares."
    
    # Cerrar el contenedor del gráfico
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Explicación del gráfico
    st.markdown(f"""
    <div class="graph-explanation">
        <h3 style="color: #1e5799;">Explicación</h3>
        <p style="color: #333;">{explicacion}</p>
        <p style="color: #333;"><b>¿Por qué es importante?</b> Esta información te ayuda a tomar decisiones más informadas sobre tu consumo energético y posibles instalaciones solares.</p>
    </div>
    """, unsafe_allow_html=True)

# Sección de Recomendador
elif seccion_seleccionada == "Recomendador Tarifas Eléctricas":
    # CSS adicional para esta sección
    st.markdown("""
    <style>
        /* Header con gradiente */
        .recomendador-header {
            background: linear-gradient(135deg, #1e5799 0%, #207cca 51%, #2989d8 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        /* Tarjetas para las diferentes secciones */
        .form-section {
            background: white;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        /* Iconos de sección */
        .section-icon {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-align: center;
            color: #2989d8;
        }
        
        /* Títulos de sección */
        .section-title {
            color: #1e5799;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 15px;
            border-bottom: 2px solid #eaeaea;
            padding-bottom: 10px;
        }
        
        /* Notas informativas */
        .info-note {
            background: #f0f7ff;
            border-left: 4px solid #2989d8;
            padding: 15px;
            margin: 15px 0;
            border-radius: 0 5px 5px 0;
        }
        
        /* Pasos del proceso */
        .process-step {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }
        
        .step-number {
            background: #2989d8;
            color: white;
            width: 25px;
            height: 25px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 10px;
            font-weight: bold;
            font-size: 0.8rem;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header principal con iconos
    st.markdown("""
    <div class="recomendador-header">
        <h1>💡 Recomendador de Tarifas Eléctricas ⚡</h1>
        <p>Encuentra la tarifa que mejor se adapta a tus necesidades y ahorra en tu factura de luz</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Introducción en columnas para mejor presentación
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="form-section">
            <div class="section-title">¿Cómo funciona?</div>
            <div class="process-step">
                <div class="step-number">1</div>
                <div>Proporciónanos información sobre tu consumo eléctrico</div>
            </div>
            <div class="process-step">
                <div class="step-number">2</div>
                <div>Nuestro algoritmo analiza las mejores tarifas disponibles</div>
            </div>
            <div class="process-step">
                <div class="step-number">3</div>
                <div>Recibe recomendaciones personalizadas de tarifas</div>
            </div>
            <div class="process-step">
                <div class="step-number">4</div>
                <div>Compara y elige la opción que más te convenga</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="form-section" style="text-align: center;">
            <div class="section-icon">💰</div>
            <p style="font-size: 1.2rem; font-weight: 500; color: #1e5799;">Ahorra hasta un 30%</p>
            <p>en tu factura de luz eligiendo la tarifa correcta</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Nota informativa sobre datos necesarios
    st.markdown("""
    <div class="info-note">
        <p><strong>📝 Para obtener los mejores resultados</strong></p>
        <p>Necesitaremos algunos datos sobre tu consumo eléctrico. Si no conoces algún dato, te ayudaremos a estimarlo.</p>
    </div>
    """, unsafe_allow_html=True)

    # Función para cargar tarifas desde un archivo CSV

    import csv
    def cargar_tarifas():
        tarifas = []
        with open(os.path.join(current_dir, 'tarifas_nosolar.csv'), 'r') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            for fila in lector:
                tarifa = {
                    "compañia": fila['Empresa'],
                    "nombre": fila['Tarifa'],
                    "punta": float(fila['Punta']),
                    "llano": float(fila['Llano']),
                    "valle": float(fila['Valle']),
                    "P1": float(fila['P1']) if 'P1' in fila else 0,
                    "P3": float(fila['P3']) if 'P3' in fila else 0,
                    "batería": 0
                }
                tarifas.append(tarifa)
        return tarifas

    def obtener_incremento_por_habitante(num_personas):
        if num_personas == 1:
            return 1.0
        elif num_personas == 2:
            return 1.25
        elif num_personas == 3:
            return 1.45
        elif num_personas == 4:
            return 1.60
        else:
            return 1.60 + 0.1 * (num_personas - 4)

    # Función para ajustar el consumo en función del número de habitantes
    def ajustar_consumo_por_habitantes(consumo, num_personas):
        incremento = obtener_incremento_por_habitante(num_personas)
        return consumo * incremento

    # Diccionario de meses y días
    dias_por_mes = {
        "enero": 31, "febrero": 28, "marzo": 31, "abril": 30,
        "mayo": 31, "junio": 30, "julio": 31, "agosto": 31,
        "septiembre": 30, "octubre": 31, "noviembre": 30, "diciembre": 31
    }

    # Comparativa de tarifas
    def calcular_mejor_tarifa(datos_consumo, tarifas):
        mes = datos_consumo["mes"]
        if mes is None:
            st.error("El mes no ha sido proporcionado correctamente.")
            return
        dias = dias_por_mes.get(mes.lower(), 30)  # Usar 30 días si el mes es inválido o no está en el diccionario
        excedentes = 0
        potencia = datos_consumo['potencia']
        iva = 1.21
        bono_social = 0.006282
        impuesto = 3.8 / 100
        equipos = 0.82

        comparativa = []
        for empresa in tarifas:
            consumo_total = (empresa["punta"] * datos_consumo["punta"] +
                             empresa["llano"] * datos_consumo["llano"] +
                             empresa["valle"] * datos_consumo["valle"])
            potencia_total = potencia * dias * (empresa["P1"] + empresa["P3"])
            
            precionormal = ((potencia_total + bono_social * dias + consumo_total) * (1 + impuesto) +
                            equipos) * iva 
            
            calculado = {
                "Empresa": empresa["compañia"],
                "Tarifa": empresa["nombre"],
                "Precio": precionormal
            }
            comparativa.append(calculado)

        comparativa.sort(key=lambda x: x["Precio"])
        mejor_tarifa = comparativa[0]

        st.write("\nComparativa de tarifas:")
        for tarifa in comparativa:
            st.write(f"{tarifa['Empresa']} - {tarifa['Tarifa']}: {tarifa['Precio']:.2f} €")

        st.write(f"\nLa tarifa más económica es la de {mejor_tarifa['Empresa']} - {mejor_tarifa['Tarifa']} con un precio de {mejor_tarifa['Precio']:.2f} €.")

    # Formulario para ingresar datos del usuario
    st.header("Formulario de Consumo")
    num_personas = st.number_input("¿Cuántas personas viven en tu domicilio?", min_value=1, step=1)
    mes = st.selectbox("¿Para qué mes deseas hacer la comparativa?", list(dias_por_mes.keys()))
    conoce_consumo = st.radio("¿Conoces tu consumo en kWh para los periodos de Valle, Llano y Punta?", ('Sí', 'No'))

    if conoce_consumo == 'Sí':
        consumo_valle = st.number_input("Introduce tu consumo en kWh para el periodo Valle:", min_value=0.0, step=0.1)
        consumo_llano = st.number_input("Introduce tu consumo en kWh para el periodo Llano:", min_value=0.0, step=0.1)
        consumo_punta = st.number_input("Introduce tu consumo en kWh para el periodo Punta:", min_value=0.0, step=0.1)
        potencia = st.number_input("Introduce tu potencia en kW:", min_value=0.0, step=0.1)

        # Mostrar gráfico de franjas horarias
        discriminacion = {
            "00": 'valle', "01": 'valle', "02": 'valle', "03": 'valle',
            "04": 'valle', "05": 'valle', "06": 'valle', "07": 'valle',
            "08": 'llano', "09": 'llano', "10": 'punta', "11": 'punta',
            "12": 'punta', "13": 'punta', "14": 'llano', "15": 'llano',
            "16": 'llano', "17": 'llano', "18": 'punta', "19": 'punta',
            "20": 'punta', "21": 'punta', "22": 'llano', "23": 'llano',
        }

        # Crear un pie chart simulando las 24 horas de un reloj
        labels = list(discriminacion.keys())
        sizes = [1] * 24  # Cada hora tiene el mismo tamaño
        colors = ['#2ca02c' if discriminacion[hora] == 'valle' else '#ffdd44' if discriminacion[hora] == 'llano' else '#d62728' for hora in labels]

        fig, ax = plt.subplots(figsize=(6, 6))  # Ajustar el tamaño del gráfico
        ax.pie(sizes, labels=labels, colors=colors, startangle=90, counterclock=False)
        ax.axis('equal')  # Para asegurar que el pie chart es un círculo
        ax.set_title('Distribución de las Franjas Horarias', pad=20)  # Ajustar el padding del título

        # Añadir leyenda
        custom_lines = [plt.Line2D([0], [0], color='#2ca02c', lw=4),
                        plt.Line2D([0], [0], color='#ffdd44', lw=4),
                        plt.Line2D([0], [0], color='#d62728', lw=4)]
        ax.legend(custom_lines, ['Valle', 'Llano', 'Punta'], loc='upper right', bbox_to_anchor=(1.1, 1), fontsize='x-small')

        st.pyplot(fig)

        # Ajustar el consumo en función del número de habitantes
        consumo_valle = ajustar_consumo_por_habitantes(consumo_valle, num_personas)
        consumo_llano = ajustar_consumo_por_habitantes(consumo_llano, num_personas)
        consumo_punta = ajustar_consumo_por_habitantes(consumo_punta, num_personas)
        
        datos_consumo = {"valle": consumo_valle, "llano": consumo_llano, "punta": consumo_punta, "potencia": potencia,"mes": mes }

    elif conoce_consumo == 'No':
        consumo_estimado = 0
        electrodomesticos = {
            "Frigorífico": 1.2, "Lavadora": 0.9, "Lavavajillas": 0.85,
            "Televisor": 0.2, "Aire Acondicionado": 3.0, "Vitroceramica": 1.5,
            "Horno": 1.0, "Calefactores eléctricos": 2.0, "Microondas": 0.2,
            "Ordenador": 0.5, "Plancha de ropa": 0.3, "Algún otro electrodomestico": 0.5
        }
        
        st.write("Vamos a estimar tu consumo. Por favor, indica si tienes los siguientes electrodomésticos:")
        for electrodomestico, consumo in electrodomesticos.items():
            respuesta = st.radio(f"¿Tienes {electrodomestico}?", ('Sí', 'No'))
            if respuesta == 'Sí':
                consumo_estimado += consumo

        consumo_valle = consumo_estimado * 0.4 * 30
        consumo_llano = consumo_estimado * 0.3 * 30
        consumo_punta = consumo_estimado * 0.3 * 30
        potencia = st.number_input("Introduce tu potencia en kW:", min_value=0.0, step=0.1)

        # Ajuste del consumo basado en habitantes
        consumo_valle = ajustar_consumo_por_habitantes(consumo_valle, num_personas)
        consumo_llano = ajustar_consumo_por_habitantes(consumo_llano, num_personas)
        consumo_punta = ajustar_consumo_por_habitantes(consumo_punta, num_personas)

        st.write("\nEstimación de consumo:")
        st.write(f"Consumo estimado en Valle: {consumo_valle:.2f} kWh")
        st.write(f"Consumo estimado en Llano: {consumo_llano:.2f} kWh")
        st.write(f"Consumo estimado en Punta: {consumo_punta:.2f} kWh")

        datos_consumo = {"valle": consumo_valle, "llano": consumo_llano, "punta": consumo_punta, "potencia": potencia, "mes": mes }

    # Botón para calcular la mejor tarifa
    if st.button("Calcular Mejor Tarifa"):
        tarifas = cargar_tarifas()
        calcular_mejor_tarifa(datos_consumo, tarifas)


# Sección de Recomendador Solar
elif seccion_seleccionada == "Recomendador Placas Solares":
    st.header("Recomendador Placas Solares")

    st.write("""
    🌞 **¡Bienvenido al Recomendador de Placas Solares!** 🌞

    Por favor, complete el siguiente formulario para recibir recomendaciones personalizadas sobre la instalación de placas solares en su hogar. 💡🔋

    **¡Hagamos un mundo más sostenible juntos!** 🌍✨
    """)

    # Diccionario de meses y días
    dias_por_mes = {
    "enero": 31, "febrero": 28, "marzo": 31, "abril": 30,
    "mayo": 31, "junio": 30, "julio": 31, "agosto": 31,
    "septiembre": 30, "octubre": 31, "noviembre": 30, "diciembre": 31
    }

    # Función para obtener el incremento por habitante
    def obtener_incremento_por_habitante(num_personas):
        if num_personas == 1:
            return 1.0
        elif num_personas == 2:
            return 1.25
        elif num_personas == 3:
            return 1.45
        elif num_personas == 4:
            return 1.60
        else:
            return 1.60 + 0.1 * (num_personas - 4)

    # Función para ajustar el consumo en función del número de habitantes
    def ajustar_consumo_por_habitantes(consumo, num_personas):
        incremento = obtener_incremento_por_habitante(num_personas)
        return consumo * incremento

    # Formulario para ingresar datos del usuario
    st.header("Formulario de Consumo")
    mes = st.selectbox("¿Para qué mes deseas hacer la comparativa?", list(dias_por_mes.keys()))
    provincia = st.text_input("¿En qué provincia te encuentras?")
    num_personas = st.number_input("¿Cuántas personas viven en tu domicilio?", min_value=1, step=1)

    conoce_consumo = st.radio("¿Conoces tu consumo en kWh para los periodos de Valle, Llano y Punta?", ('Sí', 'No'))

    if conoce_consumo == 'Sí':
        consumo_valle = st.number_input("Introduce tu consumo en kWh para el periodo Valle:", min_value=0.0, step=0.1)
        consumo_llano = st.number_input("Introduce tu consumo en kWh para el periodo Llano:", min_value=0.0, step=0.1)
        consumo_punta = st.number_input("Introduce tu consumo en kWh para el periodo Punta:", min_value=0.0, step=0.1)
        potencia = st.number_input("Introduce tu potencia en kW:", min_value=0.0, step=0.1)

        # Ajustar el consumo en función del número de habitantes
        consumo_valle = ajustar_consumo_por_habitantes(consumo_valle, num_personas)
        consumo_llano = ajustar_consumo_por_habitantes(consumo_llano, num_personas)
        consumo_punta = ajustar_consumo_por_habitantes(consumo_punta, num_personas)
        
        datos_consumo = {"valle": consumo_valle, "llano": consumo_llano, "punta": consumo_punta, "potencia": potencia, "mes": mes}

    elif conoce_consumo == 'No':
        consumo_estimado = 0
        electrodomesticos = {
            "Frigorífico": 1.2, "Lavadora": 0.9, "Lavavajillas": 0.85,
            "Televisor": 0.2, "Aire Acondicionado": 3.0, "Vitroceramica": 1.5,
            "Horno": 1.0, "Calefactores eléctricos": 2.0, "Microondas": 0.2,
            "Ordenador": 0.5, "Plancha de ropa": 0.3, "Algún otro electrodomestico": 0.5
        }
        
        st.write("Vamos a estimar tu consumo. Por favor, indica si tienes los siguientes electrodomésticos:")
        for electrodomestico, consumo in electrodomesticos.items():
            respuesta = st.radio(f"¿Tienes {electrodomestico}?", ('Sí', 'No'))
            if respuesta == 'Sí':
                consumo_estimado += consumo

        consumo_valle = consumo_estimado * 0.4 * 30
        consumo_llano = consumo_estimado * 0.3 * 30
        consumo_punta = consumo_estimado * 0.3 * 30
        potencia = st.number_input("Introduce tu potencia en kW:", min_value=0.0, step=0.1)

        # Ajuste del consumo basado en habitantes
        consumo_valle = ajustar_consumo_por_habitantes(consumo_valle, num_personas)
        consumo_llano = ajustar_consumo_por_habitantes(consumo_llano, num_personas)
        consumo_punta = ajustar_consumo_por_habitantes(consumo_punta, num_personas)

        st.write("\nEstimación de consumo:")
        st.write(f"Consumo estimado en Valle: {consumo_valle:.2f} kWh")
        st.write(f"Consumo estimado en Llano: {consumo_llano:.2f} kWh")
        st.write(f"Consumo estimado en Punta: {consumo_punta:.2f} kWh")

        datos_consumo = {"valle": consumo_valle, "llano": consumo_llano, "punta": consumo_punta, "potencia": potencia, "mes": mes}

    # Cálculo de placas solares
    if st.button("Calcular Placas Solares"):

        # Función para prorratear el consumo
        def prorrateo_consumo(mesecito, consumito):
            mes = {
                'enero': 'Ene', 'febrero': 'Feb', 'marzo': 'Mar', 'abril': 'Apr', 'mayo': 'May', 'junio': 'Jun',
                'julio': 'Jul', 'agosto': 'Aug', 'septiembre': 'Sep', 'octubre': 'Oct', 'noviembre': 'Nov', 'diciembre': 'Dec'
            }
            month = mes[mesecito.lower()]

            # Definimos los períodos para un día laborable
            discriminacion = {
                "00": 'valle', "01": 'valle', "02": 'valle', "03": 'valle',
                "04": 'valle', "05": 'valle', "06": 'valle', "07": 'valle',
                "08": 'llano', "09": 'llano', "10": 'punta', "11": 'punta',
                "12": 'punta', "13": 'punta', "14": 'llano', "15": 'llano',
                "16": 'llano', "17": 'llano', "18": 'punta', "19": 'punta',
                "20": 'punta', "21": 'punta', "22": 'llano', "23": 'llano',
            }
            # Calcula horas diarias por tipo para días laborables
            horas_llano_lab = sum(1 for h in discriminacion if discriminacion[h] == 'llano')
            horas_punta_lab = sum(1 for h in discriminacion if discriminacion[h] == 'punta')

            # Obtén el número total de días en el mes
            dias = {
            'enero': 31, 'febrero': 29, 'marzo': 31, 'abril': 30, 'mayo': 31, 'junio': 30,
            'julio': 31, 'agosto': 31, 'septiembre': 30, 'octubre': 31, 'noviembre': 30, 'diciembre': 31
            }
            num_dias_mes = dias[mesecito]

            # Asumimos que hay 8 fines de semana en cada mes (4 semanas completas)
            dias_finde = 8
            dias_laborables = num_dias_mes - dias_finde
            # Calcular horas totales para ese mes
            horas_llano_totales = horas_llano_lab * dias_laborables
            horas_punta_totales = horas_punta_lab * dias_laborables
            # Calculamos los consumos prorrateados, obviando la diferencia de laborable o no
            c_p = consumito[0] * 8 / horas_punta_totales
            c_l = consumito[1] * 8 / horas_llano_totales
            c_v = (sum(consumito) - c_p * num_dias_mes - c_l * num_dias_mes) / num_dias_mes
            c_totales = [c_p * num_dias_mes, c_l * num_dias_mes, c_v * num_dias_mes]
            return c_totales

        # Función para leer datos horarios por provincia
        def leer_datos_horarios(ciudad):    
            
            # Obtener la ruta absoluta del directorio actual
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "datos_provincias.csv")

            try:
                df = pd.read_csv(file_path)
            except FileNotFoundError:
                st.error(f"El archivo no se encuentra en la ruta especificada: {file_path}")
                return None
            except Exception as e:
                st.error(f"Ocurrió un error al intentar leer el archivo: {e}")
                return None

            df.columns = ['Dia', 'Ciudad', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto',
            'septiembre', 'octubre', 'noviembre', 'diciembre']
            
            df["Ciudad"] = df["Ciudad"].str.lower()
            nuevo_df = df[df['Ciudad'] == ciudad.lower()]

            return nuevo_df

        # Prorrateamos el consumo para el mes
        consumo_total = prorrateo_consumo(mes, [datos_consumo["valle"], datos_consumo["llano"], datos_consumo["punta"]])

        # Sacamos los datos de la ciudad especificada
        df_ciudad = leer_datos_horarios(provincia)

        factor_solar = 0.8  # Durante el ocaso y el amanecer, las horas de sol no son tan efectivas, por lo que se introduce este factor para ser conservativos en el cálculo
        pot_placa = 0.455  # kWp
        dias = {
            'enero': 31, 'febrero': 29, 'marzo': 31, 'abril': 30, 'mayo': 31, 'junio': 30,
            'julio': 31, 'agosto': 31, 'septiembre': 30, 'octubre': 31, 'noviembre': 30, 'diciembre': 31
            }

        # Crear el diccionario para almacenar las sumas mensuales
        meses = df_ciudad.columns.difference(['Dia', 'Ciudad'])
        horas_sol = {mes: df_ciudad[mes].sum() * factor_solar for mes in meses}
        porcen_sol = {mes: round(df_ciudad[mes].sum() * factor_solar / (dias[mes] * 24), 2) for mes in meses}
        # Aproximadamente entre el 40% y el 50% de luz al día. 

        # Convertir el mes a la abreviatura correspondiente
        mes_abreviado = {
            'enero': 'Ene', 'febrero': 'Feb', 'marzo': 'Mar', 'abril': 'Apr', 'mayo': 'May', 'junio': 'Jun',
            'julio': 'Jul', 'agosto': 'Aug', 'septiembre': 'Sep', 'octubre': 'Oct', 'noviembre': 'Nov', 'diciembre': 'Dec'
        }[mes.lower()]

        # El consumo anual de energía por parte del consumidor debe ser igual o mayor al 80 % de la energía anual generada por la instalación.
        c_total = sum(consumo_total)
        n_placas = int(c_total / (pot_placa * 0.7 * horas_sol[mes] * 0.8))
        if n_placas < 2:
            st.write('''Tu consumo es muy bajo para poder beneficiarte de una instalación de placas solares.
                ¡Gracias por ser un consumidor eficiente!''')
        else:
            st.write(f'Con los datos de consumo suministrados, ¡Te podría interesar instalar hasta {n_placas} placas!')
            st.write('''Ten en cuenta que la mejor estimación del número de placas se realiza con el consumo en verano, 
                además de ser donde te beneficiarás del mayor ahorro.''')
            
            # AHORRO PLACAS
            e_generada = n_placas * pot_placa * 0.7 * horas_sol[mes]

            # La energia generada no afecta al periodo valle y sólo afecta al 50% del periodo llano:
            datos_consumo = {
                'Punta': max(0, consumo_total[0] - e_generada * 2 / 3),
                'Llano': max(0, consumo_total[1] - e_generada * 1 / 3),
                'Valle': consumo_total[2],
                'Excedentes': min(0, consumo_total[0] - e_generada * 2 / 3) + min(0, consumo_total[1] - e_generada * 1 / 3),
                'Dias': dias[mes],
                'Potencia': potencia
            }

            # TARIFA SOLAR
            # Una vez conocidos los consumos con las placas, obtenemos el precio con las tarifas solares:
            #df_solar = pd.read_csv("tarifas_solar.csv")

            def calcular_mejor_tarifa(consumo):
                # Parámetros
                iva = 1.21
                bono_social = 0.006282
                impuesto = 3.8 / 100
                equipos = 0.82

                #df = pd.read_csv("tarifas_solar.csv")
                #df_solar = pd.read_csv("/mount/src/data-wrangling-project/streamlit_app/tarifas_solar.csv")

                # Obtener la ruta absoluta del directorio actual
                current_dir = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(current_dir, "tarifas_solar.csv")

                try:
                    df_solar = pd.read_csv(file_path)
                except FileNotFoundError:
                    st.error(f"El archivo no se encuentra en la ruta especificada: {file_path}")
                except Exception as e:
                    st.error(f"Ocurrió un error al intentar leer el archivo: {e}")

                # Crear un DataFrame con los resultados
                resultado_df = df_solar[['Empresa', 'Tarifa']].copy()
                
                consumo_total = (df_solar['Punta'] * consumo['Punta'] +
                                df_solar['Llano'] * consumo['Llano'] +
                                df_solar['Valle'] * consumo['Valle'])
                resultado_df['Consumo'] = consumo_total
                excedentes_total = df_solar['Excedentes'] * consumo['Excedentes']
                resultado_df['Excedentes'] = excedentes_total
                potencia_total = (df_solar['P1'] + df_solar['P3']) * consumo['Potencia'] * consumo['Dias']
                resultado_df['Potencia'] = potencia_total
                precio_bat = ((potencia_total + bono_social * consumo['Dias'] + consumo_total) * (1 + impuesto) +
                            equipos + df_solar["Bateria"] * consumo['Dias'] / 30) * iva + excedentes_total
                resultado_df['Precio con Bateria'] = precio_bat
                consumo_total_nobat = (consumo_total + excedentes_total).clip(lower=0)
                precio_nobat = ((potencia_total + bono_social * consumo['Dias'] + consumo_total_nobat) * (1 + impuesto) +
                                equipos) * iva
                resultado_df['Precio sin Bateria'] = precio_nobat

                # Crear columna precio con las condiciones reales de cada compañía
                resultado_df['Precio'] = resultado_df.apply(
                    lambda row: row['Precio sin Bateria'] if row['Empresa'] == 'Naturgy' else row['Precio con Bateria'], axis=1)
                
                df_sorted = resultado_df.sort_values(by='Precio', ascending=True)
                mejor_tarifa = df_sorted.iloc[0]


                st.write("\nComparativa de tarifas:")
                for _, tarifa in df_sorted.iterrows():  # Usamos iterrows para iterar sobre las filas
                    st.write(f"{tarifa['Empresa']} - {tarifa['Tarifa']}: {tarifa['Precio']:.2f} €")

                st.write(f"\nLa tarifa más económica es la de {mejor_tarifa['Empresa']} - {mejor_tarifa['Tarifa']} con un precio de {mejor_tarifa['Precio']:.2f} €.")

                return mejor_tarifa

            # Llamar a la función 
            tarifas = calcular_mejor_tarifa(datos_consumo)
            st.write(tarifas)
        

        

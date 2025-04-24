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

# Estilos personalizados globales
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
    
    .banner h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .banner p {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    /* Estilos para las secciones */
    .section-header {
        border-left: 4px solid #2989d8;
        padding-left: 10px;
        margin: 2rem 0 1rem 0;
    }
    
    /* Estilos para el sidebar */
    .sidebar .sidebar-content {
        background-image: linear-gradient(180deg, #2e7bcf 0%, #154277 100%);
        color: white;
    }
    
    [data-testid=stSidebar] [data-testid=stImage]{
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Banner personalizado en lugar de imagen
st.markdown("""
<div class="banner">
    <h1>⚡ Recomendador de Tarifas de Luz y Placas Solares ☀️</h1>
    <p>Ahorra energía y dinero con recomendaciones personalizadas basadas en tus necesidades</p>
</div>
""", unsafe_allow_html=True)

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Añadir una imagen en la parte superior del menú de navegación
st.sidebar.image(os.path.join(current_dir, "octocat.jpg"), use_container_width=True)

# Menú de navegación mejorado
st.sidebar.markdown("# 🌟 Navegación")
st.sidebar.markdown("---")

# Opciones de navegación con iconos
opciones = {
    "🏠 Inicio": "Introducción",
    "🎯 Objetivos": "Objetivos",
    "📊 Metodología": "Metodología",
    "📈 Visualizaciones": "Visualizaciones",
    "💡 Tarifas Eléctricas": "Recomendador Tarifas Eléctricas",
    "☀️ Placas Solares": "Recomendador Placas Solares"
}

seccion = st.sidebar.radio("", list(opciones.keys()), key="nav")
seccion_seleccionada = opciones[seccion]

# Información adicional en el sidebar
st.sidebar.markdown("---")
st.sidebar.info("Desarrollado con ❤️ usando Streamlit")

# Sección de Introducción
if seccion_seleccionada == "Introducción":
    st.header("Introducción")
    st.write("""
    🌞 **Bienvenido al Recomendador de Tarifas de Luz y Placas Solares** 🌞

    En este proyecto, hemos desarrollado una aplicación web innovadora que recomienda tarifas de luz y placas solares basadas en los datos ingresados por el usuario. La aplicación utiliza datos actualizados de tarifas de luz y eficiencia de placas solares para proporcionar recomendaciones personalizadas que pueden ayudar a los usuarios a ahorrar en sus facturas de electricidad y a aprovechar la energía solar de manera eficiente. 💡🔋

    **¿Por qué es importante el ahorro energético?** 🌍

    El ahorro energético no solo tiene beneficios económicos, sino que también contribuye significativamente a la sostenibilidad del medio ambiente. Al reducir el consumo de energía y utilizar fuentes de energía renovable como la solar, podemos disminuir nuestra huella de carbono y ayudar a combatir el cambio climático. 🌱🌞

    **Beneficios del ahorro energético:**
    - **Ahorro económico:** Reducir el consumo de energía puede resultar en ahorros significativos en las facturas de electricidad. Esto libera recursos financieros que pueden ser utilizados para otras necesidades. 💰
    - **Sostenibilidad ambiental:** Utilizar energía renovable como la solar ayuda a reducir la dependencia de combustibles fósiles y disminuye las emisiones de gases de efecto invernadero. 🌍
    - **Independencia energética:** La instalación de placas solares permite a los usuarios generar su propia energía, reduciendo la dependencia de las compañías eléctricas y aumentando la resiliencia ante posibles fluctuaciones en los precios de la energía. ☀️🔋
    - **Innovación y tecnología:** Este proyecto fomenta el uso de tecnologías avanzadas como el web scraping, el análisis de datos y la visualización interactiva para proporcionar recomendaciones precisas y útiles. 🚀💡

    **¿Cómo funciona nuestra aplicación?** 🛠️

    Esta aplicación está diseñada para ser fácil de usar y accesible para todos. Simplemente ingrese sus datos en el formulario y obtenga recomendaciones personalizadas en cuestión de segundos. 🚀📊

    **Pasos para utilizar la aplicación:**
    1. **Ingrese sus datos:** Proporcione información sobre su consumo mensual de electricidad, la potencia contratada, las horas de sol disponibles y la superficie disponible para la instalación de placas solares.
    2. **Obtenga recomendaciones:** La aplicación analizará los datos ingresados y proporcionará recomendaciones personalizadas de tarifas de luz y placas solares.
    3. **Tome decisiones informadas:** Utilice las recomendaciones proporcionadas para elegir la tarifa de luz más adecuada y optimizar el uso de energía solar en su hogar.

    **Compromiso con la sostenibilidad:**

    Al utilizar esta aplicación, no solo está tomando decisiones informadas para ahorrar en sus facturas de electricidad, sino que también está contribuyendo a un futuro más sostenible. 🌱🔋

    ¡Gracias por utilizar nuestra aplicación y por su compromiso con el ahorro energético y la sostenibilidad ambiental! 🌍💡
    """)

# Sección de Objetivos
elif seccion_seleccionada == "Objetivos":
    st.header("Objetivos")
    st.write("""
    🎯 **Objetivos del Proyecto** 🎯

    Los objetivos principales de este proyecto son:

    1. **Proporcionar recomendaciones personalizadas de tarifas de luz**:
       - Analizar las tarifas de luz disponibles y recomendar la mejor opción basada en el consumo mensual y la potencia contratada del usuario. 💡
       - Ayudar a los usuarios a reducir sus facturas de electricidad eligiendo la tarifa más económica. 💰
       - Facilitar el acceso a información clara y precisa sobre las diferentes tarifas de luz disponibles en el mercado. 📊

    2. **Proporcionar recomendaciones personalizadas de placas solares**:
       - Evaluar la eficiencia de diferentes placas solares y recomendar la mejor opción basada en las horas de sol disponibles y la superficie disponible para la instalación. ☀️
       - Promover el uso de energía solar como una fuente de energía renovable y sostenible. 🌱
       - Ayudar a los usuarios a entender los beneficios económicos y ambientales de la instalación de placas solares. 🌍

    3. **Visualizar datos relevantes sobre tarifas de luz y energía solar**:
       - Crear gráficos y visualizaciones que faciliten la comprensión de los datos y las recomendaciones. 📊
       - Mostrar comparativas de tarifas y eficiencia de placas solares para ayudar a los usuarios a tomar decisiones informadas. 📈
       - Proporcionar herramientas interactivas que permitan a los usuarios explorar diferentes escenarios y opciones. 🛠️
    """)

# Sección de Metodología
elif seccion_seleccionada == "Metodología":
    st.header("🛠️ Metodología del Proyecto 🛠️")
    st.write("""
    En este proyecto, hemos seguido una metodología estructurada para garantizar la precisión y la utilidad de nuestras recomendaciones. A continuación, se detallan los pasos clave que hemos seguido:

    1. **Recopilación de Datos** 🌐:
       - Recopilamos datos de tarifas de luz de diferentes proveedores y datos de eficiencia de placas solares. 📊
       - Utilizamos técnicas de web scraping para obtener datos actualizados de las páginas web de los proveedores de energía. 🕸️🔍
       - Los datos incluyen información sobre precios de energía, precios de potencia, eficiencia de placas solares, y más. 💡

    2. **Análisis de Datos** 📈:
       - Analizamos los datos recopilados para identificar las mejores opciones de tarifas de luz y placas solares. 🔍
       - Utilizamos técnicas de análisis de datos para calcular los costos estimados y la energía generada por las placas solares. 💡

    3. **Desarrollo de la Aplicación Web** 💻:
       - Desarrollamos una aplicación web utilizando Streamlit para proporcionar una interfaz fácil de usar. 🚀
       - La aplicación permite a los usuarios ingresar sus datos y obtener recomendaciones personalizadas en tiempo real. ⏱️

    4. **Visualización de Datos** 👁️:
       - Creamos gráficos y visualizaciones utilizando Seaborn y Matplotlib para mostrar comparativas de tarifas y eficiencia de placas solares. 📊
       - Las visualizaciones ayudan a los usuarios a comprender mejor los datos y las recomendaciones proporcionadas. 📈

    5. **Validación y Pruebas** ✅:
       - Probamos la aplicación con diferentes conjuntos de datos para asegurarnos de que las recomendaciones sean precisas y útiles. 🔧
       - Realizamos ajustes y mejoras basadas en los comentarios de los usuarios y los resultados de las pruebas. 🛠️

    Al seguir esta metodología, hemos creado una herramienta poderosa que puede ayudar a los usuarios a tomar decisiones informadas sobre sus tarifas de luz y el uso de energía solar. 🌞🔋
    """)

# Sección de Visualizaciones
elif seccion_seleccionada == "Visualizaciones":
    st.header("📊 Visualizaciones 📊")
    st.write("""
    Bienvenido a la sección de visualizaciones. Aquí podrás explorar diferentes gráficos que te ayudarán a entender mejor los datos relacionados con las tarifas de luz y la energía solar. 📈📉

    Selecciona el gráfico que deseas ver a continuación y obtén una visión detallada de la información. ¡Esperamos que estas visualizaciones te sean útiles para tomar decisiones informadas! 💡🔍
    """)

    # Menú de selección de gráficos
    grafico_seleccionado = st.selectbox("Seleccione un gráfico", [
        "Punta por Empresa", 
        "Punta por Tarifa", 
        "Llano por Empresa", 
        "Llano por Tarifa", 
        "Valle por Empresa", 
        "Valle por Tarifa", 
        "Dashboard Tarifas", 
        "Potencia por Empresas", 
        "Top Sol Ciudades", 
        "Bottom Sol Ciudades"
    ])

    # Mostrar el gráfico seleccionado y su explicación
    if grafico_seleccionado == "Punta por Empresa":
        st.image(os.path.join(current_dir, "punta_por_empresa.png"), caption="Punta por Empresa", use_container_width=True)
        st.write("Este gráfico muestra la tarifa de punta (P1) por empresa. La tarifa de punta se aplica durante las horas de mayor demanda de energía, generalmente durante el día. Este gráfico permite comparar las tarifas de punta ofrecidas por diferentes empresas.")

    elif grafico_seleccionado == "Punta por Tarifa":
        st.image(os.path.join(current_dir, "punta_por_tarifa.png"), caption="Punta por Tarifa", use_container_width=True)
        st.write("Este gráfico muestra la tarifa de punta (P1) por tarifa. La tarifa de punta se aplica durante las horas de mayor demanda de energía. Este gráfico permite comparar las diferentes tarifas de punta disponibles en el mercado.")

    elif grafico_seleccionado == "Llano por Empresa":
        st.image(os.path.join(current_dir, "llano_por_empresa.png"), caption="Llano por Empresa", use_container_width=True)
        st.write("Este gráfico muestra la tarifa de llano (P2) por empresa. La tarifa de llano se aplica durante las horas de demanda moderada de energía. Este gráfico permite comparar las tarifas de llano ofrecidas por diferentes empresas.")

    elif grafico_seleccionado == "Llano por Tarifa":
        st.image(os.path.join(current_dir, "llano_por_tarifa.png"), caption="Llano por Tarifa", use_container_width=True)
        st.write("Este gráfico muestra la tarifa de llano (P2) por tarifa. La tarifa de llano se aplica durante las horas de demanda moderada de energía. Este gráfico permite comparar las diferentes tarifas de llano disponibles en el mercado.")

    elif grafico_seleccionado == "Valle por Empresa":
        st.image(os.path.join(current_dir, "valle_por_empresa.png"), caption="Valle por Empresa", use_container_width=True)
        st.write("Este gráfico muestra la tarifa de valle (P3) por empresa. La tarifa de valle se aplica durante las horas de menor demanda de energía, generalmente durante la noche. Este gráfico permite comparar las tarifas de valle ofrecidas por diferentes empresas.")

    elif grafico_seleccionado == "Valle por Tarifa":
        st.image(os.path.join(current_dir, "valle_por_tarifa.png"), caption="Valle por Tarifa", use_container_width=True)
        st.write("Este gráfico muestra la tarifa de valle (P3) por tarifa. La tarifa de valle se aplica durante las horas de menor demanda de energía. Este gráfico permite comparar las diferentes tarifas de valle disponibles en el mercado.")

    elif grafico_seleccionado == "Dashboard Tarifas":
        st.image(os.path.join(current_dir, "dashboard_tarifas.png"), caption="Dashboard Tarifas", use_container_width=True)
        st.write("Este dashboard muestra una visión general de las tarifas de luz, incluyendo las tarifas de punta, llano y valle por diferentes empresas y tarifas. Permite una comparación rápida y visual de las diferentes opciones disponibles en el mercado.")

    elif grafico_seleccionado == "Potencia por Empresas":
        st.image(os.path.join(current_dir, "potencia_por_empresas.png"), caption="Potencia por Empresas", use_container_width=True)
        st.write("Este gráfico muestra la potencia contratada por diferentes empresas. La potencia contratada es la cantidad de energía que una empresa puede suministrar a sus clientes. Este gráfico permite comparar la capacidad de suministro de energía de diferentes empresas.")

    elif grafico_seleccionado == "Top Sol Ciudades":
        st.image(os.path.join(current_dir, "top_sol_ciudades.png"), caption="Top Sol Ciudades", use_container_width=True)
        st.write("Este gráfico muestra las ciudades con más horas de sol al año. Las horas de sol son un factor importante a considerar al instalar placas solares, ya que determinan la cantidad de energía que se puede generar. Este gráfico permite identificar las mejores ciudades para la instalación de placas solares.")

    elif grafico_seleccionado == "Bottom Sol Ciudades":
        st.image(os.path.join(current_dir, "bottom_sol_ciudades.png"), caption="Bottom Sol Ciudades", use_container_width=True)
        st.write("Este gráfico muestra las ciudades con menos horas de sol al año. Las horas de sol son un factor importante a considerar al instalar placas solares. Este gráfico permite identificar las ciudades menos favorables para la instalación de placas solares.")

# Sección de Recomendador
elif seccion_seleccionada == "Recomendador Tarifas Eléctricas":
    st.header("Recomendador Tarifas Eléctricas")

    st.write("""
    🌞 **¡Bienvenido al Recomendador de Tarifas de Luz y Placas Solares!** 🌞

    Por favor, complete el siguiente formulario para recibir recomendaciones personalizadas que le ayudarán a ahorrar en su factura de electricidad y a aprovechar la energía solar de manera eficiente. 💡🔋

    **¡Hagamos un mundo más sostenible juntos!** 🌍✨
    """)

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
        

        

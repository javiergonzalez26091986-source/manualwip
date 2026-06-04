import streamlit as st

# 1. Configuración principal de la página
st.set_page_config(
    page_title="Manual Interactivo Wip", 
    page_icon="📦", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inyección de CSS para estética profesional
st.markdown("""
<style>
    .main-title { font-size: 2.8rem; color: #1E3A8A; font-weight: 800; margin-bottom: 0px;}
    .sub-title { font-size: 1.2rem; color: #64748B; margin-bottom: 30px;}
    .section-header { font-size: 1.8rem; color: #0284C7; border-bottom: 2px solid #E2E8F0; padding-bottom: 10px; margin-top: 20px;}
    .highlight-card { background-color: #F8FAFC; padding: 20px; border-radius: 10px; border-left: 6px solid #0EA5E9; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
</style>
""", unsafe_allow_html=True)

# 3. Encabezado Principal
st.markdown('<p class="main-title">Manual Operativo Dinámico: Plataforma Wip</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Gestión y Coordinación de Mensajería - Constructora Bolívar</p>', unsafe_allow_html=True)

# 4. Menú de Navegación Lateral
st.sidebar.title("Navegación del Manual")
menu = st.sidebar.radio(
    "Selecciona un módulo:",
    ["1. Inicio y Políticas (ANS)", "2. Flujo Operativo", "3. Paso a Paso en Wip", "4. Videotutorial"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip de uso:** Navega por los menús para entender cada etapa del proceso de mensajería corporativa.")

# --- MÓDULO 1: INICIO Y POLÍTICAS ---
if menu == "1. Inicio y Políticas (ANS)":
    st.markdown('<p class="section-header">1. Introducción al Servicio</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="highlight-card">
    Esta plataforma interactiva documenta el proceso estandarizado de recepción, coordinación y ejecución de mensajería a través de la herramienta <b>Wip</b>. El objetivo es garantizar la trazabilidad de las solicitudes desde los funcionarios hasta los mensajeros a nivel nacional.
    </div>
    <br>
    """, unsafe_allow_html=True)
    
    st.subheader("📋 Acuerdos de Nivel de Servicio (ANS)")
    st.write("Aquí se detallarán las políticas operativas:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("**Tiempos de Respuesta**")
        st.write("* Peticiones Normales: [Insertar tiempo]*")
        st.write("* Peticiones Urgentes: [Insertar tiempo]*")
    with col2:
        st.warning("**Cobertura Nacional**")
        st.write("* Bogotá, Cali, Barranquilla, Santa Marta, Cartagena, Ibagué, Manizales.*")

# --- MÓDULO 2: FLUJO OPERATIVO ---
elif menu == "2. Flujo Operativo":
    st.markdown('<p class="section-header">2. Modelo de Operación Centralizada</p>', unsafe_allow_html=True)
    st.write("El ecosistema de la aplicación Wip funciona mediante la interacción de tres actores principales:")
    
    st.write("") # Espaciador
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.info("🏢 **1. Usuario (Funcionario Bolívar)**")
        st.write("Detecta la necesidad de envío/recolección e ingresa la solicitud directamente en la interfaz de Wip.")
    with c2:
        st.error("👨‍💻 **2. Coordinador de Operaciones**")
        st.write("Recibe todas las alertas del sistema. Filtra, audita la información y distribuye la ruta de acuerdo con la ciudad y disponibilidad.")
    with c3:
        st.success("🛵 **3. Mensajero**")
        st.write("Recibe la instrucción filtrada por el coordinador, ejecuta el servicio en calle y reporta la novedad para el cierre.")

# --- MÓDULO 3: PASO A PASO EN WIP ---
elif menu == "3. Paso a Paso en Wip":
    st.markdown('<p class="section-header">3. Procedimiento en Plataforma</p>', unsafe_allow_html=True)
    st.write("Selecciona la fase del proceso para visualizar las instrucciones detalladas y capturas de pantalla:")
    
    etapa = st.selectbox("Fase Operativa:", ["1. Creación de Solicitud (Usuario)", "2. Asignación de Ruta (Coordinador)", "3. Cierre de Servicio"])
    
    if etapa == "1. Creación de Solicitud (Usuario)":
        st.write("### Radicación de un nuevo servicio")
        st.write("**Paso 1:** Ingresar a [wiptool.com](https://wiptool.com/) con las credenciales corporativas.")
        st.write("**Paso 2:** Navegar a la pestaña 'Nueva Solicitud'.")
        st.write("**Paso 3:** Llenar los campos obligatorios: Dirección de origen, destino y centro de costos.")
        st.caption("📸 *(Aquí insertaremos la captura de pantalla de la plataforma real)*")
        
    elif etapa == "2. Asignación de Ruta (Coordinador)":
        st.write("### Gestión del Coordinador")
        st.write("**Paso 1:** Revisar la bandeja de entrada de Wip.")
        st.write("**Paso 2:** Validar los datos de la solicitud.")
        st.write("**Paso 3:** Asignar al mensajero correspondiente en la zona (Ej. Zona Norte Bogotá).")
        st.caption("📸 *(Aquí insertaremos la vista del coordinador en Wip)*")
        
    else:
        st.write("### Confirmación y Cierre")
        st.write("**Paso 1:** El mensajero confirma la entrega.")
        st.write("**Paso 2:** El coordinador cambia el estado del ticket en Wip a 'Cerrado'.")

# --- MÓDULO 4: VIDEOTUTORIAL ---
elif menu == "4. Videotutorial":
    st.markdown('<p class="section-header">4. Material Audiovisual</p>', unsafe_allow_html=True)
    st.write("En esta sección integraremos el video de inducción general para que cualquier usuario nuevo entienda la dinámica de la plataforma en pocos minutos.")
    
    # Marcador de posición para el video
    st.info("🎥 El video se integrará aquí una vez esté grabado.")
    # st.video("ruta_del_video.mp4") # Descomentar cuando tengas el video

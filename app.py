import streamlit as st

# 1. Configuración principal de la página (Ícono de pestaña configurado)
st.set_page_config(
    page_title="Manual Interactivo Wip - SERGEM", 
    page_icon="sergemLogo.ico", # <- Archivo .ico asignado como favicon de la pestaña
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inyección de CSS y FontAwesome (Íconos profesionales)
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
    .main-title { font-size: 2.4rem; color: #1E3A8A; font-weight: 800; margin-bottom: 0px; margin-top: 10px;}
    .sub-title { font-size: 1.1rem; color: #64748B; margin-bottom: 30px;}
    .section-header { font-size: 1.6rem; color: #0284C7; border-bottom: 2px solid #E2E8F0; padding-bottom: 10px; margin-top: 20px; margin-bottom: 20px;}
    .highlight-card { background-color: #F8FAFC; color: #0F172A; padding: 20px; border-radius: 8px; border-left: 5px solid #0EA5E9; box-shadow: 0 2px 4px rgb(0 0 0 / 0.05); }
    .icon-prof { color: #0284C7; margin-right: 10px; }
</style>
""", unsafe_allow_html=True)

# 3. Encabezado en el cuerpo con los tres logotipos alineados
col_logo1, col_logo2, col_logo3 = st.columns([1, 1, 1])
with col_logo1:
    try:
        st.image("wipLogo.png", width=120)
    except:
        st.caption("[Logo WIP]")
with col_logo2:
    try:
        st.image("sergemLogo.png", width=130) # <- Logo de SERGEM en el cuerpo de la app
    except:
        st.caption("[Logo SERGEM]")
with col_logo3:
    try:
        st.image("constructoraBolivarLogo.png", width=140)
    except:
        st.caption("[Logo Bolívar]")

st.markdown('<p class="main-title">Manual Operativo Dinámico</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Gestión y Coordinación de Mensajería Wip - Operación Nacional</p>', unsafe_allow_html=True)

# 4. Buscador Rápido (Sidebar)
st.sidebar.markdown("### <i class='fas fa-search icon-prof'></i> Búsqueda Rápida", unsafe_allow_html=True)
busqueda = st.sidebar.text_input("", placeholder="Ej. contraseña, tiempos, rutas...")
st.sidebar.markdown("---")

# Base de datos simulada para el buscador
faq_db = {
    "contraseña": "Para recuperar la contraseña, haz clic en '¿Olvidaste tu contraseña?' en wiptool.com. Recibirás un enlace en tu correo corporativo.",
    "tiempos ans": "Los ANS son: 24 a 48 horas para peticiones normales y menos de 4 horas para urgentes.",
    "novedad destinatario ausente": "Si el destinatario no está, el mensajero reporta una 'Novedad' y el paquete regresa al punto de origen para reprogramación.",
    "cancelar editar solicitud": "Solo puedes editar o cancelar si el estado es 'Pendiente'. Si está 'Asignado', debes contactar al coordinador.",
    "rastreo seguimiento": "Desde tu panel en Wip, puedes ver el historial en tiempo real: Creado, Asignado, En Tránsito, Entregado o Novedad."
}

# 5. Lógica del Buscador
if busqueda:
    st.markdown(f'<p class="section-header"><i class="fas fa-search"></i> Resultados para: "{busqueda}"</p>', unsafe_allow_html=True)
    encontrado = False
    
    for clave, respuesta in faq_db.items():
        if busqueda.lower() in clave.lower() or busqueda.lower() in respuesta.lower():
            st.info(f"**Resultado encontrado:** {respuesta}")
            encontrado = True
            
    if not encontrado:
        st.warning("No encontramos un resultado exacto en las preguntas frecuentes. Por favor, intenta con otra palabra clave o utiliza el menú de navegación.")

# 6. Menú de Navegación Lateral (Solo se muestra si no hay búsqueda activa)
else:
    st.sidebar.title("Navegación")
    menu = st.sidebar.radio(
        "Módulos del Manual:",
        [
            "1. Inicio y Políticas (ANS)", 
            "2. Flujo Operativo", 
            "3. Procedimiento en Plataforma", 
            "4. Base de Conocimiento",
            "5. Videotutorial Completo"
        ]
    )

    # --- MÓDULO 1 ---
    if menu == "1. Inicio y Políticas (ANS)":
        st.markdown('<p class="section-header"><i class="fas fa-book-open icon-prof"></i> 1. Introducción al Servicio</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="highlight-card">
        Esta plataforma interactiva documenta el proceso estandarizado de recepción, coordinación y ejecución de mensajería a través de la herramienta <b>Wip</b>. Garantiza la trazabilidad desde la solicitud hasta la entrega final a nivel nacional.
        </div>
        <br>
        """, unsafe_allow_html=True)
        
        st.markdown('### <i class="fas fa-clipboard-check icon-prof"></i> Acuerdos de Nivel de Servicio (ANS)', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.success("**Tiempos de Respuesta Estimados**")
            st.write("• **Normales:** [Insertar tiempo, ej. 24 a 48 horas]")
            st.write("• **Urgentes:** [Insertar tiempo, ej. Menos de 4 horas]")
        with col2:
            st.warning("**Cobertura Nacional Activa**")
            st.write("• Bogotá (Sede Principal)")
            st.write("• Barranquilla, Santa Marta y Cartagena")
            st.write("• Cali, Ibagué y Manizales")

    # --- MÓDULO 2 ---
    elif menu == "2. Flujo Operativo":
        st.markdown('<p class="section-header"><i class="fas fa-project-diagram icon-prof"></i> 2. Modelo de Operación Centralizada</p>', unsafe_allow_html=True)
        st.write("El ecosistema Wip funciona mediante la interacción de tres roles clave:")
        st.write("") 
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown('#### <i class="fas fa-user-tie" style="color:#1E3A8A;"></i> Funcionario Bolívar', unsafe_allow_html=True)
            st.info("Ingresa la solicitud directamente en la interfaz web de Wip, especificando origen, destino y prioridad.")
        with c2:
            st.markdown('#### <i class="fas fa-headset" style="color:#1E3A8A;"></i> Coordinador Logístico', unsafe_allow_html=True)
            st.error("Audita la información desde el panel central, consolida las rutas nacionales y despacha las órdenes según disponibilidad.")
        with c3:
            st.markdown('#### <i class="fas fa-motorcycle" style="color:#1E3A8A;"></i> Mensajero', unsafe_allow_html=True)
            st.success("Ejecuta la orden en calle, recolecta la firma digital y cierra el ciclo reportando el estado final en su App.")

    # --- MÓDULO 3 ---
    elif menu == "3. Procedimiento en Plataforma":
        st.markdown('<p class="section-header"><i class="fas fa-desktop icon-prof"></i> 3. Paso a Paso en Plataforma</p>', unsafe_allow_html=True)
        
        etapa = st.selectbox("Selecciona tu rol operativo:", ["Creación de Solicitud (Usuario)", "Asignación de Ruta (Coordinador)", "Ejecución y Cierre (Mensajero)"])
        
        if etapa == "Creación de Solicitud (Usuario)":
            st.markdown("### Radicación de servicio")
            st.write("1. Ingresar a **wiptool.com** con credenciales corporativas.")
            st.write("2. Navegar a 'Nueva Solicitud'.")
            st.write("3. Diligenciar: Dirección, contacto, tipo de paquete y centro de costos.")
            st.markdown('<div style="padding:10px; border-left:4px solid #0284C7; background-color:#F0F9FF; margin-top:15px;"><b><i class="fas fa-video"></i> Video de apoyo:</b> Radicación de servicio en Wip</div>', unsafe_allow_html=True)
            st.caption("*(Espacio reservado para el video paso a paso del usuario)*")
            
        elif etapa == "Asignación de Ruta (Coordinador)":
            st.markdown("### Gestión de Coordinación")
            st.write("1. Acceder al Dashboard de Wip.")
            st.write("2. Filtrar solicitudes 'Pendientes' por ciudad.")
            st.write("3. Asignar al mensajero disponible y cambiar estado a 'Asignado'.")
            st.markdown('<div style="padding:10px; border-left:4px solid #0284C7; background-color:#F0F9FF; margin-top:15px;"><b><i class="fas fa-video"></i> Video de apoyo:</b> Asignación de rutas</div>', unsafe_allow_html=True)
            st.caption("*(Espacio reservado para el video del coordinador)*")
            
        else:
            st.markdown("### Confirmación y Novedades")
            st.write("1. El mensajero visualiza la tarea en su dispositivo móvil.")
            st.write("2. Adjunta evidencia fotográfica o firma digital en el destino.")
            st.write("3. Marca el servicio como 'Entregado' o reporta una 'Novedad'.")
            st.markdown('<div style="padding:10px; border-left:4px solid #0284C7; background-color:#F0F9FF; margin-top:15px;"><b><i class="fas fa-video"></i> Video de apoyo:</b> Cierre de entregas en calle</div>', unsafe_allow_html=True)
            st.caption("*(Espacio reservado para el video del mensajero)*")

    # --- MÓDULO 4 ---
    elif menu == "4. Base de Conocimiento":
        st.markdown('<p class="section-header"><i class="fas fa-question-circle icon-prof"></i> 4. Preguntas Frecuentes (FAQ)</p>', unsafe_allow_html=True)
        
        for pregunta, respuesta in faq_db.items():
            titulo_pregunta = "¿Dudas sobre " + pregunta.split()[0] + "?"
            with st.expander(titulo_pregunta.capitalize()):
                st.write(respuesta)
                
    # --- MÓDULO 5 ---
    elif menu == "5. Videotutorial Completo":
        st.markdown('<p class="section-header"><i class="fas fa-play-circle icon-prof"></i> 5. Inducción General</p>', unsafe_allow_html=True)
        st.write("En este video consolidado repasamos el flujo completo de la plataforma Wip, desde la creación de la solicitud hasta el cierre del servicio. Ideal para capacitaciones de nuevo personal.")
        st.markdown("""
        <div style="text-align: center; padding: 50px; background-color: #000; color: #FFF; border-radius: 10px; margin-top: 20px;">
            <h2><i class="fas fa-play"></i></h2>
            <p>El videotutorial general se cargará aquí</p>
        </div>
        """, unsafe_allow_html=True)

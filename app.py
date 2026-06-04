import streamlit as st

# 1. Configuración principal de la página
st.set_page_config(
    page_title="Manual Interactivo Wip", 
    page_icon="📦", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inyección de CSS para estética profesional (¡Corregido para Modo Oscuro!)
st.markdown("""
<style>
    .main-title { font-size: 2.8rem; color: #1E3A8A; font-weight: 800; margin-bottom: 0px;}
    .sub-title { font-size: 1.2rem; color: #64748B; margin-bottom: 30px;}
    .section-header { font-size: 1.8rem; color: #0284C7; border-bottom: 2px solid #E2E8F0; padding-bottom: 10px; margin-top: 20px;}
    .highlight-card { 
        background-color: #F8FAFC; 
        color: #0F172A; /* FIX: Esto fuerza que el texto sea oscuro siempre */
        padding: 20px; 
        border-radius: 10px; 
        border-left: 6px solid #0EA5E9; 
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); 
    }
    .faq-question { font-weight: 700; color: #0369A1; margin-top: 15px;}
    .faq-answer { color: #334155; margin-bottom: 15px;}
</style>
""", unsafe_allow_html=True)

# 3. Encabezado Principal
st.markdown('<p class="main-title">Manual Operativo Dinámico: Plataforma Wip</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Gestión y Coordinación de Mensajería - Constructora Bolívar</p>', unsafe_allow_html=True)

# 4. Menú de Navegación Lateral
st.sidebar.title("Navegación del Manual")
menu = st.sidebar.radio(
    "Selecciona un módulo:",
    [
        "1. Inicio y Políticas (ANS)", 
        "2. Flujo Operativo", 
        "3. Paso a Paso en Wip", 
        "4. Preguntas Frecuentes (FAQ)",
        "5. Videotutorial General"
    ]
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
    st.write("A continuación se detallan las métricas de cumplimiento:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("**Tiempos de Respuesta Estimados**")
        st.write("* **Peticiones Normales:** [Insertar tiempo, ej. 24 a 48 horas]*")
        st.write("* **Peticiones Urgentes:** [Insertar tiempo, ej. Menos de 4 horas]*")
        st.write("* **Cierre de Novedades:** [Insertar tiempo]*")
    with col2:
        st.warning("**Cobertura Nacional Activa**")
        st.write("* Bogotá (Sede Principal)*")
        st.write("* Barranquilla, Santa Marta y Cartagena*")
        st.write("* Cali, Ibagué y Manizales*")

# --- MÓDULO 2: FLUJO OPERATIVO ---
elif menu == "2. Flujo Operativo":
    st.markdown('<p class="section-header">2. Modelo de Operación Centralizada</p>', unsafe_allow_html=True)
    st.write("El ecosistema de la aplicación Wip funciona mediante la interacción de tres actores principales:")
    
    st.write("") 
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.info("🏢 **1. Funcionario Bolívar**")
        st.write("Detecta la necesidad de envío o recolección e ingresa la solicitud directamente en la interfaz web de Wip, especificando origen, destino y nivel de prioridad.")
    with c2:
        st.error("👨‍💻 **2. Coordinador de Operaciones**")
        st.write("Recibe todas las alertas del sistema. Audita la información, consolida las rutas y despacha las órdenes al personal en calle según su ubicación.")
    with c3:
        st.success("🛵 **3. Mensajero**")
        st.write("Visualiza la orden en su dispositivo, ejecuta la recolección/entrega, recolecta la firma digital y cierra el ciclo reportando el estado final.")

# --- MÓDULO 3: PASO A PASO EN WIP ---
elif menu == "3. Paso a Paso en Wip":
    st.markdown('<p class="section-header">3. Procedimiento en Plataforma</p>', unsafe_allow_html=True)
    st.write("Selecciona tu rol para ver las instrucciones y el video de apoyo:")
    
    etapa = st.selectbox("Fase Operativa:", ["1. Creación de Solicitud (Usuario)", "2. Asignación de Ruta (Coordinador)", "3. Ejecución y Cierre (Mensajero)"])
    
    if etapa == "1. Creación de Solicitud (Usuario)":
        st.write("### Radicación de un nuevo servicio")
        st.write("**Paso 1:** Ingresar a [wiptool.com](https://wiptool.com/) con el usuario y contraseña corporativa.")
        st.write("**Paso 2:** Navegar a la sección de 'Nueva Solicitud' o 'Nuevo Envío'.")
        st.write("**Paso 3:** Diligenciar los campos requeridos: Dirección exacta, contacto de quien recibe, tipo de paquete y centro de costos.")
        st.write("**Paso 4:** Confirmar y guardar el número de guía/radicado generado.")
        st.info("▶️ **Clip de Apoyo:** Observa cómo radicar un servicio en menos de 1 minuto.")
        st.caption("*(Espacio reservado para el micro-video del usuario)*")
        # st.video("ruta_video_usuario.mp4")
        
    elif etapa == "2. Asignación de Ruta (Coordinador)":
        st.write("### Gestión del Coordinador")
        st.write("**Paso 1:** Acceder al panel de control / Dashboard de Wip.")
        st.write("**Paso 2:** Filtrar las solicitudes 'Pendientes' por ciudad o zona.")
        st.write("**Paso 3:** Seleccionar la solicitud y asignar al mensajero disponible de esa ruta.")
        st.write("**Paso 4:** Cambiar el estado a 'En Tránsito' o 'Asignado'.")
        st.info("▶️ **Clip de Apoyo:** Observa cómo auditar y asignar rutas eficientemente.")
        st.caption("*(Espacio reservado para el micro-video del coordinador)*")
        # st.video("ruta_video_coordinador.mp4")
        
    else:
        st.write("### Confirmación y Cierre")
        st.write("**Paso 1:** El mensajero visualiza la tarea asignada en su vista de la app.")
        st.write("**Paso 2:** Se dirige al punto de origen/destino.")
        st.write("**Paso 3:** Adjunta evidencia fotográfica o firma digital si es requerido.")
        st.write("**Paso 4:** Marca el servicio como 'Entregado' o reporta una 'Novedad' para cerrar la tarea.")
        st.info("▶️ **Clip de Apoyo:** Observa cómo reportar una entrega exitosa desde la calle.")
        st.caption("*(Espacio reservado para el micro-video del mensajero)*")
        # st.video("ruta_video_mensajero.mp4")

# --- MÓDULO 4: PREGUNTAS FRECUENTES (FAQ) ---
elif menu == "4. Preguntas Frecuentes (FAQ)":
    st.markdown('<p class="section-header">4. Base de Conocimiento y FAQ</p>', unsafe_allow_html=True)
    st.write("Respuestas rápidas a las dudas más comunes sobre la plataforma Wip y nuestros procesos logísticos:")

    with st.expander("¿Qué hago si olvidé mi contraseña de acceso a Wip?"):
        st.write("Debes hacer clic en la opción '¿Olvidaste tu contraseña?' en la pantalla de inicio de wiptool.com. Recibirás un enlace en tu correo corporativo para restablecerla. Si el problema persiste, contacta a soporte técnico.")

    with st.expander("¿Es posible editar o cancelar una solicitud una vez enviada?"):
        st.write("Sí, siempre y cuando el estado de la solicitud siga como 'Pendiente' o 'Creada'. Una vez que el Coordinador le asigne la tarea a un mensajero (Estado: 'Asignado' o 'En Tránsito'), no podrás modificarla desde tu perfil y deberás comunicarte directamente con el área de operaciones.")

    with st.expander("¿Cómo puedo hacer seguimiento (rastreo) a mi paquete o documento?"):
        st.write("Desde tu panel de usuario en Wip, puedes visualizar el historial de tus solicitudes. La plataforma actualiza en tiempo real los estados: Creado, Asignado, En Tránsito, Entregado o Novedad.")

    with st.expander("¿Qué sucede si el destinatario no se encuentra en la dirección?"):
        st.write("El mensajero reportará una 'Novedad' desde la calle, indicando que el sitio estaba cerrado o la persona no se encontraba. El paquete regresará al punto de origen o a la base de coordinación para reprogramar la visita según las políticas establecidas.")

    with st.expander("¿Qué tipo de soporte técnico está disponible si la plataforma falla?"):
        st.write("Si experimentas caídas del sistema o errores en la radicación, por favor documenta el caso con una captura de pantalla y envíalo al coordinador logístico encargado para que lo escale con los desarrolladores de Wip.")

# --- MÓDULO 5: VIDEOTUTORIAL GENERAL ---
elif menu == "5. Videotutorial General":
    st.markdown('<p class="section-header">5. Inducción Completa</p>', unsafe_allow_html=True)
    st.write("En este video consolidado repasamos el flujo completo de la plataforma Wip, desde la creación de la solicitud hasta el cierre del servicio. Ideal para capacitaciones de nuevo personal.")
    
    st.info("🎥 El video general se integrará aquí.")
    st.caption("*(Espacio reservado para el videotutorial completo)*")
    # st.video("ruta_del_video_general.mp4")

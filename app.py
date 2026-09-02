import streamlit as st
from pathlib import Path

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="Control Interno • GDP",
    page_icon="CI",
    layout="wide"
)

# Paleta Verde Corporativa Ultra-Premium
COLOR1 = "#0b5334"  # Verde Oscuro
COLOR2 = "#0b5334"  # Verde Principal
COLOR3 = "#0b5334"  # Verde Accent

# URL Por defecto para reportes sin enlace aún
URL_PENDIENTE = "https://app.powerbi.com"

# =========================================================
# RUTA BASE
# =========================================================
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

# =========================================================
# PASSWORDS
# =========================================================
PASSWORDS = {
    "Planta de Beneficio": "planta2026",
    "Tienda Mi Casero": "micasero2026",
    "PAB": "pab2026",
    "Gerencia": "gerencia2026"
}

# =========================================================
# SESSION STATE
# =========================================================
if "area" not in st.session_state:
    st.session_state.area = None

if "auth" not in st.session_state:
    st.session_state.auth = False


# =========================================================
# SIDEBAR GERENCIA
# =========================================================
with st.sidebar:
    st.markdown(f"""
    <style>
    .executive-card-sidebar {{
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 24px 20px;
        border: 1px solid rgba(255, 255, 255, 0.8);
        box-shadow: 0 15px 35px -10px rgba(11, 83, 52, 0.12), 0 0 0 1px rgba(11, 83, 52, 0.05);
        text-align: center;
        margin-bottom: 24px;
        position: relative;
        overflow: hidden;
    }}
    .executive-card-sidebar::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 4px;
        background: linear-gradient(90deg, {COLOR1}, #15803d);
    }}
    .exe-title-sidebar {{
        font-weight: 800;
        color: {COLOR1};
        margin-bottom: 6px;
        font-size: 1.15rem;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }}
    .exe-status-sidebar {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 14px;
        background: rgba(254, 226, 226, 0.8);
        color: #dc2626;
        border: 1px solid rgba(252, 165, 165, 0.6);
        border-radius: 20px;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.6px;
        margin-bottom: 12px;
    }}
    .pulse-dot {{
        width: 6px;
        height: 6px;
        background-color: #dc2626;
        border-radius: 50%;
        box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.7);
        animation: pulse 1.8s infinite;
    }}
    @keyframes pulse {{
        0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.7); }}
        70% {{ transform: scale(1); box-shadow: 0 0 0 8px rgba(220, 38, 38, 0); }}
        100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(220, 38, 38, 0); }}
    }}
    </style>
    
    <div class="executive-card-sidebar">
        <div style="font-size: 2.5rem; margin-bottom: 10px; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.08));">🔍</div>
        <div class="exe-title-sidebar">Panel Ejecutivo</div>
        <div class="exe-status-sidebar"><span class="pulse-dot"></span> ACCESO RESTRINGIDO</div>
        <p style="color: #475569; font-size: 0.85rem; line-height: 1.5; margin-top: 6px; font-weight: 400;">
            Ecosistema de Control Interno consolidado en una sola vista estratégica.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("INGRESAR", use_container_width=True, help="Solo personal autorizado"):
        st.session_state.area = "Gerencia"
        st.session_state.auth = False
        st.rerun()
    
    st.markdown("---")
    st.caption("© 2026 • Grupo Don Pollo")


# =========================================================
# ESTILOS VISUALES EXPERT LEVEL
# =========================================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* Reset y Fondo Dinámico */
html, body, [class*="css"] {{
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
}}

.stApp {{
    background: radial-gradient(circle at 50% -20%, rgba(11, 83, 52, 0.05), transparent 70%),
                radial-gradient(circle at 0% 100%, rgba(11, 83, 52, 0.03), transparent 50%),
                #f8fafc;
}}

/* Encabezados Ultra Clean */
.main-title {{
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(135deg, {COLOR1} 0%, #15803d 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.03em;
    line-height: 1.2;
    margin-bottom: 4px;
}}

.subtitle {{
    color: #64748b;
    font-size: 1.05rem;
    font-weight: 500;
    margin-bottom: 12px;
}}

.title-accent {{
    height: 4px;
    width: 80px;
    background: linear-gradient(90deg, {COLOR1}, #16a34a);
    border-radius: 99px;
    margin-bottom: 36px;
    box-shadow: 0 4px 12px rgba(11, 83, 52, 0.25);
}}

/* TARJETAS GLASSMORPHISM CON SHIMMER EFFECT */
.card {{
    border-radius: 20px;
    overflow: hidden;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(226, 232, 240, 0.8);
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.05);
    margin-bottom: 12px;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
}}

.card:hover {{
    transform: translateY(-8px) scale(1.01);
    background: #ffffff;
    border-color: rgba(11, 83, 52, 0.3);
    box-shadow: 0 25px 40px -12px rgba(11, 83, 52, 0.18), 0 0 0 1px rgba(11, 83, 52, 0.1);
}}

.card img {{
    border-radius: 20px 20px 0 0;
    transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}}

.card:hover img {{
    transform: scale(1.06);
}}

.card-title {{
    padding: 20px;
    font-weight: 700;
    font-size: 1.1rem;
    color: #0f172a;
    line-height: 1.4;
}}

/* BOTONES DE ACTION SYSTEM */
div.stButton > button {{
    width: 100%;
    background: linear-gradient(135deg, {COLOR1} 0%, #0d633e 100%);
    color: #ffffff !important;
    border-radius: 12px;
    border: none;
    font-weight: 700;
    font-size: 0.95rem;
    letter-spacing: 0.3px;
    height: 48px;
    box-shadow: 0 6px 16px rgba(11, 83, 52, 0.22);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}}

div.stButton > button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 12px 25px rgba(11, 83, 52, 0.35);
    background: linear-gradient(135deg, #0e613d 0%, #15803d 100%);
}}

/* CAJA DE LOGIN PROFESIONAL */
.login-box {{
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(20px);
    padding: 48px;
    border-radius: 24px;
    box-shadow: 0 25px 50px -12px rgba(11, 83, 52, 0.15), 0 0 0 1px rgba(226, 232, 240, 0.8);
    border-top: 6px solid {COLOR1};
    animation: loginAppear 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}}

@keyframes loginAppear {{
    from {{ opacity: 0; transform: scale(0.95) translateY(10px); }}
    to {{ opacity: 1; transform: scale(1) translateY(0); }}
}}

/* STYLING EN INPUTS */
div[data-baseweb="input"] {{
    border-radius: 12px !important;
    background-color: #f8fafc !important;
    border: 1.5px solid #e2e8f0 !important;
    transition: all 0.2s ease !important;
}}

div[data-baseweb="input"]:focus-within {{
    border-color: {COLOR1} !important;
    background-color: #ffffff !important;
    box-shadow: 0 0 0 4px rgba(11, 83, 52, 0.12) !important;
}}
</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNCIONES
# =========================================================
def report_card(titulo, desc, img_relative_path):
    img_path = ASSETS_DIR / img_relative_path
    fallback = ASSETS_DIR / "default.jpg"

    st.markdown('<div class="card">', unsafe_allow_html=True)

    if img_path.exists():
        st.image(img_path.read_bytes(), use_container_width=True)
    elif fallback.exists():
        st.image(fallback.read_bytes(), use_container_width=True)
    else:
        st.image("https://via.placeholder.com/800x400.png?text=Imagen+no+disponible",
                 use_container_width=True)

    st.markdown(f"""
        <div class="card-title">
            {titulo}<br>
            <span style="font-weight:500;color:#64748b;font-size:0.88rem;display:inline-block;margin-top:4px;">
                {desc}
            </span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def open_panel_button(url, key):
    st.markdown(f"""
    <a href="{url}" target="_blank" style="text-decoration:none;">
        <div style="
            width:100%;
            text-align:center;
            padding:13px 18px;
            border-radius:12px;
            font-weight:700;
            font-size:0.92rem;
            color:white;
            background: linear-gradient(135deg, {COLOR1} 0%, #0d633e 100%);
            box-shadow: 0 6px 16px rgba(11, 83, 52, 0.2);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            margin-top: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        " onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 12px 24px rgba(11, 83, 52, 0.35)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 6px 16px rgba(11, 83, 52, 0.2)';" >
            <span>Abrir Dashboard</span>
            <span style="font-size: 1.1rem; transition: transform 0.2s ease;">→</span>
        </div>
    </a>
    """, unsafe_allow_html=True)


# =========================================================
# PORTAL PRINCIPAL
# =========================================================
if st.session_state.area is None:

    st.markdown('<div class="main-title">Ecosistema Digital • Control Interno</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Seleccione el área estratégica para desplegar indicadores</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-accent"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        report_card("Planta de Beneficio",
                    "Aseguramiento y calidad de planta",
                    "PlantaBeneficio.jpg")
        if st.button("Ingresar", key="pb", use_container_width=True):
            st.session_state.area = "Planta de Beneficio"
            st.session_state.auth = False
            st.rerun()

    with col2:
        report_card("Tienda Mi Casero",
                    "Auditoría y planes de mejora en tienda",
                    "TiendaMiCasero.jpg")
        if st.button("Ingresar", key="tmc", use_container_width=True):
            st.session_state.area = "Tienda Mi Casero"
            st.session_state.auth = False
            st.rerun()

    with col3:
        report_card("PAB",
                    "Monitoreo de finos, granulometría y PDI",
                    "PAB.jpg")
        if st.button("Ingresar", key="pab", use_container_width=True):
            st.session_state.area = "PAB"
            st.session_state.auth = False
            st.rerun()

else:

    area = st.session_state.area

    if not st.session_state.auth:

        col1, col2, col3 = st.columns([1,2,1])
        with col2:

            st.markdown(f"""
            <div class="login-box">
                <div style="font-size:1.6rem;font-weight:800;color:{COLOR1};text-align:center;letter-spacing:-0.5px;">
                    {area}
                </div>
                <div style="text-align:center;color:#64748b;margin-bottom:24px;font-size:0.92rem;font-weight:500;">
                    Ingrese su clave de acceso restringido
                </div>
            </div>
            """, unsafe_allow_html=True)

            pwd = st.text_input("Contraseña", type="password", placeholder="••••••••")

            if st.button("Ingresar", use_container_width=True):
                if pwd == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Acceso denegado: Contraseña incorrecta")

            if st.button("Volver", use_container_width=True):
                st.session_state.area = None
                st.rerun()

    else:

        st.markdown(f'<div class="main-title">{area}</div>', unsafe_allow_html=True)
        st.markdown('<div class="title-accent"></div>', unsafe_allow_html=True)

        if st.button("Cambiar área"):
            st.session_state.area = None
            st.session_state.auth = False
            st.rerun()

        st.divider()

        # ================= GERENCIA VE TODO =================
        if area == "Gerencia":
        
            st.subheader("Planta de Beneficio")
            col1, col2, col3 = st.columns(3)
            with col1:
                report_card("Calidad Planta de Beneficio", "Control de procesos e higiene", "CalidadPlanta.jpg")
                open_panel_button("https://app.powerbi.com/links/bjtEfCK9QD?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "g_pb1")
            with col2:
                report_card("Hígado Descarte", "Seguimiento y merma de descarte", "HigadoDescarte.jpg")
                open_panel_button("https://app.powerbi.com/links/hyk8FNTUbL?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "g_pb2")
            with col3:
                report_card("Reclamos Internos", "En Desarrollo - Registro de no conformidades internas", "ReclamosInternos.jpg")
                open_panel_button(URL_PENDIENTE, "g_pb3")
            
            col_g1, col_g2, col_g3 = st.columns(3)
            with col_g1:
                report_card("Reclamos Externos", "En Desarrollo - Gestión de reclamos de clientes", "ReclamosExternos.jpg")
                open_panel_button(URL_PENDIENTE, "g_pb4")

            st.divider()
            st.subheader("Tienda Mi Casero")
            col1, col2 = st.columns(2)
            with col1:
                report_card("CheckList Tienda Mi Casero", "Evaluación operacional de tiendas", "ChecklistMiCasero.jpg")
                open_panel_button("https://app.powerbi.com/links/4HbKF8s_Vp?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "g_tmc1")
            with col2:
                report_card("Planes de Mejora", "En Desarrollo - Acciones correctivas y seguimiento", "PlanesMejora.jpg")
                open_panel_button(URL_PENDIENTE, "g_tmc2")

            st.divider()
            st.subheader("PAB")
            col1, col2, col3 = st.columns(3)
            with col1:
                report_card("Reporte de Finos", "En Desarrollo - Análisis de porcentaje de finos", "ReporteFinos.jpg")
                open_panel_button(URL_PENDIENTE, "g_pab1")
            with col2:
                report_card("Reporte de Granulometría", "En Desarrollo - Control de tamaño de partícula", "Granulometria.jpg")
                open_panel_button(URL_PENDIENTE, "g_pab2")
            with col3:
                report_card("Reporte de PDI", "En Desarrollo - Índice de durabilidad del pellet", "ReportePDI.jpg")
                open_panel_button(URL_PENDIENTE, "g_pab3")

        # ================= PLANTA DE BENEFICIO =================
        elif area == "Planta de Beneficio":

            col1, col2, col3 = st.columns(3)
            with col1:
                report_card("Calidad Planta de Beneficio", "Control de procesos e higiene", "CalidadPlanta.jpg")
                open_panel_button("https://app.powerbi.com/links/bjtEfCK9QD?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "pb1")
            with col2:
                report_card("Hígado Descarte", "Seguimiento y merma de descarte", "HigadoDescarte.jpg")
                open_panel_button("https://app.powerbi.com/links/hyk8FNTUbL?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "pb2")
            with col3:
                report_card("Reclamos Internos", "En Desarrollo - Registro de no conformidades internas", "ReclamosInternos.jpg")
                open_panel_button(URL_PENDIENTE, "pb3")
            
            col4, col5, col6 = st.columns(3)
            with col4:
                report_card("Reclamos Externos", "En Desarrollo - Gestión de reclamos de clientes", "ReclamosExternos.jpg")
                open_panel_button(URL_PENDIENTE, "pb4")

        # ================= TIENDA MI CASERO =================
        elif area == "Tienda Mi Casero":

            col1, col2 = st.columns(2)
            with col1:
                report_card("CheckList Tienda Mi Casero", "Evaluación operacional de tiendas", "ChecklistMiCasero.jpg")
                open_panel_button("https://app.powerbi.com/links/4HbKF8s_Vp?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "tmc1")
            with col2:
                report_card("Planes de Mejora", "En Desarrollo - Acciones correctivas y seguimiento", "PlanesMejora.jpg")
                open_panel_button(URL_PENDIENTE, "tmc2")

        # ================= PAB =================
        elif area == "PAB":

            col1, col2, col3 = st.columns(3)
            with col1:
                report_card("Reporte de Finos", "En Desarrollo - Análisis de porcentaje de finos", "ReporteFinos.jpg")
                open_panel_button(URL_PENDIENTE, "pab1")
            with col2:
                report_card("Reporte de Granulometría", "En Desarrollo - Control de tamaño de partícula", "Granulometria.jpg")
                open_panel_button(URL_PENDIENTE, "pab2")
            with col3:
                report_card("Reporte de PDI", "En Desarrollo - Índice de durabilidad del pellet", "ReportePDI.jpg")
                open_panel_button(URL_PENDIENTE, "pab3")

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    "<center style='color:#94a3b8;margin-top:60px;font-size:0.85rem;font-weight:600;letter-spacing:0.5px;'>Gerencia de Control de Gestión • Grupo Don Pollo</center>",
    unsafe_allow_html=True
)

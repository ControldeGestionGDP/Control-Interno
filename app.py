from pathlib import Path
import streamlit as st
from PIL import Image

# =========================================================
# RUTAS DE ARCHIVOS
# =========================================================
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo.png"

# =========================================================
# CARGAR ICONO/LOGO DE LA EMPRESA
# =========================================================
if LOGO_PATH.exists():
    icon_image = Image.open(LOGO_PATH)
else:
    icon_image = "🔍"

# =========================================================
# CONFIGURACIÓN DE PÁGINA
# =========================================================
st.set_page_config(
    page_title="Control Interno • GDP",
    page_icon=icon_image,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Paleta Verde Corporativa
COLOR1 = "#0b5334"

# URL Por defecto para reportes sin enlace aún
URL_PENDIENTE = "https://app.powerbi.com"

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
# OCULTAR BARRA LATERAL
# =========================================================
st.markdown("""
<style>
[data-testid="stSidebar"], [data-testid="stSidebarCollapseButton"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# ESTILOS VISUALES
# =========================================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {{
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
}}

.stApp {{
    background: radial-gradient(circle at 50% -20%, rgba(11, 83, 52, 0.05), transparent 70%),
                radial-gradient(circle at 0% 100%, rgba(11, 83, 52, 0.03), transparent 50%),
                #f8fafc;
}}

.main-title {{
    font-size: 2.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, {COLOR1} 0%, #15803d 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.03em;
    line-height: 1.2;
}}

.subtitle {{
    color: #64748b;
    font-size: 0.98rem;
    font-weight: 500;
    margin-top: 4px;
}}

.title-accent {{
    height: 4px;
    width: 80px;
    background: linear-gradient(90deg, {COLOR1}, #16a34a);
    border-radius: 99px;
    margin-top: 16px;
    margin-bottom: 28px;
    box-shadow: 0 4px 12px rgba(11, 83, 52, 0.2);
}}

/* TARJETAS ESTÁNDAR */
.card {{
    border-radius: 20px;
    overflow: hidden;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(226, 232, 240, 0.8);
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.05);
    margin-bottom: 12px;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}}

.card:hover {{
    transform: translateY(-8px) scale(1.01);
    background: #ffffff;
    border-color: rgba(11, 83, 52, 0.3);
    box-shadow: 0 25px 40px -12px rgba(11, 83, 52, 0.18);
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
    font-size: 1.05rem;
    color: #0f172a;
    line-height: 1.4;
}}

/* BOTÓN ACCESO GERENCIAL ESTILO NAV (PILL BUTTON) */
div[data-testid="stColumn"] > div > div > div > button[key="btn_open_modal"] {{
    background: rgba(11, 83, 52, 0.08) !important;
    color: {COLOR1} !important;
    border: 1.5px solid rgba(11, 83, 52, 0.25) !important;
    border-radius: 99px !important;
    height: 42px !important;
    font-size: 0.88rem !important;
    font-weight: 700 !important;
    box-shadow: none !important;
    backdrop-filter: blur(8px);
    transition: all 0.3s ease !important;
}}

div[data-testid="stColumn"] > div > div > div > button[key="btn_open_modal"]:hover {{
    background: {COLOR1} !important;
    color: #ffffff !important;
    border-color: {COLOR1} !important;
    box-shadow: 0 8px 20px rgba(11, 83, 52, 0.25) !important;
    transform: translateY(-2px) !important;
}}

/* BOTÓN CAMBIAR ÁREA (ESTILO GHOST NEUTRO) */
div[data-testid="stColumn"] > div > div > div > button[key="btn_cambiar_area"] {{
    background: transparent !important;
    color: #64748b !important;
    border: 1.5px solid #cbd5e1 !important;
    border-radius: 99px !important;
    height: 40px !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    box-shadow: none !important;
    transition: all 0.2s ease !important;
}}

div[data-testid="stColumn"] > div > div > div > button[key="btn_cambiar_area"]:hover {{
    background: #f1f5f9 !important;
    color: #0f172a !important;
    border-color: #94a3b8 !important;
    transform: translateY(-1px) !important;
}}

/* ESTILIZACIÓN DEL MODAL */
div[data-testid="stDialog"] > div {{
    background: rgba(255, 255, 255, 0.96) !important;
    backdrop-filter: blur(24px) !important;
    border-radius: 28px !important;
    border: 1px solid rgba(11, 83, 52, 0.15) !important;
    box-shadow: 0 30px 60px -12px rgba(11, 83, 52, 0.25) !important;
    padding: 32px !important;
}}

div[data-testid="stDialog"] header {{
    background: transparent !important;
}}

.exe-modal-header {{
    text-align: center;
    padding-bottom: 8px;
}}

.exe-title-modal {{
    font-weight: 800;
    color: {COLOR1};
    font-size: 1.35rem;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-top: 10px;
    margin-bottom: 6px;
}}

.exe-badge-modal {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 14px;
    background: rgba(254, 226, 226, 0.85);
    color: #dc2626;
    border: 1px solid rgba(252, 165, 165, 0.6);
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.6px;
    margin-bottom: 12px;
}}

.pulse-dot {{
    width: 6px;
    height: 6px;
    background-color: #dc2626;
    border-radius: 50%;
    animation: pulse 1.8s infinite;
}}

@keyframes pulse {{
    0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.7); }}
    70% {{ transform: scale(1); box-shadow: 0 0 0 8px rgba(220, 38, 38, 0); }}
    100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(220, 38, 38, 0); }}
}}

/* BOTONES GENERALES */
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

div[data-baseweb="input"] {{
    border-radius: 12px !important;
    background-color: #f8fafc !important;
    border: 1.5px solid #e2e8f0 !important;
}}
</style>
""", unsafe_allow_html=True)

# =========================================================
# FUNCIONES AUXILIARES
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
        " onmouseover="this.style.transform='translateY(-3px)';" onmouseout="this.style.transform='translateY(0)';" >
            <span>Abrir Dashboard</span>
            <span style="font-size: 1.1rem;">→</span>
        </div>
    </a>
    """, unsafe_allow_html=True)


# =========================================================
# MODAL DE ACCESO GERENCIAL
# =========================================================
@st.dialog(" ")
def modal_gerencia():
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        if LOGO_PATH.exists():
            st.image(LOGO_PATH.read_bytes(), use_container_width=True)
        else:
            st.markdown("<div style='text-align:center;font-size:3rem;'>🏢</div>", unsafe_allow_html=True)

    st.markdown("""
        <div class="exe-modal-header">
            <div class="exe-title-modal">Panel Ejecutivo</div>
            <div class="exe-badge-modal"><span class="pulse-dot"></span> ACCESO GERENCIAL</div>
            <p style="color: #64748b; font-size: 0.88rem; margin-top: 4px; font-weight: 500;">
                Ingrese su clave restringida para desplegar el panel consolidado.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    pwd = st.text_input("Contraseña Gerencial", type="password", placeholder="••••••••", key="modal_pwd_input")

    if st.button("INGRESAR AL PANEL", use_container_width=True, key="btn_confirmar_modal"):
        if pwd == PASSWORDS["Gerencia"]:
            st.session_state.area = "Gerencia"
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta")


# =========================================================
# PORTAL PRINCIPAL
# =========================================================
if st.session_state.area is None:

    # ENCABEZADO TIPO NAVBAR CON BOTÓN ALINEADO
    nav_col1, nav_col2 = st.columns([3.8, 1.2], vertical_alignment="center")
    
    with nav_col1:
        st.markdown('<div class="main-title">Ecosistema Digital • Control Interno</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Seleccione el área estratégica para desplegar indicadores</div>', unsafe_allow_html=True)
    
    with nav_col2:
        # Botón estilo Pill/Badge perfectamente integrado arriba
        if st.button("🔒 Acceso Gerencial", key="btn_open_modal", use_container_width=True):
            modal_gerencia()

    st.markdown('<div class="title-accent"></div>', unsafe_allow_html=True)

    # 3 TARJETAS PRINCIPALES
    col1, col2, col3 = st.columns(3)

    with col1:
        report_card("Planta de Beneficio", "Aseguramiento y calidad de planta", "PlantaBeneficio.jpg")
        if st.button("Ingresar", key="pb", use_container_width=True):
            st.session_state.area = "Planta de Beneficio"
            st.session_state.auth = False
            st.rerun()

    with col2:
        report_card("Tienda Mi Casero", "Auditoría y planes de mejora en tienda", "TiendaMiCasero.jpg")
        if st.button("Ingresar", key="tmc", use_container_width=True):
            st.session_state.area = "Tienda Mi Casero"
            st.session_state.auth = False
            st.rerun()

    with col3:
        report_card("PAB", "Monitoreo de finos, granulometría y PDI", "PAB.jpg")
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
            <div style="background: white; padding: 40px; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.05); text-align: center;">
                <div style="font-size:1.5rem;font-weight:800;color:{COLOR1};margin-bottom:8px;">
                    {area}
                </div>
                <div style="color:#64748b;margin-bottom:20px;font-size:0.9rem;">
                    Ingrese su clave de acceso
                </div>
            </div>
            """, unsafe_allow_html=True)

            pwd = st.text_input("Contraseña", type="password", placeholder="••••••••")

            if st.button("Ingresar", use_container_width=True, key="btn_login_auth"):
                if pwd == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Acceso denegado: Contraseña incorrecta")

            if st.button("Volver", use_container_width=True, key="btn_login_volver"):
                st.session_state.area = None
                st.rerun()

    else:

        # ENCABEZADO SUPERIOR CON NAVEGACIÓN LIMPIA
        head_col1, head_col2 = st.columns([3.8, 1.2], vertical_alignment="center")
        
        with head_col1:
            st.markdown(f'<div class="main-title">{area}</div>', unsafe_allow_html=True)
            st.markdown('<div class="subtitle">Módulos e indicadores disponibles para esta área</div>', unsafe_allow_html=True)
            
        with head_col2:
            if st.button("← Cambiar área", key="btn_cambiar_area", use_container_width=True):
                st.session_state.area = None
                st.session_state.auth = False
                st.rerun()

        st.markdown('<div class="title-accent"></div>', unsafe_allow_html=True)

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
                report_card("Reclamos Internos", "En Desarrollo - Registro de no conformidades", "ReclamosInternos.jpg")
                open_panel_button(URL_PENDIENTE, "g_pb3")

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
                report_card("Reclamos Internos", "En Desarrollo - Registro de no conformidades", "ReclamosInternos.jpg")
                open_panel_button(URL_PENDIENTE, "pb3")

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
st.markdown(f"""
<div style="
    margin-top: 80px;
    padding-top: 24px;
    padding-bottom: 30px;
    border-top: 1px solid rgba(226, 232, 240, 0.8);
    text-align: center;
">
    <div style="
        font-size: 0.88rem;
        font-weight: 700;
        color: #334155;
        letter-spacing: 0.3px;
        margin-bottom: 4px;
    ">
        Gerencia de Control de Gestión <span style="color: {COLOR1}; font-weight: 800;">•</span> Grupo Don Pollo
    </div>
    <div style="
        font-size: 0.78rem;
        color: #94a3b8;
        font-weight: 500;
    ">
        © 2026 Ecosistema Digital de Indicadores. Todos los derechos reservados.
    </div>
</div>
""", unsafe_allow_html=True)

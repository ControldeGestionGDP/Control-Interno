import streamlit as st
from pathlib import Path

# =========================================================
# CONFIGURACIÓN DE PÁGINA
# =========================================================
st.set_page_config(
    page_title="Control Interno | Grupo Don Pollo",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# PALETA DE COLORES CORPORATIVA (AZUL & NARANJA GDP)
# =========================================================
COLOR_AZUL = "#094780"     # Azul Primario Corporativo
COLOR_AZUL_HOVER = "#073663" # Azul Oscuro para Hover
COLOR_NARANJA = "#ED701B"  # Naranja Acento Corporativo
COLOR_NARANJA_HOVER = "#D95E0D"
COLOR_BG = "#F6F6F6"       # Gris Claro Ejecutivo

URL_PENDIENTE = "https://app.powerbi.com"

# =========================================================
# RUTAS BASE & ASSETS
# =========================================================
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

# =========================================================
# ACCESOS Y CONTRASEÑAS
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
# 🔐 SIDEBAR GERENCIAL MEJORADO
# =========================================================
with st.sidebar:
    st.markdown(f"""
    <style>
    .executive-card-sidebar {{
        background: white;
        border-radius: 10px;
        padding: 20px;
        border-top: 4px solid {COLOR_AZUL};
        box-shadow: 0 10px 25px rgba(0,0,0,0.04);
        text-align: center;
        margin-bottom: 20px;
    }}
    .exe-title-sidebar {{
        font-weight: 800;
        color: {COLOR_AZUL};
        margin-bottom: 4px;
        font-size: 1.1rem;
        letter-spacing: -0.3px;
    }}
    .exe-status-sidebar {{
        display: inline-block;
        padding: 3px 12px;
        background: #FEE2E2;
        color: #EF4444;
        border-radius: 12px;
        font-size: 0.72rem;
        font-weight: 700;
        margin-bottom: 12px;
        letter-spacing: 0.5px;
    }}
    </style>
    
    <div class="executive-card-sidebar">
        <div style="font-size: 2.2rem; margin-bottom: 8px;">🔍</div>
        <div class="exe-title-sidebar">Panel Ejecutivo</div>
        <div class="exe-status-sidebar">● ACCESO RESTRINGIDO</div>
        <p style="color: #64748b; font-size: 0.85rem; line-height: 1.4; margin-top: 5px;">
            Ecosistema de Control Interno consolidado en una sola vista estratégica.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("INGRESAR GERENCIA", use_container_width=True, help="Solo personal autorizado"):
        st.session_state.area = "Gerencia"
        st.session_state.auth = False
        st.rerun()
    
    st.markdown("---")
    st.caption("© 2026 • Grupo Don Pollo | Control de Gestión")


# =========================================================
# ESTILOS CSS ALTA GAMA GERENCIAL (PLANTILLA UNIFICADA)
# =========================================================
st.markdown(f"""
<style>
/* Estructura Global */
.stApp {{
    background-color: {COLOR_BG};
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}}

/* Ocultar elementos nativos */
#MainMenu, footer, header {{visibility: hidden;}}

/* Contenedor Principal Flotante (Card Ejecutivo) */
.block-container {{
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
    max-width: 1180px !important;
}}

.main-card {{
    background-color: #ffffff;
    border-radius: 12px;
    border-top: 4px solid {COLOR_NARANJA};
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.04);
    padding: 2.5rem;
    margin-bottom: 1.5rem;
    animation: fadeInCard 0.5s ease;
}}

@keyframes fadeInCard {{
    from {{ opacity: 0; transform: translateY(12px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

/* Encabezados Corporativos */
.brand-tag {{
    color: {COLOR_NARANJA};
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
}}
.header-title {{
    color: {COLOR_AZUL};
    font-size: 2rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    margin-bottom: 0.2rem;
}}
.header-subtitle {{
    color: #64748b;
    font-size: 0.95rem;
    font-weight: 400;
    margin-bottom: 1.8rem;
}}

.title-accent {{
    height: 4px;
    width: 100px;
    background: linear-gradient(90deg, {COLOR_AZUL}, {COLOR_NARANJA});
    border-radius: 4px;
    margin-bottom: 24px;
}}

/* Login Box */
.login-box {{
    background: white;
    padding: 35px;
    border-radius: 12px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.06);
    border-top: 4px solid {COLOR_AZUL};
    animation: fadeInCard 0.4s ease;
}}

/* Tarjetas de Reportes */
.card {{
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0,0,0,0.06);
    margin-bottom: 12px;
    background: white;
    border: 1px solid #e2e8f0;
    transition: all 0.3s ease;
}}
.card:hover {{
    transform: translateY(-6px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.12);
    border-color: {COLOR_NARANJA};
}}
.card img {{
    border-radius: 10px 10px 0 0;
    transition: transform 0.4s ease;
}}
.card:hover img {{
    transform: scale(1.03);
}}
.card-title {{
    padding: 16px;
    font-weight: 700;
    font-size: 1.05rem;
    color: {COLOR_AZUL};
}}

/* Botones Principales (Azul Corporativo) */
div.stButton > button {{
    background-color: {COLOR_AZUL} !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.65rem 1.8rem !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.3px !important;
    width: 100% !important;
    box-shadow: 0 4px 12px rgba(9, 71, 128, 0.15) !important;
    transition: all 0.2s ease !important;
}}
div.stButton > button:hover {{
    background-color: {COLOR_AZUL_HOVER} !important;
    box-shadow: 0 6px 16px rgba(9, 71, 128, 0.25) !important;
    transform: translateY(-2px);
}}

/* Footer Ejecutivo */
.custom-footer {{
    text-align: center;
    color: #94a3b8;
    font-size: 0.8rem;
    font-weight: 500;
    letter-spacing: 0.5px;
    margin-top: 2rem;
    padding-top: 1.2rem;
    border-top: 1px solid #e2e8f0;
}}
</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNCIONES REUTILIZABLES
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
        st.image("https://via.placeholder.com/800x450.png?text=Imagen+no+disponible", use_container_width=True)

    st.markdown(f"""
        <div class="card-title">
            {titulo}<br>
            <span style="font-weight:400;color:#64748b;font-size:0.88rem;">
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
            padding:11px;
            border-radius:8px;
            font-weight:700;
            font-size:0.9rem;
            color:white;
            background: linear-gradient(90deg, {COLOR_NARANJA}, {COLOR_NARANJA_HOVER});
            box-shadow: 0 4px 12px rgba(237, 112, 27, 0.2);
            transition: all 0.2s ease;
        ">
            Abrir Dashboard ↗
        </div>
    </a>
    <div style="margin-bottom:15px;"></div>
    """, unsafe_allow_html=True)


# =========================================================
# ESTRUCTURA PRINCIPAL DEL PORTAL
# =========================================================
st.markdown('<div class="main-card">', unsafe_allow_html=True)

if st.session_state.area is None:

    st.markdown(f"""
        <div class="brand-tag">GRUPO DON POLLO | GERENCIA DE CONTROL DE GESTIÓN</div>
        <div class="header-title">Ecosistema Digital • Control Interno</div>
        <div class="header-subtitle">Seleccione el módulo estratégico para acceder a los tableros analíticos</div>
        <div class="title-accent"></div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        report_card("Planta de Beneficio",
                    "Aseguramiento, rendimientos y calidad de planta",
                    "PlantaBeneficio.jpg")
        if st.button("Ingresar al Área", key="pb", use_container_width=True):
            st.session_state.area = "Planta de Beneficio"
            st.session_state.auth = False
            st.rerun()

    with col2:
        report_card("Tienda Mi Casero",
                    "Auditoría, checklists y planes de mejora en tiendas",
                    "TiendaMiCasero.jpg")
        if st.button("Ingresar al Área", key="tmc", use_container_width=True):
            st.session_state.area = "Tienda Mi Casero"
            st.session_state.auth = False
            st.rerun()

    with col3:
        report_card("PAB",
                    "Monitoreo de finos, granulometría y PDI",
                    "PAB.jpg")
        if st.button("Ingresar al Área", key="pab", use_container_width=True):
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
                <div class="brand-tag" style="text-align:center;">MÓDULO SEGURO</div>
                <div style="font-size:1.5rem;font-weight:800;color:{COLOR_AZUL};text-align:center;margin-bottom:4px;">
                    {area}
                </div>
                <div style="text-align:center;color:#64748b;font-size:0.9rem;margin-bottom:20px;">
                    Ingrese su clave de acceso autorizada
                </div>
            </div>
            """, unsafe_allow_html=True)

            pwd = st.text_input("Contraseña", type="password", label_visibility="collapsed")

            col_btn1, col_btn2 = st.columns(2, gap="small")
            with col_btn1:
                if st.button("Acceder", use_container_width=True):
                    if pwd == PASSWORDS[area]:
                        st.session_state.auth = True
                        st.rerun()
                    else:
                        st.error("Contraseña incorrecta")
            with col_btn2:
                if st.button("Volver", use_container_width=True):
                    st.session_state.area = None
                    st.rerun()

    else:

        col_title, col_back = st.columns([3, 1])
        with col_title:
            st.markdown(f'<div class="brand-tag">CONTROL INTERNO</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="header-title">{area}</div>', unsafe_allow_html=True)
            st.markdown('<div class="title-accent"></div>', unsafe_allow_html=True)
        with col_back:
            if st.button("← Cambiar área", use_container_width=True):
                st.session_state.area = None
                st.session_state.auth = False
                st.rerun()

        # ================= GERENCIA VE TODO =================
        if area == "Gerencia":
        
            st.markdown(f'<h3 style="color:{COLOR_AZUL};font-weight:700;">1. Planta de Beneficio</h3>', unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3, gap="medium")
            with col1:
                report_card("Calidad Planta de Beneficio", "Control de procesos e higiene", "CalidadPlanta.jpg")
                open_panel_button("https://app.powerbi.com/links/bjtEfCK9QD?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "g_pb1")
            with col2:
                report_card("Hígado Descarte", "Seguimiento y merma de descarte", "HigadoDescarte.jpg")
                open_panel_button("https://app.powerbi.com/links/hyk8FNTUbL?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "g_pb2")
            with col3:
                report_card("Reclamos Internos", "Registro de no conformidades internas", "ReclamosInternos.jpg")
                open_panel_button(URL_PENDIENTE, "g_pb3")
            
            col_g1, col_g2, col_g3 = st.columns(3, gap="medium")
            with col_g1:
                report_card("Reclamos Externos", "Gestión de reclamos de clientes", "ReclamosExternos.jpg")
                open_panel_button(URL_PENDIENTE, "g_pb4")

            st.divider()
            st.markdown(f'<h3 style="color:{COLOR_AZUL};font-weight:700;">2. Tienda Mi Casero</h3>', unsafe_allow_html=True)
            col1, col2 = st.columns(2, gap="medium")
            with col1:
                report_card("CheckList Tienda Mi Casero", "Evaluación operacional de tiendas", "ChecklistMiCasero.jpg")
                open_panel_button("https://app.powerbi.com/links/4HbKF8s_Vp?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "g_tmc1")
            with col2:
                report_card("Planes de Mejora", "Acciones correctivas y seguimiento", "PlanesMejora.jpg")
                open_panel_button(URL_PENDIENTE, "g_tmc2")

            st.divider()
            st.markdown(f'<h3 style="color:{COLOR_AZUL};font-weight:700;">3. PAB</h3>', unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3, gap="medium")
            with col1:
                report_card("Reporte de Finos", "Análisis de porcentaje de finos", "ReporteFinos.jpg")
                open_panel_button(URL_PENDIENTE, "g_pab1")
            with col2:
                report_card("Reporte de Granulometría", "Control de tamaño de partícula", "Granulometria.jpg")
                open_panel_button(URL_PENDIENTE, "g_pab2")
            with col3:
                report_card("Reporte de PDI", "Índice de durabilidad del pellet", "ReportePDI.jpg")
                open_panel_button(URL_PENDIENTE, "g_pab3")

        # ================= PLANTA DE BENEFICIO =================
        elif area == "Planta de Beneficio":

            col1, col2, col3 = st.columns(3, gap="medium")
            with col1:
                report_card("Calidad Planta de Beneficio", "Control de procesos e higiene", "CalidadPlanta.jpg")
                open_panel_button("https://app.powerbi.com/links/bjtEfCK9QD?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "pb1")
            with col2:
                report_card("Hígado Descarte", "Seguimiento y merma de descarte", "HigadoDescarte.jpg")
                open_panel_button("https://app.powerbi.com/links/hyk8FNTUbL?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "pb2")
            with col3:
                report_card("Reclamos Internos", "Registro de no conformidades internas", "ReclamosInternos.jpg")
                open_panel_button(URL_PENDIENTE, "pb3")
            
            col4, col5, col6 = st.columns(3, gap="medium")
            with col4:
                report_card("Reclamos Externos", "Gestión de reclamos de clientes", "ReclamosExternos.jpg")
                open_panel_button(URL_PENDIENTE, "pb4")

        # ================= TIENDA MI CASERO =================
        elif area == "Tienda Mi Casero":

            col1, col2 = st.columns(2, gap="medium")
            with col1:
                report_card("CheckList Tienda Mi Casero", "Evaluación operacional de tiendas", "ChecklistMiCasero.jpg")
                open_panel_button("https://app.powerbi.com/links/4HbKF8s_Vp?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "tmc1")
            with col2:
                report_card("Planes de Mejora", "Acciones correctivas y seguimiento", "PlanesMejora.jpg")
                open_panel_button(URL_PENDIENTE, "tmc2")

        # ================= PAB =================
        elif area == "PAB":

            col1, col2, col3 = st.columns(3, gap="medium")
            with col1:
                report_card("Reporte de Finos", "Análisis de porcentaje de finos", "ReporteFinos.jpg")
                open_panel_button(URL_PENDIENTE, "pab1")
            with col2:
                report_card("Reporte de Granulometría", "Control de tamaño de partícula", "Granulometria.jpg")
                open_panel_button(URL_PENDIENTE, "pab2")
            with col3:
                report_card("Reporte de PDI", "Índice de durabilidad del pellet", "ReportePDI.jpg")
                open_panel_button(URL_PENDIENTE, "pab3")

st.markdown('</div>', unsafe_allow_html=True) # Cierre del main-card

# =========================================================
# FOOTER CORPORATIVO
# =========================================================
st.markdown("""
    <div class="custom-footer">
        Desarrollado por Gerencia de Control de Gestión — Grupo Don Pollo
    </div>
""", unsafe_allow_html=True)

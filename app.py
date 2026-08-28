import streamlit as st
from pathlib import Path

# =========================================================
# CONFIGURACIÓN DE PÁGINA
# =========================================================
st.set_page_config(
    page_title="Control Interno • GDP",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PALETA DE COLORES CORPORATIVA
# =========================================================
COLOR_AZUL = "#0A3866"        # Azul Marino Premium
COLOR_AZUL_HOVER = "#062444"  # Azul Profundo Hover
COLOR_NARANJA = "#E65100"     # Naranja Corporativo GDP
COLOR_NARANJA_ACCENT = "#F57C00"
COLOR_BG = "#F4F6FB"          # Gris Claro Ejecutivo

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
# 🔐 SIDEBAR GERENCIA
# =========================================================
with st.sidebar:
    st.markdown(f"""
    <style>
    .executive-card-sidebar {{
        background: white;
        border-radius: 14px;
        padding: 22px 18px;
        border-top: 4px solid {COLOR_NARANJA};
        box-shadow: 0 8px 20px rgba(0,0,0,0.04);
        text-align: center;
        margin-bottom: 20px;
    }}
    .exe-title-sidebar {{
        font-weight: 800;
        color: {COLOR_AZUL};
        margin-bottom: 4px;
        font-size: 1.1rem;
        letter-spacing: -0.3px;
        text-transform: uppercase;
    }}
    .exe-status-sidebar {{
        display: inline-block;
        padding: 3px 12px;
        background: #FEE2E2;
        color: #DC2626;
        border-radius: 12px;
        font-size: 0.72rem;
        font-weight: 800;
        margin-bottom: 12px;
        letter-spacing: 0.5px;
    }}
    </style>
    
    <div class="executive-card-sidebar">
        <div style="font-size: 2.2rem; margin-bottom: 6px;">🔍</div>
        <div class="exe-title-sidebar">Panel Ejecutivo</div>
        <div class="exe-status-sidebar">● ACCESO RESTRINGIDO</div>
        <p style="color: #64748b; font-size: 0.83rem; line-height: 1.45; margin-top: 4px;">
            Ecosistema de Control Interno consolidado en una sola vista estratégica.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("INGRESAR A GERENCIA", use_container_width=True, help="Solo personal autorizado"):
        st.session_state.area = "Gerencia"
        st.session_state.auth = False
        st.rerun()
    
    st.markdown("---")
    st.caption("© 2026 • Grupo Don Pollo | Control de Gestión")


# =========================================================
# ESTILOS VISUALES ALTA GAMA (CSS UNIFICADO)
# =========================================================
st.markdown(f"""
<style>
/* Estructura Global */
.stApp {{
    background-color: {COLOR_BG};
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}}

#MainMenu, footer, header {{visibility: hidden;}}

.block-container {{
    padding-top: 1.8rem !important;
    padding-bottom: 3rem !important;
    max-width: 1200px !important;
}}

/* Header Hero Gerencial */
.hero-header {{
    background: white;
    border-radius: 16px;
    padding: 2.2rem 2.5rem;
    border-top: 5px solid {COLOR_NARANJA};
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03);
    margin-bottom: 2rem;
}}

.brand-tag {{
    color: {COLOR_NARANJA};
    font-size: 0.78rem;
    font-weight: 800;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}}

.hero-title {{
    color: {COLOR_AZUL};
    font-size: 2.2rem;
    font-weight: 800;
    letter-spacing: -0.8px;
    margin-bottom: 0.3rem;
}}

.hero-subtitle {{
    color: #64748b;
    font-size: 0.98rem;
    font-weight: 400;
}}

.title-accent {{
    height: 4px;
    width: 90px;
    background: linear-gradient(90deg, {COLOR_AZUL}, {COLOR_NARANJA});
    border-radius: 4px;
    margin-top: 14px;
}}

/* Login Box Estilizado */
.login-box {{
    background: white;
    padding: 35px;
    border-radius: 16px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.05);
    border-top: 5px solid {COLOR_AZUL};
    margin-bottom: 20px;
}}

/* Tarjetas Flexibles con Altura Fija */
.card {{
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 8px 24px rgba(0,0,0,0.04);
    background: white;
    border: 1px solid #e2e8f0;
    transition: all 0.3s cubic-bezier(.4,0,.2,1);
    display: flex;
    flex-direction: column;
    height: 380px; /* Altura uniforme para alineación perfecta */
    margin-bottom: 10px;
}}

.card:hover {{
    transform: translateY(-6px);
    box-shadow: 0 18px 36px rgba(0,0,0,0.09);
    border-color: {COLOR_NARANJA};
}}

.card-img-container {{
    height: 180px;
    width: 100%;
    overflow: hidden;
    background: #f1f5f9;
}}

.card-img-container img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
}}

.card:hover .card-img-container img {{
    transform: scale(1.04);
}}

.card-body {{
    padding: 16px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    flex-grow: 1;
}}

.card-title-text {{
    font-weight: 800;
    font-size: 1.08rem;
    color: {COLOR_AZUL};
    margin-bottom: 6px;
}}

.card-desc-text {{
    font-weight: 400;
    color: #64748b;
    font-size: 0.88rem;
    line-height: 1.35;
    height: 40px; /* Espacio fijo para texto */
    overflow: hidden;
}}

/* Botones Nativos */
div.stButton > button {{
    background-color: {COLOR_AZUL} !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.7rem 1.5rem !important;
    font-size: 0.92rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.3px !important;
    width: 100% !important;
    box-shadow: 0 4px 14px rgba(10, 56, 102, 0.15) !important;
    transition: all 0.25s ease !important;
}}

div.stButton > button:hover {{
    background-color: {COLOR_AZUL_HOVER} !important;
    box-shadow: 0 8px 20px rgba(10, 56, 102, 0.25) !important;
    transform: translateY(-2px);
}}

/* Footer */
.custom-footer {{
    text-align: center;
    color: #94a3b8;
    font-size: 0.82rem;
    font-weight: 500;
    letter-spacing: 0.5px;
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid #e2e8f0;
}}
</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNCIONES AUXILIARES
# =========================================================
import base64

def get_image_base64(img_path):
    if img_path.exists():
        with open(img_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    return None

def render_aligned_card(titulo, desc, img_relative_path):
    img_path = ASSETS_DIR / img_relative_path
    fallback = ASSETS_DIR / "default.jpg"
    
    b64_img = get_image_base64(img_path) or get_image_base64(fallback)
    
    if b64_img:
        src = f"data:image/jpeg;base64,{b64_img}"
    else:
        src = "https://via.placeholder.com/800x450.png?text=Imagen+no+disponible"

    st.markdown(f"""
        <div class="card">
            <div class="card-img-container">
                <img src="{src}" alt="{titulo}">
            </div>
            <div class="card-body">
                <div>
                    <div class="card-title-text">{titulo}</div>
                    <div class="card-desc-text">{desc}</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def open_panel_button(url, key):
    st.markdown(f"""
    <a href="{url}" target="_blank" style="text-decoration:none;">
        <div style="
            width:100%;
            text-align:center;
            padding:12px;
            border-radius:10px;
            font-weight:700;
            font-size:0.9rem;
            color:white;
            background: linear-gradient(90deg, {COLOR_NARANJA}, {COLOR_NARANJA_ACCENT});
            box-shadow: 0 4px 14px rgba(230, 81, 0, 0.25);
            transition: all 0.25s ease;
        ">
            Abrir Dashboard ↗
        </div>
    </a>
    <div style="margin-bottom:18px;"></div>
    """, unsafe_allow_html=True)


# =========================================================
# CONTENIDO DEL PORTAL
# =========================================================
if st.session_state.area is None:

    st.markdown(f"""
        <div class="hero-header">
            <div class="brand-tag">GRUPO DON POLLO | GERENCIA DE CONTROL DE GESTIÓN</div>
            <div class="hero-title">Ecosistema Digital • Control Interno</div>
            <div class="hero-subtitle">Seleccione el módulo estratégico para acceder a los tableros analíticos</div>
            <div class="title-accent"></div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        render_aligned_card("Planta de Beneficio",
                             "Aseguramiento, rendimientos y calidad de planta",
                             "PlantaBeneficio.jpg")
        if st.button("Ingresar al Área", key="pb", use_container_width=True):
            st.session_state.area = "Planta de Beneficio"
            st.session_state.auth = False
            st.rerun()

    with col2:
        render_aligned_card("Tienda Mi Casero",
                             "Auditoría, checklists y planes de mejora en tiendas",
                             "TiendaMiCasero.jpg")
        if st.button("Ingresar al Área", key="tmc", use_container_width=True):
            st.session_state.area = "Tienda Mi Casero"
            st.session_state.auth = False
            st.rerun()

    with col3:
        render_aligned_card("PAB",
                             "Monitoreo de finos, granulometría y PDI",
                             "PAB.jpg")
        if st.button("Ingresar al Área", key="pab", use_container_width=True):
            st.session_state.area = "PAB"
            st.session_state.auth = False
            st.rerun()

else:

    area = st.session_state.area

    if not st.session_state.auth:

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:

            st.markdown(f"""
            <div class="login-box">
                <div class="brand-tag" style="text-align:center;">MÓDULO DE SEGURIDAD</div>
                <div style="font-size:1.6rem;font-weight:800;color:{COLOR_AZUL};text-align:center;margin-bottom:4px;">
                    {area}
                </div>
                <div style="text-align:center;color:#64748b;font-size:0.9rem;">
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

        st.markdown(f"""
            <div class="hero-header" style="padding: 1.8rem 2.2rem;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <div class="brand-tag">CONTROL DE GESTIÓN • {area.upper()}</div>
                        <div class="hero-title" style="margin-bottom:0;">Tableros Operativos</div>
                    </div>
                </div>
                <div class="title-accent"></div>
            </div>
        """, unsafe_allow_html=True)

        col_back, _ = st.columns([1, 4])
        with col_back:
            if st.button("← Cambiar módulo", use_container_width=True):
                st.session_state.area = None
                st.session_state.auth = False
                st.rerun()

        st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)

        # ================= GERENCIA VE TODO =================
        if area == "Gerencia":
        
            st.markdown(f'<h3 style="color:{COLOR_AZUL};font-weight:800;margin-bottom:15px;">1. Planta de Beneficio</h3>', unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3, gap="medium")
            with col1:
                render_aligned_card("Calidad Planta de Beneficio", "Control de procesos e higiene", "CalidadPlanta.jpg")
                open_panel_button("https://app.powerbi.com/links/bjtEfCK9QD?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "g_pb1")
            with col2:
                render_aligned_card("Hígado Descarte", "Seguimiento y merma de descarte", "HigadoDescarte.jpg")
                open_panel_button("https://app.powerbi.com/links/hyk8FNTUbL?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "g_pb2")
            with col3:
                render_aligned_card("Reclamos Internos", "Registro de no conformidades internas", "ReclamosInternos.jpg")
                open_panel_button(URL_PENDIENTE, "g_pb3")
            
            col_g1, col_g2, col_g3 = st.columns(3, gap="medium")
            with col_g1:
                render_aligned_card("Reclamos Externos", "Gestión de reclamos de clientes", "ReclamosExternos.jpg")
                open_panel_button(URL_PENDIENTE, "g_pb4")

            st.divider()
            st.markdown(f'<h3 style="color:{COLOR_AZUL};font-weight:800;margin-bottom:15px;">2. Tienda Mi Casero</h3>', unsafe_allow_html=True)
            col1, col2 = st.columns(2, gap="medium")
            with col1:
                render_aligned_card("CheckList Tienda Mi Casero", "Evaluación operacional de tiendas", "ChecklistMiCasero.jpg")
                open_panel_button("https://app.powerbi.com/links/4HbKF8s_Vp?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "g_tmc1")
            with col2:
                render_aligned_card("Planes de Mejora", "Acciones correctivas y seguimiento", "PlanesMejora.jpg")
                open_panel_button(URL_PENDIENTE, "g_tmc2")

            st.divider()
            st.markdown(f'<h3 style="color:{COLOR_AZUL};font-weight:800;margin-bottom:15px;">3. PAB</h3>', unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3, gap="medium")
            with col1:
                render_aligned_card("Reporte de Finos", "Análisis de porcentaje de finos", "ReporteFinos.jpg")
                open_panel_button(URL_PENDIENTE, "g_pab1")
            with col2:
                render_aligned_card("Reporte de Granulometría", "Control de tamaño de partícula", "Granulometria.jpg")
                open_panel_button(URL_PENDIENTE, "g_pab2")
            with col3:
                render_aligned_card("Reporte de PDI", "Índice de durabilidad del pellet", "ReportePDI.jpg")
                open_panel_button(URL_PENDIENTE, "g_pab3")

        # ================= PLANTA DE BENEFICIO =================
        elif area == "Planta de Beneficio":

            col1, col2, col3 = st.columns(3, gap="medium")
            with col1:
                render_aligned_card("Calidad Planta de Beneficio", "Control de procesos e higiene", "CalidadPlanta.jpg")
                open_panel_button("https://app.powerbi.com/links/bjtEfCK9QD?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "pb1")
            with col2:
                render_aligned_card("Hígado Descarte", "Seguimiento y merma de descarte", "HigadoDescarte.jpg")
                open_panel_button("https://app.powerbi.com/links/hyk8FNTUbL?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "pb2")
            with col3:
                render_aligned_card("Reclamos Internos", "Registro de no conformidades internas", "ReclamosInternos.jpg")
                open_panel_button(URL_PENDIENTE, "pb3")
            
            col4, col5, col6 = st.columns(3, gap="medium")
            with col4:
                render_aligned_card("Reclamos Externos", "Gestión de reclamos de clientes", "ReclamosExternos.jpg")
                open_panel_button(URL_PENDIENTE, "pb4")

        # ================= TIENDA MI CASERO =================
        elif area == "Tienda Mi Casero":

            col1, col2 = st.columns(2, gap="medium")
            with col1:
                render_aligned_card("CheckList Tienda Mi Casero", "Evaluación operacional de tiendas", "ChecklistMiCasero.jpg")
                open_panel_button("https://app.powerbi.com/links/4HbKF8s_Vp?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "tmc1")
            with col2:
                render_aligned_card("Planes de Mejora", "Acciones correctivas y seguimiento", "PlanesMejora.jpg")
                open_panel_button(URL_PENDIENTE, "tmc2")

        # ================= PAB =================
        elif area == "PAB":

            col1, col2, col3 = st.columns(3, gap="medium")
            with col1:
                render_aligned_card("Reporte de Finos", "Análisis de porcentaje de finos", "ReporteFinos.jpg")
                open_panel_button(URL_PENDIENTE, "pab1")
            with col2:
                render_aligned_card("Reporte de Granulometría", "Control de tamaño de partícula", "Granulometria.jpg")
                open_panel_button(URL_PENDIENTE, "pab2")
            with col3:
                render_aligned_card("Reporte de PDI", "Índice de durabilidad del pellet", "ReportePDI.jpg")
                open_panel_button(URL_PENDIENTE, "pab3")


# =========================================================
# FOOTER CORPORATIVO
# =========================================================
st.markdown("""
    <div class="custom-footer">
        Desarrollado por Gerencia de Control de Gestión — Grupo Don Pollo
    </div>
""", unsafe_allow_html=True)

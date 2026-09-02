import streamlit as st
from pathlib import Path

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="Control Interno • GDP",
    page_icon="🔍",
    layout="wide"
)

# Paleta Verde Corporativa
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
# 🔐 SIDEBAR GERENCIA
# =========================================================
with st.sidebar:
    st.markdown(f"""
    <style>
    .executive-card-sidebar {{
        background: white;
        border-radius: 18px;
        padding: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 20px;
    }}
    .exe-title-sidebar {{
        font-weight: 800;
        color: {COLOR1};
        margin-bottom: 5px;
        font-size: 1.1rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    .exe-status-sidebar {{
        display: inline-block;
        padding: 3px 12px;
        background: #FEE2E2;
        color: #EF4444;
        border-radius: 12px;
        font-size: 0.7rem;
        font-weight: 700;
        margin-bottom: 12px;
    }}
    </style>
    
    <div class="executive-card-sidebar">
        <div style="font-size: 2.2rem; margin-bottom: 10px;">🔍</div>
        <div class="exe-title-sidebar">Panel Ejecutivo</div>
        <div class="exe-status-sidebar">● ACCESO RESTRINGIDO</div>
        <p style="color: #64748b; font-size: 0.85rem; line-height: 1.4; margin-top: 5px;">
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
# ESTILOS VISUALES
# =========================================================
st.markdown(f"""
<style>
html, body {{
    font-family: "Segoe UI", sans-serif;
    background: #f4f6fb;
    animation: fadeInBody 0.6s ease-in-out;
}}
@keyframes fadeInBody {{
    from {{ opacity: 0; transform: translateY(8px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}
.main-title {{
    font-size: 2.6rem;
    font-weight: 800;
    color: {COLOR1};
    animation: slideInTitle 0.7s ease;
}}
@keyframes slideInTitle {{
    from {{ opacity: 0; transform: translateX(-10px); }}
    to {{ opacity: 1; transform: translateX(0); }}
}}
.subtitle {{
    color: #6b7280;
    margin-bottom: 12px;
}}
.title-accent {{
    height: 4px;
    width: 120px;
    background: linear-gradient(90deg,{COLOR1},{COLOR2},{COLOR3});
    border-radius: 4px;
    margin-bottom: 28px;
    animation: expandBar 0.8s ease forwards;
}}
@keyframes expandBar {{
    from {{ width: 0; }}
    to {{ width: 120px; }}
}}
.login-box {{
    background: white;
    padding: 40px;
    border-radius: 18px;
    box-shadow: 0 25px 55px rgba(0,0,0,0.12);
    border-top: 5px solid {COLOR1};
    animation: fadeInCard 0.5s ease;
}}
@keyframes fadeInCard {{
    from {{ opacity: 0; transform: translateY(12px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}
.card {{
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 15px 35px rgba(0,0,0,0.12);
    margin-bottom: 8px;
    background: white;
    transition: all 0.35s cubic-bezier(.4,0,.2,1);
}}
.card:hover {{
    transform: translateY(-8px);
    box-shadow: 0 25px 55px rgba(0,0,0,0.18);
}}
.card img {{
    border-radius: 18px;
    transition: transform 0.4s ease;
}}
.card:hover img {{
    transform: scale(1.04);
}}
.card-title {{
    padding: 15px;
    font-weight: 700;
    font-size: 1.1rem;
}}
div.stButton > button {{
    width: 100%;
    background: linear-gradient(90deg, {COLOR1}, {COLOR2}, {COLOR3});
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: 700;
    height: 45px;
    transition: all 0.25s ease;
}}
div.stButton > button:hover {{
    transform: translateY(-3px);
    box-shadow: 0 10px 22px rgba(0,0,0,0.2);
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
            <span style="font-weight:400;color:#6b7280;font-size:0.95rem;">
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
            padding:12px;
            border-radius:10px;
            font-weight:700;
            color:white;
            background: linear-gradient(90deg,{COLOR1},{COLOR2},{COLOR3});
            box-shadow: 0 6px 14px rgba(0,0,0,0.15);
        ">
            Abrir Dashboard
        </div>
    </a>
    """, unsafe_allow_html=True)


# =========================================================
# PORTAL PRINCIPAL
# =========================================================
if st.session_state.area is None:

    st.markdown('<div class="main-title">Ecosistema Digital • Control Interno</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Seleccione el área de interés</div>', unsafe_allow_html=True)
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
                <div style="font-size:1.4rem;font-weight:700;color:{COLOR1};text-align:center;">
                    {area}
                </div>
                <div style="text-align:center;color:#6b7280;margin-bottom:20px;">
                    Ingrese su contraseña
                </div>
            </div>
            """, unsafe_allow_html=True)

            pwd = st.text_input("Contraseña", type="password")

            if st.button("Ingresar", use_container_width=True):
                if pwd == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Contraseña incorrecta")

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
                report_card("Reclamos Internos", "Registro de no conformidades internas", "ReclamosInternos.jpg")
                open_panel_button(URL_PENDIENTE, "g_pb3")
            
            col_g1, col_g2, col_g3 = st.columns(3)
            with col_g1:
                report_card("Reclamos Externos", "Gestión de reclamos de clientes", "ReclamosExternos.jpg")
                open_panel_button(URL_PENDIENTE, "g_pb4")

            st.divider()
            st.subheader("Tienda Mi Casero")
            col1, col2 = st.columns(2)
            with col1:
                report_card("CheckList Tienda Mi Casero", "Evaluación operacional de tiendas", "ChecklistMiCasero.jpg")
                open_panel_button("https://app.powerbi.com/links/4HbKF8s_Vp?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "g_tmc1")
            with col2:
                report_card("Planes de Mejora", "Acciones correctivas y seguimiento", "PlanesMejora.jpg")
                open_panel_button(URL_PENDIENTE, "g_tmc2")

            st.divider()
            st.subheader("PAB")
            col1, col2, col3 = st.columns(3)
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

            col1, col2, col3 = st.columns(3)
            with col1:
                report_card("Calidad Planta de Beneficio", "Control de procesos e higiene", "CalidadPlanta.jpg")
                open_panel_button("https://app.powerbi.com/links/bjtEfCK9QD?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "pb1")
            with col2:
                report_card("Hígado Descarte", "Seguimiento y merma de descarte", "HigadoDescarte.jpg")
                open_panel_button("https://app.powerbi.com/links/hyk8FNTUbL?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "pb2")
            with col3:
                report_card("Reclamos Internos", "Registro de no conformidades internas", "ReclamosInternos.jpg")
                open_panel_button(URL_PENDIENTE, "pb3")
            
            col4, col5, col6 = st.columns(3)
            with col4:
                report_card("Reclamos Externos", "Gestión de reclamos de clientes", "ReclamosExternos.jpg")
                open_panel_button(URL_PENDIENTE, "pb4")

        # ================= TIENDA MI CASERO =================
        elif area == "Tienda Mi Casero":

            col1, col2 = st.columns(2)
            with col1:
                report_card("CheckList Tienda Mi Casero", "Evaluación operacional de tiendas", "ChecklistMiCasero.jpg")
                open_panel_button("https://app.powerbi.com/links/4HbKF8s_Vp?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare", "tmc1")
            with col2:
                report_card("Planes de Mejora", "Acciones correctivas y seguimiento", "PlanesMejora.jpg")
                open_panel_button(URL_PENDIENTE, "tmc2")

        # ================= PAB =================
        elif area == "PAB":

            col1, col2, col3 = st.columns(3)
            with col1:
                report_card("Reporte de Finos", "Análisis de porcentaje de finos", "ReporteFinos.jpg")
                open_panel_button(URL_PENDIENTE, "pab1")
            with col2:
                report_card("Reporte de Granulometría", "Control de tamaño de partícula", "Granulometria.jpg")
                open_panel_button(URL_PENDIENTE, "pab2")
            with col3:
                report_card("Reporte de PDI", "Índice de durabilidad del pellet", "ReportePDI.jpg")
                open_panel_button(URL_PENDIENTE, "pab3")

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    "<center style='color:#9ca3af;margin-top:40px;'>Gerencia de Control de Gestión • Grupo Don Pollo</center>",
    unsafe_allow_html=True
)

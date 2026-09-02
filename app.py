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

COLOR1 = "#0b5334"
URL_PENDIENTE = "https://app.powerbi.com"

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

PASSWORDS = {
    "Planta de Beneficio": "planta2026",
    "Tienda Mi Casero": "micasero2026",
    "PAB": "pab2026",
    "Gerencia": "gerencia2026"
}

if "area" not in st.session_state:
    st.session_state.area = None

if "auth" not in st.session_state:
    st.session_state.auth = False

# =========================================================
# 🔐 SIDEBAR
# =========================================================
with st.sidebar:
    st.markdown(f"""
    <style>
    .executive-card-sidebar {{
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(16px);
        border-radius: 20px;
        padding: 24px 20px;
        border: 1px solid rgba(226, 232, 240, 0.8);
        box-shadow: 0 15px 35px -10px rgba(11, 83, 52, 0.12);
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
    }}
    </style>
    
    <div class="executive-card-sidebar">
        <div style="font-size: 2.5rem; margin-bottom: 10px;">🔍</div>
        <div class="exe-title-sidebar">Panel Ejecutivo</div>
        <div class="exe-status-sidebar">ACCESO RESTRINGIDO</div>
        <p style="color: #475569; font-size: 0.85rem; margin-top: 10px;">
            Ecosistema de Control Interno consolidado.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("INGRESAR", use_container_width=True):
        st.session_state.area = "Gerencia"
        st.session_state.auth = False
        st.rerun()
    
    st.markdown("---")
    st.caption("© 2026 • Grupo Don Pollo")


# =========================================================
# ESTILOS CSS REFORZADOS (INCLUYE ANIMACIÓN HOVER GARANTIZADA)
# =========================================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {{
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
}}

.stApp {{
    background: #f8fafc;
}}

.main-title {{
    font-size: 2.6rem;
    font-weight: 800;
    color: {COLOR1};
    letter-spacing: -0.03em;
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
    background: {COLOR1};
    border-radius: 99px;
    margin-bottom: 36px;
}}

/* ESTILOS DE BOTONES NATIVOS STREAMLIT CON ANIMACIÓN */
div.stButton > button {{
    width: 100% !important;
    background-color: {COLOR1} !important;
    color: #ffffff !important;
    border-radius: 18px !important;
    border: none !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    height: 48px !important;
    box-shadow: 0 10px 20px -5px rgba(11, 83, 52, 0.4) !important;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    cursor: pointer !important;
}}

div.stButton > button:hover {{
    transform: translateY(-5px) scale(1.02) !important;
    box-shadow: 0 18px 30px -4px rgba(11, 83, 52, 0.6) !important;
    background-color: #083e27 !important;
}}

/* BOTÓN PERSONALIZADO DE DASHBOARD CON ANIMACIÓN HOVER ENLACE */
a.dashboard-link {{
    text-decoration: none !important;
    display: block !important;
    width: 100% !important;
    margin-top: 15px;
}}

.dashboard-btn-custom {{
    width: 100%;
    text-align: center;
    padding: 14px 18px;
    border-radius: 18px;
    font-weight: 700;
    font-size: 0.95rem;
    color: #ffffff !important;
    background-color: {COLOR1};
    box-shadow: 0 10px 20px -5px rgba(11, 83, 52, 0.4);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    box-sizing: border-box;
}}

/* ANIMACIÓN AL PASAR EL MOUSE (HOVER) */
a.dashboard-link:hover .dashboard-btn-custom {{
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0 18px 30px -4px rgba(11, 83, 52, 0.6);
    background-color: #083e27;
}}

a.dashboard-link:hover .arrow-anim {{
    transform: translateX(5px);
}}

.arrow-anim {{
    font-size: 1.1rem;
    transition: transform 0.3s ease;
}}

/* CAJA TARJETA */
.card-container {{
    background: #ffffff;
    border-radius: 20px;
    border: 1px solid rgba(226, 232, 240, 0.8);
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
    padding-bottom: 8px;
    margin-bottom: 20px;
    overflow: hidden;
}}

.login-box {{
    background: #ffffff;
    padding: 44px;
    border-radius: 24px;
    box-shadow: 0 20px 40px -12px rgba(11, 83, 52, 0.12);
    border-top: 6px solid {COLOR1};
}}
</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNCION PARA MOSTRAR TARJETA + BOTÓN UNIFICADOS
# =========================================================
def show_card_with_button(titulo, desc, img_relative_path, url_powerbi):
    img_path = ASSETS_DIR / img_relative_path
    
    # Renderizamos todo en un solo bloque HTML para evitar saltos de línea molestos
    import base64
    if img_path.exists():
        encoded = base64.b64encode(img_path.read_bytes()).decode()
        img_src = f"data:image/jpeg;base64,{encoded}"
    else:
        img_src = "https://via.placeholder.com/800x400.png?text=Imagen+no+disponible"

    html_code = f"""
    <div class="card-container">
        <img src="{img_src}" style="width:100%; height:180px; object-fit:cover; border-radius: 20px 20px 0 0;" />
        <div style="padding: 18px 18px 10px 18px;">
            <div style="font-weight:700; font-size:1.05rem; color:#0f172a; line-height:1.3;">{titulo}</div>
            <div style="font-weight:500; color:#64748b; font-size:0.88rem; margin-top:4px;">{desc}</div>
            <a href="{url_powerbi}" target="_blank" class="dashboard-link">
                <div class="dashboard-btn-custom">
                    <span>Abrir Dashboard</span>
                    <span class="arrow-anim">→</span>
                </div>
            </a>
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)


# =========================================================
# PORTAL PRINCIPAL
# =========================================================
if st.session_state.area is None:

    st.markdown('<div class="main-title">Ecosistema Digital • Control Interno</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Seleccione el área de interés</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-accent"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(str(ASSETS_DIR / "PlantaBeneficio.jpg") if (ASSETS_DIR / "PlantaBeneficio.jpg").exists() else "https://via.placeholder.com/800x400")
        st.markdown("**Planta de Beneficio**\nAseguramiento y calidad de planta")
        if st.button("Ingresar", key="pb"):
            st.session_state.area = "Planta de Beneficio"
            st.session_state.auth = False
            st.rerun()

    with col2:
        st.image(str(ASSETS_DIR / "TiendaMiCasero.jpg") if (ASSETS_DIR / "TiendaMiCasero.jpg").exists() else "https://via.placeholder.com/800x400")
        st.markdown("**Tienda Mi Casero**\nAuditoría y planes de mejora en tienda")
        if st.button("Ingresar", key="tmc"):
            st.session_state.area = "Tienda Mi Casero"
            st.session_state.auth = False
            st.rerun()

    with col3:
        st.image(str(ASSETS_DIR / "PAB.jpg") if (ASSETS_DIR / "PAB.jpg").exists() else "https://via.placeholder.com/800x400")
        st.markdown("**PAB**\nMonitoreo de finos, granulometría y PDI")
        if st.button("Ingresar", key="pab"):
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
                <div style="font-size:1.6rem;font-weight:800;color:{COLOR1};text-align:center;">
                    {area}
                </div>
                <div style="text-align:center;color:#64748b;margin-bottom:24px;font-size:0.92rem;">
                    Ingrese su clave de acceso restringido
                </div>
            </div>
            """, unsafe_allow_html=True)

            pwd = st.text_input("Contraseña", type="password", placeholder="••••••••")

            if st.button("Ingresar"):
                if pwd == PASSWORDS[area]:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Acceso denegado: Contraseña incorrecta")

            if st.button("Volver"):
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
                show_card_with_button("Calidad Planta de Beneficio", "Control de procesos e higiene", "CalidadPlanta.jpg", "https://app.powerbi.com/links/bjtEfCK9QD?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
            with col2:
                show_card_with_button("Hígado Descarte", "Seguimiento y merma de descarte", "HigadoDescarte.jpg", "https://app.powerbi.com/links/hyk8FNTUbL?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
            with col3:
                show_card_with_button("Reclamos Internos", "Registro de no conformidades internas", "ReclamosInternos.jpg", URL_PENDIENTE)
            
            col_g1, col_g2, col_g3 = st.columns(3)
            with col_g1:
                show_card_with_button("Reclamos Externos", "Gestión de reclamos de clientes", "ReclamosExternos.jpg", URL_PENDIENTE)

            st.divider()
            st.subheader("Tienda Mi Casero")
            col1, col2 = st.columns(2)
            with col1:
                show_card_with_button("CheckList Tienda Mi Casero", "Evaluación operacional de tiendas", "ChecklistMiCasero.jpg", "https://app.powerbi.com/links/4HbKF8s_Vp?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
            with col2:
                show_card_with_button("Planes de Mejora", "Acciones correctivas y seguimiento", "PlanesMejora.jpg", URL_PENDIENTE)

            st.divider()
            st.subheader("PAB")
            col1, col2, col3 = st.columns(3)
            with col1:
                show_card_with_button("Reporte de Finos", "Análisis de porcentaje de finos", "ReporteFinos.jpg", URL_PENDIENTE)
            with col2:
                show_card_with_button("Reporte de Granulometría", "Control de tamaño de partícula", "Granulometria.jpg", URL_PENDIENTE)
            with col3:
                show_card_with_button("Reporte de PDI", "Índice de durabilidad del pellet", "ReportePDI.jpg", URL_PENDIENTE)

        # ================= PLANTA DE BENEFICIO =================
        elif area == "Planta de Beneficio":

            col1, col2, col3 = st.columns(3)
            with col1:
                show_card_with_button("Calidad Planta de Beneficio", "Control de procesos e higiene", "CalidadPlanta.jpg", "https://app.powerbi.com/links/bjtEfCK9QD?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
            with col2:
                show_card_with_button("Hígado Descarte", "Seguimiento y merma de descarte", "HigadoDescarte.jpg", "https://app.powerbi.com/links/hyk8FNTUbL?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
            with col3:
                show_card_with_button("Reclamos Internos", "Registro de no conformidades internas", "ReclamosInternos.jpg", URL_PENDIENTE)
            
            col4, col5, col6 = st.columns(3)
            with col4:
                show_card_with_button("Reclamos Externos", "Gestión de reclamos de clientes", "ReclamosExternos.jpg", URL_PENDIENTE)

        # ================= TIENDA MI CASERO =================
        elif area == "Tienda Mi Casero":

            col1, col2 = st.columns(2)
            with col1:
                show_card_with_button("CheckList Tienda Mi Casero", "Evaluación operacional de tiendas", "ChecklistMiCasero.jpg", "https://app.powerbi.com/links/4HbKF8s_Vp?ctid=42fc96b3-c018-482d-8ada-cab81720489e&pbi_source=linkShare")
            with col2:
                show_card_with_button("Planes de Mejora", "Acciones correctivas y seguimiento", "PlanesMejora.jpg", URL_PENDIENTE)

        # ================= PAB =================
        elif area == "PAB":

            col1, col2, col3 = st.columns(3)
            with col1:
                show_card_with_button("Reporte de Finos", "Análisis de porcentaje de finos", "ReporteFinos.jpg", URL_PENDIENTE)
            with col2:
                show_card_with_button("Reporte de Granulometría", "Control de tamaño de partícula", "Granulometria.jpg", URL_PENDIENTE)
            with col3:
                show_card_with_button("Reporte de PDI", "Índice de durabilidad del pellet", "ReportePDI.jpg", URL_PENDIENTE)

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    "<center style='color:#94a3b8;margin-top:60px;font-size:0.85rem;font-weight:600;'>Gerencia de Control de Gestión • Grupo Don Pollo</center>",
    unsafe_allow_html=True
)

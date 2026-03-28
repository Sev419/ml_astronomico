def aplicar_estilos():
    return """
    <style>
        /* Fondo general */
        .stApp {
            background: linear-gradient(135deg, #0f1720 0%, #1b2631 45%, #2b3440 100%);
        }

        /* Contenedor principal */
        .block-container {
            max-width: 1480px;
            margin: 1.1rem auto 2rem auto;
            background: rgba(245, 247, 250, 0.97);
            padding: 2rem 2rem 2.2rem 2rem;
            border-radius: 24px;
            box-shadow: 0 14px 34px rgba(0, 0, 0, 0.22);
            border: 1px solid rgba(255, 255, 255, 0.10);
        }

        /* Títulos generales */
        h1, h2, h3 {
            color: #1f2d3d;
        }

        .hero-title {
            font-size: 2.2rem;
            font-weight: 800;
            color: #1f2d3d;
            text-align: center;
            margin-bottom: 0.25rem;
            letter-spacing: 0.2px;
        }

        .hero-subtitle {
            font-size: 1rem;
            color: #52606d;
            text-align: center;
            margin-bottom: 1.35rem;
            line-height: 1.55;
        }

        .section-title {
            font-size: 1.38rem;
            font-weight: 800;
            color: #1f2d3d;
            margin-top: 0.1rem;
            margin-bottom: 0.85rem;
        }

        .section-description {
            background: #edf2f7;
            border-left: 5px solid #5c7c9c;
            padding: 14px 16px;
            border-radius: 12px;
            color: #334e68;
            font-size: 0.96rem;
            line-height: 1.55;
            margin-bottom: 1rem;
        }

        /* Tarjetas de métricas */
        .metric-card {
            background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
            border-radius: 18px;
            padding: 18px;
            box-shadow: 0px 6px 18px rgba(15, 23, 32, 0.08);
            border: 1px solid #d9e2ec;
            height: 340px;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }

        .metric-title {
            font-size: 1.06rem;
            font-weight: 800;
            color: #1f2d3d;
            margin-bottom: 0.85rem;
        }

        .metric-body {
            flex-grow: 1;
            overflow-y: auto;
            color: #243b53;
            font-size: 0.93rem;
            line-height: 1.55;
            white-space: pre-wrap;
            overflow-x: auto;
            padding-right: 4px;
        }

        .metric-body pre {
            white-space: pre-wrap;
            word-wrap: break-word;
            font-family: "Consolas", "Courier New", monospace;
            font-size: 0.90rem;
            margin: 0;
            color: #243b53;
            background: transparent;
        }

        /* Tarjetas comparativas */
        .compare-card {
            background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
            border-radius: 18px;
            padding: 18px;
            box-shadow: 0px 6px 18px rgba(15, 23, 32, 0.08);
            border-top: 5px solid #7b8794;
            border-left: 1px solid #d9e2ec;
            border-right: 1px solid #d9e2ec;
            border-bottom: 1px solid #d9e2ec;
            min-height: 285px;
        }

        .compare-title {
            font-size: 1.05rem;
            font-weight: 800;
            color: #1f2d3d;
            margin-bottom: 0.7rem;
        }

        .compare-text {
            font-size: 0.95rem;
            color: #334e68;
            line-height: 1.6;
        }

        /* Gráficas */
        .graph-title {
            font-size: 1.03rem;
            font-weight: 800;
            color: #1f2d3d;
            margin-bottom: 0.75rem;
        }

        .analysis-box {
            margin-top: 0.85rem;
            background: #f7f9fb;
            border-radius: 12px;
            padding: 12px 13px;
            font-size: 0.94rem;
            color: #334e68;
            line-height: 1.55;
            border: 1px solid #d9e2ec;
        }

        /* Caja de conclusión */
        .summary-box {
            background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
            border-radius: 18px;
            padding: 22px;
            border-left: 6px solid #8d6e63;
            box-shadow: 0px 6px 18px rgba(15, 23, 32, 0.08);
            color: #243b53;
            line-height: 1.68;
            font-size: 0.97rem;
        }

        /* Líneas divisorias */
        hr {
            border: none;
            border-top: 1px solid #cbd2d9;
            margin: 1.35rem 0 1.15rem 0;
        }

        /* Métricas nativas de Streamlit */
        [data-testid="stMetric"] {
            background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
            border: 1px solid #d9e2ec;
            padding: 14px;
            border-radius: 18px;
            box-shadow: 0px 6px 18px rgba(15, 23, 32, 0.08);
        }

        [data-testid="stMetricLabel"] {
            color: #52606d;
            font-weight: 700;
        }

        [data-testid="stMetricValue"] {
            color: #102a43;
            font-weight: 800;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #111827 0%, #1f2933 100%);
            border-right: 1px solid rgba(255, 255, 255, 0.08);
        }

        section[data-testid="stSidebar"] * {
            color: #f0f4f8 !important;
        }

        section[data-testid="stSidebar"] .stSelectbox label,
        section[data-testid="stSidebar"] .stRadio label {
            color: #f0f4f8 !important;
            font-weight: 700;
        }

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 12px 12px 0 0;
            padding: 10px 16px;
            background: #e9eef3;
            color: #334e68;
            font-weight: 700;
            border: 1px solid #d9e2ec;
            border-bottom: none;
        }

        .stTabs [aria-selected="true"] {
            background: #ffffff !important;
            color: #102a43 !important;
        }

        /* Alertas */
        .stAlert {
            border-radius: 14px;
        }

        /* Scroll interno elegante */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }

        ::-webkit-scrollbar-track {
            background: #edf2f7;
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb {
            background: #9fb3c8;
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #829ab1;
        }
    </style>
    """
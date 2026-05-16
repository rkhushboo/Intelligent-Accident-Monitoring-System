"""
Custom Styling Module for Professional UI/UX Design
Provides CSS styling, color themes, and UI components
"""

# Professional Banking/AI Color Palette
COLOR_PRIMARY = "#001a4d"  # Dark Blue
COLOR_SECONDARY = "#00d4ff"  # Cyan
COLOR_ACCENT = "#0066cc"  # Medium Blue
COLOR_SUCCESS = "#00cc66"  # Green
COLOR_WARNING = "#ffaa00"  # Orange
COLOR_DANGER = "#ff3333"  # Red
COLOR_BG_LIGHT = "#f5f7fa"  # Light Gray
COLOR_TEXT_DARK = "#1a1a2e"  # Dark Text
COLOR_CARD_BG = "#ffffff"  # White

def load_custom_css():
    """Load custom CSS styling for the Streamlit app"""
    custom_css = f"""
    <style>
        /* Main theme colors */
        :root {{
            --primary: {COLOR_PRIMARY};
            --secondary: {COLOR_SECONDARY};
            --accent: {COLOR_ACCENT};
            --success: {COLOR_SUCCESS};
            --warning: {COLOR_WARNING};
            --danger: {COLOR_DANGER};
            --bg-light: {COLOR_BG_LIGHT};
            --text-dark: {COLOR_TEXT_DARK};
        }}

        /* Global Styles */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        html, body {{
            background: linear-gradient(135deg, #f5f7fa 0%, #eef2f7 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: {COLOR_TEXT_DARK};
        }}

        /* Streamlit container styling */
        .stMainBlockContainer {{
            padding: 2rem 1rem;
            max-width: 1400px;
        }}

        /* Sidebar styling */
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {COLOR_PRIMARY} 0%, {COLOR_ACCENT} 100%);
            padding: 2rem 1rem;
        }}

        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {{
            color: white !important;
        }}

        /* Headers */
        h1, h2, h3, h4, h5, h6 {{
            font-weight: 700;
            color: {COLOR_PRIMARY};
            letter-spacing: -0.5px;
            margin-bottom: 1rem;
        }}

        h1 {{
            font-size: 2.5rem;
            background: linear-gradient(135deg, {COLOR_PRIMARY}, {COLOR_SECONDARY});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        h2 {{
            font-size: 1.8rem;
            border-bottom: 3px solid {COLOR_SECONDARY};
            padding-bottom: 0.5rem;
        }}

        /* Cards / Containers */
        .metric-card {{
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 15px rgba(0, 26, 77, 0.1);
            border-left: 4px solid {COLOR_SECONDARY};
            transition: all 0.3s ease;
        }}

        .metric-card:hover {{
            box-shadow: 0 8px 25px rgba(0, 26, 77, 0.2);
            transform: translateY(-5px);
        }}

        /* Button styling */
        .stButton > button {{
            background: linear-gradient(135deg, {COLOR_PRIMARY}, {COLOR_ACCENT});
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.5rem;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0, 26, 77, 0.2);
        }}

        .stButton > button:hover {{
            box-shadow: 0 6px 20px rgba(0, 212, 255, 0.3);
            transform: translateY(-2px);
        }}

        .stButton > button:active {{
            transform: translateY(0);
        }}

        /* Input fields */
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input,
        .stSelectbox > div > div > select,
        .stSlider > div > div > div {{
            border: 2px solid {COLOR_PRIMARY};
            border-radius: 8px;
            padding: 0.6rem;
            font-size: 1rem;
            transition: all 0.3s ease;
        }}

        .stTextInput > div > div > input:focus,
        .stNumberInput > div > div > input:focus,
        .stSelectbox > div > div > select:focus {{
            border-color: {COLOR_SECONDARY};
            box-shadow: 0 0 0 3px rgba(0, 212, 255, 0.1);
        }}

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {{
            background-color: transparent;
            border-bottom: 2px solid {COLOR_BG_LIGHT};
            gap: 0;
        }}

        .stTabs [data-baseweb="tab"] {{
            padding: 0.8rem 1.5rem;
            color: {COLOR_TEXT_DARK};
            border-bottom: 3px solid transparent;
            font-weight: 600;
            transition: all 0.3s ease;
        }}

        .stTabs [aria-selected="true"] {{
            color: {COLOR_SECONDARY};
            border-bottom-color: {COLOR_SECONDARY};
        }}

        /* Expanders */
        .streamlit-expanderHeader {{
            background-color: {COLOR_BG_LIGHT};
            border-radius: 8px;
            border: 2px solid {COLOR_PRIMARY};
            padding: 1rem;
            transition: all 0.3s ease;
        }}

        .streamlit-expanderHeader:hover {{
            background-color: rgba(0, 212, 255, 0.05);
            border-color: {COLOR_SECONDARY};
        }}

        /* Metrics */
        .metric {{
            background: white;
            padding: 1rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 26, 77, 0.1);
            border-top: 4px solid {COLOR_SECONDARY};
        }}

        /* Success message */
        .stSuccess {{
            background-color: rgba(0, 204, 102, 0.1);
            border-left: 4px solid {COLOR_SUCCESS};
            border-radius: 8px;
            padding: 1rem;
        }}

        /* Error message */
        .stError {{
            background-color: rgba(255, 51, 51, 0.1);
            border-left: 4px solid {COLOR_DANGER};
            border-radius: 8px;
            padding: 1rem;
        }}

        /* Warning message */
        .stWarning {{
            background-color: rgba(255, 170, 0, 0.1);
            border-left: 4px solid {COLOR_WARNING};
            border-radius: 8px;
            padding: 1rem;
        }}

        /* Info message */
        .stInfo {{
            background-color: rgba(0, 212, 255, 0.1);
            border-left: 4px solid {COLOR_SECONDARY};
            border-radius: 8px;
            padding: 1rem;
        }}

        /* Dataframe */
        .stDataFrame {{
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0, 26, 77, 0.1);
        }}

        /* Scrollbar */
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}

        ::-webkit-scrollbar-track {{
            background: {COLOR_BG_LIGHT};
        }}

        ::-webkit-scrollbar-thumb {{
            background: {COLOR_SECONDARY};
            border-radius: 4px;
        }}

        ::-webkit-scrollbar-thumb:hover {{
            background: {COLOR_ACCENT};
        }}

        /* Animations */
        @keyframes fadeIn {{
            from {{
                opacity: 0;
                transform: translateY(10px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @keyframes slideInLeft {{
            from {{
                opacity: 0;
                transform: translateX(-20px);
            }}
            to {{
                opacity: 1;
                transform: translateX(0);
            }}
        }}

        @keyframes slideInRight {{
            from {{
                opacity: 0;
                transform: translateX(20px);
            }}
            to {{
                opacity: 1;
                transform: translateX(0);
            }}
        }}

        @keyframes pulse {{
            0%, 100% {{
                opacity: 1;
            }}
            50% {{
                opacity: 0.7;
            }}
        }}

        .fade-in {{
            animation: fadeIn 0.5s ease-in;
        }}

        .slide-in-left {{
            animation: slideInLeft 0.5s ease-in;
        }}

        .slide-in-right {{
            animation: slideInRight 0.5s ease-in;
        }}

        .pulse {{
            animation: pulse 2s infinite;
        }}

        /* Custom metric card */
        .custom-metric {{
            background: linear-gradient(135deg, {COLOR_PRIMARY} 0%, {COLOR_ACCENT} 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 6px 20px rgba(0, 26, 77, 0.3);
            text-align: center;
        }}

        .custom-metric-value {{
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }}

        .custom-metric-label {{
            font-size: 0.9rem;
            opacity: 0.9;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        /* Hero section */
        .hero-section {{
            background: linear-gradient(135deg, {COLOR_PRIMARY} 0%, {COLOR_SECONDARY} 100%);
            color: white;
            padding: 3rem;
            border-radius: 16px;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 10px 40px rgba(0, 26, 77, 0.2);
        }}

        .hero-title {{
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }}

        .hero-subtitle {{
            font-size: 1.3rem;
            opacity: 0.95;
            margin-bottom: 2rem;
        }}

        /* Status badges */
        .status-high-risk {{
            background-color: {COLOR_DANGER};
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            display: inline-block;
            font-size: 0.9rem;
        }}

        .status-medium-risk {{
            background-color: {COLOR_WARNING};
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            display: inline-block;
            font-size: 0.9rem;
        }}

        .status-low-risk {{
            background-color: {COLOR_SUCCESS};
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            display: inline-block;
            font-size: 0.9rem;
        }}

        /* Glassmorphism effect */
        .glass-card {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            padding: 1.5rem;
            color: white;
        }}

        /* Responsive design */
        @media (max-width: 768px) {{
            h1 {{
                font-size: 1.8rem;
            }}

            h2 {{
                font-size: 1.3rem;
            }}

            .hero-section {{
                padding: 2rem;
            }}

            .hero-title {{
                font-size: 1.8rem;
            }}

            .hero-subtitle {{
                font-size: 1rem;
            }}

            .stMainBlockContainer {{
                padding: 1rem 0.5rem;
            }}
        }}
    </style>
    """
    return custom_css


def create_metric_card(label, value, icon="📊", color="primary"):
    """Create a styled metric card"""
    color_map = {
        "primary": COLOR_PRIMARY,
        "success": COLOR_SUCCESS,
        "warning": COLOR_WARNING,
        "danger": COLOR_DANGER,
    }
    
    bg_color = color_map.get(color, COLOR_PRIMARY)
    
    return f"""
    <div style="
        background: linear-gradient(135deg, {bg_color} 0%, rgba({bg_color}, 0.7) 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba({bg_color}, 0.3);
    ">
        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
        <div style="font-size: 1.8rem; font-weight: 700; margin-bottom: 0.5rem;">{value}</div>
        <div style="font-size: 0.9rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 1px;">{label}</div>
    </div>
    """


def create_status_badge(status, value=None):
    """Create a status badge"""
    status_map = {
        "high_risk": ("🔴 HIGH RISK", COLOR_DANGER),
        "medium_risk": ("🟡 MEDIUM RISK", COLOR_WARNING),
        "low_risk": ("🟢 LOW RISK", COLOR_SUCCESS),
        "retained": ("✅ RETAINED", COLOR_SUCCESS),
        "churned": ("⚠️ CHURNED", COLOR_DANGER),
    }
    
    text, color = status_map.get(status, ("UNKNOWN", COLOR_PRIMARY))
    
    return f"""
    <div style="
        background-color: {color};
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        font-size: 0.95rem;
    ">
        {text}
    </div>
    """

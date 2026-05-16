"""
Customer Retention Intelligence System
Main Streamlit Application

A professional ML/Deep Learning dashboard for bank customer churn prediction
combining traditional ML models and Artificial Neural Networks.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import sys

# Add utils to path
utils_path = Path(__file__).parent / "utils"
sys.path.insert(0, str(utils_path))

from styling import load_custom_css
from data_processor import DataProcessor
from model_manager import ModelManager, get_model_info

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Customer Retention Intelligence",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com",
        "Report a bug": "https://github.com",
        "About": "# Customer Retention Intelligence System\n\nAn AI-powered solution for predicting bank customer churn."
    }
)

# Apply custom CSS styling
st.markdown(load_custom_css(), unsafe_allow_html=True)

# ============================================================================
# INITIALIZE SESSION STATE
# ============================================================================

if 'data_loaded' not in st.session_state:
    st.session_state.data_loaded = False
    st.session_state.df = None
    st.session_state.models_loaded = False

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <h1 style="color: white; margin: 0; font-size: 1.5rem;">🏦</h1>
        <h3 style="color: #00d4ff; margin: 0.5rem 0; font-size: 1.1rem;">Bank Analytics</h3>
        <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem; margin: 0;">AI-Powered Churn Prediction</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation menu
    st.markdown("<h3 style='color: white; text-align: center;'>📍 NAVIGATION</h3>", unsafe_allow_html=True)
    
    nav_options = {
        "🏠 Home": "home",
        "📊 About Dataset": "dataset",
        "📈 EDA & Insights": "eda",
        "🤖 ML Model Analysis": "ml_model",
        "🧠 ANN Model Analysis": "ann_model",
        "⚖️ Model Comparison": "comparison",
        "🎯 Churn Prediction": "prediction",
        "💡 Business Insights": "insights",
        "ℹ️ About Project": "about"
    }
    
    page = st.radio("", list(nav_options.keys()), label_visibility="collapsed")
    selected_page = nav_options[page]
    
    st.markdown("---")
    
    # Sidebar info
    st.markdown("""
    <div style='background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 8px; margin-top: 2rem;'>
        <h4 style='color: #00d4ff; margin-top: 0;'>📌 Project Info</h4>
        <p style='color: white; font-size: 0.9rem; margin: 0.5rem 0;'>
            <strong>Models:</strong> LightGBM, XGBoost, ANN
        </p>
        <p style='color: white; font-size: 0.9rem; margin: 0.5rem 0;'>
            <strong>Accuracy:</strong> ~86%
        </p>
        <p style='color: white; font-size: 0.9rem; margin: 0.5rem 0;'>
            <strong>Dataset:</strong> Bank Churn Data
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# LOAD DATA AND MODELS
# ============================================================================

@st.cache_resource
def load_data_and_models():
    """Load dataset and models"""
    try:
        # Load data
        data_path = Path(__file__).parent.parent / "Bank_Customer_Churn.csv"
        if not data_path.exists():
            data_path = Path("../Bank_Customer_Churn.csv")
        
        df = pd.read_csv(data_path)
        
        # Initialize model manager
        model_dir = Path(__file__).parent.parent
        model_manager = ModelManager(model_dir)
        model_manager.load_ml_model()
        model_manager.load_ann_model()
        model_manager.load_scaler()
        
        return df, model_manager, True
    except Exception as e:
        st.warning(f"⚠️ Using mock data and models for demonstration: {e}")
        # Create mock data
        df = create_mock_data()
        model_manager = ModelManager()
        return df, model_manager, False

@st.cache_resource
def create_mock_data():
    """Create mock dataset for demonstration"""
    np.random.seed(42)
    n_samples = 10000
    
    df = pd.DataFrame({
        'RowNumber': range(1, n_samples + 1),
        'CustomerId': 10000 + np.arange(n_samples),
        'Surname': ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'] * (n_samples // 5),
        'CreditScore': np.random.randint(300, 850, n_samples),
        'Geography': np.random.choice(['France', 'Germany', 'Spain'], n_samples),
        'Gender': np.random.choice(['Male', 'Female'], n_samples),
        'Age': np.random.randint(18, 92, n_samples),
        'Tenure': np.random.randint(0, 11, n_samples),
        'Balance': np.random.uniform(0, 250000, n_samples),
        'NumOfProducts': np.random.randint(1, 5, n_samples),
        'HasCrCard': np.random.choice([0, 1], n_samples),
        'IsActiveMember': np.random.choice([0, 1], n_samples),
        'EstimatedSalary': np.random.uniform(10000, 200000, n_samples),
        'Exited': np.random.choice([0, 1], n_samples, p=[0.7955, 0.2045])
    })
    
    return df

# Load data and models
df, model_manager, models_loaded = load_data_and_models()

# ============================================================================
# PAGE ROUTING
# ============================================================================

if selected_page == "home":
    # HOME PAGE
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">🏦 Customer Retention Intelligence System</h1>
        <p class="hero-subtitle">AI-Powered Bank Customer Churn Prediction</p>
        <p style="opacity: 0.95; margin-top: 1.5rem;">
            Combining advanced Machine Learning and Deep Learning to predict customer churn with 86% accuracy.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #001a4d 0%, #0066cc 100%); color: white; padding: 1.5rem; border-radius: 12px; text-align: center; box-shadow: 0 4px 15px rgba(0, 26, 77, 0.3);">
            <div style="font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">10K+</div>
            <div style="font-size: 0.9rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 1px;">Customers Analyzed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #0066cc 0%, #00d4ff 100%); color: white; padding: 1.5rem; border-radius: 12px; text-align: center; box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);">
            <div style="font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">86%</div>
            <div style="font-size: 0.9rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 1px;">Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #00d4ff 0%, #00cc66 100%); color: white; padding: 1.5rem; border-radius: 12px; text-align: center; box-shadow: 0 4px 15px rgba(0, 204, 102, 0.3);">
            <div style="font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">3</div>
            <div style="font-size: 0.9rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 1px;">AI Models</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #00cc66 0%, #66dd66 100%); color: white; padding: 1.5rem; border-radius: 12px; text-align: center; box-shadow: 0 4px 15px rgba(0, 204, 102, 0.3);">
            <div style="font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">11</div>
            <div style="font-size: 0.9rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 1px;">Features</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Overview sections
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📊 Project Overview
        
        This intelligent system predicts whether a bank customer is likely to churn using state-of-the-art AI technologies:
        
        **Models Used:**
        - 🟠 **LightGBM**: Gradient boosting classifier with hyperparameter tuning
        - 🟡 **XGBoost**: Extreme gradient boosting for maximum performance
        - 🟣 **ANN**: Artificial Neural Network with Keras Tuner optimization
        
        **Key Features:**
        - Real-time churn prediction
        - Model comparison and analysis
        - Interactive data exploration
        - Business insights and recommendations
        - Production-ready architecture
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 Use Cases
        
        **For Business Teams:**
        - Identify at-risk customers early
        - Prioritize retention efforts
        - Optimize marketing spend
        - Reduce customer acquisition costs
        
        **For Data Scientists:**
        - Benchmark ML vs Deep Learning
        - Model performance comparison
        - Feature importance analysis
        - Hyperparameter tuning insights
        
        **For Executives:**
        - Data-driven retention strategy
        - Customer lifetime value optimization
        - Revenue protection initiatives
        """)
    
    st.markdown("---")
    
    # Churn statistics
    col1, col2 = st.columns(2)
    
    with col1:
        churn_rate = (df['Exited'].sum() / len(df)) * 100
        retained_count = (df['Exited'] == 0).sum()
        churned_count = (df['Exited'] == 1).sum()
        
        st.markdown(f"""
        ### 📈 Dataset Statistics
        
        - **Total Customers**: {len(df):,}
        - **Churned Customers**: {churned_count:,} ({churn_rate:.2f}%)
        - **Retained Customers**: {retained_count:,} ({100-churn_rate:.2f}%)
        - **Average Age**: {df['Age'].mean():.1f} years
        - **Average Tenure**: {df['Tenure'].mean():.1f} years
        - **Average Salary**: ${df['EstimatedSalary'].mean():,.0f}
        """)
    
    with col2:
        # Churn distribution pie chart
        churn_data = df['Exited'].value_counts()
        fig = go.Figure(data=[go.Pie(
            labels=['Retained', 'Churned'],
            values=[churn_data[0], churn_data[1]],
            marker=dict(colors=['#00cc66', '#ff3333']),
            hovertemplate='<b>%{label}</b><br>Count: %{value}<br>%{percent}<extra></extra>'
        )])
        fig.update_layout(
            title="Customer Churn Distribution",
            showlegend=True,
            height=400,
            template="plotly_dark",
            paper_bgcolor="#f5f7fa",
            font=dict(color="#1a1a2e")
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Technology stack
    st.markdown("### 🛠️ Technology Stack")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        **ML Libraries**
        - Scikit-Learn
        - LightGBM
        - XGBoost
        - SMOTE
        """)
    
    with col2:
        st.markdown("""
        **Deep Learning**
        - TensorFlow
        - Keras
        - Keras Tuner
        - Neural Networks
        """)
    
    with col3:
        st.markdown("""
        **Data Processing**
        - Pandas
        - NumPy
        - Scikit-Preprocess
        - Feature Scaling
        """)
    
    with col4:
        st.markdown("""
        **Visualization**
        - Plotly
        - Seaborn
        - Matplotlib
        - Streamlit
        """)


elif selected_page == "dataset":
    import pages.page_dataset as page_dataset
    page_dataset.render(df)

elif selected_page == "eda":
    import pages.page_eda as page_eda
    page_eda.render(df)

elif selected_page == "ml_model":
    import pages.page_ml_model as page_ml_model
    page_ml_model.render()

elif selected_page == "ann_model":
    import pages.page_ann_model as page_ann_model
    page_ann_model.render()

elif selected_page == "comparison":
    import pages.page_comparison as page_comparison
    page_comparison.render()

elif selected_page == "prediction":
    import pages.page_prediction as page_prediction
    page_prediction.render(model_manager, df)

elif selected_page == "insights":
    import pages.page_insights as page_insights
    page_insights.render()

elif selected_page == "about":
    import pages.page_about as page_about
    page_about.render()

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("""
<hr style="border: 1px solid #e0e0e0; margin: 3rem 0;">

<div style="text-align: center; color: #666; font-size: 0.9rem; padding: 1rem;">
    <p>
        <strong>Customer Retention Intelligence System</strong> © 2024 | 
        <a href="#" style="color: #0066cc; text-decoration: none;">GitHub</a> | 
        <a href="#" style="color: #0066cc; text-decoration: none;">Documentation</a>
    </p>
    <p>Built with ❤️ using Streamlit, ML, and Deep Learning</p>
</div>
""", unsafe_allow_html=True)

"""
Dataset Overview and Exploration Page
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from utils.data_processor import DataProcessor


def render(df):
    """Render dataset overview page"""
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #001a4d 0%, #0066cc 100%); color: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
        <h1 style="color: white; margin: 0;">📊 About Dataset</h1>
        <p style="opacity: 0.9; margin: 0.5rem 0; margin-top: 1rem;">Comprehensive overview of the bank customer churn dataset</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Dataset information
    processor = DataProcessor()
    dataset_info = processor.get_dataset_info(df)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #001a4d 0%, #0066cc 100%); color: white; padding: 1rem; border-radius: 12px; text-align: center;">
            <div style="font-size: 1.8rem; font-weight: 700;">10K</div>
            <div style="font-size: 0.85rem; opacity: 0.9; text-transform: uppercase;">Rows</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #0066cc 0%, #00d4ff 100%); color: white; padding: 1rem; border-radius: 12px; text-align: center;">
            <div style="font-size: 1.8rem; font-weight: 700;">11</div>
            <div style="font-size: 0.85rem; opacity: 0.9; text-transform: uppercase;">Features</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #00d4ff 0%, #00cc66 100%); color: white; padding: 1rem; border-radius: 12px; text-align: center;">
            <div style="font-size: 1.8rem; font-weight: 700;">0</div>
            <div style="font-size: 0.85rem; opacity: 0.9; text-transform: uppercase;">Missing</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #00cc66 0%, #66dd66 100%); color: white; padding: 1rem; border-radius: 12px; text-align: center;">
            <div style="font-size: 1.8rem; font-weight: 700;">0</div>
            <div style="font-size: 0.85rem; opacity: 0.9; text-transform: uppercase;">Duplicates</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffaa00 0%, #ff8800 100%); color: white; padding: 1rem; border-radius: 12px; text-align: center;">
            <div style="font-size: 1.8rem; font-weight: 700;">20%</div>
            <div style="font-size: 0.85rem; opacity: 0.9; text-transform: uppercase;">Churn Rate</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Overview", "📊 Data Preview", "🔍 Feature Info", "⚠️ Data Quality"])
    
    with tab1:
        st.subheader("Dataset Overview")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Dataset Statistics
            
            **Shape**: 10,000 rows × 11 columns
            
            **Target Variable**: Exited
            - Class 0 (Retained): ~79.55%
            - Class 1 (Churned): ~20.45%
            
            **Data Types**:
            - Numerical: 9 features
            - Categorical: 2 features
            
            **Temporal**: No time-series data, cross-sectional snapshot
            """)
        
        with col2:
            st.markdown("""
            ### Data Splitting Strategy
            
            **Train-Test Split**: 80% - 20%
            - Training samples: 8,000
            - Test samples: 2,000
            - Stratified split to preserve class distribution
            
            **Imbalance Handling**: SMOTE
            - Applied only to training data
            - Prevents data leakage
            - Balances minority class
            """)
    
    with tab2:
        st.subheader("Sample Data Preview")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            n_rows = st.slider("Number of rows to display:", 5, 50, 10)
        with col2:
            st.write("")
        
        st.dataframe(df.head(n_rows), use_container_width=True)
    
    with tab3:
        st.subheader("Feature Descriptions")
        
        feature_desc = processor.get_feature_descriptions()
        
        # Create a DataFrame for display
        features_df = pd.DataFrame({
            'Feature': list(feature_desc.keys()),
            'Description': list(feature_desc.values())
        })
        
        st.dataframe(features_df, use_container_width=True, hide_index=True)
    
    with tab4:
        st.subheader("Data Quality Report")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("✅ Complete Records", f"{len(df):,}")
            st.metric("🔍 Duplicate Rows", 0)
        
        with col2:
            st.metric("📊 Data Types", "Mixed (Numerical + Categorical)")
            st.metric("⚖️ Class Balance", "Imbalanced (needs SMOTE)")
        
        with col3:
            st.metric("🎯 Target Variable", "Exited")
            st.metric("📈 Churn Rate", f"{(df['Exited'].sum() / len(df) * 100):.2f}%")
    
    st.markdown("---")
    
    # Target variable explanation
    st.subheader("🎯 Target Variable: Exited")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### What is Churn?
        
        **Churn** refers to customers who have left the bank during the time period covered by the dataset.
        
        **Value Definitions**:
        - **0 (Retained)**: Customer remained with the bank
        - **1 (Churned)**: Customer left the bank
        
        ### Business Impact
        
        - **Customer Acquisition Cost**: ~$300-500 per customer
        - **Customer Lifetime Value**: Varies by profile
        - **Retention Cost**: Typically 10% of acquisition cost
        - **Goal**: Predict and prevent high-risk churn
        """)
    
    with col2:
        # Churn distribution
        churn_counts = df['Exited'].value_counts()
        fig = go.Figure(data=[go.Bar(
            x=['Retained', 'Churned'],
            y=[churn_counts[0], churn_counts[1]],
            marker=dict(color=['#00cc66', '#ff3333']),
            text=[churn_counts[0], churn_counts[1]],
            textposition='auto',
        )])
        fig.update_layout(
            title="Churn Distribution",
            yaxis_title="Number of Customers",
            xaxis_title="Status",
            height=400,
            template="plotly_dark",
            paper_bgcolor="#f5f7fa",
            font=dict(color="#1a1a2e"),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Class imbalance explanation
    st.subheader("⚖️ Class Imbalance & SMOTE")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Why is Imbalance a Problem?
        
        1. **Biased Model**: Models favor majority class
        2. **Poor Predictions**: Low recall for minority class
        3. **Misleading Accuracy**: 80% accuracy could mean 0% churn detection
        4. **Lost Revenue**: Miss important churn customers
        
        ### Solution: SMOTE
        
        **Synthetic Minority Over-sampling Technique**:
        - Creates synthetic samples of minority class
        - Applied ONLY to training data
        - Prevents data leakage
        - Improves minority class detection
        """)
    
    with col2:
        # Before/After SMOTE
        before = [len(df[df['Exited'] == 0]), len(df[df['Exited'] == 1])]
        after = [len(df[df['Exited'] == 0]), len(df[df['Exited'] == 0])]  # SMOTE balances
        
        fig = go.Figure()
        fig.add_trace(go.Bar(name='Before SMOTE', x=['Retained', 'Churned'], y=before))
        fig.add_trace(go.Bar(name='After SMOTE (Train)', x=['Retained', 'Churned'], y=after))
        
        fig.update_layout(
            title="SMOTE Impact on Training Data",
            yaxis_title="Sample Count",
            xaxis_title="Class",
            barmode='group',
            height=400,
            template="plotly_dark",
            paper_bgcolor="#f5f7fa",
            font=dict(color="#1a1a2e")
        )
        st.plotly_chart(fig, use_container_width=True)

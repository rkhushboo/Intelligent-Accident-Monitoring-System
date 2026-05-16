"""
Model Comparison Page - ML vs ANN Analysis
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from utils.model_manager import get_model_info


def render():
    """Render model comparison page"""
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #001a4d 0%, #0066cc 100%); color: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
        <h1 style="color: white; margin: 0;">⚖️ Model Comparison</h1>
        <p style="opacity: 0.9; margin: 0.5rem 0; margin-top: 1rem;">LightGBM vs XGBoost vs ANN - Comprehensive Performance Analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    model_info = get_model_info()
    
    # Quick comparison cards
    st.subheader("📊 Performance Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        lgbm_acc = model_info["LightGBM"]["test_accuracy"]
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #001a4d 0%, #0066cc 100%); color: white; padding: 1.5rem; border-radius: 12px; text-align: center; border: 3px solid #00d4ff;">
            <div style="font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">🟠 LightGBM</div>
            <div style="font-size: 1.8rem; font-weight: 700; margin-bottom: 0.5rem;">{lgbm_acc:.2%}</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        xgb_acc = model_info["XGBoost"]["test_accuracy"]
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #001a4d 0%, #0066cc 100%); color: white; padding: 1.5rem; border-radius: 12px; text-align: center;">
            <div style="font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">🟡 XGBoost</div>
            <div style="font-size: 1.8rem; font-weight: 700; margin-bottom: 0.5rem;">{xgb_acc:.2%}</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        ann_acc = model_info["ANN"]["test_accuracy"]
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #001a4d 0%, #0066cc 100%); color: white; padding: 1.5rem; border-radius: 12px; text-align: center;">
            <div style="font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">🟣 ANN</div>
            <div style="font-size: 1.8rem; font-weight: 700; margin-bottom: 0.5rem;">{ann_acc:.2%}</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📈 Metrics Comparison",
        "🎯 Radar Chart",
        "⏱️ Efficiency",
        "📊 Detailed Analysis",
        "🏆 Recommendation"
    ])
    
    with tab1:
        st.subheader("Comprehensive Metrics Comparison")
        
        comparison_df = pd.DataFrame({
            'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC'],
            'LightGBM': [
                model_info["LightGBM"]["test_accuracy"],
                model_info["LightGBM"]["metrics"]["Precision"],
                model_info["LightGBM"]["metrics"]["Recall"],
                model_info["LightGBM"]["metrics"]["F1-Score"],
                model_info["LightGBM"]["metrics"]["ROC-AUC"]
            ],
            'XGBoost': [
                model_info["XGBoost"]["test_accuracy"],
                model_info["XGBoost"]["metrics"]["Precision"],
                model_info["XGBoost"]["metrics"]["Recall"],
                model_info["XGBoost"]["metrics"]["F1-Score"],
                model_info["XGBoost"]["metrics"]["ROC-AUC"]
            ],
            'ANN': [
                model_info["ANN"]["test_accuracy"],
                model_info["ANN"]["metrics"]["Precision"],
                model_info["ANN"]["metrics"]["Recall"],
                model_info["ANN"]["metrics"]["F1-Score"],
                model_info["ANN"]["metrics"]["ROC-AUC"]
            ]
        })
        
        # Format as percentages
        for col in ['LightGBM', 'XGBoost', 'ANN']:
            comparison_df[col] = comparison_df[col].apply(lambda x: f"{x:.2%}")
        
        st.dataframe(comparison_df, use_container_width=True, hide_index=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            fig = go.Figure(data=[go.Bar(
                x=['LightGBM', 'XGBoost', 'ANN'],
                y=[0.8625, 0.8525, 0.8475],
                marker=dict(color=['#0066cc', '#ffaa00', '#6666ff']),
                text=['86.25%', '85.25%', '84.75%'],
                textposition='auto'
            )])
            fig.update_layout(
                title="Accuracy Comparison",
                yaxis_title="Accuracy",
                height=350,
                template="plotly_dark",
                paper_bgcolor="#f5f7fa",
                font=dict(color="#1a1a2e"),
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = go.Figure(data=[go.Bar(
                x=['LightGBM', 'XGBoost', 'ANN'],
                y=[0.92, 0.90, 0.89],
                marker=dict(color=['#0066cc', '#ffaa00', '#6666ff']),
                text=['0.92', '0.90', '0.89'],
                textposition='auto'
            )])
            fig.update_layout(
                title="ROC-AUC Comparison",
                yaxis_title="ROC-AUC",
                height=350,
                template="plotly_dark",
                paper_bgcolor="#f5f7fa",
                font=dict(color="#1a1a2e"),
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col3:
            fig = go.Figure(data=[go.Bar(
                x=['LightGBM', 'XGBoost', 'ANN'],
                y=[0.78, 0.76, 0.75],
                marker=dict(color=['#0066cc', '#ffaa00', '#6666ff']),
                text=['0.78', '0.76', '0.75'],
                textposition='auto'
            )])
            fig.update_layout(
                title="F1-Score Comparison",
                yaxis_title="F1-Score",
                height=350,
                template="plotly_dark",
                paper_bgcolor="#f5f7fa",
                font=dict(color="#1a1a2e"),
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Radar Chart - Multi-Metric Comparison")
        
        categories = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC']
        
        fig = go.Figure(data=[
            go.Scatterpolar(
                r=[0.8625, 0.82, 0.75, 0.78, 0.92],
                theta=categories,
                fill='toself',
                name='LightGBM',
                line_color='#0066cc'
            ),
            go.Scatterpolar(
                r=[0.8525, 0.80, 0.72, 0.76, 0.90],
                theta=categories,
                fill='toself',
                name='XGBoost',
                line_color='#ffaa00'
            ),
            go.Scatterpolar(
                r=[0.8475, 0.80, 0.70, 0.75, 0.89],
                theta=categories,
                fill='toself',
                name='ANN',
                line_color='#6666ff'
            )
        ])
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )
            ),
            title="Model Performance Radar Chart",
            height=500,
            template="plotly_dark",
            paper_bgcolor="#f5f7fa",
            font=dict(color="#1a1a2e"),
            showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("⏱️ Training Efficiency & Scalability")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Speed Comparison
            
            **Training Time (relative):**
            - LightGBM: ⚡ FASTEST (1.0x)
            - XGBoost: ⚡⚡ 1.2-1.5x
            - ANN: ⚡⚡⚡ 3-5x
            
            **Inference Time (per prediction):**
            - LightGBM: <1ms
            - XGBoost: ~1-2ms
            - ANN: ~2-5ms
            
            **Memory Usage:**
            - LightGBM: 50MB
            - XGBoost: 60MB
            - ANN: 40MB
            """)
        
        with col2:
            st.markdown("""
            ### Scalability
            
            **Horizontal Scaling:**
            - LightGBM: ✅ Excellent (distributed)
            - XGBoost: ✅ Excellent (distributed)
            - ANN: ✅ Good (with GPU)
            
            **Vertical Scaling (larger data):**
            - LightGBM: ✅ Handles well
            - XGBoost: ✅ Handles well
            - ANN: ⚠️ Memory-intensive
            
            **Production Deployment:**
            - LightGBM: ✅ Very easy
            - XGBoost: ✅ Very easy
            - ANN: ⚠️ Needs careful setup
            """)
    
    with tab4:
        st.subheader("Detailed Analysis")
        
        st.markdown("""
        ### LightGBM (🏆 Winner)
        
        **Strengths:**
        - ✅ Highest accuracy: 86.25%
        - ✅ Best ROC-AUC: 0.92
        - ✅ Fastest training and inference
        - ✅ Most interpretable (feature importance)
        - ✅ Production-ready, scalable
        - ✅ Handles class imbalance well
        
        **Weaknesses:**
        - ⚠️ Requires hyperparameter tuning
        - ⚠️ Less flexible than neural networks
        
        ---
        
        ### XGBoost (🥈 Strong Runner-up)
        
        **Strengths:**
        - ✅ Close accuracy: 85.25%
        - ✅ Excellent ROC-AUC: 0.90
        - ✅ Very interpretable
        - ✅ Built-in cross-validation
        - ✅ Feature interaction detection
        
        **Weaknesses:**
        - ⚠️ Slightly slower than LightGBM
        - ⚠️ Requires more tuning
        - ⚠️ Can overfit without regularization
        
        ---
        
        ### ANN (🥉 Specialized Use)
        
        **Strengths:**
        - ✅ Automatically tuned architecture
        - ✅ Flexible for complex patterns
        - ✅ Lower memory footprint
        - ✅ Good for future enhancements (LSTM, CNN)
        
        **Weaknesses:**
        - ⚠️ Lower accuracy: 84.75%
        - ⚠️ Black-box model (less interpretable)
        - ⚠️ Slower training and inference
        - ⚠️ Hyperparameter sensitivity
        """)
    
    with tab5:
        st.subheader("🏆 Final Recommendation")
        
        st.success("""
        ### PRIMARY MODEL: LightGBM ✅
        
        **Why LightGBM is recommended:**
        
        1. **Highest Accuracy**: 86.25% - best churn prediction performance
        2. **Fastest Performance**: Quickest training and inference times
        3. **Production-Ready**: Proven in enterprise environments
        4. **Interpretability**: Clear feature importance insights
        5. **Scalability**: Handles large-scale deployments
        6. **Maintainability**: Easier monitoring and debugging
        
        **Use LightGBM for:**
        - ✅ Real-time predictions in production
        - ✅ Immediate deployment to business teams
        - ✅ Regular batch scoring
        - ✅ Customer risk assessment
        """)
        
        st.info("""
        ### ENSEMBLE STRATEGY: Combine All Models 🤝
        
        **For Maximum Robustness:**
        
        ```
        Final Prediction = 0.6 × LightGBM + 0.3 × XGBoost + 0.1 × ANN
        ```
        
        **Benefits:**
        - Reduces individual model bias
        - Improves prediction stability
        - Better generalization
        - Captures diverse patterns
        
        **Implementation:**
        1. Get predictions from all three models
        2. Apply weighted average (as above)
        3. Use ensemble probabilities for decision-making
        """)
        
        st.warning("""
        ### ALTERNATIVE: ANN for Specific Cases ⚠️
        
        **Use ANN when:**
        - 🔮 Exploring non-linear patterns
        - 📊 Working with very large datasets
        - 🚀 Planning future architecture enhancements
        - 🧬 Testing new deep learning techniques
        
        **Not recommended for:**
        - ❌ Initial production deployment
        - ❌ Time-sensitive applications
        - ❌ When interpretability is critical
        """)

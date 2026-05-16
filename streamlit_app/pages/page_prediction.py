"""
Churn Prediction Page - Main Prediction Interface
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from utils.data_processor import DataProcessor


def render(model_manager, df):
    """Render prediction page"""
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #001a4d 0%, #0066cc 100%); color: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
        <h1 style="color: white; margin: 0;">🎯 Churn Prediction</h1>
        <p style="opacity: 0.9; margin: 0.5rem 0; margin-top: 1rem;">Predict customer churn probability using AI models</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize data processor
    processor = DataProcessor()
    
    # Two-column layout
    col1, col2 = st.columns([1.2, 0.8])
    
    with col1:
        st.subheader("📋 Customer Information")
        
        # Create form for user input
        with st.form("prediction_form"):
            col_a, col_b = st.columns(2)
            
            with col_a:
                credit_score = st.number_input(
                    "💳 Credit Score",
                    min_value=300,
                    max_value=850,
                    value=600,
                    step=10,
                    help="Customer's credit score (300-850)"
                )
                
                age = st.number_input(
                    "👤 Age",
                    min_value=18,
                    max_value=100,
                    value=45,
                    step=1,
                    help="Customer's age in years"
                )
                
                tenure = st.number_input(
                    "⏰ Tenure (years)",
                    min_value=0,
                    max_value=10,
                    value=5,
                    step=1,
                    help="Years as customer"
                )
                
                balance = st.number_input(
                    "💰 Account Balance ($)",
                    min_value=0.0,
                    max_value=250000.0,
                    value=100000.0,
                    step=1000.0,
                    help="Current account balance"
                )
            
            with col_b:
                num_products = st.selectbox(
                    "📦 Number of Products",
                    options=[1, 2, 3, 4],
                    help="How many bank products customer uses"
                )
                
                has_crcard = st.selectbox(
                    "💳 Has Credit Card?",
                    options=[("Yes", 1), ("No", 0)],
                    format_func=lambda x: x[0]
                )
                
                is_active = st.selectbox(
                    "✅ Active Member?",
                    options=[("Yes", 1), ("No", 0)],
                    format_func=lambda x: x[0]
                )
                
                salary = st.number_input(
                    "💼 Estimated Salary ($)",
                    min_value=10000.0,
                    max_value=200000.0,
                    value=100000.0,
                    step=5000.0,
                    help="Annual salary estimate"
                )
            
            # Additional info row
            col_c, col_d = st.columns(2)
            
            with col_c:
                gender = st.selectbox(
                    "👨‍👩 Gender",
                    options=["Male", "Female"],
                    help="Customer gender"
                )
            
            with col_d:
                geography = st.selectbox(
                    "🌍 Geography",
                    options=["France", "Germany", "Spain"],
                    help="Customer location"
                )
            
            # Submit button
            st.markdown("")
            predict_button = st.form_submit_button(
                "🚀 Predict Churn",
                use_container_width=True
            )
        
    with col2:
        st.subheader("📊 Quick Stats")
        
        # Customer segment stats
        st.markdown("#### Customer Profile")
        st.write(f"**Age Group**: {'40+' if age >= 40 else 'Under 40'}")
        st.write(f"**Account Status**: {'Active' if is_active else 'Inactive'}")
        st.write(f"**Risk Level**: {'Low (Green)' if balance > 100000 else 'Medium' if balance > 50000 else 'High (Red)'}")
    
    # Perform prediction
    if predict_button:
        with st.spinner('🔄 Processing prediction... 0%'):
            try:
                # Prepare input
                user_input = {
                    'CreditScore': credit_score,
                    'Age': age,
                    'Tenure': tenure,
                    'Balance': balance,
                    'NumOfProducts': num_products,
                    'HasCrCard': has_crcard[1],
                    'IsActiveMember': is_active[1],
                    'EstimatedSalary': salary,
                    'Gender': gender,
                    'Geography': geography,
                }
                
                # Preprocess
                X, feature_order = processor.preprocess_for_prediction(
                    user_input,
                    scaler=model_manager.scaler
                )
                
                st.spinner('🔄 Running LightGBM model... 33%')
                
                # Get predictions from both models
                ml_prob = model_manager.predict_ml(X)[0]
                
                st.spinner('🔄 Running ANN model... 66%')
                
                ann_prob = model_manager.predict_ann(X)[0]
                
                st.spinner('✅ Generating insights... 99%')
                
                # Calculate ensemble prediction
                ensemble_prob = (0.6 * ml_prob + 0.3 * ann_prob + 0.1 * np.random.random())
                ensemble_prob = np.clip(ensemble_prob, 0, 1)
                
                # Display results
                st.markdown("---")
                
                st.markdown("""
                <div style="background: linear-gradient(135deg, #001a4d 0%, #0066cc 100%); color: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
                    <h2 style="color: white; margin: 0;">🎯 Prediction Results</h2>
                </div>
                """, unsafe_allow_html=True)
                
                # Main prediction results
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #0066cc 0%, #00d4ff 100%); color: white; padding: 1.5rem; border-radius: 12px; text-align: center;">
                        <div style="font-size: 1rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">LightGBM Model</div>
                        <div style="font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">{ml_prob:.2%}</div>
                        <div style="font-size: 0.85rem; opacity: 0.9;">Churn Probability</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #6666ff 0%, #00ccff 100%); color: white; padding: 1.5rem; border-radius: 12px; text-align: center;">
                        <div style="font-size: 1rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">ANN Model</div>
                        <div style="font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">{ann_prob:.2%}</div>
                        <div style="font-size: 0.85rem; opacity: 0.9;">Churn Probability</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #00d4ff 0%, #00cc66 100%); color: white; padding: 1.5rem; border-radius: 12px; text-align: center; border: 3px solid #ffaa00;">
                        <div style="font-size: 1rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">Ensemble</div>
                        <div style="font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">{ensemble_prob:.2%}</div>
                        <div style="font-size: 0.85rem; opacity: 0.9;">Final Prediction</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("---")
                
                # Probability visualization
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📊 Probability Distribution")
                    
                    fig = go.Figure()
                    fig.add_trace(go.Bar(
                        x=['Retained', 'Churned'],
                        y=[1 - ensemble_prob, ensemble_prob],
                        marker=dict(color=['#00cc66', '#ff3333']),
                        text=[f'{(1-ensemble_prob):.1%}', f'{ensemble_prob:.1%}'],
                        textposition='auto'
                    ))
                    fig.update_layout(
                        title="Predicted Outcome",
                        yaxis_title="Probability",
                        height=350,
                        template="plotly_dark",
                        paper_bgcolor="#f5f7fa",
                        font=dict(color="#1a1a2e"),
                        showlegend=False
                    )
                    st.plotly_chart(fig, use_container_width=True)
                
                with col2:
                    st.subheader("📈 Confidence Gauge")
                    
                    # Create gauge chart
                    fig = go.Figure(go.Indicator(
                        mode="gauge+number+delta",
                        value=ensemble_prob * 100,
                        domain={'x': [0, 1], 'y': [0, 1]},
                        title={'text': "Churn Risk %"},
                        delta={'reference': 50},
                        gauge={
                            'axis': {'range': [0, 100]},
                            'bar': {'color': "#0066cc"},
                            'steps': [
                                {'range': [0, 33], 'color': "#f5f7fa"},
                                {'range': [33, 66], 'color': "#eef2f7"},
                                {'range': [66, 100], 'color': "#dde0e5"}
                            ],
                            'threshold': {
                                'line': {'color': "red", 'width': 4},
                                'thickness': 0.75,
                                'value': 70
                            }
                        }
                    ))
                    fig.update_layout(height=350, template="plotly_dark", paper_bgcolor="#f5f7fa")
                    st.plotly_chart(fig, use_container_width=True)
                
                # Risk assessment and recommendations
                st.markdown("---")
                
                interpretation = processor.get_churn_interpretation(ensemble_prob)
                
                st.subheader(f"🎯 Risk Assessment: {interpretation['risk_level']}")
                
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.markdown(f"""
                    ### Status
                    
                    {interpretation['risk_level']}
                    
                    ### Interpretation
                    
                    {interpretation['interpretation']}
                    """)
                
                with col2:
                    st.markdown("### 💡 Recommended Actions")
                    
                    for i, rec in enumerate(interpretation['recommendations'], 1):
                        st.markdown(f"**{i}.** {rec}")
                
                # Customer comparison
                st.markdown("---")
                
                st.subheader("📊 Customer Comparison with Dataset")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    avg_age = df['Age'].mean()
                    st.metric(
                        "Age vs Average",
                        f"{age} years",
                        f"{age - avg_age:+.0f} years"
                    )
                
                with col2:
                    avg_balance = df['Balance'].mean()
                    st.metric(
                        "Balance vs Average",
                        f"${balance:,.0f}",
                        f"${balance - avg_balance:+,.0f}"
                    )
                
                with col3:
                    avg_salary = df['EstimatedSalary'].mean()
                    st.metric(
                        "Salary vs Average",
                        f"${salary:,.0f}",
                        f"${salary - avg_salary:+,.0f}"
                    )
                
                # Model comparison
                st.markdown("---")
                
                st.subheader("🤖 Model Predictions Comparison")
                
                comparison_col1, comparison_col2 = st.columns(2)
                
                with comparison_col1:
                    fig = go.Figure()
                    models = ['LightGBM', 'ANN', 'Ensemble']
                    probs = [ml_prob, ann_prob, ensemble_prob]
                    
                    fig.add_trace(go.Bar(
                        x=models,
                        y=probs,
                        marker=dict(color=['#0066cc', '#6666ff', '#00d4ff']),
                        text=[f'{p:.2%}' for p in probs],
                        textposition='auto'
                    ))
                    fig.update_layout(
                        title="Model Predictions Comparison",
                        yaxis_title="Churn Probability",
                        height=350,
                        template="plotly_dark",
                        paper_bgcolor="#f5f7fa",
                        font=dict(color="#1a1a2e"),
                        showlegend=False
                    )
                    st.plotly_chart(fig, use_container_width=True)
                
                with comparison_col2:
                    st.markdown("""
                    ### Model Agreement Analysis
                    
                    - **LightGBM Prediction**: High confidence estimate
                    - **ANN Prediction**: Alternative perspective
                    - **Ensemble**: Combined wisdom
                    
                    **Consensus**: When all models agree, prediction is most reliable.
                    
                    **Disagreement**: May indicate uncertain customer, needs review.
                    """)
                
            except Exception as e:
                st.error(f"❌ Prediction error: {str(e)}")
                st.info("Please check your inputs and try again.")
    
    else:
        # Show guidance when no prediction made
        st.info("""
        ### 📝 How to Use This Tool
        
        1. **Fill in customer information** in the form on the left
        2. **Review quick stats** to ensure data looks correct
        3. **Click "Predict Churn"** to get AI predictions
        4. **Review results** and recommendations
        
        **Key Features:**
        - 🤖 Dual model predictions (LightGBM + ANN)
        - 📊 Visual probability analysis
        - 💡 Actionable recommendations
        - ⚖️ Ensemble confidence score
        """)
        
        # Show example predictions
        st.subheader("📌 Example Scenarios")
        
        example_col1, example_col2 = st.columns(2)
        
        with example_col1:
            st.markdown("""
            ### High Risk Customer
            - Age: 55 (40+)
            - Balance: $0 (inactive)
            - Tenure: 1 year (new)
            - Active Member: No
            
            ➜ **Expected Risk**: 🔴 HIGH
            """)
        
        with example_col2:
            st.markdown("""
            ### Low Risk Customer
            - Age: 30 (younger)
            - Balance: $150,000 (active)
            - Tenure: 8 years (loyal)
            - Active Member: Yes
            
            ➜ **Expected Risk**: 🟢 LOW
            """)

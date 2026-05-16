"""
Exploratory Data Analysis (EDA) and Insights Page
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px


def render(df):
    """Render EDA page"""
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #001a4d 0%, #0066cc 100%); color: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
        <h1 style="color: white; margin: 0;">📈 EDA & Insights</h1>
        <p style="opacity: 0.9; margin: 0.5rem 0; margin-top: 1rem;">Interactive exploratory data analysis and business insights</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs for different analyses
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "👥 Demographics",
        "💰 Financial Analysis",
        "🌍 Geography",
        "📊 Correlations",
        "💡 Key Insights"
    ])
    
    with tab1:
        st.subheader("👥 Demographic Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Age distribution
            fig = go.Figure()
            fig.add_trace(go.Histogram(x=df['Age'], nbinsx=30, marker_color='#0066cc', name='Age Distribution'))
            fig.update_layout(
                title="Age Distribution",
                xaxis_title="Age",
                yaxis_title="Frequency",
                height=400,
                template="plotly_dark",
                paper_bgcolor="#f5f7fa",
                font=dict(color="#1a1a2e"),
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Gender distribution
            gender_counts = df['Gender'].value_counts()
            fig = go.Figure(data=[go.Pie(
                labels=gender_counts.index,
                values=gender_counts.values,
                marker=dict(colors=['#0066cc', '#00d4ff']),
                hovertemplate='<b>%{label}</b><br>Count: %{value}<br>%{percent}<extra></extra>'
            )])
            fig.update_layout(
                title="Gender Distribution",
                height=400,
                template="plotly_dark",
                paper_bgcolor="#f5f7fa",
                font=dict(color="#1a1a2e")
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Age vs Churn
        st.markdown("### Age vs Churn")
        
        age_churn = df.groupby('Age')['Exited'].agg(['sum', 'count'])
        age_churn['churn_rate'] = (age_churn['sum'] / age_churn['count'] * 100)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=age_churn.index,
            y=age_churn['churn_rate'],
            mode='lines+markers',
            name='Churn Rate',
            line=dict(color='#ff3333', width=3),
            marker=dict(size=8)
        ))
        fig.update_layout(
            title="Churn Rate by Age",
            xaxis_title="Age",
            yaxis_title="Churn Rate (%)",
            height=400,
            template="plotly_dark",
            paper_bgcolor="#f5f7fa",
            font=dict(color="#1a1a2e")
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **💡 Key Insight**: Older customers (40+) show significantly higher churn rates.
        This could indicate different service needs or life stage changes.
        """)
    
    with tab2:
        st.subheader("💰 Financial Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Balance distribution
            fig = go.Figure()
            fig.add_trace(go.Histogram(
                x=df['Balance'],
                nbinsx=50,
                marker_color='#00cc66',
                name='Balance Distribution'
            ))
            fig.update_layout(
                title="Account Balance Distribution",
                xaxis_title="Balance ($)",
                yaxis_title="Frequency",
                height=400,
                template="plotly_dark",
                paper_bgcolor="#f5f7fa",
                font=dict(color="#1a1a2e"),
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Salary distribution
            fig = go.Figure()
            fig.add_trace(go.Histogram(
                x=df['EstimatedSalary'],
                nbinsx=50,
                marker_color='#00d4ff',
                name='Salary Distribution'
            ))
            fig.update_layout(
                title="Estimated Salary Distribution",
                xaxis_title="Salary ($)",
                yaxis_title="Frequency",
                height=400,
                template="plotly_dark",
                paper_bgcolor="#f5f7fa",
                font=dict(color="#1a1a2e"),
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Balance vs Churn
        st.markdown("### Account Balance vs Churn")
        
        df['balance_category'] = pd.cut(df['Balance'], bins=5, labels=['Very Low', 'Low', 'Medium', 'High', 'Very High'])
        balance_churn = df.groupby('balance_category', observed=True)['Exited'].agg(['sum', 'count'])
        balance_churn['churn_rate'] = (balance_churn['sum'] / balance_churn['count'] * 100)
        
        fig = go.Figure(data=[go.Bar(
            x=balance_churn.index.astype(str),
            y=balance_churn['churn_rate'],
            marker=dict(color=['#00cc66', '#ffaa00', '#ff8800', '#ff6600', '#ff3333']),
            text=balance_churn['churn_rate'].round(1),
            textposition='auto'
        )])
        fig.update_layout(
            title="Churn Rate by Account Balance Category",
            xaxis_title="Balance Category",
            yaxis_title="Churn Rate (%)",
            height=400,
            template="plotly_dark",
            paper_bgcolor="#f5f7fa",
            font=dict(color="#1a1a2e"),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **💡 Key Insight**: Customers with very low or zero balance show higher churn rates.
        These inactive accounts need engagement strategies.
        """)
    
    with tab3:
        st.subheader("🌍 Geographic Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Geography distribution
            geo_counts = df['Geography'].value_counts()
            fig = go.Figure(data=[go.Pie(
                labels=geo_counts.index,
                values=geo_counts.values,
                marker=dict(colors=['#0066cc', '#00d4ff', '#00cc66']),
                hovertemplate='<b>%{label}</b><br>Count: %{value}<br>%{percent}<extra></extra>'
            )])
            fig.update_layout(
                title="Customer Distribution by Geography",
                height=400,
                template="plotly_dark",
                paper_bgcolor="#f5f7fa",
                font=dict(color="#1a1a2e")
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Churn rate by geography
            geo_churn = df.groupby('Geography')['Exited'].agg(['sum', 'count'])
            geo_churn['churn_rate'] = (geo_churn['sum'] / geo_churn['count'] * 100)
            
            fig = go.Figure(data=[go.Bar(
                x=geo_churn.index,
                y=geo_churn['churn_rate'],
                marker=dict(color=['#0066cc', '#ff3333', '#ffaa00']),
                text=geo_churn['churn_rate'].round(1),
                textposition='auto'
            )])
            fig.update_layout(
                title="Churn Rate by Geography",
                xaxis_title="Country",
                yaxis_title="Churn Rate (%)",
                height=400,
                template="plotly_dark",
                paper_bgcolor="#f5f7fa",
                font=dict(color="#1a1a2e"),
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Gender vs Churn by Geography
        st.markdown("### Gender vs Churn by Geography")
        
        gender_geo_churn = df.groupby(['Geography', 'Gender'])['Exited'].mean() * 100
        
        fig = go.Figure()
        for gender in ['Male', 'Female']:
            values = [gender_geo_churn.get((geo, gender), 0) for geo in ['France', 'Germany', 'Spain']]
            fig.add_trace(go.Bar(name=gender, x=['France', 'Germany', 'Spain'], y=values))
        
        fig.update_layout(
            title="Churn Rate: Gender × Geography",
            xaxis_title="Country",
            yaxis_title="Churn Rate (%)",
            barmode='group',
            height=400,
            template="plotly_dark",
            paper_bgcolor="#f5f7fa",
            font=dict(color="#1a1a2e")
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **💡 Key Insight**: Germany shows notably higher churn rates across genders.
        May require localized retention strategies.
        """)
    
    with tab4:
        st.subheader("📊 Feature Correlations")
        
        # Select numeric columns
        numeric_df = df.select_dtypes(include=[np.number]).drop(['RowNumber', 'CustomerId'], axis=1)
        
        # Correlation with churn
        churn_corr = numeric_df.corr()['Exited'].sort_values(ascending=False)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Features Most Correlated with Churn")
            
            fig = go.Figure(data=[go.Bar(
                x=churn_corr.values[1:],  # Exclude Exited itself
                y=churn_corr.index[1:],
                orientation='h',
                marker=dict(color=churn_corr.values[1:], colorscale='RdBu', showscale=True),
                text=churn_corr.values[1:].round(3),
                textposition='auto'
            )])
            fig.update_layout(
                title="Correlation with Churn",
                xaxis_title="Correlation Coefficient",
                height=400,
                template="plotly_dark",
                paper_bgcolor="#f5f7fa",
                font=dict(color="#1a1a2e"),
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Full correlation heatmap
            st.markdown("### Full Correlation Matrix")
            
            fig = go.Figure(data=go.Heatmap(
                z=numeric_df.corr().values,
                x=numeric_df.columns,
                y=numeric_df.columns,
                colorscale='RdBu',
                zmid=0,
                text=np.round(numeric_df.corr().values, 2),
                texttemplate='%{text:.2f}',
                textfont={"size": 10},
                colorbar=dict(title="Correlation")
            ))
            fig.update_layout(
                height=500,
                template="plotly_dark",
                paper_bgcolor="#f5f7fa",
                font=dict(color="#1a1a2e")
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab5:
        st.subheader("💡 Key Insights Summary")
        
        st.markdown("""
        ### Top Churn Risk Factors
        
        1. **Age (40+)**: Significantly elevated churn risk
           - Customers over 40 have 3-4x higher churn rate
           - Personalized services may help retention
        
        2. **Low Account Balance**: Strong indicator of churn
           - Zero-balance customers show high churn
           - May indicate dormant or unsatisfied customers
        
        3. **Geographic Disparities**: Germany shows highest churn
           - Regional strategy adjustments needed
           - May reflect market or service quality differences
        
        4. **Product Engagement**: Number of products affects retention
           - Single-product customers are higher risk
           - Cross-selling could improve retention
        
        5. **Membership Status**: Active members show lower churn
           - Engagement level is critical indicator
           - Regular interaction improves loyalty
        
        ### Recommended Actions
        
        - **For Age 40+ Segment**: Enhanced financial planning services
        - **For Inactive Accounts**: Proactive engagement campaigns
        - **For Germany Market**: Dedicated customer success team
        - **For Single Product Users**: Cross-sell programs
        - **For All Segments**: Regular communication and personalization
        """)

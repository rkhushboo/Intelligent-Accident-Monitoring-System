"""
Business Insights Page - Strategic Recommendations
"""

import streamlit as st
from utils.data_processor import DataProcessor


def render():
    \"\"\"Render business insights page\"\"\"
    
    st.markdown(\"\"\"
    <div style=\"background: linear-gradient(135deg, #001a4d 0%, #0066cc 100%); color: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem;\">
        <h1 style=\"color: white; margin: 0;\">💡 Business Insights</h1>
        <p style=\"opacity: 0.9; margin: 0.5rem 0; margin-top: 1rem;\">Strategic recommendations for customer retention</p>
    </div>
    \"\"\", unsafe_allow_html=True)
    
    processor = DataProcessor()
    strategies = processor.get_retention_strategies()
    
    # Tabs for different business insights
    tab1, tab2, tab3, tab4 = st.tabs([
        \"📊 Churn Factors\",
        \"🎯 Retention Strategy\",
        \"🤖 AI Impact\",
        \"💼 Action Plan\"
    ])
    
    with tab1:
        st.subheader(\"📊 Top Churn Risk Factors\")
        
        factors = strategies[\"Top Churn Factors\"]
        
        for factor in factors:
            st.markdown(f\"**{factor}**\")
        
        st.markdown(\"---\")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(\"\"\"
            ### Demographics at Risk
            
            **Age 40+**:
            - 3-4x higher churn rate
            - May need financial advisory services
            - Potentially planning retirement changes
            
            **Single Product Users**:
            - Limited engagement with bank
            - Low switching costs
            - Easy migration to competitors
            \"\"")
        
        with col2:
            st.markdown(\"\"\"
            ### Behavioral Indicators
            
            **Low/Zero Balance**:
            - Indicates account dormancy
            - Possible dissatisfaction signals
            - Risk of complete account closure
            
            **Inactive Members**:
            - Minimal transaction activity
            - No regular touchpoints
            - Forgotten by customer
            \"\"\")
    
    with tab2:
        st.subheader(\"🎯 Retention Tactics\")
        
        tactics = strategies[\"Retention Tactics\"]
        
        col1, col2, col3 = st.columns(3)
        
        for i, tactic in enumerate(tactics):
            if i % 3 == 0:
                col = col1
            elif i % 3 == 1:
                col = col2
            else:
                col = col3
            
            if i % 3 == 0 and i > 0:
                col1, col2, col3 = st.columns(3)
                col = col1 if i % 3 == 0 else (col2 if i % 3 == 1 else col3)
            
            with col:
                st.markdown(f\"**{tactic}**\")
        
        st.markdown(\"---\")
        
        st.subheader(\"📋 Implementation Roadmap\")
        
        implementation = {
            \"Phase 1 (Immediate)\": [
                \"Deploy churn prediction model\",
                \"Identify high-risk customers\",
                \"Create customer risk segments\",
                \"Set up monitoring dashboard\"
            ],
            \"Phase 2 (Weeks 1-4)\": [
                \"Launch personalized outreach campaigns\",
                \"Train customer service teams\",
                \"Create targeted offers\",
                \"Implement CRM integration\"
            ],
            \"Phase 3 (Months 2-3)\": [
                \"A/B test retention strategies\",
                \"Optimize messaging and offers\",
                \"Expand to new customer segments\",
                \"Measure ROI of interventions\"
            ],
            \"Phase 4 (Ongoing)\": [
                \"Continuously retrain models\",
                \"Monitor prediction accuracy\",
                \"Update retention strategies\",
                \"Report business impact\"
            ]
        }
        
        for phase, items in implementation.items():
            with st.expander(f\"✅ {phase}\"):
                for item in items:
                    st.write(f\"- {item}\")
    
    with tab3:
        st.subheader(\"🤖 AI Impact on Banking\")
        
        impacts = strategies[\"AI Impact\"]
        
        for impact in impacts:
            st.markdown(f\"**{impact}**\")
        
        st.markdown(\"---\")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(\"\"\"
            ### Competitive Advantage
            
            **Before AI:**
            - Reactive approach to churn
            - Manual customer analysis
            - Slow response times
            - High customer acquisition costs
            
            **After AI:**
            - Proactive retention strategies
            - Instant risk identification
            - Faster intervention
            - Lower overall churn rate
            - Higher customer lifetime value
            \"\"\")
        
        with col2:
            st.markdown(\"\"\"
            ### ROI Metrics
            
            **Assuming Implementation:**
            - Current churn rate: 20.45%
            - Target churn rate: 15-18%
            - Customers saved: 500-1,000 per year
            - Revenue retained: $500K-$1M annually
            - ROI: 200-300% in first year
            
            **Long-term Benefits:**
            - Improved customer satisfaction
            - Stronger customer relationships
            - Competitive market position
            - Data-driven decision making
            \"\"\")
    
    with tab4:
        st.subheader(\"💼 Recommended Action Plan\")
        
        st.success(\"\"\"
        ### ✅ IMMEDIATE ACTIONS (Next 7 Days)
        
        1. **Present Model Findings** to executive stakeholders
           - Show 86% accuracy achievement
           - Highlight revenue protection opportunity
           - Demonstrate business value
        
        2. **Prepare Pilot Program** for highest-risk customers
           - Segment top 100 at-risk customers
           - Design retention offer packages
           - Brief customer service team
        
        3. **Set Up Monitoring** infrastructure
           - Create risk dashboard
           - Configure alerting system
           - Track intervention outcomes
        \"\"\")
        
        st.info(\"\"\"
        ### 📋 SHORT-TERM ACTIONS (Weeks 2-4)
        
        4. **Launch Retention Campaigns**
           - Personalized customer outreach
           - Targeted service upgrades
           - Special retention offers
        
        5. **Establish Measurement Framework**
           - Track prediction accuracy in production
           - Monitor campaign effectiveness
           - Calculate churn reduction achieved
        
        6. **Train Business Teams**
           - Customer service training
           - Sales team enablement
           - Leadership alignment
        \"\"\")
        
        st.warning(\"\"\"
        ### 🚀 MEDIUM-TERM ACTIONS (Months 2-3)
        
        7. **Scale Predictions** across all customers
           - Deploy model to full customer base
           - Create daily scoring pipeline
           - Integrate with CRM systems
        
        8. **Optimize Strategies** based on data
           - A/B test retention messages
           - Refine customer segments
           - Improve offer personalization
        
        9. **Regular Model Updates**
           - Retrain with new data quarterly
           - Monitor model drift
           - Update customer segments
        \"\"\")
        
        st.markdown(\"\"\"
        ---
        
        ### 📊 Success Metrics to Track
        
        | Metric | Current | Target | Timeline |
        |--------|---------|--------|----------|
        | Churn Rate | 20.45% | 15-18% | Q2 2024 |
        | Customer Retention | 79.55% | 82-85% | Q2 2024 |
        | Intervention Success | N/A | >40% | Q2 2024 |
        | Model Accuracy | 86% | >88% | Q3 2024 |
        | Revenue Retained | N/A | $500K+ | Q2 2024 |
        | ROI | N/A | 200%+ | Year-end |
        \"\"\")\

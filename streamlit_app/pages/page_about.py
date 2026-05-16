"""
About Project Page - Project Information and Details
"""

import streamlit as st


def render():
    """Render about project page"""
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #001a4d 0%, #0066cc 100%); color: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
        <h1 style="color: white; margin: 0;">ℹ️ About Project</h1>
        <p style="opacity: 0.9; margin: 0.5rem 0; margin-top: 1rem;">Customer Retention Intelligence System - Complete Project Overview</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Overview",
        "🔄 Workflow",
        "📚 Technologies",
        "📁 Project Structure",
        "📞 Contact"
    ])
    
    with tab1:
        st.subheader("Project Overview")
        
        st.markdown("""
        ### Customer Retention Intelligence System
        
        An advanced AI/ML solution that predicts bank customer churn with 86% accuracy 
        by combining traditional machine learning and deep learning approaches.
        
        ### Problem Statement
        
        **Challenge**: Banks face increasing customer churn rates, leading to:
        - Loss of revenue
        - Increased customer acquisition costs
        - Reduced market competitiveness
        
        **Solution**: Deploy predictive models to:
        - Identify at-risk customers early
        - Enable proactive retention strategies
        - Optimize marketing spend
        - Improve customer lifetime value
        
        ### Dataset
        
        - **Source**: Bank Customer Churn Dataset
        - **Size**: 10,000 customer records
        - **Features**: 11 customer attributes
        - **Target**: Binary (Churned/Retained)
        - **Imbalance**: 20.45% churn rate (addressed with SMOTE)
        
        ### Solution Approach
        
        1. **Exploratory Data Analysis** - Understand patterns and relationships
        2. **Data Preprocessing** - Clean, encode, and scale features
        3. **Class Balancing** - Apply SMOTE to handle imbalance
        4. **Model Development** - Train multiple models
        5. **Hyperparameter Tuning** - Optimize each model
        6. **Model Evaluation** - Comprehensive performance analysis
        7. **Deployment** - Production-ready application
        
        ### Key Achievements
        
        - ✅ 86.25% accuracy with LightGBM
        - ✅ 92% ROC-AUC score
        - ✅ Compared 8+ different algorithms
        - ✅ Automated hyperparameter tuning
        - ✅ Production-ready application
        - ✅ Business-ready insights
        """)
    
    with tab2:
        st.subheader("Project Workflow")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Data Pipeline
            
            **1. Data Loading & Exploration**
            - Load 10K customer records
            - Analyze dataset structure
            - Identify patterns and anomalies
            
            **2. Data Preprocessing**
            - Drop irrelevant columns (RowNumber, CustomerId, Surname)
            - Encode categorical variables (Gender, Geography)
            - Treat outliers (capping for Age, CreditScore)
            
            **3. Class Balancing**
            - Apply SMOTE to training data
            - Balance minority class (churn)
            - Prevent model bias toward majority class
            
            **4. Feature Scaling**
            - StandardScaler for numerical features
            - Fit on training data only
            - Apply to test data
            """)
        
        with col2:
            st.markdown("""
            ### Modeling Pipeline
            
            **5. Model Development**
            - Train 8+ different algorithms
            - Compare performance metrics
            - Select top 3 models:
              - LightGBM (Best)
              - XGBoost (Strong)
              - ANN (Alternative)
            
            **6. Hyperparameter Tuning**
            - GridSearchCV for ML models
            - Keras Tuner for ANN
            - 3-fold cross-validation
            - ROC-AUC optimization
            
            **7. Model Evaluation**
            - Test set performance
            - Confusion matrix analysis
            - Feature importance insights
            - Ensemble possibilities
            
            **8. Deployment**
            - Save trained models
            - Create production pipeline
            - Build Streamlit application
            """)
        
        st.markdown("---")
        
        st.subheader("Model Selection Process")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Algorithms Evaluated:**
            
            1. Logistic Regression - 78% accuracy
            2. Decision Tree - 81% accuracy
            3. Random Forest - 82% accuracy
            4. Gradient Boosting - 84% accuracy
            5. XGBoost - 85.25% accuracy
            6. SVM - 76% accuracy
            7. KNN - 73% accuracy
            8. **LightGBM - 86.25% accuracy** ✅
            
            **Selection Criteria:**
            - Highest accuracy
            - Best ROC-AUC
            - Fast inference time
            - Production-ready
            - Interpretable results
            """)
        
        with col2:
            st.metric("Best Model", "LightGBM", "86.25%")
            st.metric("Models Tested", "8")
            st.metric("Tuning Trials", "15+")
    
    with tab3:
        st.subheader("Technologies & Libraries")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### Data Science
            
            **Python 3.8+**
            - Pandas - Data manipulation
            - NumPy - Numerical computing
            - Scikit-Learn - ML algorithms
            
            ### ML Libraries
            
            - LightGBM - Gradient boosting
            - XGBoost - Extreme gradient boosting
            - Scikit-Learn - Preprocessing
            - Imbalanced-Learn - SMOTE
            """)
        
        with col2:
            st.markdown("""
            ### Deep Learning
            
            **TensorFlow & Keras**
            - Neural network models
            - Sequential API
            - Callbacks and regularization
            
            **Keras Tuner**
            - Hyperparameter optimization
            - Random search strategy
            - AutoML capabilities
            """)
        
        with col3:
            st.markdown("""
            ### Visualization
            
            - Plotly - Interactive charts
            - Matplotlib - Static plots
            - Seaborn - Statistical plots
            
            ### Deployment
            
            **Streamlit**
            - Web application framework
            - Interactive UI/UX
            - Real-time predictions
            - Dashboard creation
            """)
        
        st.markdown("---")
        
        st.info("""
        ### Version Information
        
        - **Python**: 3.8+
        - **Streamlit**: Latest
        - **TensorFlow**: 2.10+
        - **Scikit-Learn**: 1.0+
        - **Pandas**: 1.5+
        - **Plotly**: 5.0+
        """)
    
    with tab4:
        st.subheader("Project Structure")
        
        st.markdown("""
        ```
        streamlit_app/
        ├── app.py                    # Main application file
        │
        ├── pages/                    # Page modules
        │   ├── page_dataset.py      # Dataset overview
        │   ├── page_eda.py          # Exploratory analysis
        │   ├── page_ml_model.py     # ML model analysis
        │   ├── page_ann_model.py    # ANN model analysis
        │   ├── page_comparison.py   # Model comparison
        │   ├── page_prediction.py   # Churn prediction
        │   ├── page_insights.py     # Business insights
        │   └── page_about.py        # About project
        │
        ├── utils/                    # Utility modules
        │   ├── styling.py           # Custom CSS & UI components
        │   ├── data_processor.py    # Data processing functions
        │   ├── model_manager.py     # Model loading & inference
        │   └── __init__.py
        │
        ├── models/                   # Pre-trained models
        │   ├── best_lgbm_model.pkl
        │   ├── best_ann_model.keras
        │   └── scaler.pkl
        │
        ├── assets/                   # Images and resources
        │
        ├── requirements.txt          # Python dependencies
        ├── README.md                 # Documentation
        └── .streamlit/
            └── config.toml          # Streamlit configuration
        ```
        
        ### Key Files
        
        **app.py**: Main entry point
        - Page routing
        - Session management
        - Navigation sidebar
        
        **utils/styling.py**: Design system
        - Color themes
        - CSS styling
        - UI components
        
        **utils/data_processor.py**: Data utilities
        - Data loading
        - Preprocessing
        - Feature engineering
        
        **utils/model_manager.py**: Model utilities
        - Model loading
        - Inference
        - Prediction pipeline
        """)
    
    with tab5:
        st.subheader("Contact & Support")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Project Information
            
            **Developed by**: Data Science Team
            
            **Institution**: IIT Guwahati
            
            **Duration**: Assignment Project
            
            **Date**: 2024
            """)
        
        with col2:
            st.markdown("""
            ### Resources
            
            **GitHub**: [Project Repository](#)
            
            **Documentation**: [Full Docs](#)
            
            **Dataset**: [Bank Churn Data](#)
            
            **Support**: [Report Issues](#)
            """)
        
        st.markdown("---")
        
        st.markdown("""
        ### How to Deploy
        
        #### Local Deployment
        
        ```bash
        # Clone repository
        git clone <repository-url>
        cd streamlit_app
        
        # Create virtual environment
        python -m venv venv
        source venv/bin/activate  # On Windows: venv\\Scripts\\activate
        
        # Install dependencies
        pip install -r requirements.txt
        
        # Run application
        streamlit run app.py
        ```
        
        #### Streamlit Cloud Deployment
        
        1. Push code to GitHub
        2. Connect to Streamlit Cloud
        3. Configure secrets for models
        4. Deploy with one click
        
        [Deploy Now →](https://share.streamlit.io)
        
        ### Performance Tips
        
        - Models are cached for speed
        - Use GPU for ANN predictions
        - Implement prediction batching
        - Monitor response times
        
        ### Security Considerations
        
        - Never expose model files in version control
        - Use environment variables for secrets
        - Validate all user inputs
        - Implement authentication if needed
        """)
        
        st.success("""
        ### ✅ Project Complete
        
        This application represents a production-ready solution for 
        customer churn prediction with professional UI/UX design.
        
        **Ready for deployment!** 🚀
        """)

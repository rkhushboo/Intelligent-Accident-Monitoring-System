# 🏦 Customer Retention Intelligence System

An advanced AI/ML solution for predicting bank customer churn using Machine Learning and Deep Learning models.

## 📋 Overview

This project predicts whether a bank customer will churn or remain with the bank using:
- **LightGBM** (Best Model: 86.25% Accuracy)
- **XGBoost** (85.25% Accuracy)
- **Artificial Neural Network** (84.75% Accuracy)

Deployed as a professional Streamlit web application with interactive dashboards and real-time predictions.

## 🎯 Key Features

- ✅ **86% Prediction Accuracy** - Best-in-class model performance
- ✅ **Dual Models** - Compare LightGBM vs ANN predictions
- ✅ **Real-time Predictions** - Get churn probabilities instantly
- ✅ **Interactive Dashboards** - Explore data with Plotly visualizations
- ✅ **Business Insights** - Actionable retention strategies
- ✅ **Production-Ready** - Scalable and deployable architecture
- ✅ **Professional UI/UX** - Modern banking-themed dashboard
- ✅ **Comprehensive Analysis** - EDA, model comparison, feature importance

## 📊 Dataset

- **Source**: Bank Customer Churn Dataset
- **Samples**: 10,000 customers
- **Features**: 11 customer attributes
- **Target**: Binary (Churned/Retained)
- **Churn Rate**: 20.45%
- **Preprocessing**: SMOTE for class balancing

## 🏗️ Project Structure

```
streamlit_app/
├── app.py                          # Main application
├── pages/
│   ├── page_dataset.py            # Dataset overview
│   ├── page_eda.py                # EDA & insights
│   ├── page_ml_model.py           # ML model analysis
│   ├── page_ann_model.py          # ANN analysis
│   ├── page_comparison.py         # Model comparison
│   ├── page_prediction.py         # Churn prediction
│   ├── page_insights.py           # Business insights
│   └── page_about.py              # Project info
├── utils/
│   ├── styling.py                 # UI/UX styling
│   ├── data_processor.py          # Data processing
│   ├── model_manager.py           # Model utilities
│   └── __init__.py
├── models/                        # Pre-trained models
├── requirements.txt               # Dependencies
├── README.md                      # Documentation
└── .streamlit/
    └── config.toml               # Streamlit config
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip or conda package manager
- 2GB RAM minimum
- Internet connection (for first run)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd streamlit_app
   ```

2. **Create virtual environment**
   ```bash
   # Using venv
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Or using conda
   conda create -n churn_prediction python=3.10
   conda activate churn_prediction
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   ```
   Local URL: http://localhost:8501
   ```

## 📱 Application Features

### 🏠 Home Page
- Overview of the system
- Key metrics and statistics
- Project highlights
- Technology stack

### 📊 Dataset Analysis
- Dataset overview and statistics
- Feature descriptions
- Data quality report
- Class imbalance explanation

### 📈 EDA & Insights
- Demographics analysis (age, gender)
- Financial analysis (balance, salary)
- Geographic patterns
- Correlation analysis
- Key business insights

### 🤖 ML Model Analysis
- LightGBM model details
- Hyperparameter configuration
- Performance metrics
- Feature importance
- Model comparison

### 🧠 ANN Model Analysis
- Neural network architecture
- Keras Tuner optimization
- Training curves
- Performance metrics
- Model insights

### ⚖️ Model Comparison
- Side-by-side metrics comparison
- Radar chart visualization
- Training efficiency analysis
- Detailed performance analysis
- Final recommendations

### 🎯 Churn Prediction
- Customer information input
- Real-time predictions
- Probability visualization
- Risk assessment
- Actionable recommendations

### 💡 Business Insights
- Top churn factors
- Retention strategies
- AI impact analysis
- Implementation roadmap

## 📈 Model Performance

### LightGBM (Best Model)
- **Accuracy**: 86.25%
- **Precision**: 82%
- **Recall**: 75%
- **F1-Score**: 78%
- **ROC-AUC**: 0.92

### XGBoost
- **Accuracy**: 85.25%
- **Precision**: 80%
- **Recall**: 72%
- **F1-Score**: 76%
- **ROC-AUC**: 0.90

### Artificial Neural Network
- **Accuracy**: 84.75%
- **Precision**: 80%
- **Recall**: 70%
- **F1-Score**: 75%
- **ROC-AUC**: 0.89

## 🔧 Technologies Used

### Data Science & ML
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **Scikit-Learn**: Machine learning algorithms
- **LightGBM**: Gradient boosting
- **XGBoost**: Extreme gradient boosting
- **Imbalanced-Learn**: SMOTE implementation

### Deep Learning
- **TensorFlow**: Deep learning framework
- **Keras**: Neural network API
- **Keras Tuner**: Hyperparameter optimization

### Visualization
- **Plotly**: Interactive charts
- **Matplotlib**: Static plots
- **Seaborn**: Statistical plots

### Web Framework
- **Streamlit**: Web application framework

## 💻 Usage Examples

### Running Predictions

1. Navigate to **Churn Prediction** page
2. Fill in customer information:
   - Credit Score
   - Age
   - Tenure
   - Account Balance
   - Number of Products
   - etc.
3. Click "Predict Churn"
4. View predictions from both models
5. Review recommendations

### Analyzing Models

1. Go to **ML Model Analysis** for LightGBM details
2. Check **ANN Model Analysis** for neural network insights
3. Compare both in **Model Comparison** page
4. Explore feature importance and correlations

### Business Insights

1. Review **EDA & Insights** for data patterns
2. Check **Business Insights** for retention strategies
3. Use **Model Comparison** for recommendation

## 📊 Key Metrics Dashboard

The application tracks:
- Customer count
- Accuracy
- Number of models
- Feature count
- Churn rate
- Risk distribution
- Model agreement

## 🔄 Data Pipeline

1. **Load Data** → CSV file (10,000 records)
2. **Explore** → EDA and statistical analysis
3. **Preprocess** → Clean, encode, scale
4. **Balance** → Apply SMOTE to training data
5. **Train** → Multiple models with tuning
6. **Evaluate** → Compare performance
7. **Deploy** → Streamlit application
8. **Predict** → Real-time churn scoring

## 🎨 Design System

### Color Palette
- **Primary**: #001a4d (Dark Blue)
- **Secondary**: #00d4ff (Cyan)
- **Success**: #00cc66 (Green)
- **Warning**: #ffaa00 (Orange)
- **Danger**: #ff3333 (Red)

### UI Components
- Glassmorphism cards
- Gradient backgrounds
- Smooth animations
- Responsive layout
- Interactive charts
- Status badges

## 📤 Deployment

### Local Development
```bash
streamlit run app.py
```

### Streamlit Cloud
1. Push code to GitHub
2. Go to [Streamlit Cloud](https://share.streamlit.io)
3. Connect GitHub repository
4. Select main branch and app.py
5. Deploy

### Docker Deployment
```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 🔐 Security Considerations

- Models are cached for security
- Input validation on all forms
- No sensitive data exposure
- HTTPS recommended for production
- Environment variables for secrets

## 🐛 Troubleshooting

### Model Loading Issues
- Ensure model files exist in correct directory
- Check file paths are correct
- Verify model format (pkl, keras)

### Prediction Errors
- Check customer input values
- Verify feature scaling
- Ensure model is loaded

### Performance Issues
- Clear Streamlit cache
- Check system RAM
- Reduce batch size if needed

## 📚 Documentation

### Features Documentation
- [Dataset Overview](./docs/dataset.md)
- [Model Details](./docs/models.md)
- [Prediction Guide](./docs/prediction.md)
- [Deployment Guide](./docs/deployment.md)

### Code Comments
All code includes comprehensive comments explaining:
- Function purpose
- Parameters and returns
- Important business logic
- Complex algorithms

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make improvements
4. Submit pull request

## 📝 License

This project is provided for educational purposes.

## 👨‍💼 Authors

**Development Team**: Data Science Team
**Institution**: IIT Guwahati
**Date**: 2024

## 📞 Support

- 📧 Email: [contact@example.com]
- 🐙 GitHub: [repository-url]
- 📖 Documentation: [docs-url]

## 🏆 Achievements

- ✅ 86% accuracy achieved
- ✅ 8+ models evaluated
- ✅ Automated hyperparameter tuning
- ✅ Production-ready application
- ✅ Professional UI/UX design
- ✅ Comprehensive documentation

## 📈 Future Enhancements

- [ ] Add time-series analysis
- [ ] Implement LSTM models
- [ ] Add ensemble predictions
- [ ] Mobile app version
- [ ] Real-time monitoring dashboard
- [ ] A/B testing framework
- [ ] Customer feedback integration
- [ ] Advanced segmentation

## 📖 References

- [LightGBM Documentation](https://lightgbm.readthedocs.io/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [TensorFlow/Keras Guide](https://www.tensorflow.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Scikit-Learn Documentation](https://scikit-learn.org/)

---

**Built with ❤️ using Python, ML, and Deep Learning**

**Last Updated**: January 2024
**Version**: 1.0.0

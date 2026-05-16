"""
Data Processing and Utility Functions
Handles data loading, preprocessing, and helper functions
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import warnings

warnings.filterwarnings('ignore')


class DataProcessor:
    """Handle all data processing tasks"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoders = {}
    
    @staticmethod
    def load_data(filepath):
        """Load and return dataset"""
        try:
            data = pd.read_csv(filepath)
            return data
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    @staticmethod
    def get_dataset_info(df):
        """Get comprehensive dataset information"""
        info = {
            "rows": len(df),
            "columns": len(df.columns),
            "features": list(df.columns),
            "dtypes": df.dtypes.to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "duplicates": len(df[df.duplicated()]),
        }
        return info
    
    @staticmethod
    def get_feature_descriptions():
        """Return feature descriptions for the dataset"""
        descriptions = {
            "CreditScore": "Customer's credit score (300-850)",
            "Age": "Customer's age in years (18-92)",
            "Tenure": "Number of years as customer (0-10)",
            "Balance": "Account balance in currency units",
            "NumOfProducts": "Number of bank products used (1-4)",
            "HasCrCard": "Whether customer has credit card (0/1)",
            "IsActiveMember": "Whether customer is active (0/1)",
            "EstimatedSalary": "Estimated annual salary",
            "Gender": "Customer gender (Male/Female)",
            "Geography": "Customer location (France/Germany/Spain)",
            "Exited": "Whether customer churned (0=No, 1=Yes)"
        }
        return descriptions
    
    def preprocess_for_prediction(self, user_input_dict, scaler=None):
        """
        Preprocess user input for model prediction
        
        Args:
            user_input_dict: Dictionary with user input values
            scaler: StandardScaler instance (if already fitted)
        
        Returns:
            Preprocessed array ready for prediction
        """
        try:
            # Create a copy to avoid modifying original
            processed = user_input_dict.copy()
            
            # Encode categorical variables
            gender_map = {"Male": 1, "Female": 0}
            geography_map = {"France": 0, "Germany": 1, "Spain": 2}
            
            processed['Gender'] = gender_map.get(processed.get('Gender', 'Male'), 1)
            
            # Handle Geography (one-hot encoding style)
            geo = processed.get('Geography', 'France')
            processed['Geography_Germany'] = 1 if geo == 'Germany' else 0
            processed['Geography_Spain'] = 1 if geo == 'Spain' else 0
            
            # Remove original Geography
            processed.pop('Geography', None)
            
            # Create ordered feature list (must match training order)
            feature_order = [
                'CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
                'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Gender',
                'Geography_Germany', 'Geography_Spain'
            ]
            
            # Create array in correct order
            values = [processed.get(feat, 0) for feat in feature_order]
            values = np.array(values).reshape(1, -1)
            
            # Scale if scaler provided
            if scaler is not None:
                values = scaler.transform(values)
            
            return values, feature_order
        
        except Exception as e:
            raise ValueError(f"Error preprocessing input: {str(e)}")
    
    @staticmethod
    def get_churn_interpretation(churn_prob):
        """
        Get interpretation and recommendation based on churn probability
        
        Args:
            churn_prob: Probability of churn (0-1)
        
        Returns:
            Dictionary with interpretation and action items
        """
        if churn_prob >= 0.7:
            risk_level = "🔴 HIGH RISK"
            interpretation = "This customer has a HIGH probability of churning."
            recommendation = [
                "🎯 Immediate action required",
                "📞 Schedule direct outreach",
                "💰 Offer special retention incentives",
                "📈 Upgrade account benefits",
                "🎁 Personalized offers/promotions"
            ]
            color = "danger"
        elif churn_prob >= 0.4:
            risk_level = "🟡 MEDIUM RISK"
            interpretation = "This customer shows MODERATE churn signals."
            recommendation = [
                "📧 Send engagement campaigns",
                "💡 Highlight new features",
                "🤝 Improve customer experience",
                "📊 Regular check-ins",
                "💳 Cross-sell opportunities"
            ]
            color = "warning"
        else:
            risk_level = "🟢 LOW RISK"
            interpretation = "This customer is likely to REMAIN loyal."
            recommendation = [
                "✅ Maintain regular engagement",
                "🔄 Continue quality service",
                "📈 Explore upsell opportunities",
                "🎯 Build long-term relationships",
                "⭐ Request referrals/testimonials"
            ]
            color = "success"
        
        return {
            "risk_level": risk_level,
            "interpretation": interpretation,
            "recommendations": recommendation,
            "color": color
        }
    
    @staticmethod
    def get_retention_strategies():
        """Get strategic business insights for retention"""
        strategies = {
            "Top Churn Factors": [
                "📊 Age > 40: Significantly higher churn rate",
                "💼 Geographic location: Certain regions show higher churn",
                "💰 Low balance: Indicates disengagement",
                "🏦 Single product customers: Higher retention risk",
                "⏰ New customers (low tenure): Need more engagement"
            ],
            "Retention Tactics": [
                "🎯 Personalized offers based on customer profile",
                "📱 Enhanced digital banking experience",
                "💳 Premium banking services for high-value customers",
                "🎁 Loyalty rewards program",
                "📞 Proactive customer service outreach",
                "💼 Business advisory services for inactive members"
            ],
            "AI Impact": [
                "🤖 Early churn detection enables preventive action",
                "📈 Targeted interventions improve retention rate",
                "💡 Data-driven insights guide strategy",
                "⏱️ Automated alerts for at-risk customers",
                "🎯 Personalization at scale"
            ]
        }
        return strategies


def get_model_comparison_data():
    """Get benchmark comparison data between ML and ANN models"""
    return {
        "metrics": ["Accuracy", "Precision", "Recall", "F1-Score", "ROC-AUC"],
        "lightgbm": [0.86, 0.82, 0.75, 0.78, 0.92],
        "ann": [0.85, 0.80, 0.72, 0.76, 0.90],
    }


def format_currency(value):
    """Format value as currency"""
    return f"${value:,.2f}"


def format_percentage(value):
    """Format value as percentage"""
    return f"{value:.2%}"


def format_number(value):
    """Format number with thousands separator"""
    return f"{value:,.0f}"

"""
Model Loading and Management
Handles loading pre-trained ML and ANN models
"""

import pickle
import joblib
import numpy as np
import pandas as pd
import warnings
from pathlib import Path

warnings.filterwarnings('ignore')


class ModelManager:
    """Manage loading and inference with trained models"""
    
    def __init__(self, model_dir="../"):
        """
        Initialize ModelManager
        
        Args:
            model_dir: Directory containing trained models
        """
        self.model_dir = Path(model_dir)
        self.ml_model = None
        self.ann_model = None
        self.scaler = None
        
    def load_ml_model(self, model_path=None):
        """
        Load the best ML model (LightGBM)
        
        Args:
            model_path: Path to model file. If None, uses default naming
        """
        try:
            if model_path is None:
                # Try common model names
                possible_paths = [
                    self.model_dir / "best_lgbm_model.pkl",
                    self.model_dir / "best_lgbm_model.joblib",
                    self.model_dir / "best_ml_model.pkl",
                    self.model_dir / "lgbm_model.pkl",
                ]
                
                for path in possible_paths:
                    if path.exists():
                        model_path = path
                        break
                
                if model_path is None:
                    # If no model found, create a mock model for demonstration
                    print("⚠️ ML Model not found. Using mock model for demonstration.")
                    self.ml_model = MockMLModel()
                    return
            
            # Try joblib first, then pickle
            try:
                self.ml_model = joblib.load(model_path)
            except:
                with open(model_path, 'rb') as f:
                    self.ml_model = pickle.load(f)
            
            print(f"✅ ML Model loaded successfully from {model_path}")
            
        except Exception as e:
            print(f"⚠️ Error loading ML model: {e}. Using mock model.")
            self.ml_model = MockMLModel()
    
    def load_ann_model(self, model_path=None):
        """
        Load the trained ANN model
        
        Args:
            model_path: Path to model file. If None, uses default naming
        """
        try:
            import tensorflow as tf
            
            if model_path is None:
                possible_paths = [
                    self.model_dir / "best_ann_model.h5",
                    self.model_dir / "best_ann_model.keras",
                    self.model_dir / "ann_model.h5",
                    self.model_dir / "best_model.keras",
                ]
                
                for path in possible_paths:
                    if path.exists():
                        model_path = path
                        break
                
                if model_path is None:
                    print("⚠️ ANN Model not found. Using mock model for demonstration.")
                    self.ann_model = MockANNModel()
                    return
            
            # Load Keras model
            self.ann_model = tf.keras.models.load_model(model_path)
            print(f"✅ ANN Model loaded successfully from {model_path}")
            
        except ImportError:
            print("⚠️ TensorFlow not installed. Using mock ANN model.")
            self.ann_model = MockANNModel()
        except Exception as e:
            print(f"⚠️ Error loading ANN model: {e}. Using mock model.")
            self.ann_model = MockANNModel()
    
    def load_scaler(self, scaler_path=None):
        """
        Load the feature scaler
        
        Args:
            scaler_path: Path to scaler file. If None, uses default naming
        """
        try:
            if scaler_path is None:
                possible_paths = [
                    self.model_dir / "scaler.pkl",
                    self.model_dir / "scaler.joblib",
                    self.model_dir / "feature_scaler.pkl",
                ]
                
                for path in possible_paths:
                    if path.exists():
                        scaler_path = path
                        break
                
                if scaler_path is None:
                    print("⚠️ Scaler not found. Models will receive unscaled features.")
                    return
            
            # Load scaler
            try:
                self.scaler = joblib.load(scaler_path)
            except:
                with open(scaler_path, 'rb') as f:
                    self.scaler = pickle.load(f)
            
            print(f"✅ Scaler loaded successfully from {scaler_path}")
            
        except Exception as e:
            print(f"⚠️ Error loading scaler: {e}")
    
    def predict_ml(self, X, return_proba=True):
        """
        Make prediction with ML model
        
        Args:
            X: Input features (numpy array or pandas DataFrame)
            return_proba: Return probability or class prediction
        
        Returns:
            Probability or class prediction
        """
        if self.ml_model is None:
            raise ValueError("ML model not loaded")
        
        try:
            if return_proba:
                proba = self.ml_model.predict_proba(X)
                return proba[:, 1]  # Return probability of churn (class 1)
            else:
                return self.ml_model.predict(X)
        
        except Exception as e:
            print(f"Error in ML prediction: {e}")
            raise
    
    def predict_ann(self, X):
        """
        Make prediction with ANN model
        
        Args:
            X: Input features (numpy array)
        
        Returns:
            Probability of churn
        """
        if self.ann_model is None:
            raise ValueError("ANN model not loaded")
        
        try:
            # Ensure X is scaled if scaler available
            if self.scaler is not None:
                X = self.scaler.transform(X)
            
            proba = self.ann_model.predict(X, verbose=0)
            return proba.flatten()
        
        except Exception as e:
            print(f"Error in ANN prediction: {e}")
            raise
    
    def scale_features(self, X):
        """Scale features using loaded scaler"""
        if self.scaler is None:
            return X
        return self.scaler.transform(X)


class MockMLModel:
    """Mock ML model for demonstration when actual model not available"""
    
    def predict_proba(self, X):
        """Return mock probabilities"""
        n_samples = X.shape[0] if len(X.shape) > 1 else 1
        # Generate realistic but varied probabilities
        np.random.seed(hash(tuple(X.flatten())) % 2**32)
        proba = np.random.uniform(0.2, 0.9, n_samples)
        return np.column_stack([1 - proba, proba])
    
    def predict(self, X):
        """Return mock predictions"""
        proba = self.predict_proba(X)
        return (proba[:, 1] > 0.5).astype(int)


class MockANNModel:
    """Mock ANN model for demonstration when actual model not available"""
    
    def predict(self, X, verbose=0):
        """Return mock predictions"""
        n_samples = X.shape[0] if len(X.shape) > 1 else 1
        # Generate realistic but varied probabilities
        np.random.seed(hash(tuple(X.flatten())) % 2**32)
        proba = np.random.uniform(0.2, 0.85, (n_samples, 1))
        return proba


def get_model_info():
    """Get information about trained models"""
    model_info = {
        "LightGBM": {
            "type": "Gradient Boosting Classifier",
            "best_params": {
                "n_estimators": 200,
                "learning_rate": 0.1,
                "num_leaves": 50,
                "boosting_type": "gbdt"
            },
            "cv_accuracy": 0.8734,
            "test_accuracy": 0.8625,
            "metrics": {
                "Precision": 0.82,
                "Recall": 0.75,
                "F1-Score": 0.78,
                "ROC-AUC": 0.92
            }
        },
        "XGBoost": {
            "type": "Extreme Gradient Boosting",
            "best_params": {
                "n_estimators": 200,
                "learning_rate": 0.1,
                "max_depth": 6,
                "eval_metric": "logloss"
            },
            "cv_accuracy": 0.8601,
            "test_accuracy": 0.8525,
            "metrics": {
                "Precision": 0.80,
                "Recall": 0.72,
                "F1-Score": 0.76,
                "ROC-AUC": 0.90
            }
        },
        "ANN": {
            "type": "Artificial Neural Network",
            "architecture": {
                "layers": "Variable (1-3 dense layers)",
                "activation": "ReLU / Tanh / Sigmoid",
                "dropout": "0.0-0.5",
                "optimizer": "Adam / RMSprop / SGD"
            },
            "test_accuracy": 0.8475,
            "metrics": {
                "Precision": 0.80,
                "Recall": 0.70,
                "F1-Score": 0.75,
                "ROC-AUC": 0.89
            }
        }
    }
    return model_info

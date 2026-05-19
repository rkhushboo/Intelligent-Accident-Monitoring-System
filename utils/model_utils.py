import os
import tempfile
import numpy as np
import cv2
import gdown
import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image

# Google Drive model setup
MODEL_PATH = "models/best_model_vgg.h5"

# Paste your Google Drive FILE ID here
FILE_ID = "1n6RClhmQcWuG5p2HHonIuYK8rlexqWpl"

# Download URL
DOWNLOAD_URL = f"https://drive.google.com/uc?id={FILE_ID}"


def download_model():
    """
    Download model from Google Drive if not available locally
    """

    os.makedirs("models", exist_ok=True)

    if not os.path.exists(MODEL_PATH):

        

        gdown.download(
            DOWNLOAD_URL,
            MODEL_PATH,
            quiet=False
        )

        
        
@st.cache_resource
def load_cnn_model(model_path: str = MODEL_PATH):

    try:
        download_model()

        model = load_model(model_path, compile=False)

        return model, {
            "status": "loaded",
            "message": f"Loaded model from {model_path}."
        }

    except Exception as e:

        return None, {
            "status": "missing",
            "message": f"Error loading model: {str(e)}"
        }

@st.cache_data
def load_model_status():
    if os.path.exists(MODEL_PATH):
        return {"status": "loaded", "model_path": MODEL_PATH}
    return {"status": "missing", "model_path": MODEL_PATH}

def preprocess_image(image, target_size=(256, 256)):
    if isinstance(image, bytes):
        np_image = np.frombuffer(image, np.uint8)
        image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)
    elif isinstance(image, Image.Image):
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    elif isinstance(image, str):
        image = cv2.imread(image)
    if image is None:
        raise ValueError("Unable to read the image for preprocessing.")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, target_size)
    image = image.astype(np.float32) / 255.0
    return image

def predict_image(image_array, model):
    if model is None:
        return "Model missing", 0.0
    x = np.expand_dims(image_array, axis=0)
    score = float(model.predict(x, verbose=0).reshape(-1)[0])
    label = "No Accident Detected" if score >= 0.5 else "Accident Detected"
    
    return label, score

def analyze_video_upload(uploaded_file, model, sample_frames=5):
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name
    cap = cv2.VideoCapture(temp_path)
    if not cap.isOpened():
        raise ValueError("Unable to read the uploaded video.")
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    step = max(1, frame_count // sample_frames)
    predictions = []
    frames = []
    current = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if current % step == 0:
            frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            processed = preprocess_image(frames[-1])
            _, prob = predict_image(processed, model)
            predictions.append(prob)
        current += 1
    cap.release()
    if len(predictions) == 0:
        raise ValueError("No valid frames were extracted from the video.")
    average_score = float(np.mean(predictions))
    label = "Accident Detected" if average_score >= 0.5 else "No Accident Detected"
    return label, average_score, frames

def format_confidence(score: float) -> str:
    return f"{score * 100:.1f}%" if score is not None else "0%"

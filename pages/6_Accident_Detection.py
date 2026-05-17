import streamlit as st
from utils.ui_utils import load_css
from utils.model_utils import load_cnn_model, preprocess_image, predict_image, analyze_video_upload, format_confidence
from PIL import Image
import numpy as np

st.set_page_config(page_title="Accident Detection | Intelligent Accident Monitoring System", page_icon="🚨", layout="wide")
load_css()

model, model_status = load_cnn_model()

st.markdown("""
# 🚨 Accident Detection
**Upload CCTV imagery or video and get instant accident detection results.**
""", unsafe_allow_html=True)

if model_status["status"] != "loaded":
    st.warning("The trained CNN model is not loaded. Add `best_model.h5` to the project root.")

mode = st.radio("Choose input type", ["Image", "Video"])

if mode == "Image":
    uploaded_file = st.file_uploader("Upload an accident or scene image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image_data = uploaded_file.read()
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded image", use_column_width=True)
        with st.spinner("Analyzing image..."):
            try:
                processed = preprocess_image(image_data)
                label, score = predict_image(processed, model)
                confidence = format_confidence(score)
                st.markdown(f"### **{label}**")
                progress_bar = st.progress(int(score * 100))
                progress_bar.progress(int(score * 100))
                if score >= 0.5:
                    st.markdown(f"<div class='predict-alert danger'><strong>High risk detected:</strong> emergency response recommended.</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='predict-alert success'><strong>Safe scene:</strong> no accident patterns detected.</div>", unsafe_allow_html=True)
                st.write(f"**Confidence:** {confidence}")
            except Exception as exc:
                st.error(f"Prediction failed: {exc}")

else:
    uploaded_file = st.file_uploader("Upload CCTV footage for frame-level analysis", type=["mp4", "mov", "avi", "mkv"])
    if uploaded_file is not None:
        with st.spinner("Processing video frames..."):
            try:
                label, score, frames = analyze_video_upload(uploaded_file, model)
                st.markdown(f"### **{label}**")
                st.progress(int(score * 100))
                if score >= 0.5:
                    st.markdown(f"<div class='predict-alert danger'><strong>Emergency alert:</strong> accident was detected in video frames.</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='predict-alert success'><strong>Scene stable:</strong> no accident events detected across sampled frames.</div>", unsafe_allow_html=True)
                st.write(f"**Average confidence:** {format_confidence(score)}")
                st.markdown("### Sample analyzed frames")
                cols = st.columns(min(4, len(frames)))
                for col, frame in zip(cols, frames):
                    col.image(frame, use_column_width=True)
            except Exception as exc:
                st.error(f"Video analysis failed: {exc}")

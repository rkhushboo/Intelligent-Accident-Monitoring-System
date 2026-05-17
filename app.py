import streamlit as st
from utils.ui_utils import load_css, render_hero_banner, render_impact_cards
from utils.data_utils import get_dataset_summary, load_sample_images
from utils.model_utils import load_cnn_model, load_model_status

st.set_page_config(page_title="Intelligent Accident Monitoring System", page_icon="🚨", layout="wide")
load_css()

model, model_status = load_cnn_model()
summary = get_dataset_summary()
samples = load_sample_images(n_samples=3)

st.markdown("""
# 🚦 Intelligent Accident Monitoring System
**A professional deep learning dashboard for accident detection using CCTV imagery.**
""", unsafe_allow_html=True)

render_hero_banner(summary, model_status)

with st.container():
    st.subheader("Project Highlights")
    st.write(
        "This application uses a production-ready CNN model trained on real CCTV accident imagery to detect incidents with confidence scoring, visual explanations, and operational insights."
    )

with st.container():
    st.subheader("Dataset Preview")
    cols = st.columns([1, 1, 1])
    for idx, label in enumerate(samples):
        with cols[idx]:
            st.markdown(f"### {label}")
            for image_path in samples[label]:
                st.image(image_path, caption=f"{label} sample", use_column_width=True)

with st.container():
    st.subheader("Why this system matters")
    st.write(
        "Accident detection with AI improves response times, reduces false alarms, and enables proactive traffic surveillance. This solution is built for real-world deployment with an explainable interface and business-ready metrics."
    )

render_impact_cards()

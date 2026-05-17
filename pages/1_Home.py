import streamlit as st
from utils.ui_utils import load_css, render_hero_banner, render_impact_cards
from utils.data_utils import get_dataset_summary, load_sample_images
from utils.model_utils import load_model_status

st.set_page_config(page_title="Home | Intelligent Accident Monitoring System", page_icon="🏠", layout="wide")
load_css()

summary = get_dataset_summary()
model_status = load_model_status()

st.markdown("""
# 🚦 Intelligent Accident Monitoring System
**A next-generation accident monitoring dashboard for CCTV image analytics and rapid response.**
""", unsafe_allow_html=True)

render_hero_banner(summary, model_status)

st.markdown("## Why this system matters")
col1, col2 = st.columns([3, 2])
with col1:
    st.write(
        "This app brings a production-style interface to CNN-based accident detection. Users can explore data, inspect detailed model behavior, and run prediction analysis on uploaded images and videos."
    )
    st.write(
        "It is designed for emergency response teams, traffic authorities, and smart city operators who need fast, explainable alerts from CCTV feeds."
    )
with col2:
    st.metric(label="Deployment readiness", value="Production-ready", delta="+Stable")
    st.metric(label="Platform", value="Streamlit + TensorFlow", delta="CNN model")
    st.metric(label="Inference mode", value="Batch / Live preview", delta="Optimized")

st.markdown("## Quick dataset preview")
image_samples = load_sample_images(n_samples=2)
if image_samples:
    cols = st.columns(len(image_samples))
    for idx, (label, images) in enumerate(image_samples.items()):
        with cols[idx]:
            st.write(f"### {label}")
            for image_path in images:
                st.image(image_path, use_column_width=True, caption=label)
else:
    st.info("Sample dataset images are not available in the current workspace.")

render_impact_cards()

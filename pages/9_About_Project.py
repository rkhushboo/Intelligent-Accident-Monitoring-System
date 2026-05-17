import streamlit as st
from utils.ui_utils import load_css

st.set_page_config(page_title="About Project | Intelligent Accident Monitoring System", page_icon="📘", layout="wide")
load_css()

st.markdown("""
# 📘 About Project
**An intelligent accident monitoring system built with Streamlit, TensorFlow, OpenCV, and CNN technology.**
""", unsafe_allow_html=True)

st.markdown("## Project overview")
st.write(
    "This project uses a trained CNN model to detect accidents in CCTV imagery and video. The Streamlit interface provides a polished dashboard for prediction, data exploration, and deployment-ready storytelling."
)

st.markdown("## Technologies used")
st.write("- Python\n- Streamlit\n- TensorFlow / Keras\n- OpenCV\n- Pillow\n- Plotly\n- Scikit-learn")

st.markdown("## Model architecture")
st.write(
    "The core model uses convolutional layers to extract spatial features, followed by dense layers for binary classification. Dropout and batch normalization help improve generalization on accident imagery."
)

st.markdown("## Dataset source")
st.write(
    "The dataset is organized into accident and non-accident categories within train, test, and validation directories. This structure supports supervised learning and reliable performance estimation."
)

with st.expander("Future enhancements"):
    st.write(
        "- Add object detection to locate accident regions in the frame.\n"
        "- Add multi-frame temporal analysis for video-based accident prediction.\n"
        "- Deploy the model as an edge service for low-latency CCTV inference."
    )

st.markdown("## Deployment guidance")
st.write("Place the trained `best_model.h5` in the project root and run `streamlit run app.py` to launch the dashboard.")

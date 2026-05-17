import streamlit as st
from utils.ui_utils import load_css
from utils.model_utils import load_cnn_model, preprocess_image, predict_image, format_confidence
from PIL import Image

st.set_page_config(page_title="Real-Time Analysis | Intelligent Accident Monitoring System", page_icon="🎥", layout="wide")
load_css()

model, model_status = load_cnn_model()

st.markdown("""
# 🎥 Real-Time Analysis
**Live camera support for instant accident monitoring simulations.**
""", unsafe_allow_html=True)

if model_status["status"] != "loaded":
    st.warning("The trained model is not loaded. Add `best_model.h5` to the project root to enable live analysis.")

camera_input = st.camera_input("Use your camera to capture a live frame")
if camera_input is not None:
    try:
        image = Image.open(camera_input)
        st.image(image, caption="Live capture", use_column_width=True)
        if st.button("Analyze frame"):
            processed = preprocess_image(camera_input.read())
            label, score = predict_image(processed, model)
            st.markdown(f"### **{label}**")
            st.write(f"**Confidence:** {format_confidence(score)}")
            if score >= 0.5:
                st.error("Accident condition detected. Trigger alert sequence.")
            else:
                st.success("No accident indicators found in the live frame.")
    except Exception as exc:
        st.error(f"Live analysis error: {exc}")
else:
    st.info("Camera input is available in supported browsers. Use this section to simulate real-time monitoring.")

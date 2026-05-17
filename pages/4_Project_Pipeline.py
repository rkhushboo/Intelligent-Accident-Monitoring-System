import streamlit as st
from utils.ui_utils import load_css

st.set_page_config(page_title="Project Pipeline | Intelligent Accident Monitoring System", page_icon="🧠", layout="wide")
load_css()

st.markdown("""
# 🔄 Project Pipeline
**A modern workflow view of the complete accident detection system.**
""", unsafe_allow_html=True)

st.markdown("## Workflow overview")
steps = [
    ("1", "Data Collection", "Gather CCTV frames and labeled accident imagery from the road network."),
    ("2", "Preprocessing", "Clean images, resize to 256x256, normalize pixels, and prepare labels."),
    ("3", "Image Resizing", "Standardize input size for the CNN pipeline and accelerate inference."),
    ("4", "Data Augmentation", "Add flips, rotations, and zoom to improve model generalization."),
    ("5", "CNN Training", "Train convolutional layers to extract accident-specific spatial features."),
    ("6", "Validation", "Monitor validation loss and accuracy with a held-out dataset."),
    ("7", "Hyperparameter Tuning", "Tune learning rate, batch sizes, and dropout to improve stability."),
    ("8", "Model Evaluation", "Compute accuracy, precision, recall, F1-score and confusion metrics."),
    ("9", "Prediction System", "Deploy the inference engine for image and CCTV video uploads."),
    ("10", "Deployment", "Deliver a Streamlit interface with monitoring-ready alerts and reports."),
]
for step, title, description in steps:
    st.markdown(
        f"<div class='glass-card'><h3>{step}. {title}</h3><p>{description}</p></div>", unsafe_allow_html=True
    )

st.markdown("## Why CNN is ideal for accident detection")
col1, col2 = st.columns(2)
with col1:
    st.write("**Convolutional layers** detect edges, contours, and object areas in CCTV frames.")
    st.write("**Pooling layers** reduce spatial dimensions and make the network robust to position changes.")
    st.write("**Dropout** prevents overfitting by randomly disabling neurons during training.")
with col2:
    st.write("**Activation functions** such as ReLU enable the model to learn non-linear patterns in accident imagery.")
    st.write("**Optimizers** like Adam adapt learning rates during training to speed up convergence.")
    st.write("**Binary crossentropy** is effective for accident vs non-accident classification tasks.")

with st.expander("CNN architecture concepts"):
    st.write(
        "A CNN learns from pixel neighborhoods through convolutional filters, then pools the strongest features and uses dense layers for final accident scoring."
    )

with st.expander("Deployment-ready model design"):
    st.write(
        "This app uses a pre-trained Keras CNN that is loaded in inference mode, ensuring quick response and a low memory footprint for production use."
    )

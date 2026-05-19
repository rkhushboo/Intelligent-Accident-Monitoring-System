import streamlit as st
import plotly.graph_objects as go
from utils.ui_utils import load_css
from utils.data_utils import compute_validation_metrics
from utils.model_utils import load_cnn_model
from utils.data_utils import download_dataset

st.set_page_config(page_title="Model Performance | Intelligent Accident Monitoring System", page_icon="📈", layout="wide")
load_css()

model, model_status = load_cnn_model()
metrics = compute_validation_metrics(model)

st.markdown("""
# 🧾 Model Performance
**Trusted evaluation metrics for the accident detection CNN.**
""", unsafe_allow_html=True)

if model_status["status"] != "loaded":
    st.warning("Model file is missing. Place `best_model.h5` in the project root to enable performance analysis.")

st.markdown("## Evaluation summary")
if metrics:
    cols = st.columns(4)
    cols[0].metric("Accuracy", f"{metrics['accuracy']:.2%}")
    cols[1].metric("Precision", f"{metrics['precision']:.2%}")
    cols[2].metric("Recall", f"{metrics['recall']:.2%}")
    cols[3].metric("F1 Score", f"{metrics['f1_score']:.2%}")
    if metrics.get("roc_auc") is not None:
        st.markdown(f"**ROC AUC:** {metrics['roc_auc']:.3f}")
    st.markdown("### Confusion matrix")
    cm = metrics["confusion_matrix"]
    fig = go.Figure(data=go.Heatmap(z=cm, x=["No Accident", "Accident"], y=["No Accident", "Accident"], colorscale='Viridis'))
    fig.update_layout(template='plotly_dark', xaxis_title='Predicted', yaxis_title='Actual')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Validation dataset or model is unavailable. Place the dataset and model in the workspace to compute metrics.")

with st.expander("CNN architecture summary"):
    if model is not None:
        model.summary(print_fn=lambda x: st.text(x))
    else:
        st.write("Model summary is unavailable until the model file is loaded.")

with st.expander("Training insights"):
    st.write(
        "- EarlyStopping halts training when validation loss stops improving, protecting the model from overfitting.\n"
        "- ModelCheckpoint saves the best weights, ensuring deployment uses the most reliable version.\n"
        "- Data augmentation creates more variety so the CNN generalizes to new CCTV scenes."
    )

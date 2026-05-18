import os
import gdown
import glob
import random
import pandas as pd
import numpy as np
import streamlit as st
from pathlib import Path
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix, roc_auc_score)
from tensorflow.keras.utils import image_dataset_from_directory

DATASET_FOLDER_ID = "1p-vDa8PnHlPrVj5uzKRwdoRlHGoPGKZf"

DATASET_PATH = "datasets"


def download_dataset():

    # Skip download if dataset already exists
    if os.path.exists(DATASET_PATH) and len(os.listdir(DATASET_PATH)) > 0:
        return

    os.makedirs(DATASET_PATH, exist_ok=True)

    st.info("Downloading dataset from Google Drive...")

    gdown.download_folder(
        id=DATASET_FOLDER_ID,
        output=DATASET_PATH,
        quiet=False
    )

    st.success("Dataset downloaded successfully!")

DATA_ROOT = "datasets/data"

@st.cache_data
def get_dataset_summary(base_dir: str = DATA_ROOT):
    summary = {
        "train": {},
        "test": {},
        "val": {},
        "totals": {"images": 0, "classes": 0, "accidents": 0, "non_accidents": 0}
    }
    for split in ["train", "test", "val"]:
        split_path = os.path.join(base_dir, split)
        if os.path.isdir(split_path):
            for cls in sorted(os.listdir(split_path)):
                cls_path = os.path.join(split_path, cls)
                if os.path.isdir(cls_path):
                    count = len(glob.glob(os.path.join(cls_path, "*")))
                    summary[split][cls] = count
                    summary["totals"]["images"] += count
                    if cls.lower().startswith("accident"):
                        summary["totals"]["accidents"] += count
                    else:
                        summary["totals"]["non_accidents"] += count
    summary["totals"]["classes"] = len(summary["train"])
    return summary

@st.cache_data
def load_sample_images(base_dir: str = DATA_ROOT, n_samples: int = 3):
    samples = {}
    train_path = os.path.join(base_dir, "train")
    if not os.path.isdir(train_path):
        return samples
    for cls in sorted(os.listdir(train_path)):
        cls_path = os.path.join(train_path, cls)
        if os.path.isdir(cls_path):
            image_files = glob.glob(os.path.join(cls_path, "*"))
            if image_files:
                samples[cls] = random.sample(image_files, min(n_samples, len(image_files)))
    return samples

@st.cache_data
def build_distribution_dataframe(summary):
    counts = []
    for label, count in summary.get("train", {}).items():
        counts.append({"Class": label, "Images": count})
    return pd.DataFrame(counts)

@st.cache_data
def compute_validation_metrics(model, target_dir: str = os.path.join(DATA_ROOT, "test"), target_size=(256, 256), batch_size=32):
    if model is None or not os.path.isdir(target_dir):
        return {}
    dataset = image_dataset_from_directory(
        target_dir,
        labels="inferred",
        label_mode="int",
        batch_size=batch_size,
        image_size=target_size,
        shuffle=False,
    )
    dataset = dataset.map(lambda x, y: (x / 255.0, y))
    y_true = []
    y_pred = []
    y_score = []
    for x_batch, y_batch in dataset:
        preds = model.predict(x_batch, verbose=0).reshape(-1)
        y_true.extend(y_batch.numpy().astype(int).tolist())
        y_pred.extend((preds >= 0.5).astype(int).tolist())
        y_score.extend(preds.tolist())
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1_score": f1_score(y_true, y_pred, zero_division=0),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
    }
    try:
        metrics["roc_auc"] = roc_auc_score(y_true, y_score)
    except Exception:
        metrics["roc_auc"] = None
    return metrics

@st.cache_data
def create_class_image_gallery(sample_images):
    gallery = []
    for cls, paths in sample_images.items():
        for path in paths:
            gallery.append({"class": cls, "path": path})
    return gallery

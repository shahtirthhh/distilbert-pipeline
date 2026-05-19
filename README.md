# Goodreads Genre Classification - MLOps Pipeline

**Author:** Tirth Shah  
**Program:** MTech AI, IIT Jodhpur

This repository contains an end-to-end MLOps pipeline for fine-tuning a transformer model (`distilbert-base-cased`) to classify book reviews into genres. The project demonstrates cloud-based training, experiment tracking, model artifact versioning, and deployment to a model registry.

## Setup & Installation

To run the inference script or reproduce the training environment locally:

1. Clone this repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the inference script: `python inference.py`

## Training Platform & Pipeline

- **Platform:** Kaggle Notebooks (GPU T4 x2)
- **Tracking:** Weights & Biases (W&B) for metrics and artifact versioning.
- **Model Registry:** Hugging Face Hub.

## Results

Final evaluation metrics on the unseen test dataset:

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 0.XX  |
| F1 Score  | 0.XX  |
| Eval Loss | 0.XX  |

## Project Links

- **Hugging Face Model:** https://huggingface.co/shahtirthhh/distilbert-goodreads-genres-mlops
- **Weights & Biases Dashboard:** https://wandb.ai/shahtirthhh-iitj/mlops-assignment2/workspace?nw=nwusershahtirthhh

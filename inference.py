from transformers import pipeline

# Replace this with your actual Hugging Face model path
MODEL_PATH = "your_huggingface_username/distilbert-goodreads-genres-mlops"

def predict_genre(text):
    # Initialize the pipeline with your deployed model
    classifier = pipeline("text-classification", model=MODEL_PATH, tokenizer=MODEL_PATH)
    
    # Run prediction
    result = classifier(text)
    return result

if __name__ == "__main__":
    sample_review = "This book was a thrilling ride full of magic, dragons, and epic battles!"
    prediction = predict_genre(sample_review)
    
    print(f"Review: {sample_review}")
    print(f"Predicted Genre: {prediction[0]['label']} (Confidence: {prediction[0]['score']:.2f})")
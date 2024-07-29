from django.shortcuts import render
import pickle
import os
from pathlib import Path

# Define the root directory
ROOT_DIR = Path(__file__).resolve().parent.parent

# Load model and vectorizer from the root directory
model_path = os.path.join(ROOT_DIR, 'model.pkl')
vectorizer_path = os.path.join(ROOT_DIR, 'tfidf_vectorizer.pkl')

model = pickle.load(open(model_path, 'rb'))
tfidf_vectorizer = pickle.load(open(vectorizer_path, 'rb'))

def detect(input_text):
    vectorized_text = tfidf_vectorizer.transform([input_text])
    result = model.predict(vectorized_text)
    return "Plagiarism Detected" if result[0] == 1 else "No Plagiarism Detected"

def home(request):
    return render(request, 'detector/index.html')

def detect_plagiarism(request):
    if request.method == 'POST':
        input_text = request.POST['text']
        detection_result = detect(input_text)
        return render(request, 'detector/index.html', {'result': detection_result})
    return render(request, 'detector/index.html')
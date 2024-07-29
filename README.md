# Plagiarism Detector Using Machine Learning
This repository contains code and resources for a Plagiarism Detector built using Python and various machine learning techniques. The detector uses a logistic regression model to determine the likelihood of plagiarism in a given text by comparing it to a trained dataset.

## Project Overview
This project implements a plagiarism detection system using machine learning techniques. The main objective is to identify instances of plagiarism by comparing text documents. The model is trained using a TF-IDF vectorizer to convert text data into numerical format and a logistic regression model for classification.

## Features
- **Text Preprocessing**: Cleans and prepares text data for analysis.
- **TF-IDF Vectorization**: Converts text data into numerical features.
- **Logistic Regression Model**: Classifies text data to detect plagiarism.
- **Web Interface**: User-friendly interface to input text and view results.
- **Persistent Text Area**: Keeps the input text in the textarea after the result is displayed.

## Installation
To get started with the project, follow these steps:

1. Clone the repository:
```sh
git clone https://github.com/Dispenser254/Plagiarism-Detector-using-Machine-Learning.git
cd Plagiarism-Detector-using-Machine-Learning
```
2. Install the required dependencies:

Ensure you have Python 3.6+ and pip installed. Then, run:
```sh
pip install -r requirements.txt
```
3. Prepare the Model and Vectorizer:

Place the ``model.pkl`` and ``tfidf_vectorizer.pkl`` files in the root directory of the project.

## Usage
To run the project, follow these steps:

i. Start the Django server:
```sh
python manage.py runserver
```
ii. Open your web browser and navigate to:
``sh
http://127.0.0.1:8000/
``
Enter text into the provided textarea and click the "Check for Plagiarism" button. The result will be displayed below the textarea, and the input text will remain in place.

## Examples
### Plagiarized Text
Researchers have discovered a new species of butterfly in the Amazon rainforest.

### Non-plagiarized Text
Playing yoga enhances physical flexibility

The project is limited due to the ``dataset.csv`` used.


## Model and Vectorizer
The logistic regression model and TF-IDF vectorizer are stored in pickle files (``model.pkl`` and ``tfidf_vectorizer.pkl``). These files should be placed in the root directory of the project.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

# E-Mail_Spam_Classifier
E-Mail_Spam_Classifier using Machine Learning and NLP with Multi-Model Approach

Project Flow of ML Model Building – Email Spam Classifier

1. Text Cleaning
Feature extraction requires normalized text.
Lowercase
Remove URLs
Remove numbers
Remove punctuation
Tokenization

2. EDA (Exploratory Data Analysis)
Initial analysis phase to understand dataset characteristics. Key Tasks:
Class distribution (Spam vs Ham)
Email length analysis
Word frequency visualization
Detect anomalies or imbalance Purpose: Identify patterns and validate modeling assumptions.

3. Text Pre-processing
Transforms raw email text into machine-readable features.
Lowercasing text
Remove punctuation & stopwords
Tokenization
Stemming/Lemmatization
Vectorization using TF-IDF / Bag of Words

4. Model Building
Training the classification algorithms.
Train–test split
Feature extraction from text
Train models:
Naïve Bayes
Logistic Regression
SVM
Fit on vectorized dataset

5. Model Evaluation
Assess model effectiveness. Metrics:
Accuracy
Precision
Recall
F1-Score
Confusion Matrix
Focus: Balance between spam detection and false positives.

6. Improvement
Performance optimization stage.
Hyperparameter tuning
N-gram features
Handle class imbalance
Ensemble / advanced models

7. User Interface (Website)
Front-end system for predictions.
Email text input
Predict button
Output: Spam / Not Spam
Built with HTML, CSS, JS + Flask/Django

8. Deployment on Heroku
Cloud hosting for public access.
Upload Flask app + model files
Add requirements.txt
Add Procfile
Deploy via Git
Generate live public URL

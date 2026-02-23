# E-Mail_Spam_Classifier

E-Mail_Spam_Classifier using Machine Learning and NLP with Multi-Model Approach

## Project Flow of ML Model Building – Email Spam Classifier

### 1. Text Cleaning
Feature extraction requires normalized text.
- Lowercase
- Remove URLs
- Remove numbers
- Remove punctuation
- Tokenization

### 2. EDA (Exploratory Data Analysis)
Initial analysis phase to understand dataset characteristics. Key Tasks:
- Class distribution (Spam vs Ham)
- Email length analysis
- Word frequency visualization
- Detect anomalies or imbalance
- Purpose: Identify patterns and validate modeling assumptions.

### 3. Text Pre-processing
Transforms raw email text into machine-readable features.
- Lowercasing text
- Remove punctuation & stopwords
- Tokenization
- Stemming/Lemmatization
- Vectorization using TF-IDF

### 4. Model Building
Training the classification algorithms.
- Train–test split
- Feature extraction from text
- Train models:
  - Naïve Bayes
  - Logistic Regression
  - SVM

### 5. Model Evaluation
Assess model effectiveness.
- Metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - Confusion Matrix
- Focus: Balance between spam detection and false positives.

### 6. Improvement
Performance optimization stage.
- Hyperparameter tuning
- N-gram features
- Handle class imbalance
- Ensemble / advanced models

### 7. User Interface (Website)
Front-end system for predictions.
- Email text input
- Predict button
- Output: Spam / Not Spam
- Built with HTML, CSS, JS + Flask/Django

### 8. Deployment on Heroku
Cloud hosting for public access.
- Upload Flask app + model files
- Add requirements.txt
- Add Procfile
- Deploy via Git
- Generate live public URL

## Project Tree

```
E-Mail_Spam_Classifier/
├── README.md                                  # Project documentation
├── LICENSE                                    # License file
├── Multi_Model_E-Mail_Spam_Classifier.pptx   # Project presentation
│
├── data/
│   ├── raw/                                   # Raw email data
│   │   └── emails.csv                        # Original email dataset
│   └── processed/                             # Cleaned and processed data
│       └── preprocessed_emails.csv           # Feature-engineered data
│
├── notebooks/
│   ├── 01_EDA.ipynb                          # Exploratory Data Analysis
│   ├── 02_Text_Preprocessing.ipynb            # Text cleaning and preprocessing
│   ├── 03_Model_Building.ipynb                # Model training and comparison
│   └── 04_Model_Evaluation.ipynb              # Performance metrics analysis
│
├── src/
│   ├── __init__.py
│   ├── text_cleaning.py                       # Text cleaning utilities
│   ├── preprocessing.py                       # Data preprocessing functions
│   ├── feature_extraction.py                  # TF-IDF vectorization
│   ├── model_training.py                      # Model training pipeline
│   ├── model_evaluation.py                    # Evaluation metrics
│   └── utils.py                               # Helper functions
│
├── models/
│   ├── naive_bayes_model.pkl                  # Trained Naïve Bayes model
│   ├── logistic_regression_model.pkl          # Trained Logistic Regression
│   ├── svm_model.pkl                          # Trained SVM model
│   ├── tfidf_vectorizer.pkl                   # TF-IDF vectorizer
│   └── best_model.pkl                         # Best performing model
│
├── app/
│   ├── app.py                                 # Flask/Django application
│   ├── templates/
│   │   └── index.html                         # Web interface
│   └── static/
│       ├── css/
│       │   └── style.css                      # Styling
│       └── js/
│           └── script.js                      # Frontend logic
│
├── tests/
│   ├── __init__.py
│   ├── test_text_cleaning.py                  # Unit tests for cleaning
│   ├── test_preprocessing.py                  # Unit tests for preprocessing
│   └── test_models.py                         # Unit tests for models
│
├── requirements.txt                           # Python dependencies
├── Procfile                                   # Heroku deployment configuration
├── .gitignore                                 # Git ignore file
└── config.py                                  # Configuration settings
```

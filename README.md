Deploy Link: https://dermaa.streamlit.app/

# Project Name

**AI-Dermatology Assistant**

# Description

AI-Dermatology Assistant is a Streamlit-based medical diagnostic assistant that uses A* reasoning to analyze patient-reported symptoms and predict the most likely dermatological conditions. The system combines symptom matching with condition severity weighting to provide ranked diagnoses and recommended next steps for patients or healthcare professionals. This lightweight prototype is designed to demonstrate AI-assisted medical reasoning and a clean, modern web interface.

# Features

* Interactive web interface built with Streamlit.
* A* search-based diagnostic engine that ranks possible diseases.
* Symptom matching combined with severity scoring.
* Clean and modern UI with responsive cards and highlighted probability scores.
* Provides recommended next steps for each condition.
* Lightweight and prototype-friendly — suitable for local/offline usage.

# Getting Started

## Prerequisites

* Python 3.10 or higher
* Streamlit

```bash
pip install streamlit
```

## Running the App

1. Clone this repository.
2. Navigate to the project folder.
3. Run the app using Streamlit:

```bash
streamlit run main.py
```

4. Open the provided local URL in your browser to interact with the diagnostic assistant.

# Usage

* Enter patient-reported symptoms separated by commas.
* Click **Analyze Condition**.
* View ranked disease predictions, matched symptoms, and recommended next steps.

# Technologies Used

* Python 3.12
* Streamlit for UI
* Heapq for A* priority queue handling

# Future Enhancements

* Add BFS and DFS search comparison for educational purposes.
* Incorporate NLP-based symptom extraction for free-text input.
* Add red-flag alerts for critical conditions.
* Extend to multi-specialty medical diagnosis.
* Deploy as a lightweight edge app for low-bandwidth settings.

# License

This project is open-source and free to use for educational and prototype purposes.

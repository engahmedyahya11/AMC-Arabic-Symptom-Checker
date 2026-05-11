# AMC Arabic Symptom Checker

Arabic medical symptom checker using Python and Gradio.  
The app helps users enter their symptoms in Arabic and get a list of possible specialties to visit.

## Features

- Arabic text input for symptoms
- Simple UI built with Gradio
- Suggests medical specialties based on the described symptoms

## Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/engahmedyahya11/AMC-Arabic-Symptom-Checker.git
   cd AMC-Arabic-Symptom-Checker
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python app.py
   ```

4. Open the Gradio link shown in the terminal in your browser.

## Files"link "https://amc-arabic-symptom-checker.onrender.com/""

- `app.py`: Gradio interface and main app logic
- `model.py`: functions for processing symptoms and predicting specialties
- `specialties.py`: list/mapping of medical specialties in Arabic
- `requirements.txt`: Python dependencies
- `logo.png`: app logo

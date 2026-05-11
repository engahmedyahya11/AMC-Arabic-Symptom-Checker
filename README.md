# 🏥 AMC Hospital - Arabic Medical Symptom Checker

A production-ready bilingual (Arabic/English) symptom analysis application built for **Aseel Medical Care Hospital (AMC)**, Red Sea, Egypt.

## 🌟 Features

- **Bilingual Support:** Full Arabic and English interface with RTL support
- **15+ Medical Specialties:** Comprehensive coverage of all AMC departments
- **AI-Powered Analysis:** TF-IDF embeddings with cosine similarity matching
- **Urgency Detection:** Automated red flag keyword detection
- **AMC Branding:** Custom theme with hospital colors and information
- **24/7 Emergency Integration:** Direct contact information included

## 🏗️ Technical Stack

- **Framework:** Gradio 4.0+
- **NLP:** Scikit-learn TF-IDF, LangDetect
- **Deployment:** Hugging Face Spaces
- **Language Models:** Rule-based + embedding similarity (no API costs)

## 📁 Project Structure

amc-symptom-checker/
├── app.py              # Main Gradio application
├── model.py            # Symptom analysis engine
├── specialties.py      # Medical specialty database
├── requirements.txt    # Python dependencies
└── README.md          # Documentation

## 🚀 Local Testing in Colab

%cd /content/drive/MyDrive/amc-symptom-checker
!python app.py

## 🌐 Deployment to Hugging Face Spaces

### Method 1: Using Colab (Recommended)

from huggingface_hub import HfApi, create_repo, login

# Login to Hugging Face
login(token="YOUR_HF_TOKEN_HERE")

# Create Space
api = HfApi()
repo_id = "YOUR_USERNAME/amc-symptom-checker"

try:
    create_repo(repo_id=repo_id, repo_type="space", space_sdk="gradio")
except:
    print("Repo already exists")

# Upload files
files_to_upload = ['app.py', 'model.py', 'specialties.py', 'requirements.txt', 'README.md']
project_dir = '/content/drive/MyDrive/amc-symptom-checker'

for file in files_to_upload:
    api.upload_file(
        path_or_fileobj=f"{project_dir}/{file}",
        path_in_repo=file,
        repo_id=repo_id,
        repo_type="space"
    )
    print(f"✅ Uploaded {file}")

print(f"🎉 Visit: https://huggingface.co/spaces/{repo_id}")

### Method 2: Manual Upload

1. Go to [Hugging Face Spaces](https://huggingface.co/new-space)
2. Create new Space with **Gradio SDK**
3. Upload all 5 files from Google Drive
4. Space will auto-deploy

## 🏥 AMC Hospital Information

**Aseel Medical Care Hospital (AMC)**
- 📍 Address: 9 El Kamar District, El Hadaba, Hurghada, Red Sea, Egypt
- 📞 Emergency 24/7: +20 65 344 1110
- 🌐 Website: [www.amc-redsea.com](https://www.amc-redsea.com)
- ✅ JCI Accredited | Established 2010
- 🛏️ 25 beds | Specialized in Orthopedics, Cardiology, Emergency Care

## 📊 Supported Specialties

1. Orthopedics (جراحة العظام)
2. Cardiology (أمراض القلب)
3. Emergency Medicine (الطوارئ)
4. General Surgery (الجراحة العامة)
5. Intensive Care (العناية المركزة)
6. Internal Medicine (الباطنة)
7. Pediatrics (طب الأطفال)
8. Women's Health (صحة المرأة)
9. Neurology (المخ والأعصاب)
10. Urology (المسالك البولية)
11. ENT (الأنف والأذن والحنجرة)
12. Dermatology (الأمراض الجلدية)
13. Ophthalmology (طب العيون)
14. Dentistry (طب الأسنان)
15. Radiology (الأشعة التشخيصية)
16. Laboratory (المختبر الطبي)

## ⚕️ Medical Disclaimer

This system is a diagnostic **assistant only** and not a substitute for direct medical consultation. All results are indicative and do not constitute a final medical diagnosis.

## 👨‍💻 Developer

Built by Ahmed Yahya for AMC Hospital
Portfolio-ready code with production standards

## 📄 License

Proprietary - AMC Hospital © 2026

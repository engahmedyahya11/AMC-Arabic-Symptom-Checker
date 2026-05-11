"""
AMC Hospital Symptom Analyzer
AI-powered medical symptom analysis using Arabic NLP
"""

import re
import numpy as np
from typing import Dict, List, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from langdetect import detect, LangDetectException
from specialties import SPECIALTIES, get_all_specialties

class SymptomAnalyzer:
    """Advanced symptom analysis engine for AMC Hospital."""

    def __init__(self) -> None:
        """Initialize analyzer with specialty database and TF-IDF."""
        self.specialties = SPECIALTIES
        self.specialty_keys = get_all_specialties()
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 3),
            max_features=1000,
            min_df=1
        )
        self._prepare_symptom_database()

    def _prepare_symptom_database(self) -> None:
        """Prepare TF-IDF vectors for each specialty symptom list."""
        self.symptom_texts: List[str] = []
        self.specialty_map: List[str] = []

        for key in self.specialty_keys:
            data = self.specialties[key]
            combined = " ".join(data["symptoms_ar"] + data["symptoms_en"])
            self.symptom_texts.append(combined)
            self.specialty_map.append(key)

        self.symptom_vectors = self.vectorizer.fit_transform(self.symptom_texts)

    def detect_language(self, text: str) -> str:
        """Detect language: 'ar', 'en', or fallback."""
        try:
            lang = detect(text)
            if lang == "ar":
                return "ar"
            return "en"
        except LangDetectException:
            arabic_chars = sum(1 for c in text if "؀" <= c <= "ۿ")
            return "ar" if arabic_chars > len(text) * 0.3 else "en"

    def preprocess(self, text: str) -> str:
        """Normalize text (remove tashkeel, normalize Arabic letters, lowercase)."""
        text = re.sub(r"[ً-ٟ]", "", text)
        text = text.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
        text = text.replace("ى", "ي").replace("ة", "ه")
        text = re.sub(r"\s+", " ", text).strip()
        return text.lower()

    def get_urgency(self, text: str, language: str) -> Tuple[str, str]:
        """Infer urgency level from red flag keywords and severity words."""
        text_lower = text.lower()
        high_cnt = 0
        med_cnt = 0

        for data in self.specialties.values():
            key = f"urgency_keywords_{language}"
            if key in data:
                for kw in data[key]:
                    if kw.lower() in text_lower:
                        high_cnt += 1

        if high_cnt >= 2:
            return "عالية - HIGH", "#DC2626"
        if high_cnt == 1:
            return "متوسطة - MEDIUM", "#F59E0B"

        severe_ar = ["شديد", "حاد", "مفاجئ", "غير محتمل", "مستمر"]
        severe_en = ["severe", "acute", "sudden", "unbearable", "persistent"]
        indicators = severe_ar if language == "ar" else severe_en
        for ind in indicators:
            if ind in text_lower:
                med_cnt += 1
        if med_cnt >= 2:
            return "متوسطة - MEDIUM", "#F59E0B"
        return "منخفضة - LOW", "#10B981"

    def analyze(self, symptoms_text: str) -> Dict:
        """Analyze free text symptoms and return best matching specialties."""
        language = self.detect_language(symptoms_text)
        cleaned = self.preprocess(symptoms_text)
        vec = self.vectorizer.transform([cleaned])
        sims = cosine_similarity(vec, self.symptom_vectors)[0]
        top_idx = np.argsort(sims)[::-1][:3]

        results: List[Dict] = []
        for idx in top_idx:
            key = self.specialty_map[idx]
            data = self.specialties[key]
            conf = float(sims[idx]) * 100.0
            urg_key = f"urgency_keywords_{language}"
            if urg_key in data:
                for kw in data[urg_key]:
                    if kw.lower() in cleaned:
                        conf = min(conf * 1.2, 99.9)
                        break
            results.append({
                "specialty_key": key,
                "name_ar": data["name_ar"],
                "name_en": data["name_en"],
                "confidence": round(conf, 1)
            })

        urgency, color = self.get_urgency(cleaned, language)

        return {
            "top_specialty": results[0] if results else None,
            "all_matches": results,
            "urgency": urgency,
            "urgency_color": color,
            "language": language
        }

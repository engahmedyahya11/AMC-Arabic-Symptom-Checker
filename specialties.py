"""
AMC Hospital Medical Specialties Database
Contains comprehensive symptom mappings for all hospital departments
"""

SPECIALTIES = {
    # === Orthopedics ===
    "orthopedics": {
        "name_ar": "جراحة العظام",
        "name_en": "Orthopedics",
        "symptoms_ar": [
            "ألم في المفاصل", "تورم في الركبة", "كسر", "التواء", "ألم في الظهر",
            "ألم في الرقبة", "صعوبة في المشي", "تيبس المفاصل", "ألم في الكتف",
            "ألم في الكوع", "ألم في الورك", "عدم القدرة على تحريك الذراع",
            "تشوه في العظام", "ألم بعد إصابة رياضية", "خلع في المفصل",
            "ألم في العمود الفقري", "ألم في القدم", "كسر في العظم",
            "ألم مزمن في الظهر", "إصابة في الرباط الصليبي", "هشاشة عظام",
            "انزلاق غضروفي", "ألم في الفقرات", "تمزق في الأربطة"
        ],
        "symptoms_en": [
            "joint pain", "knee swelling", "fracture", "sprain", "back pain",
            "neck pain", "difficulty walking", "joint stiffness", "shoulder pain",
            "elbow pain", "hip pain", "unable to move arm", "bone deformity",
            "sports injury pain", "joint dislocation", "spine pain", "foot pain",
            "broken bone", "chronic back pain", "ACL injury", "osteoporosis",
            "herniated disc", "vertebrae pain", "ligament tear"
        ],
        "urgency_keywords_ar": ["كسر", "خلع", "نزيف", "تشوه شديد", "فقدان الإحساس", "شلل"],
        "urgency_keywords_en": ["fracture", "dislocation", "bleeding", "severe deformity", "numbness", "paralysis"]
    },

    # === Cardiology ===
    "cardiology": {
        "name_ar": "أمراض القلب",
        "name_en": "Cardiology",
        "symptoms_ar": [
            "ألم في الصدر", "ضيق في التنفس", "خفقان", "دوخة", "إغماء",
            "تعب شديد", "تورم في القدمين", "عدم انتظام ضربات القلب",
            "ألم في الذراع الأيسر", "تعرق بارد", "غثيان مع ألم الصدر",
            "ضغط على الصدر", "ألم يمتد للفك", "تسارع نبضات القلب",
            "بطء نبضات القلب", "ألم عند المجهود", "ضيق تنفس عند النوم",
            "سعال مع دم", "ازرقاق الشفاه", "ألم حارق في الصدر",
            "نبض ضعيف", "برودة الأطراف", "انتفاخ البطن مع ضيق التنفس"
        ],
        "symptoms_en": [
            "chest pain", "shortness of breath", "palpitations", "dizziness", "fainting",
            "extreme fatigue", "swollen feet", "irregular heartbeat", "left arm pain",
            "cold sweat", "nausea with chest pain", "chest pressure",
            "pain radiating to jaw", "rapid heartbeat", "slow heartbeat",
            "pain during exertion", "breathlessness while lying down",
            "coughing blood", "blue lips", "burning chest pain",
            "weak pulse", "cold extremities", "abdominal bloating with dyspnea"
        ],
        "urgency_keywords_ar": ["ألم في الصدر", "إغماء", "ضيق شديد في التنفس", "تعرق بارد", "ألم في الذراع الأيسر", "سعال مع دم"],
        "urgency_keywords_en": ["chest pain", "fainting", "severe shortness of breath", "cold sweat", "left arm pain", "coughing blood"]
    },

    # === Emergency ===
    "emergency": {
        "name_ar": "الطوارئ",
        "name_en": "Emergency Medicine",
        "symptoms_ar": [
            "نزيف حاد", "حادث سيارة", "إصابة خطيرة", "فقدان الوعي",
            "حروق شديدة", "تسمم", "صدمة", "ألم حاد مفاجئ",
            "صعوبة شديدة في التنفس", "نوبة قلبية محتملة", "جلطة محتملة",
            "كسر مفتوح", "إصابة في الرأس", "نزيف داخلي", "قيء مستمر",
            "إسهال شديد مع جفاف", "حمى عالية جداً", "تشنجات",
            "رد فعل تحسسي شديد", "لدغة عقرب أو ثعبان", "غرق جزئي",
            "صعق كهربائي", "جرح عميق", "ألم بطن حاد"
        ],
        "symptoms_en": [
            "severe bleeding", "car accident", "serious injury", "loss of consciousness",
            "severe burns", "poisoning", "shock", "sudden severe pain",
            "severe breathing difficulty", "possible heart attack", "possible stroke",
            "open fracture", "head injury", "internal bleeding", "persistent vomiting",
            "severe diarrhea with dehydration", "very high fever", "seizures",
            "severe allergic reaction", "scorpion or snake bite", "near drowning",
            "electric shock", "deep wound", "acute abdominal pain"
        ],
        "urgency_keywords_ar": ["نزيف", "حادث", "إغماء", "تسمم", "حروق", "صدمة", "كسر مفتوح", "جلطة", "تشنجات"],
        "urgency_keywords_en": ["bleeding", "accident", "unconscious", "poisoning", "burns", "shock", "open fracture", "stroke", "seizures"]
    },

    # === باقي التخصصات ===
    "general_surgery": {
        "name_ar": "الجراحة العامة",
        "name_en": "General Surgery",
        "symptoms_ar": [
            "ألم في البطن", "انتفاخ البطن", "فتق", "كتلة في البطن",
            "ألم عند الضغط على البطن", "قيء مع ألم بطني", "إمساك شديد",
            "عدم القدرة على إخراج الغازات", "ألم حول السرة", "ألم في الجانب الأيمن السفلي",
            "ألم بعد تناول الطعام", "حرقة شديدة", "ألم في المرارة",
            "يرقان", "تغير في حركة الأمعاء", "دم في البراز",
            "ألم في الشرج", "بواسير مؤلمة", "خراج", "جرح لا يلتئم",
            "كتلة في الثدي", "ألم عند البلع", "صعوبة في الهضم"
        ],
        "symptoms_en": [
            "abdominal pain", "bloating", "hernia", "abdominal mass",
            "pain when pressing abdomen", "vomiting with abdominal pain", "severe constipation",
            "inability to pass gas", "pain around navel", "right lower quadrant pain",
            "pain after eating", "severe heartburn", "gallbladder pain",
            "jaundice", "change in bowel habits", "blood in stool",
            "anal pain", "painful hemorrhoids", "abscess", "non-healing wound",
            "breast lump", "pain while swallowing", "digestive difficulty"
        ],
        "urgency_keywords_ar": ["ألم حاد في البطن", "قيء مستمر", "دم في البراز", "يرقان", "فتق مختنق"],
        "urgency_keywords_en": ["severe abdominal pain", "persistent vomiting", "blood in stool", "jaundice", "strangulated hernia"]
    },

    "icu": {
        "name_ar": "العناية المركزة",
        "name_en": "Intensive Care Unit",
        "symptoms_ar": [
            "فشل تنفسي", "غيبوبة", "صدمة إنتانية", "فشل عضو متعدد",
            "انخفاض حاد في ضغط الدم", "نوبة قلبية حادة", "جلطة دماغية حادة",
            "فشل كلوي حاد", "تسمم شديد", "إصابة متعددة الأعضاء",
            "حالة حرجة بعد عملية جراحية", "نزيف داخلي شديد",
            "عدم استقرار حيوي", "حاجة لجهاز تنفس", "حالة صدمة",
            "التهاب رئوي حاد", "حموضة دم شديدة", "اضطراب في الكهارل"
        ],
        "symptoms_en": [
            "respiratory failure", "coma", "septic shock", "multi-organ failure",
            "severe hypotension", "acute heart attack", "acute stroke",
            "acute kidney failure", "severe poisoning", "multi-trauma",
            "critical post-operative condition", "severe internal bleeding",
            "hemodynamic instability", "need for ventilator", "shock state",
            "severe pneumonia", "severe acidosis", "electrolyte imbalance"
        ],
        "urgency_keywords_ar": ["غيبوبة", "فشل", "صدمة", "حرجة", "نزيف شديد"],
        "urgency_keywords_en": ["coma", "failure", "shock", "critical", "severe bleeding"]
    },

    "internal_medicine": {
        "name_ar": "الباطنة",
        "name_en": "Internal Medicine",
        "symptoms_ar": [
            "حمى", "صداع", "تعب عام", "فقدان الشهية", "فقدان وزن",
            "سعال مزمن", "ألم في المعدة", "إسهال", "غثيان", "قيء",
            "ألم في العضلات", "ألم في المفاصل بدون تورم", "دوخة خفيفة",
            "عطش شديد", "كثرة التبول", "تنميل في الأطراف", "ضعف عام",
            "اصفرار العينين", "حكة جلدية", "تعرق ليلي", "قشعريرة",
            "ألم في الحلق", "احتقان", "رعشة"
        ],
        "symptoms_en": [
            "fever", "headache", "general fatigue", "loss of appetite", "weight loss",
            "chronic cough", "stomach pain", "diarrhea", "nausea", "vomiting",
            "muscle pain", "joint pain without swelling", "mild dizziness",
            "excessive thirst", "frequent urination", "numbness in limbs", "general weakness",
            "yellowing of eyes", "skin itching", "night sweats", "chills",
            "sore throat", "congestion", "tremor"
        ],
        "urgency_keywords_ar": ["حمى عالية", "قيء دموي", "فقدان وزن سريع"],
        "urgency_keywords_en": ["high fever", "bloody vomit", "rapid weight loss"]
    },

    "pediatrics": {
        "name_ar": "طب الأطفال",
        "name_en": "Pediatrics",
        "symptoms_ar": [
            "حمى عند طفل", "بكاء مستمر", "رفض الرضاعة", "قيء عند رضيع",
            "إسهال عند طفل", "طفح جلدي", "سعال عند طفل", "صعوبة في التنفس عند طفل",
            "تشنجات حموية", "خمول غير طبيعي", "ألم في الأذن عند طفل",
            "ألم في البطن عند طفل", "تأخر في النمو", "فقدان شهية عند طفل",
            "حساسية غذائية", "تطعيمات", "فحص روتيني للطفل"
        ],
        "symptoms_en": [
            "child fever", "continuous crying", "refusing feeding", "infant vomiting",
            "child diarrhea", "skin rash", "child cough", "child breathing difficulty",
            "febrile seizures", "abnormal lethargy", "child ear pain",
            "child abdominal pain", "growth delay", "child appetite loss",
            "food allergy", "vaccinations", "child routine checkup"
        ],
        "urgency_keywords_ar": ["تشنجات", "صعوبة شديدة في التنفس", "خمول شديد", "رفض الرضاعة التام"],
        "urgency_keywords_en": ["seizures", "severe breathing difficulty", "severe lethargy", "complete feeding refusal"]
    },

    "women_health": {
        "name_ar": "صحة المرأة",
        "name_en": "Women's Health",
        "symptoms_ar": [
            "ألم أثناء الدورة الشهرية", "نزيف غير طبيعي", "تأخر الدورة",
            "ألم في الحوض", "إفرازات مهبلية", "ألم أثناء العلاقة الزوجية",
            "أعراض الحمل", "غثيان الحمل", "ألم في الثدي", "كتلة في الثدي",
            "انقطاع الطمث", "عدم انتظام الدورة", "نزيف بعد سن اليأس",
            "ألم في المبايض", "تكيس المبايض"
        ],
        "symptoms_en": [
            "menstrual pain", "abnormal bleeding", "missed period",
            "pelvic pain", "vaginal discharge", "painful intercourse",
            "pregnancy symptoms", "morning sickness", "breast pain", "breast lump",
            "amenorrhea", "irregular period", "postmenopausal bleeding",
            "ovarian pain", "polycystic ovaries"
        ],
        "urgency_keywords_ar": ["نزيف حاد", "ألم حوضي شديد", "نزيف في الحمل"],
        "urgency_keywords_en": ["severe bleeding", "severe pelvic pain", "pregnancy bleeding"]
    },

    "neurology": {
        "name_ar": "المخ والأعصاب",
        "name_en": "Neurology",
        "symptoms_ar": [
            "صداع شديد", "صداع نصفي", "دوخة مستمرة", "فقدان التوازن",
            "تنميل في جانب من الجسم", "ضعف في الذراع أو الساق",
            "صعوبة في الكلام", "تشويش في الرؤية", "ازدواج الرؤية",
            "رعشة لا إرادية", "نوبات صرع", "فقدان الذاكرة",
            "تشنجات عضلية", "ألم في العصب", "شلل في الوجه",
            "صعوبة في البلع", "فقدان حاسة الشم أو التذوق"
        ],
        "symptoms_en": [
            "severe headache", "migraine", "persistent dizziness", "loss of balance",
            "numbness on one side", "weakness in arm or leg",
            "difficulty speaking", "blurred vision", "double vision",
            "involuntary tremor", "epileptic seizures", "memory loss",
            "muscle spasms", "nerve pain", "facial paralysis",
            "difficulty swallowing", "loss of smell or taste"
        ],
        "urgency_keywords_ar": ["صداع مفاجئ شديد", "فقدان الوعي", "شلل", "صعوبة في الكلام", "تنميل مفاجئ", "نوبة صرع"],
        "urgency_keywords_en": ["sudden severe headache", "loss of consciousness", "paralysis", "difficulty speaking", "sudden numbness", "seizure"]
    },

    "urology": {
        "name_ar": "المسالك البولية",
        "name_en": "Urology",
        "symptoms_ar": [
            "حرقان عند التبول", "دم في البول", "ألم في الخاصرة",
            "تبول متكرر", "صعوبة في التبول", "عدم القدرة على التبول",
            "ألم في الكلى", "حصوات الكلى", "التهاب المثانة",
            "تضخم البروستاتا", "ألم في الخصية", "تورم في الخصية",
            "سلس بولي", "تقطع في البول", "لون بول غامق"
        ],
        "symptoms_en": [
            "burning during urination", "blood in urine", "flank pain",
            "frequent urination", "difficulty urinating", "inability to urinate",
            "kidney pain", "kidney stones", "bladder infection",
            "enlarged prostate", "testicular pain", "testicular swelling",
            "urinary incontinence", "interrupted urine stream", "dark urine"
        ],
        "urgency_keywords_ar": ["عدم القدرة على التبول", "دم في البول", "ألم شديد في الكلى"],
        "urgency_keywords_en": ["inability to urinate", "blood in urine", "severe kidney pain"]
    },

    "ent": {
        "name_ar": "الأنف والأذن والحنجرة",
        "name_en": "ENT (Ear, Nose, Throat)",
        "symptoms_ar": [
            "ألم في الأذن", "طنين في الأذن", "فقدان السمع", "دوخة ودوار",
            "انسداد الأنف", "رعاف", "التهاب الجيوب الأنفية", "فقدان حاسة الشم",
            "ألم في الحلق", "صعوبة في البلع", "بحة في الصوت", "تضخم اللوزتين",
            "صعوبة في التنفس من الأنف", "إفرازات من الأذن", "حساسية الأنف"
        ],
        "symptoms_en": [
            "ear pain", "tinnitus", "hearing loss", "vertigo",
            "nasal congestion", "nosebleed", "sinusitis", "loss of smell",
            "sore throat", "difficulty swallowing", "hoarseness", "enlarged tonsils",
            "nasal breathing difficulty", "ear discharge", "allergic rhinitis"
        ],
        "urgency_keywords_ar": ["صعوبة شديدة في التنفس", "نزيف أنف مستمر", "فقدان مفاجئ للسمع"],
        "urgency_keywords_en": ["severe breathing difficulty", "persistent nosebleed", "sudden hearing loss"]
    },

    "dermatology": {
        "name_ar": "الأمراض الجلدية",
        "name_en": "Dermatology",
        "symptoms_ar": [
            "طفح جلدي", "حكة جلدية", "احمرار الجلد", "تقشير الجلد",
            "حب الشباب", "أكزيما", "صدفية", "حساسية جلدية",
            "بقع بيضاء", "بقع داكنة", "ثآليل", "فطريات الجلد",
            "تساقط الشعر", "جفاف البشرة", "التهاب الجلد"
        ],
        "symptoms_en": [
            "skin rash", "skin itching", "skin redness", "skin peeling",
            "acne", "eczema", "psoriasis", "skin allergy",
            "white patches", "dark spots", "warts", "skin fungus",
            "hair loss", "dry skin", "dermatitis"
        ],
        "urgency_keywords_ar": ["طفح مع حمى", "حساسية شديدة", "تورم في الوجه"],
        "urgency_keywords_en": ["rash with fever", "severe allergy", "facial swelling"]
    },

    "ophthalmology": {
        "name_ar": "طب العيون",
        "name_en": "Ophthalmology",
        "symptoms_ar": [
            "ألم في العين", "احمرار العين", "حكة في العين", "تشويش الرؤية",
            "فقدان الرؤية المفاجئ", "ازدواج الرؤية", "حساسية للضوء",
            "دموع زائدة", "جفاف العين", "رؤية هالات حول الأضواء",
            "إفرازات من العين", "تورم الجفن", "ألم عند تحريك العين"
        ],
        "symptoms_en": [
            "eye pain", "red eye", "itchy eye", "blurred vision",
            "sudden vision loss", "double vision", "light sensitivity",
            "excessive tearing", "dry eye", "halos around lights",
            "eye discharge", "swollen eyelid", "pain when moving eye"
        ],
        "urgency_keywords_ar": ["فقدان مفاجئ للرؤية", "ألم شديد في العين", "إصابة في العين"],
        "urgency_keywords_en": ["sudden vision loss", "severe eye pain", "eye injury"]
    },

    "dentistry": {
        "name_ar": "طب الأسنان",
        "name_en": "Dentistry",
        "symptoms_ar": [
            "ألم في الأسنان", "تسوس الأسنان", "نزيف اللثة", "تورم اللثة",
            "خراج في الأسنان", "حساسية الأسنان", "رائحة الفم الكريهة",
            "كسر في السن", "سقوط حشوة", "ألم عند المضغ",
            "تقرحات في الفم", "جفاف الفم", "ألم في الفك"
        ],
        "symptoms_en": [
            "toothache", "tooth decay", "bleeding gums", "swollen gums",
            "dental abscess", "tooth sensitivity", "bad breath",
            "broken tooth", "lost filling", "pain while chewing",
            "mouth ulcers", "dry mouth", "jaw pain"
        ],
        "urgency_keywords_ar": ["خراج", "تورم شديد في اللثة", "ألم أسنان غير محتمل"],
        "urgency_keywords_en": ["abscess", "severe gum swelling", "unbearable toothache"]
    },

    "radiology": {
        "name_ar": "الأشعة التشخيصية",
        "name_en": "Radiology",
        "symptoms_ar": [
            "طلب أشعة سينية", "طلب أشعة مقطعية", "طلب رنين مغناطيسي",
            "طلب أشعة بالصبغة", "طلب موجات فوق صوتية", "طلب إيكو",
            "طلب دوبلر", "فحص تصويري", "متابعة أشعة"
        ],
        "symptoms_en": [
            "X-ray request", "CT scan request", "MRI request",
            "contrast imaging", "ultrasound request", "echo request",
            "doppler request", "imaging exam", "imaging follow-up"
        ],
        "urgency_keywords_ar": [],
        "urgency_keywords_en": []
    },

    "laboratory": {
        "name_ar": "المختبر الطبي",
        "name_en": "Laboratory",
        "symptoms_ar": [
            "طلب تحاليل دم", "طلب تحليل سكر", "طلب تحليل كوليسترول",
            "طلب تحليل وظائف كلى", "طلب تحليل وظائف كبد",
            "طلب تحليل بول", "طلب تحليل براز", "فحص شامل",
            "تحليل هرمونات", "تحليل فيتامينات", "تحليل معادن"
        ],
        "symptoms_en": [
            "blood test request", "glucose test", "cholesterol test",
            "kidney function test", "liver function test",
            "urine test", "stool test", "comprehensive checkup",
            "hormone test", "vitamin test", "mineral test"
        ],
        "urgency_keywords_ar": [],
        "urgency_keywords_en": []
    }
}

def get_all_specialties() -> list:
    """Return list of all specialty keys"""
    return list(SPECIALTIES.keys())

def get_specialty_info(specialty_key: str) -> dict:
    """Get detailed information for a specific specialty"""
    return SPECIALTIES.get(specialty_key, {})

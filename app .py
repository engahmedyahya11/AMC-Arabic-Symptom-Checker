"""
AMC Hospital - Arabic Medical Symptom Checker
Production Gradio Application with AMC Branding + Logo
"""

import gradio as gr
from model import SymptomAnalyzer
import base64
import os

analyzer = SymptomAnalyzer()

def get_logo_base64(logo_path: str = "/content/logo.png") -> str:
    """Return base64 data URL for logo if exists, else empty string."""
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode()
    return ""

AMC_LOGO = get_logo_base64()

def analyze_symptoms(symptoms: str):
    """Analyze user symptoms and return specialty, urgency, top3, disclaimer."""
    if not symptoms or len(symptoms.strip()) < 5:
        msg = "⚠️ من فضلك اكتب الأعراض بوضوح\n⚠️ Please describe your symptoms clearly"
        return msg, "", "", ""

    results = analyzer.analyze(symptoms)
    top = results["top_specialty"]

    if top:
        specialty_output = f"""
<div style="background: linear-gradient(135deg, #FF8C42 0%, #4A90E2 100%); padding: 25px; border-radius: 15px; color: white; margin: 15px 0;">
  <h2 style="margin:0 0 10px 0;">🏥 التخصص الموصى به / Recommended Specialty</h2>
  <div style="background: rgba(255,255,255,0.18); padding: 18px; border-radius: 10px;">
    <h3 style="margin:0; font-size: 1.8em;">{top['name_ar']}</h3>
    <h3 style="margin:8px 0 0 0; font-size: 1.4em;">{top['name_en']}</h3>
    <p style="margin-top:12px; font-size:1.1em;">
      <strong>مستوى الثقة / Confidence:</strong> {top['confidence']}%
    </p>
  </div>
</div>
"""
    else:
        specialty_output = "لم نتمكن من تحديد التخصص.\nUnable to determine specialty."

    urgency_badge = f"""
<div style="background-color: {results['urgency_color']}; color: white; padding: 18px; border-radius: 15px;
            text-align: center; font-size: 1.2em; font-weight: bold; margin: 15px 0;">
  ⚠️ مستوى الإلحاح / Urgency Level: {results['urgency']}
</div>
"""

    top3_html = """
<div style="margin: 20px 0;">
<table style="width:100%; border-collapse: collapse; box-shadow:0 2px 10px rgba(0,0,0,0.08);">
  <thead>
    <tr style="background: linear-gradient(135deg,#FF8C42 0%,#4A90E2 100%); color:white;">
      <th style="padding:12px; text-align:center;">الترتيب<br>Rank</th>
      <th style="padding:12px; text-align:right;">التخصص بالعربية</th>
      <th style="padding:12px; text-align:left;">Specialty</th>
      <th style="padding:12px; text-align:center;">الثقة %</th>
    </tr>
  </thead>
  <tbody>
"""
    for i, m in enumerate(results["all_matches"], 1):
        bg = "#FFF5ED" if i % 2 == 0 else "#F0F7FF"
        top3_html += f"""
    <tr style="background:{bg};">
      <td style="padding:10px; text-align:center; font-weight:bold; color:#FF8C42;">{i}</td>
      <td style="padding:10px; text-align:right; direction:rtl;">{m['name_ar']}</td>
      <td style="padding:10px; text-align:left;">{m['name_en']}</td>
      <td style="padding:10px; text-align:center; font-weight:bold; color:#4A90E2;">{m['confidence']}%</td>
    </tr>
"""
    top3_html += "  </tbody></table></div>"

    lang = results["language"]
    logo_img = (
        f'<img src="{AMC_LOGO}" alt="AMC Logo" style="height:60px; width:auto; margin-right:10px;">'
        if AMC_LOGO
        else ""
    )

    if lang == "ar":
        disclaimer = f"""
<div style="background: linear-gradient(to right,#FFF5ED,#F0F7FF); padding:22px; border-radius:15px;
            border-right:5px solid #FF8C42; margin-top:18px;">
  <h3 style="color:#FF8C42; margin-top:0;">⚕️ إخلاء المسؤولية الطبية</h3>
  <p style="line-height:1.8; color:#333;">هذا النظام مساعد تشخيصي فقط وليس بديلاً عن الاستشارة الطبية المباشرة.</p>
  <ul style="line-height:1.8; color:#333;">
    <li>النتائج استرشادية ولا تعتبر تشخيصاً نهائياً</li>
    <li>في حالات الطوارئ اتصل فوراً على: <strong style="color:#DC2626;">065 344 1110</strong></li>
    <li>الطوارئ متاحة 24/7 في مستشفى AMC بالغردقة</li>
  </ul>
  <div style="margin-top:12px; padding-top:12px; border-top:1px solid #FF8C42; display:flex; align-items:center; gap:12px; flex-wrap:wrap;">
    {logo_img}
    <div>
      <strong style="color:#4A90E2;">🏥 مستشفى أصيل للرعاية الطبية (AMC Hospital)</strong><br>
      <span style="color:#666;">Hurghada, Red Sea, Egypt</span><br>
      <a href="https://www.amc-redsea.com" target="_blank" style="color:#FF8C42; text-decoration:none;">www.amc-redsea.com</a>
    </div>
  </div>
</div>
"""
    else:
        disclaimer = f"""
<div style="background: linear-gradient(to right,#F0F7FF,#FFF5ED); padding:22px; border-radius:15px;
            border-left:5px solid #4A90E2; margin-top:18px;">
  <h3 style="color:#4A90E2; margin-top:0;">⚕️ Medical Disclaimer</h3>
  <p style="line-height:1.8; color:#333;">This tool is a diagnostic assistant only and not a substitute for medical consultation.</p>
  <ul style="line-height:1.8; color:#333;">
    <li>Results are indicative and not a final diagnosis</li>
    <li>In emergencies call: <strong style="color:#DC2626;">065 344 1110</strong></li>
    <li>Emergency Department available 24/7 at AMC Hospital</li>
  </ul>
  <div style="margin-top:12px; padding-top:12px; border-top:1px solid #4A90E2; display:flex; align-items:center; gap:12px; flex-wrap:wrap;">
    {logo_img}
    <div>
      <strong style="color:#FF8C42;">🏥 Aseel Medical Care Hospital (AMC Hospital)</strong><br>
      <span style="color:#666;">Hurghada, Red Sea, Egypt</span><br>
      <a href="https://www.amc-redsea.com" target="_blank" style="color:#4A90E2; text-decoration:none;">www.amc-redsea.com</a>
    </div>
  </div>
</div>
"""

    return specialty_output, urgency_badge, top3_html, disclaimer

custom_css = """
.gradio-container {font-family: 'Cairo', 'Segoe UI', sans-serif;
    background: linear-gradient(to bottom,#FFF5ED 0%,#F0F7FF 100%);}
#banner {background: linear-gradient(135deg,#FF8C42 0%,#4A90E2 100%);
    padding:35px 20px; border-radius:20px; margin-bottom:25px; text-align:center; color:white;}
#banner img.logo {height:80px; width:auto; margin-bottom:12px;}
.rtl-text textarea {direction:rtl; text-align:right; border:2px solid #FF8C42; border-radius:10px;}
button.primary {background: linear-gradient(135deg,#FF8C42 0%,#4A90E2 100%) !important;
    border:none !important; color:white !important; font-weight:600 !important;}
#footer {background:white; padding:25px; border-radius:15px; text-align:center; margin-top:25px;
    border-top:4px solid #4A90E2;}
#footer img.logo-footer {height:70px; width:auto; margin-bottom:10px;}
"""

examples = [
    ["ألم شديد في الصدر مع ضيق في التنفس وتعرق بارد"],
    ["كسر في الذراع بعد السقوط مع تورم وألم شديد"],
    ["حمى عالية عند طفل مع قيء"],
    ["Severe chest pain with shortness of breath"],
]

with gr.Blocks(theme=gr.themes.Soft(), css=custom_css) as demo:
    logo_html = f'<img src="{AMC_LOGO}" alt="AMC Logo" class="logo">' if AMC_LOGO else ""
    gr.HTML(f"""
    <div id="banner">
      {logo_html}
      <h1>AMC Hospital - Symptom Checker</h1>
      <h1>مستشفى أصيل - فاحص الأعراض الطبية</h1>
      <p>مساعدك الذكي لتحديد التخصص الطبي المناسب | Your Smart Medical Assistant</p>
    </div>
    """)

    with gr.Row():
        symptoms_input = gr.Textbox(
            label="✍️ اكتب الأعراض هنا / Enter Symptoms",
            placeholder="مثال: ألم في الصدر مع ضيق في التنفس\nExample: Chest pain with shortness of breath",
            lines=5,
            elem_classes=["rtl-text"],
        )

    submit_btn = gr.Button("🔍 تحليل الأعراض / Analyze", variant="primary", elem_classes=["primary"])

    specialty_output = gr.HTML()
    urgency_output = gr.HTML()
    top3_output = gr.HTML()
    disclaimer_output = gr.HTML()

    gr.Examples(examples=examples, inputs=symptoms_input, label="💡 أمثلة / Examples")

    footer_logo = f'<img src="{AMC_LOGO}" class="logo-footer">' if AMC_LOGO else ""
    gr.HTML(
        f"""
    <div id="footer">
      {footer_logo}
      <h2 style="color:#FF8C42; margin:0;">🏥 Aseel Medical Care Hospital</h2>
      <h3 style="color:#4A90E2; margin:6px 0 0 0;">مستشفى أصيل للرعاية الطبية</h3>
      <p style="margin:8px 0; color:#666;">Hurghada, Red Sea, Egypt | 📞 065 344 1110</p>
    </div>
    """
    )

    submit_btn.click(
        fn=analyze_symptoms,
        inputs=symptoms_input,
        outputs=[specialty_output, urgency_output, top3_output, disclaimer_output],
    )

if __name__ == "__main__":
    demo.launch(share=True, server_name="0.0.0.0", server_port=7860)
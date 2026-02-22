import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

aisocmodel= Groq(api_key=API_KEY)

def analyze_alert(alert_text: str) -> str:
    """
    Takes raw alert text and returns an AI-generated analysis.
    """
    prompt = f"""
You are an AI SOC analyst assistant. Analyze the security alert below.

STRICT RULES:
- Do NOT assume the alert type. Identify it based only on the content.
- Do NOT guess or infer details that are not explicitly present.
- Do NOT assume this is a Windows event unless the alert clearly shows Windows fields.
- Do NOT assume brute force, malware, or lateral movement unless the alert clearly indicates it.
- Keep the analysis factual and grounded in the alert text.
- Do NOT use bold, italics, markdown formatting, or special characters. Use plain text only.

Provide output in this structure:

1. Summary (2–3 sentences)
2. Key IOCs:
   - Users
   - IPs
   - Hosts
   - Processes
   - File paths
   - Domains / URLs
   - Hashes
3. Risk Score (Low / Medium / High)
4. Investigation Steps (3 bullets)
5. Remediation Actions (3 bullets)

Alert:
{alert_text}
"""

    response = aisocmodel.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
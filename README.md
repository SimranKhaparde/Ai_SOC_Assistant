# 🛡️ AI SOC Assistant

A fast, lightweight AI‑powered SOC analysis tool that uses **Llama 3.1 (Groq API)** to analyze security alerts, extract IOCs, assign risk scores, and provide investigation guidance.  
Designed to help analysts quickly interpret Windows Security Events and SIEM logs through a simple, intuitive interface.

---

## 🚀 Features

- Real‑time alert analysis using Llama 3.1 on Groq  
- IOC extraction (IPs, users, hosts, processes, file paths)  
- Risk scoring for quick triage  
- Investigation steps aligned with SOC workflows  
- Remediation guidance for common alert types  
- Simple Gradio UI for easy interaction  
- Compatible with Splunk Cloud logs (Windows Event Logs; Sysmon/Defender if configured)

---

## 📦 Tech Stack

- Python  
- Gradio  
- Groq API  
- Splunk Cloud  
- Windows VM  

---

## 📸 Screenshots

> Sensitive details such as URLs, IPs, and hostnames have been redacted.

### AI SOC Assistant UI  
![Model_UI](https://github.com/user-attachments/assets/8138f0cc-7d79-45d0-81bc-54777f93a947)


### Example Alert Analysis (Event ID 4625)  
![Model_analysis](https://github.com/user-attachments/assets/f054302d-50bc-473a-87c5-fbdcf10b83da)


### Splunk Log Ingestion  
<img width="1728" height="1117" alt="Splunk_index_logs" src="https://github.com/user-attachments/assets/f72cb07e-9d82-4c93-b853-7583d4dec758" />


### Groq API Setup  
![API_Key_Groq](https://github.com/user-attachments/assets/ec19b8eb-b9b2-4a8e-97e9-ab7029ee9a06)


---

## 🧠 How It Works

1. User pastes a raw security event (e.g., Windows Event ID 4625).  
2. The tool sends the text to **Groq’s Llama 3.1‑8B‑Instant model**.  
3. The model returns a structured analysis including:  
   - Summary  
   - IOCs  
   - Risk score  
   - Investigation steps  
   - Remediation actions  
4. The UI displays the output cleanly for quick triage.

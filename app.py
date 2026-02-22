import gradio as gr
from llm_client import analyze_alert

def analyze(alert_text):
    if not alert_text.strip():
        return "Please paste an alert to analyze."
    return analyze_alert(alert_text)

ui = gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(lines=12, label="Paste your raw security alert here"),
    outputs=gr.Textbox(lines=25, label="AI Based Log Analysis"),
    theme=gr.themes.Monochrome(),
    title="AI SOC Assistant"
)

ui.launch()

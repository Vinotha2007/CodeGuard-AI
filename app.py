import gradio as gr

def review_code(code):

    issues = []
    score = 100

    if "password =" in code.lower():
        issues.append("🔒 Hardcoded password detected")
        score -= 20

    if "eval(" in code:
        issues.append("🔒 Unsafe eval() usage")
        score -= 20

    if "print(" in code:
        issues.append("⚠ Debug print statements found")
        score -= 5

    if "while True" in code:
        issues.append("⚡ Possible infinite loop")
        score -= 10

    if code.count("for") >= 2:
        issues.append("⚡ Nested loops may impact performance")
        score -= 10

    if "SELECT" in code and "+" in code:
        issues.append("🔒 Possible SQL Injection vulnerability")
        score -= 20

    if len(code) > 700:
        issues.append("⚠ Large code block. Consider modularization")
        score -= 5

    if not issues:
        issues.append("✅ No major issues detected")

    summary = f"""

Code Quality Score: {max(score,0)}/100

Issues Found:
{chr(10).join(issues)}

Priority:
{"HIGH" if score < 60 else "MEDIUM" if score < 85 else "LOW"}

Recommendation:
Improve security and optimize code structure.
"""

    return summary


app = gr.Interface(
    fn=review_code,
    inputs=gr.Textbox(
        lines=20,
        label="Paste Code Here"
    ),
    outputs="text",
    title="CodeGuard AI",
    description="AI-Powered Code Review Assistant"
)

app.launch()
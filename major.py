from flask import Flask, request, render_template_string
import openai

app = Flask(__name__)

# 替换为你的 OpenAI API 密钥
openai.api_key = "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"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-1106",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            gpt_output = response['choices'][0]['message']['content']
        except Exception as e:
            gpt_output = f"发生错误: {e}"
        
        return render_template_string(HOME_HTML, result=gpt_output, user_input=user_input)
    else:
        return render_template_string(HOME_HTML)

HOME_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>GPT-3 Demo</title>
</head>
<body>
  <h1>OpenAI GPT-3 Demo</h1>
  <form method="post">
    <textarea name="user_input" rows="4" cols="50">{{ user_input }}</textarea><br>
    <input type="submit" value="Generate">
  </form>
  {% if result %}
  <h2>Output:</h2>
  <p>{{ result }}</p>
  {% endif %}
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)


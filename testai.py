import openai

# 使用你的OpenAI API密钥
openai.api_key = "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"

# 构建一个示例的提示信息
prompt = "纽约3天旅行规划"

# 调用OpenAI API
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",  # 确保使用正确的聊天模型名称
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # 打印GPT的生成文本
    print(response['choices'][0]['message']['content'])
except Exception as e:
    print(f"发生错误: {e}")

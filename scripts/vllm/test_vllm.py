from openai import OpenAI
# Set OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://10.0.4.74:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

chat_response = client.chat.completions.create(
    model="cwy/deepseek-llm-7b-chat-local", #指定要使用的模型名称 必须参数
    #"system"、"user" 或 "assistant"，分别代表系统消息、用户消息和助手消息。通常至少需要一个用户消息。
    messages=[
        {"role": "system", "content": "你是一个土壤学家."},
        {"role": "user", "content": "请讲一个笑话？."},
    ],
    #生成文本的随机性0-2。值越高越随机
    temperature = 0.5,
    # top_p = 0.9, # 表示只考虑累计概率达到 90% 的词汇
    # n = 2, #指定为每个输入消息生成多少个回复。默认值是 1
    # stream = True,
    # max_tokens = 100, #限制生成回复的最大令牌数
)

# 提取响应中的文字内容
message_text = chat_response.choices[0].message.content
print(message_text)

# for chunk in chat_response:
#     if chunk.choices[0].delta.content:
#         print(chunk.choices[0].delta.content, end="", flush=True)
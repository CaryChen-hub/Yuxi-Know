import requests

url = "http://localhost:5173/api/chat/answer"
headers = {
    "Content-Type": "application/json"
}
data = {
    "query": "你是谁呀？",
    "meta": {
        "use_web": False,
        "use_graph": False,
        "graph_name": "neo4j",
        # "selectedKB": 0,
        # "db_name": "kab74b820",
        "summary_title": False,
        # "system": "你是一个土壤学家."
        # "server_model_name": "cwy/deepseek-llm-7b-chat-local"
        
    },
    "cur_res_id": "123"
}

try:
    response = requests.post(url, headers=headers, json=data)
    # response.encoding = 'utf-8' 
    response.raise_for_status()  # 如果请求失败，抛出异常
    print(response.content.decode('utf-8'))
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP 错误发生: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"请求发生错误: {req_err}")


import requests
import json
import yaml

# 打开配置文件  
with open('config.yaml', 'r') as file:  
    config = yaml.safe_load(file)

# 替换为你的文心大模型API密钥  
API_KEY = config['WenXinYiYan_API_Key']
MODEL_NAME = config['WenXinYiYan_API_Model']
URL = config['WenXinYiYan_Base_Url']

headers = {  
    "Content-Type": "application/json",  
    "Authorization": API_KEY,  
}  
  
# 构建请求数据  
data = {  
    "model_name": MODEL_NAME,  # 替换为你的模型名称  
    "text": "咳嗽有黄痰是什么原因",  # 替换为你要输入的文本  
}  
  
# 发送请求并获取响应  
response = requests.post(URL, headers=headers, json=data)  
response.raise_for_status()  # 检查响应状态码是否为200  
  
# 解析响应数据  
result = response.json()  
print(result)
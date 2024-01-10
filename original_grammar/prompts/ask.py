import requests
import json
import yaml

# �������ļ�  
with open('config.yaml', 'r') as file:  
    config = yaml.safe_load(file)

# �滻Ϊ������Ĵ�ģ��API��Կ  
API_KEY = config['WenXinYiYan_API_Key']
MODEL_NAME = config['WenXinYiYan_API_Model']
URL = config['WenXinYiYan_Base_Url']

headers = {  
    "Content-Type": "application/json",  
    "Authorization": API_KEY,  
}  
  
# ������������  
data = {  
    "model_name": MODEL_NAME,  # �滻Ϊ���ģ������  
    "text": "�����л�̵��ʲôԭ��",  # �滻Ϊ��Ҫ������ı�  
}  
  
# �������󲢻�ȡ��Ӧ  
response = requests.post(URL, headers=headers, json=data)  
response.raise_for_status()  # �����Ӧ״̬���Ƿ�Ϊ200  
  
# ������Ӧ����  
result = response.json()  
print(result)
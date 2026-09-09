import pandas as pd

model_data = [
    {'name':'Llama 3', 'company':'Meta', 'parameter':8.0, 'open_source': True, 'license': 'Meta'},
    {'name':'Mistral', 'company':'Mistral AI', 'parameter':7.0, 'open_source': True, 'license': 'Apache'},
    {'name':'Qwen 3', 'company':'Alibaba', 'parameter':0.6, 'open_source': True, 'license': 'Apache'},
    {'name':'GPT_4', 'company':'Open AI', 'parameter':1800.0, 'open_source': False, 'license': 'Proprietary'},
    {'name':'Gemni', 'company':'Google', 'parameter':1000.0, 'open_source': False, 'license': 'Proprietary'},
]

df = pd.DataFrame(model_data)
print(df)
import pandas as pd

import json

with open('API_data/sample.json') as project_file:    
    data = json.load(project_file)  

df = pd.json_normalize(data)

print(df)
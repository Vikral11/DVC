import pandas as pd
import os

data = {
    "Name":["Alice", "Bob", "Charly"],
    "Age":[25, 30, 33],
    "City":["NY", "LA", "Chicago"],
}

df = pd.DataFrame(data)

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir, "sample1.csv")
df.to_csv(file_path, index=False)
print(
    f'the file is saved in {file_path}'
)

import pandas as pd
import gdown
import zipfile
import os
file_url = f'https://drive.google.com/uc?id=1RSkiBZlWasARlbNJGA2Zy2fA7j4c4d4K'
output_file = f'file_csv.zip'
gdown.download(file_url, output_file, quiet=False)
file_extracted = f'C:/Vo_Duyen'
with zipfile.ZipFile(output_file, 'r') as zip_ref:
    os.makedirs(file_extracted, exist_ok= True)
    zip_ref.extractall(file_extracted)
for file_name in os.listdir(file_extracted):
    if file_name.endswith('.csv'):
        file_path = os.path.join(file_extracted, file_name)
        df = pd.read_csv(file_path)
print(df)
sodong, socot = df.shape
print(f"So dong: {sodong}")
print(f"So cot: {socot}")
df["Sales_in_thousands"].fillna(0.0, inplace=True)
df['__year_resale_value'].fillna(df['__year_resale_value'].mean(), inplace=True)
df['Price_in_thousands'].fillna(df['Price_in_thousands'].median(), inplace=True)
print(f"Vi tri thieu du lieu: ")
print(df[df.isnull().any(axis=1)])
print(f"Dataframe sau khi dien du lieu thieu:\n{df}")
for cot in df.columns:
    cnt = -1
    for i in cot:
        cnt += 1
        if type(i) != object:
            df.drop(cnt)
print(f"Dataframe sau khi xoa hang vi pham:\n{df}")
print(f"So dong trung lap: {df.duplicated().sum()}")
df.drop_duplicates(inplace= True)
print(f"Dataframe sau khi xoa du lieu trung lap:\n{df}")
df["ID"] = df["Manufacturer"] + "_" + df["Model"]
print(df["ID"])
Sale = df[['ID', "Sales_in_thousands", "__year_resale_value", "Price_in_thousands"]]
Car = df.drop(["Sales_in_thousands", "__year_resale_value", "Price_in_thousands"], axis = 1)
Sale.to_csv("sale.csv")
Car.to_csv("car.csv")
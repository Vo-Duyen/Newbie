import pandas as pd
df_sale = pd.read_csv('sale.csv')
df_car = pd.read_csv('car.csv')
print(f"Tong so luong o to ban tren thi truong: {df_sale["Sales_in_thousands"].sum()}")
print(f"Gia trung binh cua o to: {df_sale["Price_in_thousands"].mean()}")
print(f"10 id co gia tri ban lai cao nhat:\n{df_sale.loc[df_sale["__year_resale_value"].nlargest(10).index]}")
cnt1, cnt2 = 0, 0
for i in df_car["Vehicle_type"]:
    if i == "Passenger":
        cnt1 += 1
    else:
        cnt2 += 1
print(f"Passenger: {cnt1}, Car: {cnt2}")
print(f"Mode cua hang xe:\n{df_car["Manufacturer"].mode()}")
print(f"After sorted:\n {df_sale.sort_values(by = ["Sales_in_thousands", "__year_resale_value", "Price_in_thousands"], ascending=False)}")
print(f"After merge:\n {pd.merge(df_car, df_sale, on="ID")}")
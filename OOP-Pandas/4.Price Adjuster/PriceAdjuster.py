#1
class Product:
    def __init__(self, prod_id, price):
        self.prod_id = prod_id
        self.price = price
    def apply_discount(self,percent_off):
        discount = (percent_off / 100) * self.price
        self.price -= discount
#2
import pandas as pd
df = pd.read_csv('products.csv')
elect_row = df[df['Category'] == 'Electronics']
#3
new_price = []
for index, row in elect_row.iterrows():
    item = Product(row['Product_Id'], row['Price'])
    item.apply_discount(20)
    new_price.append(item.price)
#4
elect_row['Price'] = new_price
elect_row['Promo_Active'] = 'Yes'
#5
elect_row.to_excel('holiday_promo.xlsx', index=False)

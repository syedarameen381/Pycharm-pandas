#1
class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    def use_item(self, amount):
        self.quantity -= amount
#2
import pandas as pd
df = pd.read_csv('morning_stock.csv')
df = df.rename(columns={"Qty_kg": "Current_Quantity"})
df['Current_Quantity'] = df['Current_Quantity'].astype(float)
#3
row = df[df['Ingredients'] == 'Coffee beans'].values[0]
item = Ingredient(row[0], row[1])
#4
item.use_item(2.5)
#5
df.loc[df['Ingredients'] == 'Coffee beans', 'Current_Quantity'] = item.quantity
df.to_csv('evening_stock.csv', index=False)

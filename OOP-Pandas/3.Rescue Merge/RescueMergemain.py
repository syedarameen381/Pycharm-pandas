#1
class RescuePet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False
    def process_adoption(self):
        self.is_adopted = True
#2
import pandas as pd
shelter1 = pd.read_csv('shelter_A.csv')
shelter2 = pd.read_csv('shelter_B.csv')
combined_df = pd.concat([shelter1, shelter2], ignore_index=True)
#print(combined_df)
#3
combined_df.dropna()
dog_rows = combined_df[combined_df['Animal_Type'] == 'Dog']
#4
one_dog = dog_rows.iloc[0]
pet_to_adopt = RescuePet(one_dog['Pet_Name'], one_dog['Animal_Type'], one_dog['Age_Years'])
pet_to_adopt.process_adoption()
#5
adopted_df =[{
    'Pet_Name': pet_to_adopt.name,
    'Animal_Type': pet_to_adopt.species,
    'Age_Years': pet_to_adopt.age,
    'Status': pet_to_adopt.is_adopted
}]
adopted_df = pd.DataFrame(adopted_df)
adopted_df.to_csv('successful_adoptions.csv', mode='a', index=False)


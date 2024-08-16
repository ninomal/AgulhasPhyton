import pandas as pd
  
  # Create a DataFrame with sample data
data = {
        'Dia': [1, 2, 3],
        'F9': [4,None, 0],
        'f12': [30, 25, 35],
        'f14': [1, None, None]
    }

df = pd.DataFrame(data)

# Define the filename
file_name = 'new_Teste_pandas.xlsx'

# Write the DataFrame to an Excel file
df.to_excel(file_name, index=False, engine='openpyxl')

print(f"Excel file '{file_name}' created successfully.")
        
import os
import pandas as pd

# Specify the folder path
folder_path = r'C:/Users/Clara/OneDrive - The University of Auckland/PhD/SE test2/Phoneme/F0_modified'  # Change to your folder path

# List all files in the folder
file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Create a DataFrame for easy writing to Excel
file_names_df = pd.DataFrame(file_list, columns=['File Names'])

# Specify the output Excel file
output_file = 'file_names.xlsx'

# Write the DataFrame to an Excel file
file_names_df.to_excel(output_file, index=False)

# Display success message
print(f'File names have been written to {output_file}')
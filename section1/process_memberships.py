import os
import shutil
import hashlib
import pandas as pd
import sys

# Define the input and output directories
input_dir = 'applications_data/'
successful_dir = 'successful_applications/'
unsuccessful_dir = 'unsuccessful_applications/'
filename = sys.argv[1]

# Loop through each file in the input directory

    # Load the data from the file
df = pd.read_csv(os.path.join(input_dir, filename))

# Define a regular expression to match prefixes and suffixes
regex = r'(Mr\.|Mrs\.|Ms\.|Dr\.|Jr\.|Sr\.|III|MD|PhD)$'

# Remove prefixes and suffixes from the 'name' column
df['name'] = df['name'].str.replace(regex, '', regex=True).str.strip()

# Split name into first_name and last_name
df[['first_name', 'last_name']] = df['name'].str.split(' ', n=1, expand=True)

# Format birthday field into YYYYMMDD, any rows with invalid dates are sert to NaN 
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format="mixed", errors="coerce").dt.strftime('%Y%m%d')

# Create a new field named above_18 based on the applicant's birthday
df['above_18'] = (pd.Timestamp('2022-01-01') - pd.to_datetime(df['date_of_birth'])) >= pd.Timedelta(days=365*18)

# Check validity of mobile number, email, and age
valid_df = df[(df['mobile_no'].astype(str).str.len() == 8) &
            (~df['name'].isna()) &
            (df['email'].str.contains('@') & df['email'].str.contains('\.(com|net)$')) &
            ((df['above_18'] == True))]

invalid_df = df[(df['mobile_no'].astype(str).str.len() != 8) |
                (df['name'].isna()) |
            (~(df['email'].str.contains('@') & df['email'].str.contains('\.(com|net)$'))) |
            ((df['above_18'] == False))]    

# Create a membership ID for successful applications
valid_df['membership_id'] = valid_df.apply(lambda row: f"{row['last_name']}_{hashlib.sha256(row['date_of_birth'].encode()).hexdigest()[:5]}", axis=1)

#  Save successful and unsuccessful data to separate folders
valid_df.to_csv(successful_dir + 'valid_'+ filename, index=False)
invalid_df.to_csv(unsuccessful_dir + 'invalid_'+ filename, index=False)


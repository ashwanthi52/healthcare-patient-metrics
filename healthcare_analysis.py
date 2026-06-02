import pandas as pd
df=pd.read_csv("healthcare.csv")
print("Healthcare Patient Metrics Project analysis")
print("\ndataset:")
print(df.head())
print("\naverage age:")
print(df["age"].mean())
print("\naverage treatment cost:")
print(df["treatment_cost"].mean())
print("\ndisease count:")
print(df["disease"].value_counts())

# Dataset will be added later

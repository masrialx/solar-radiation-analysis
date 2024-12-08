import pandas as pd

# Function to load and clean the dataset
def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna(subset=['GHI', 'DNI', 'DHI', 'ModA', 'ModB'])
    for col in ['GHI', 'DNI', 'DHI', 'ModA', 'ModB']:
        df[col] = df[col].apply(lambda x: np.nan if x < 0 else x)
        df[col].fillna(method='ffill', inplace=True)
    return df

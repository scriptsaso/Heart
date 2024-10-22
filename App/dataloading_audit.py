import pandas as pd
import streamlit as st
import base64

# Load the datasets without displaying the code block
def load_datasets():
    # Actually load the datasets
    mitbih_train = pd.read_csv('mitbih_train.csv', header=None)
    mitbih_test = pd.read_csv('mitbih_test.csv', header=None)
    ptbdb_abnormal = pd.read_csv('ptbdb_abnormal.csv', header=None)
    ptbdb_normal = pd.read_csv('ptbdb_normal.csv', header=None)
    
    return mitbih_train, mitbih_test, ptbdb_abnormal, ptbdb_normal

# Function to display the Data Loading code block (without loading the datasets again)
def display_data_loading_code():
    st.subheader("Data Loading")

    # Displaying the code block for data loading
    st.code("""
import pandas as pd

# Load the datasets
mitbih_train = pd.read_csv('mitbih_train.csv', header=None)
mitbih_test = pd.read_csv('mitbih_test.csv', header=None)
ptbdb_abnormal = pd.read_csv('ptbdb_abnormal.csv', header=None)
ptbdb_normal = pd.read_csv('ptbdb_normal.csv', header=None)
    """, language="python")
    # Display GIF from a local file
    # Path to your local GIF file
    # Path to your local GIF file
    file_path = "loadinggif.gif"  # Update with your actual file path

    # Open the GIF file in binary mode
    with open(file_path, "rb") as file_:
        contents = file_.read()

    # Encode the GIF file in base64
    data_url = base64.b64encode(contents).decode("utf-8")

    # Set desired width and height (for example, 150px width)
    width = 500  # Adjust as needed

    # Display the GIF using HTML within Streamlit and set size using width attribute
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="loading gif" width="{width}px">',
    unsafe_allow_html=True,)

# Function to generate the data audit table for a given dataset
def generate_data_audit(dataset, dataset_name):
    audit_data = []
    for col in dataset.columns:
        col_data = {
            '# Column': col,
            'Name of the Column': f'Feature {col}' if col < dataset.shape[1] - 1 else 'Label',
            'Variable\'s type': 'Feature' if col < dataset.shape[1] - 1 else 'Target',
            'Description': f'ECG signal feature {col + 1}' if col < dataset.shape[1] - 1 else 'ECG class label',
            'Is the variable available before prediction': 'Yes' if col < dataset.shape[1] - 1 else 'No',
            'Variable\'s type (detailed)': dataset.dtypes[col],
            'Percentage of missing values': f"{dataset[col].isnull().mean() * 100:.2f}%",
            'Categorical / Quantitative': 'Quantitative' if col < dataset.shape[1] - 1 else 'Categorical'
        }
        audit_data.append(col_data)
    
    audit_df = pd.DataFrame(audit_data)
    
    st.subheader(f"{dataset_name} Dataset")
    st.dataframe(audit_df) 
    
def data_audit(mitbih_train, mitbih_test, ptbdb_normal, ptbdb_abnormal):
    st.subheader("Data Audit")
    
    # Display the audit code
    st.code("""
# Function to generate the data audit table for a given dataset
def generate_data_audit(dataset, dataset_name):
    audit_data = []
    for col in dataset.columns:
        col_data = {
            '# Column': col,
            'Name of the Column': f'Feature {col}' if col < dataset.shape[1] - 1 else 'Label',
            'Variable\'s type': 'Feature' if col < dataset.shape[1] - 1 else 'Target',
            'Description': f'ECG signal feature {col + 1}' if col < dataset.shape[1] - 1 else 'ECG class label',
            'Is the variable available before prediction': 'Yes' if col < dataset.shape[1] - 1 else 'No',
            'Variable\'s type (detailed)': dataset.dtypes[col],
            'Percentage of missing values': f"{dataset[col].isnull().mean() * 100:.2f}%",
            'Categorical / Quantitative': 'Quantitative' if col < dataset.shape[1] - 1 else 'Categorical'
        }
        audit_data.append(col_data)
    
    audit_df = pd.DataFrame(audit_data)
    """, language="python")
    
    # Create a list of dataset labels
    dataset_labels = ["Train", "Test", "Normal", "Abnormal"]
    
    # Create a slider to select which dataset to display using the custom labels
    dataset_option = st.select_slider("Select Dataset to Audit", options=dataset_labels)
    
    # Check which dataset is selected and display the audit for that dataset
    if dataset_option == "Train":
        generate_data_audit(mitbih_train, "MIT-BIH Train")

    elif dataset_option == "Test":
        generate_data_audit(mitbih_test, "MIT-BIH Test ")

    elif dataset_option == "Normal":
        generate_data_audit(ptbdb_normal, "PTBDB Normal")

    elif dataset_option == "Abnormal":
        generate_data_audit(ptbdb_abnormal, "PTBDB Abnormal")


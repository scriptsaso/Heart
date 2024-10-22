import streamlit as st
from dataloading_audit import load_datasets, display_data_loading_code, data_audit  # Import functions

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Introduction", "Data Loading & Auditing"])

# Page logic based on selection
if page == "Introduction":
    from introduction import introduction_page
    introduction_page()

elif page == "Data Loading & Auditing":
    st.title("Data Loading & Auditing")

    # Checkboxes to toggle between sections
    show_data_loading = st.checkbox("Show Data Loading")
    show_data_audit = st.checkbox("Show Data Auditing")

    # Display the selected sections based on checkboxes
    if show_data_loading and not show_data_audit:
        display_data_loading_code()  # Show Data Loading section without loading the data again

    elif show_data_audit and not show_data_loading:
        # Load datasets without showing the Data Loading code
        mitbih_train, mitbih_test, ptbdb_abnormal, ptbdb_normal = load_datasets()
        data_audit(mitbih_train, mitbih_test, ptbdb_normal, ptbdb_abnormal)

    elif show_data_loading and show_data_audit:
        st.warning("Please select only one section at a time.")

    if not show_data_loading and not show_data_audit:
        st.write("Please select a section to display.")

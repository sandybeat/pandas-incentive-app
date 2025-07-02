import streamlit as st
import pandas as pd

st.title("Excel Sheet Analyzing Application")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

thresholds_1 = {
    ('A+', 'Store Manager'):           {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.30, 'high_val': 0.10},
    ('A+', 'Asst. Store Manager'):     {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.50},
    ('A+', 'Cashier'):                 {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.80, 'high_val': 0.80},
    ('A+', 'Retail Executive'):        {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.75, 'high_val': 1.00},
    ('A+', 'Tailor'):                  {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.10, 'high_val': 0.20},
    ('A+', 'VM Manager'):              {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.10, 'high_val': 0.20},
    ('A+', 'Stock Lead'):              {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.75, 'high_val': 1.00},
    ('A', 'Store Manager'):            {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.30, 'high_val': 0.50},
    ('A', 'Asst. Store Manager'):      {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.50},
    ('A', 'Cashier'):                  {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.80, 'high_val': 0.80},
    ('A', 'Retail Executive'):         {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.75, 'high_val': 1.00},
    ('A', 'Tailor'):                   {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.10, 'high_val': 0.20},
    ('A', 'VM Manager'):               {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.10, 'high_val': 0.20},
    ('A', 'Stock Lead'):               {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.75, 'high_val': 1.00},
    ('B', 'Store Manager'):            {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.30, 'high_val': 0.75},
    ('B', 'Asst. Store Manager'):      {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.50},
    ('B', 'Cashier'):                  {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.80, 'high_val': 0.80},
    ('B', 'Retail Executive'):         {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.75, 'high_val': 1.00},
    ('B', 'Tailor'):                   {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.10, 'high_val': 0.20},
    ('C', 'Store Manager'):            {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.40, 'high_val': 0.75},
    ('C', 'Retail Executive'):         {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.75, 'high_val': 1.00},
    ('D', None): {
        'ranges': [
            (0.00, 5.99,   0),
            (6.00, 6.99, 10000),
            (7.00, 7.99, 14000),
            (8.00, float('inf'), 25000),
        ]
    }
}

thresholds_2 = {
    ('A+', 'Store Manager'):           {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.30, 'high_val': 0.10},
    ('A+', 'Asst. Store Manager'):     {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.50},
    ('A+', 'Cashier'):                 {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.80, 'high_val': 0.80},
    ('A+', 'Retail Executive'):        {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.75, 'high_val': 1.00},
    ('A+', 'Tailor'):                  {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.10, 'high_val': 0.20},
    ('A+', 'VM Manager'):              {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.10, 'high_val': 0.20},
    ('A+', 'Stock Lead'):              {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.75, 'high_val': 1.00},
    ('A', 'Store Manager'):            {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.30, 'high_val': 0.50},
    ('A', 'Asst. Store Manager'):      {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.50},
    ('A', 'Cashier'):                  {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.80, 'high_val': 0.80},
    ('A', 'Retail Executive'):         {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.75, 'high_val': 1.00},
    ('A', 'Tailor'):                   {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.10, 'high_val': 0.20},
    ('A', 'VM Manager'):               {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.10, 'high_val': 0.20},
    ('A', 'Stock Lead'):               {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.75, 'high_val': 1.00},
    ('B', 'Store Manager'):            {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.30, 'high_val': 0.75},
    ('B', 'Asst. Store Manager'):      {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.50},
    ('B', 'Cashier'):                  {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.80, 'high_val': 0.80},
    ('B', 'Retail Executive'):         {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.75, 'high_val': 1.00},
    ('B', 'Tailor'):                   {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.10, 'high_val': 0.20},
    ('C', 'Store Manager'):            {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.40, 'high_val': 0.75},
    ('C', 'Retail Executive'):         {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.75, 'high_val': 1.00},
    ('D', None): {
        'ranges': [
            (0.00, 5.99,   0),
            (6.00, 6.99, 10000),
            (7.00, 7.99, 14000),
            (8.00, float('inf'), 25000),
        ]
    }
}

thresholds_3 = {
    ('A+', 'Store Manager'):           {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.30, 'high_val': 0.10},
    ('A+', 'Asst. Store Manager'):     {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.50},
    ('A+', 'Cashier'):                 {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.80, 'high_val': 0.80},
    ('A+', 'Retail Executive'):        {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.75, 'high_val': 1.00},
    ('A+', 'Tailor'):                  {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.10, 'high_val': 0.20},
    ('A+', 'VM Manager'):              {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.10, 'high_val': 0.20},
    ('A+', 'Stock Lead'):              {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.75, 'high_val': 1.00},
    ('A', 'Store Manager'):            {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.40, 'high_val': 0.60},
    ('A', 'Asst. Store Manager'):      {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.30, 'high_val': 0.60},
    ('A', 'Cashier'):                  {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.90, 'high_val': 0.90},
    ('A', 'Retail Executive'):         {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.85, 'high_val': 1.10},
    ('A', 'Tailor'):                   {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.30},
    ('A', 'VM Manager'):               {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.30},
    ('A', 'Stock Lead'):               {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.85, 'high_val': 1.10},
    ('B', 'Store Manager'):            {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.40, 'high_val': 0.85},
    ('B', 'Asst. Store Manager'):      {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.30, 'high_val': 0.60},
    ('B', 'Cashier'):                  {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.90, 'high_val': 0.90},
    ('B', 'Retail Executive'):         {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.85, 'high_val': 1.10},
    ('B', 'Tailor'):                   {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.30},
    ('C', 'Store Manager'):            {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.50, 'high_val': 0.85},
    ('C', 'Retail Executive'):         {'low': 0.90, 'high': 1.00, 'low_val': 0.00, 'mid_val': 0.85, 'high_val': 1.10},
    ('D', None): {
        'ranges': [
            (0.00, 5.99,   0),
            (6.00, 6.99, 10000),
            (7.00, 7.99, 14000),
            (8.00, float('inf'), 25000),
        ]
    }
}

thresholds_F = {
    ('A+', 'Store Manager'):           {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.40, 'high_val': 0.20},
    ('A+', 'Asst. Store Manager'):     {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.30, 'high_val': 0.60},
    ('A+', 'Cashier'):                 {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.90, 'high_val': 0.90},
    ('A+', 'Retail Executive'):        {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.85, 'high_val': 1.10},
    ('A+', 'Tailor'):                  {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.30},
    ('A+', 'VM Manager'):              {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.30},
    ('A+', 'Stock Lead'):              {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.85, 'high_val': 1.10},
    ('A', 'Store Manager'):            {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.40, 'high_val': 0.60},
    ('A', 'Asst. Store Manager'):      {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.30, 'high_val': 0.60},
    ('A', 'Cashier'):                  {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.90, 'high_val': 0.90},
    ('A', 'Retail Executive'):         {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.85, 'high_val': 1.10},
    ('A', 'Tailor'):                   {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.30},
    ('A', 'VM Manager'):               {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.30},
    ('A', 'Stock Lead'):               {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.85, 'high_val': 1.10},
    ('B', 'Store Manager'):            {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.40, 'high_val': 0.85},
    ('B', 'Asst. Store Manager'):      {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.30, 'high_val': 0.60},
    ('B', 'Cashier'):                  {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.90, 'high_val': 0.90},
    ('B', 'Retail Executive'):         {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.85, 'high_val': 1.10},
    ('B', 'Tailor'):                   {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.20, 'high_val': 0.30},
    ('C', 'Store Manager'):            {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.50, 'high_val': 0.85},
    ('C', 'Retail Executive'):         {'low': 0.95, 'high': 1.10, 'low_val': 0.00, 'mid_val': 0.85, 'high_val': 1.10},
    ('D', None): {
        'ranges': [
            (0.00, 5.99,   0),
            (6.00, 6.99, 10000),
            (7.00, 7.99, 14000),
            (8.00, float('inf'), 25000),
        ]
    }
}

thresholds = thresholds_F
lowval = 0.95
highval = 1.10

# Sidebar for threshold selection
# st.sidebar.title("Threshold Selection")
# threshold_option = st.sidebar.selectbox(
#     "Select Threshold Model",
#     options=["Model 1 (Original)", "Model 2", "Model 3", "Final Model"],
#     index=0
# )

# if threshold_option == "Model 1 (Original)":
#     thresholds = thresholds_1
#     lowval = 0.95
#     highval = 1.10
# elif threshold_option == "Model 2":
#     thresholds = thresholds_2
#     lowval = 0.90
#     highval = 1.00
# elif threshold_option == "Model 3":
#     thresholds = thresholds_3
#     lowval = 0.90
#     highval = 1.00
# else:
#     thresholds = thresholds_F
#     lowval = 0.95
#     highval = 1.10

# Debug space to display the selected threshold model
# st.sidebar.subheader("Debug Information")
# st.sidebar.write(f"Selected Threshold Model: {threshold_option}")
# st.sidebar.write(f"Low Value: {lowval}, High Value: {highval}")

def categorizeIncentive(row):
    sc = row['STORE CLASS']
    role = row['ROLE']
    
    achievement_pct = pd.to_numeric(row.get('%', 0), errors='coerce')
    ach = pd.to_numeric(row.get('ach', 0), errors='coerce')
    tgt = pd.to_numeric(row.get('TGT', 0), errors='coerce')

    if sc == 'D':
        for low, high, amt in thresholds[('D', None)]['ranges']:
            if low <= ach < high:
                return amt
        return 0

    cfg = thresholds.get((sc, role), {})
    if not cfg:
        return 0

    incentive = 0
    if achievement_pct > lowval:
        if sc == 'A+' and role == 'Store Manager':
            if ach > 20:
                base_incentive = 20 * cfg['mid_val']
                excess_incentive = ((ach - 20) * cfg['high_val'])
                incentive = base_incentive + excess_incentive
            else:
                incentive = ach * cfg['mid_val']
        else:       
            if achievement_pct > highval:
                excess = ach - (tgt * highval)
                excess_incentive = (excess * cfg['high_val']) 
                mid_portion = (tgt * highval)
                mid_incentive = mid_portion * cfg['mid_val']
                incentive = excess_incentive + mid_incentive
            else:
                incentive += ach * cfg['mid_val']

        return incentive * 1000

if st.button("Process File"):
    if uploaded_file:
        try:
            if uploaded_file.name.endswith('.xlsx'):
                engine = 'openpyxl'
            elif uploaded_file.name.endswith('.xls'):
                engine = 'xlrd'
            excel_file = pd.ExcelFile(uploaded_file, engine=engine)
            sheet_names = excel_file.sheet_names

            if not sheet_names:
                st.error("The uploaded file does NOT contain any sheets.")
            else:
                selected_sheet = st.selectbox("Select a sheet to analyze", sheet_names)
                uploaded_file.seek(0)  # Reset pointer before reading again
                df = pd.read_excel(uploaded_file, sheet_name=selected_sheet, engine=engine)

                st.success(f"Sheet '{selected_sheet}' loaded successfully!")
                
                dfNew = df.copy()

                dfNew['Incentive'] = dfNew.apply(categorizeIncentive, axis=1)
                st.dataframe(dfNew)

                # Exclude hidden columns from the CSV export
                visible_columns = [col for col in dfNew.columns if not col.startswith('_')]
                df_export = dfNew[visible_columns]

                st.subheader("Download Processed Data")
                csv = df_export.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download as CSV",
                    data=csv,
                    file_name="processed_data.csv",
                    mime="text/csv",
                )
        except ValueError:
            st.error("The uploaded file is NOT a valid Excel file.")
        except Exception as e:
            st.error(f"Error reading the file: {e}")
    else:
        st.warning("Please upload an Excel file to process.")
else:
    st.info("Click the 'Process File' button after uploading an Excel file.") # type: ignore
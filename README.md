# pandas-incentive-app

This project is a Streamlit application designed to calculate incentives for employees based on their sales performance. It utilizes the Pandas library for data manipulation and Excel file processing.

## Project Structure

```
pandas-incentive-app
├── src
│   └── pyT.py          # Main application logic for incentive calculation
├── requirements.txt     # Lists the dependencies required for the project
├── .gitignore           # Specifies files and directories to be ignored by Git
└── README.md            # Documentation for the project
```

## Installation

To run this application, you need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/pandas-incentive-app.git
   cd pandas-incentive-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run src/pyT.py
   ```

2. Open your web browser and go to `http://localhost:8501` to access the application.

3. Upload your Excel file containing employee sales data and click on "Process File" to calculate incentives.

## Dependencies

The application requires the following Python packages:

- Streamlit
- Pandas

These packages are listed in the `requirements.txt` file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
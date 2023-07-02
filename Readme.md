# PDF Reader

## Problem
A friend of mine described a tedious task his boss was facing. It involved manually extracting key data from digital PDF files and inputting it into Excel. This process consumed several hours and was prone to errors. Seeking a solution, my friend approached me with the question of whether Python could automate this task. Inspired by his inquiry, I developed the PDF Reader application to alleviate this time-consuming and error-prone process.

## Description
This Python application, built using the tkinter library, allows you to automate the extraction and processing of data from PDF files. The PDF Reader application provides a user-friendly interface where you can select an input folder containing PDF files and an output folder to store the processed data. The application extracts specific data from the PDF files, performs necessary manipulations, and saves the resulting data in Excel format for easy analysis and further processing.

## Prerequisites
- Python 3.x
- tkinter
- pandas
- numpy
- tabula-py
- glob

## Installation
1. Ensure that you have Python installed on your system.
2. Install the required packages by running the following command:
   ```
   pip install tkinter pandas numpy tabula-py
   ```

## Usage
1. Execute the script by running the command `python pdf_reader.py` or using your preferred Python IDE.
2. The application window will appear.
3. Follow the instructions displayed on the window:
   - Select the input folder containing the PDF files by clicking the "Select input" button.
   - Choose the output folder where the processed data will be saved by clicking the "Select output" button.
   - Click the "Run" button to start processing the PDF files.
4. After the processing is complete, the extracted data will be saved in Excel format in the specified output folder.

## Note
- Ensure that you have the necessary read and write permissions for the selected folders.
- Verify that the PDF files in the input folder match the expected structure and formatting for accurate data extraction.
- The application processes all PDF files in the input folder, so ensure that only the relevant files are present.

## Disclaimer
- The PDF Reader application assumes a specific structure and formatting of the PDF files. Always validate the processed data for accuracy and review the results according to your specific requirements.
- Use the application at your own discretion, and exercise caution when handling sensitive or critical data.

Feel free to modify the script according to your needs or contribute to its development. Simplify your PDF data extraction process with PDF Reader!
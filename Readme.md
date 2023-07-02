<!DOCTYPE html>
<html>

<head>
</head>

<body>
  <h1>PDF Reader</h1>

  <h2>Problem</h2>
  <p>
    A friend of mine described a tedious task his boss was facing. It involved manually extracting key data from digital PDF files and inputting it into Excel. This process consumed several hours and was prone to errors. Seeking a solution, my friend approached me with the question of whether Python could automate this task. Inspired by his inquiry, I developed the PDF Reader application to alleviate this time-consuming and error-prone process.
  </p>

  <h2>Description</h2>
  <p>
    This Python application, built using the tkinter library, allows you to automate the extraction and processing of
    data from PDF files. The PDF Reader application provides a user-friendly interface where you can select an input
    folder containing PDF files and an output folder to store the processed data. The application extracts specific data
    from the PDF files, performs necessary manipulations, and saves the resulting data in Excel format for easy analysis
    and further processing.
  </p>
   <img src="https://github.com/Jburch01/pdf-reader/blob/main/pdfr_screenshot.png" height="300" width="300"/></>

  <h2>Prerequisites</h2>
  <ul>
    <li>Python 3.x</li>
    <li>tkinter</li>
    <li>pandas</li>
    <li>numpy</li>
    <li>tabula-py</li>
    <li>glob</li>
  </ul>

  <h2>Installation</h2>
  <ol>
    <li>Ensure that you have Python installed on your system.</li>
    <li>Install the required packages by running the following command:</li>
  </ol>

  <pre>
    <code>pip install tkinter pandas numpy tabula-py</code>
  </pre>

  <h2>Usage</h2>
  <ol>
    <li>Execute the script by running the command <code>python pdf_reader.py</code> or using your preferred Python IDE.
    </li>
    <li>The application window will appear.</li>
    <li>Follow the instructions displayed on the window:</li>
  </ol>

  <ul>
    <li>Select the input folder containing the PDF files by clicking the "Select input" button.</li>
    <li>Choose the output folder where the processed data will be saved by clicking the "Select output" button.</li>
    <li>Click the "Run" button to start processing the PDF files.</li>
  </ul>

  <h2>Note</h2>
  <ul>
    <li>Ensure that you have the necessary read and write permissions for the selected folders.</li>
    <li>Verify that the PDF files in the input folder match the expected structure and formatting for accurate data
      extraction.</li>
    <li>The application processes all PDF files in the input folder, so ensure that only the relevant files are
      present.</li>
  </ul>

  <h2>Disclaimer</h2>
  <ul>
    <li>The PDF Reader application assumes a specific structure and formatting of the PDF files. Always validate the
      processed data for accuracy and review the results according to your specific requirements.</li>
    <li>Use the application at your own discretion, and exercise caution when handling sensitive or critical data.</li>
  </ul>

  <p>Feel free to modify the script according to your needs or contribute to its development. Simplify your PDF data
    extraction process with PDF Reader!</p>
</body>

</html>

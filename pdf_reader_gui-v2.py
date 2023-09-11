import tkinter as tk
from tkinter.filedialog import askdirectory
import pandas as pd
import tabula
import re
import glob
import os
    

input_directory = ''
output_directory = ''
window = tk.Tk()
window.configure(bg='light gray')
window.title("PDF Reader")
window.geometry("600x400")    
    
def main_screen():
    
    def clear_screen():
        '''
        Destroy all widgets in the root window
        '''
        for widget in window.winfo_children():
            widget.destroy()
    
    def get_directions():
        '''
        Displays the directions page with step-by-step instructions.

        This function clears the screen and displays the "Directions" page with step-by-step instructions
        on how to use the PDF Reader application. It includes information on selecting input and output folders,
        choosing to open the output directory after processing, and running the application.

        Global Variables:
        - window: The main application window.
        - back_label: A label to navigate back to the main page.

        Returns:
        None        
        '''
        clear_screen()
        label = tk.Label(font=("Bubblegum Sans", 45), bg='lightgray', fg='Black', text='Directions')
        label.place(x=200, y=10)
        back_label = tk.Label(window, text='Main Page', cursor="hand2",bg='lightgray', fg='blue')
        back_label.place(x=10, y=80)
        back_label.bind("<Button-1>", lambda e: main_screen())
        
        step_1 = tk.Label(window, text='Step one:', font=('arial', 20), fg='black', bg='lightgray')
        step_1.place(x=10, y= 110)
        step_1_text = tk.Label(window, text= 'Choose to have the pdf reader to open the output directory once the \nrun is finished.')
        step_1_text.config(font=('arial', 15), fg='black', bg='lightgray')
        step_1_text.place(x=110, y= 115)
        
        step_2 = tk.Label(window, text='Step two:', font=('arial', 20), fg='black', bg='lightgray')
        step_2.place(x=10, y= 175)
        step_2_text = tk.Label(window, text='Select the input folder you want pdf reader to choose from.')
        step_2_text.config(font=('arial', 15), fg='black', bg='lightgray')
        step_2_text.place(x=110, y= 180)
        
        step_3 = tk.Label(window, text='Step three:', font=('arial', 20), fg='black', bg='lightgray')
        step_3.place(x=10, y= 240)
        step_3_text = tk.Label(window, text=' Select the output folder you want pdf reader to choose from.')
        step_3_text.config(font=('arial', 15), fg='black', bg='lightgray')
        step_3_text.place(x=110, y= 245)
        
        step_4 = tk.Label(window, text='Step four:', font=('arial', 20), fg='black', bg='lightgray')
        step_4.place(x=10, y= 305)
        step_4_text = tk.Label(window, text=' If everything is correct, click the run button.')
        step_4_text.config(font=('arial', 15), fg='black', bg='lightgray')
        step_4_text.place(x=110, y= 310)

        
    def get_output_directory():
        '''
        Displays the operating system's folder selection window for the user to choose the output folder.

        This function opens the OS-native folder selection window to allow the user to select the output folder
        where the processed data will be saved. It also removes any previous error messages, if any.
        The selected directory path is then displayed in the output_entry field.

        Global Variables:
        - output_directory: The directory where processed data will be saved.
        - output_entry: The entry field for displaying the selected output directory.

        Returns:
        None
        '''
        global output_directory
        remove_error()
        output_directory = askdirectory()
        output_entry.config(fg='black', bg='lightgray', text=output_directory)
        
    
    def get_input_directory():
           '''
        Displays the operating system's folder selection window for the user to choose the input folder.

        This function opens the OS-native folder selection window to allow the user to select the input folder
        containing the PDF files to be processed. It also removes any previous error messages, if any.
        The selected directory path is then displayed in the input_entry field.

        Global Variables:
        - input_directory: The directory containing input PDF files.
        - input_entry: The entry field for displaying the selected input directory.

        Returns:
        None
        '''
        global input_directory
        remove_error()
        input_directory = askdirectory()
        input_entry.config(bg='lightgray', fg='black', text=input_directory)
    
       def remove_error():
        '''
        Removes the warning label from the user interface.

        This function clears the warning_label, removing any error message that might be displayed
        to the user.

        Global Variables:
        - warning_label: The label used for displaying warning messages in the user interface.

        Returns:
        None
        '''
        warning_label.config(bg='lightgray', text='')

            
            
    def run_button():
    '''
    Checks if input and output folders are selected, then initiates the PDF processing.

    This function is called when the "Run" button is clicked. It first checks if both the input
    and output folders are specified. If either of them is empty, it displays an error message
    using the warning_label. If both directories are specified, it calls the read_pdfs() function
    to process PDF files.

    Global Variables:
    - window: The main application window.
    - warning_label: A label for displaying warning messages.
    - input_directory: The directory containing input PDF files.
    - output_directory: The directory where processed data will be saved.

    Returns:
    None
    '''
    global window
    if input_directory == '' or output_directory == "":
        warning_label.config(bg='lightgray', font=('Impact', 20), fg='darkred', text="ERROR\nYou must select input/output folders before clicking run")      
    else:    
        read_pdfs()

        
        
    def read_pdfs():
        '''  
        Read and process PDF files from the input directory, extracting invoice data.

        This function reads PDF files from the specified input directory, processes them using tabula-py
        to extract invoice data, and saves the extracted data into Excel files in the output directory.

        If no PDF files are found in the input directory, it displays a warning message.
        Once the processing is complete, it updates the status to "DONE."

        Global Variables:
        - input_directory: The directory containing input PDF files.
        - output_directory: The directory where processed data will be saved.
        - warning_label: A label for displaying warning messages.
        - run_button: The button for triggering the PDF processing.
        - running_label: A label for displaying the processing status.

        Returns:
        None
        '''
        global input_directory
        global output_directory
        invoice_reg = r'\d+[^ ]*'
        acc_reg = r'(?<=\s)\d+'
        total_reg= r'\$(\d+(?:,\d+)?(?:\.\d+)?)'
        running_label.config(text='Running.....', fg='black')
        
        area = [0, 0, 1000, 1000]
        pdf_files = glob.glob(f'{input_directory}/*.pdf')
        
        if pdf_files == []:
            warning_label.config(bg='lightgray', font=('Impact', 20), fg='darkred',text='Input folder does not have pdf files.\nPlease choose another folder and try again')
        else:
            run_button.config(state='disabled')
            
            for pdf_file in pdf_files:
                print(pdf_file)
                
                dfs = tabula.read_pdf(pdf_file, area=area, pages='all')

                df = pd.concat(dfs)
                df.fillna('', inplace=True)
                df = df.drop_duplicates()
                is_invoice = df.isin(['Invoice No. / Date']).any().any()

                if is_invoice:
                    doc_type = 'Invoice'
                    invoice_column = df.columns[df.isin(['Invoice No. / Date']).any()][0]
                    invoice_mask = df[invoice_column].str.contains('Invoice No. / Date')
                    date_index = df[invoice_mask].index.values[0]
                    invoice_date = df.loc[date_index, 'Invoice']
                    acc_column = df.columns[df.isin(['Invoice No. / Date']).any()][0]
                    acc_mask = df[acc_column].str.contains('Purchase Order No.')
                    acc_index = df[acc_mask].index.values[0]

                    try:
                        acc_num = df.loc[acc_index, 'Invoice']
                        acc_num = re.findall(acc_reg, acc_num)[0]
                    except TypeError:
                        acc_num = df.loc[acc_index, 'Invoice'].values[0]
                        acc_num = re.findall(acc_reg, acc_num)[0]

                    total_mask = df["Invoice"].str.contains('Qty Total Curr.')
                    start = df[total_mask].index.values[0]
                    total = df.loc[start + 1, 'Invoice']
                    start = df[total_mask].index.values[0]
                    total = re.findall(total_reg, total)[0]  

                else:
                    doc_type = 'Returns Credit Memo'
                    invoice_mask = df['Unnamed: 1'].str.contains('Credit N. / Date')
                    date_index = df[invoice_mask].index.values[0]
                    invoice_date = df.loc[date_index, 'Returns Credit Memo']
                    acc_mask = df['Unnamed: 0'].str.contains('Bill-To Address')
                    acc_index = df[acc_mask].index.values[0] + 1 
                    acc_num = df.loc[acc_index, 'Unnamed: 0']
                    total_mask = df["Unnamed: 0"].str.contains('Credit Note Summary')
                    start = df[total_mask].index.values[0]
                    total = df.loc[start + 1, 'Returns Credit Memo']
                    total = '-' + re.findall(total_reg, total)[0]


                try:
                    invoice_num = re.findall(invoice_reg, invoice_date)[0]
                except TypeError:
                    invoice_date = invoice_date.values[0]
                    invoice_num = re.findall(invoice_reg, invoice_date)[0]

                date = re.findall(invoice_reg, invoice_date)[1]

                data = {
                    'Date': date,
                    'Doc_type': doc_type,
                    'Invoice': invoice_num,
                    'Account': acc_num,
                    'Total': total
                }

                df1 = pd.DataFrame(data, index=['0'])


                try:
                    df2 = pd.read_excel(f'{output_directory}/{acc_num}.xlsx')
                    df3 = pd.concat([df2, df1], ignore_index=True)
                    df3.to_excel(f'{output_directory}/{df1.Account[0]}.xlsx', index=False)
                    print('found existing file')

                except FileNotFoundError:
                    df1.to_excel(f'{output_directory}/{df1.Account[0]}.xlsx', index=False)
                    print('created new file')
                        
            running_label.config(text='DONE', fg='black')
            if var.get() == '1':
                os.system(f'open "{output_directory}"')
    
        
    
    clear_screen()
    label = tk.Label(window, text="Welcome to PDF Reader!")
    label.config(font=("Bubblegum Sans", 45), bg='lightgray', fg='Black')
    label.place(x=60, y=10)


    input_button = tk.Button(window, text='Select input', cursor="hand2", command=get_input_directory,  borderwidth=0, highlightthickness=0, width=8)
    input_button.place(x=10, y= 200)

    output_button = tk.Button(window, text='Select output', cursor="hand2", command=get_output_directory,  borderwidth=0, highlightthickness=0, width=8)
    output_button.place(x=10, y= 240)

    directions_label = tk.Label(window, text='Directions', cursor="hand2", fg='blue', bg="lightgray")
    directions_label.place(x=10, y=80)
    directions_label.bind("<Button-1>", lambda e: get_directions())

    run_button = tk.Button(window, text="Run", command=run_button, cursor="hand2",  borderwidth=0, highlightthickness=0)
    run_button.place(x=10, y=280)
    
    var = tk.StringVar()
    open_when_done_button = tk.Checkbutton(window, variable=var, text= ": Open output when done", bg='lightgray', fg='black', activebackground="blue")
    open_when_done_button.place(x=10, y=150)

    warning_label = tk.Label(window, text="")
    warning_label.config(bg='lightgray')
    warning_label.place(x=80, y = 310)

    running_label = tk.Label(window, text="")
    running_label.config(bg='lightgray', fg='black')
    running_label.place(x=80, y = 280)

    input_entry = tk.Label(window, bg='lightgray',fg='black')
    input_entry.place(x=150, y=200)

    output_entry = tk.Label(window, bg='lightgray')
    output_entry.place(x=150, y=240)
      
    window.mainloop() 
    
main_screen()  

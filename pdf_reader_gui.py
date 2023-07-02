import tkinter as tk
from tkinter.filedialog import askdirectory
import pandas as pd
import tabula
import re
import glob


def read_pdfs():
    global input_directory
    global output_directory
    global warning_label
    global run_button
    global running_label
    area = [0, 0, 1000, 1000]
    pdf_files = glob.glob(f'{input_directory}/*.pdf')
    if pdf_files == []:
        warning_label.config(bg='lightgray', font=('Impact', 20), fg='darkred',text='Input folder does not have pdf files.\nPlease choose another folder and try again')
    else:
        run_button.config(state='disabled')
        running_label.config(text='Running.....', fg='black')
        for pdf_file in pdf_files:  
            dfs = tabula.read_pdf(pdf_file, area=area, pages='all')

            df = pd.concat(dfs)
            df.fillna('', inplace=True)

            invoice_mask = df['Unnamed: 0'].str.contains('Invoice No. / Date')
            date_index = df[invoice_mask].index.values[0]
            invoice_date = df.loc[date_index, 'Invoice']
            invoice_reg = r'\d+[^ ]*'

            invoice_num = re.findall(invoice_reg, invoice_date)[0]
            date = re.findall(invoice_reg, invoice_date)[1]

            acc_mask = df['Unnamed: 0'].str.contains(' Purchase Order No.')
            acc_index = df[acc_mask].index.values[0] 
            acc_num = df.loc[acc_index, 'Invoice']
            acc_reg = r'(?<=\s)\d+'
            acc_num = re.findall(acc_reg, acc_num)[0]

            total_mask = df["Invoice"].str.contains('Qty Total Curr.')
            start = df[total_mask].index.values[0]
            total = df.loc[start + 1, 'Invoice']
            total_reg = r"(?<=\$)\d+\.\d+"
            total = re.findall(total_reg, total)[0]

            data = {
                'Date': date,
                'Invoice': invoice_num,
                'Account': acc_num,
                'Total': total,
                'pdf_name' : pdf_file
            }
            df1 = pd.DataFrame(data, index=['0'])

            try:
                df2 = pd.read_excel(f'{output_directory}/{acc_num}.xlsx')
                df3 = pd.concat([df2, df1], ignore_index=True)
                df3.to_excel(f'{output_directory}/{df1.Account[0]}.xlsx', index=False)
            except FileNotFoundError:
                df1.to_excel(f'{output_directory}/{df1.Account[0]}.xlsx', index=False)
        running_label.config(text='DONE', fg='black')


def button_clicked():
    global window
    global directory
    global warning_label
    if input_directory == '' or output_directory == "":
        warning_label.config(bg='lightgray', font=('Impact', 20), fg='darkred', text="ERROR\nYou must select input/output folders before clicking run")      
    else:    
        read_pdfs()
        

        
def remove_error():
     warning_label.config(bg='lightgray', text='')

        
def get_input_directory():
    global input_directory
    remove_error()
    input_directory = askdirectory()
    input_entry.config(bg='lightgray', fg='black', text=input_directory)
    
    
def get_output_directory():
    global output_directory
    remove_error()
    output_directory = askdirectory()
    output_entry.config(fg='black', bg='lightgray', text=output_directory)
    
    
input_directory = ''
output_directory = ''
window = tk.Tk()
window.configure(bg='light gray')
window.title("PDF Reader")
window.geometry("600x400")

label = tk.Label(window, text="Welcome to PDF Reader!")
label.config(font=("Bubblegum Sans", 45), bg='lightgray', fg='Black')
label.place(x=60, y=10)

directions = tk.Label(window, text="Directions:")
directions.config(font=('Bubblegum Sans', 20), bg='lightgray', fg='Black')
directions.place(x=10, y=80)

step_1 = tk.Label(window, text='Select the folder you want pdf reader to choose from.')
step_1.config(font=('arial', 13), fg='black', bg='lightgray')
step_1.place(x=10, y= 110)

step_2 = tk.Label(window, text='Check the text field to confirm the folder')
step_2.config(font=('arial', 13), fg='black', bg='lightgray')
step_2.place(x=10, y= 130)


step_3 = tk.Label(window, text='Click run')
step_3.config(font=('arial', 13), fg='black', bg='lightgray')
step_3.place(x=10, y= 150)

input_button = tk.Button(window, text='Select input', command=get_input_directory,  borderwidth=0, highlightthickness=0, width=8)
input_button.place(x=10, y= 200)

output_button = tk.Button(window, text='Select output', command=get_output_directory,  borderwidth=0, highlightthickness=0, width=8)
output_button.place(x=10, y= 240)

run_button = tk.Button(window, text="Run", command=button_clicked,   borderwidth=0, highlightthickness=0)
run_button.place(x=10, y=280)

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
"""
Code strings for UiPath RPA practicals documentation and tutorials.
Contains the EXACT original RPA workflow steps as text strings.
"""

# RPA Prac 1 - Excel Read/Write Operations
RPA_PRAC1_CODE = '''# RPA Prac 1 - Excel Read/Write Operations

# a) Read and write the Data
# 1. Open UiPath Studio and create a new project.
# 2. In the Activities panel search for 'Read Range Workbook' to read the excel file.
# 3. Assign the activity with the path of a workbook. Then mention the sheet and cell.
# 4. In Properties panel, create a variable to store the read value.
# 5. Now search 'Write Range Workbook' in the activities panel.
# 6. Drag and drop 'Write Range Workbook' in the Designer Panel below the Read Range Workbook.
# 7. Again, assign the path of the workbook and the sheet where the value should be written. Also declare the previously created variable in data table.
# 8. Run the automation workflow.

# b) Read and Append the data in the excel
# 1. In the Activities panel search for 'Read Range Workbook' to read a value in excel file.
# 2. Assign the activity with the path of a workbook. Then mention the sheet and cell.
# 3. In Properties panel, create a variable to store the read value.
# 4. Find the 'Append Range Workbook' from Activities panel to append the data to another existing workbook.
# 5. Drag and Drop the 'Append Range Workbook'.
# 6. Now, assign the path of the workbook and the sheet name. Use the variable as 'given_name' to append.
# 7. Run the automation workflow.'''

# RPA Prac 2 - Email Automation
RPA_PRAC2_CODE = '''# RPA Prac 2 - Email Automation

# a) Sending mail without attachment
# 1. Open UiPath Studio and start a new project.
# 2. In the Activities panel, search for 'Send SMTP Email' activity to send an email.
# 3. Drag and Drop the activity.
# 4. Add new connection in the Mail section.
# 5. Mention the details in the respective sections.

# b) Sending email with attachment
# 1. In the Activities panel, search for 'Send SMTP Email' activity to send an email with attachment.
# 2. Drag and Drop the activity.

# c) Receiving the email
# 1. Search the 'Get IMAP Mail Message' activity.
# 2. Drag and drop the activity to the main sequence.
# 3. Add new connection in the mail section
# 4. Create a variable to store the emails in it in the properties panel under output section.
# 5. Search 'For Each' activity under 'Workflow' in 'UiPath.System.Activities' section.
# 6. Assign the variable in this activity. Also, add a 'Message Box' activity in the 'Body Section' and fill the details in the text.'''

# RPA Prac 3 - Database Operations
RPA_PRAC3_CODE = '''# RPA Prac 3 - Database Operations with MySQL

# 1. Run MySQL Installer to install MySQL Workbench and create a connection in MySQL Workbench.
# 2. Create a new database in MySQL Workbench.
# 3. Install and open ODBC Data Sources (64 bit). Go to 'System DSN' and then, click on the 'Add' option.
# 4. Here, fill the following details to create a connection with the above MySQL database.
# 5. Check the connection on ODBC.
# 6. Now, open the UiPath Studio and create a new workflow.
# 7. Click on 'Manage Packages' from the ribbon tab and install the 'UiPath.Database.Activites' dependency.
# 8. In the Activities Panel, find 'Connect to Database' activity. And so, drag and drop the activity into the Main Sequence.
# 9. To setup the connection between the UiPath workflow and the MySQL database, click on 'Configure Connection'.
# 10. Next, click on 'Connection Wizard'.
# 11. Fill the following details for the connection in the data source and test the connection.
# 12. Thus, the connection settings should look like this.
# 13. In the Properties of the activity, under 'Output', create a variable to store the information and carry it forward.
# 14. Next, find another activity 'Run Query' and add it to the Main Sequence.
# 15. Click on 'Configure Connection' to connect the new activity to the previous one.
# 16. Here, use the previously made variable as the connection.
# 17. Fill the following information to send a query directly to the MySQL database to fill data into the table. query: "insert into songs values (3, 'Lights Up');"
# 18. To display the result, use the 'Message Box' activity.
# 19. Use the following details for the message box activity.
# 20. Again, use the 'Run Query' to send a query directly to the MySQL database to extract data from the table.
# 21. Create a new variable to store the extracted output in.
# 22. To store and view the extracted SQL table, use the 'Write Range Workbook' activity.
# 23. Next, create and save a new excel file in a folder. Then, add its path to the activity and other details as below. Also, attach the variable with the extract SQL data output.'''

# RPA Prac 4 - PDF Data Scraping
RPA_PRAC4_CODE = '''# RPA Prac 4 - PDF Data Scraping

# a) Basic PDF Text Reading
# 1. First, open UiPath Studio and create a new Project.
# 2. Click on 'Manage Packages' from the ribbon tab and install the 'UiPath.PDF.Activities' dependency.
# 3. Also, install the 'UiPath.OCR.Activties' next.
# 4. In the Activities panel, search for the 'Read PDF Text' activity to perform Data Scrapping on a PDF.
# 5. Drag and drop it and attach the path of the PDF to read.
# 6. In the Properties panel of the activity, create a variable to store the output.
# 7. Next, find the 'Write Text File' activity to store and display the scrapped data in a text file.
# 8. Drag and drop the activity and fill the activity by assigning the path of the text file.

# b) Data Scrapping using OCR
# 1. Search the 'Read PDF with OCR' activity.
# 2. Drag and drop it and assign the address of the PDF file to read.
# 3. Create a variable in the Properties to store the output.
# 4. Add it to the 'Read PDF with OCR' activity, in the 'Drop OCR Activity' section.
# 5. Now, once again add the 'Write Text File' to the sequence and fill the activity by assigning the path of a new text file.'''

# RPA Prac 5 - Email Data Extraction
RPA_PRAC5_CODE = '''# RPA Prac 5 - Email Data Extraction to Excel

# 1. Open UiPath Studio and start a new Project.
# 2. In the Activities panel, search for 'Build Data Table' activity to store data from an Email in a structured format.
# 3. Drag and drop it into the Main Sequence. Then, click on 'DataTable' to create one.
# 4. Here, add columns and specify their data type.
# 5. Now, in the Properties panel of the Data Table, create a variable to store it in.
# 6. Next, search the 'Get IMAP Mail List' activity and add it to the Main Sequence.
# 7. Establish your connection with IMAP & your email folder as "Inbox."
# 8. Create a new variable in properties panel of "Get IMAP Email List."
# 9. Find the 'For Each' activity under 'Workflow' in 'UiPath.System.Activities' section.
# 10. Drag and drop the activity to the Main Sequence. Do the following and assign the variable in this activity used in IMAP.
# 11. Next, find the 'Multiple Assign' activity.
# 12. Drag the activity and drop it in the 'Body' section of the 'For Each' activity.
# 13. In Multiple Assign, create variables in the 'Save to' part and assign their function in 'Value to save' part, such as below:
# emailDate = currentMailMessage.Headers("Date")
# emailFrom = currentMailMessage.From.AsText()
# emailTo = currentMailMessage.To.AsText()
# emailSubject = currentMailMessage.Subject.AsText()
# emailBody = currentMailMessage.Body.AsText()
# 14. In the Activities panel, search for 'Add Data Row' activity.
# 15. Fill the activity like this, by mentioning the variables with the Email data and Data Table.
# 16. Further, find the 'Write Range Workbook' activity and add it after the entire 'For Each' activity.'''

# RPA Prac 6 - Web Scraping
RPA_PRAC6_CODE = '''# RPA Prac 6 - Web Scraping Weather Data

# 1. Open UiPath Studio and start a new Project.
# 2. In the Activities panel, search for 'Build Data Table' activity to store output data.
# 3. Next, create a Data Table with columns as seen below.
# 4. In Properties, create a variable to store this data.
# 5. In Activities, find the 'Use Application/Browser' activity.
# 6. Add it to the activity.
# 7. Here, indicate to UiPath what action to take. So, keep a Google Chrome window open. Then, click on 'Indicate Application to Automate' option in the activity and when the screen shows highlights on different applications, click on the running Google Chrome browser.
# 8. Next, in the Activities panel, search for the 'Type Into' activity under 'UiPath.UIAutomation.Activites'.
# 9. Then, drag and drop it in the 'Do' section of the 'Use Application/Browser' activity.
# 10. Keep a Google Chrome browser open. Then, click on 'Indicate in Chrome: New Tab' in this activity. This will open the Chrome Window and highlight the possible actions. So, click on the search bar and then, click on the search icon. Lastly, click on 'confirm' in the open UiPath dialogue box.
# 11. Further, fill the activity with the following information: "temperature mumbai [k(enter)]"
# 12. Next, in the Activities panel, search for the 'Get Text' activity under 'UiPath.UIAutomation.Activites'.
# 13. Again, drag and drop it in the 'Do' section of the 'Use Application/Browser' activity, after the 'Type Into' activity.
# 14. Open Google Browser and search 'temperature mumbai'. Keep this browser open and then go to the project. Click on 'Indicate in Chrome' in 'Get Text' activity. Then, as the tool highlights all elements on the open Google Chrome tab, click on the one showing the temperature and confirm it. Similarly do the same process for humidity and wind.
# 15. Create 3 different 'Get Text' Activity each of temperature, humidity and wind and respectively assign the variable to store the data.
# 16. In the Activities panel, search for 'Add Data Row' activity.
# 17. Add this activity after the last 'Get Text' activity
# 18. Then, fill the activity like this by assigning the variables.
# 19. Further, find the 'Write Range Workbook' activity and add it after the entire 'Use Application/Browser' activity.
# 20. Assign the path of an existing Excel file and also, add the variable with the Data Table created.'''

# Dictionary for easy access
RPA_CODE_DICT = {
    'rpa_prac1': RPA_PRAC1_CODE,
    'rpa_prac2': RPA_PRAC2_CODE,
    'rpa_prac3': RPA_PRAC3_CODE,
    'rpa_prac4': RPA_PRAC4_CODE,
    'rpa_prac5': RPA_PRAC5_CODE,
    'rpa_prac6': RPA_PRAC6_CODE
}

def get_rpa_code(prac_name):
    """
    Get the RPA workflow steps for a specific practical.
    
    Args:
        prac_name (str): Name of the RPA practical ('rpa_prac1', 'rpa_prac2', etc.)
    
    Returns:
        str: The RPA workflow steps as a string
    """
    prac_name = prac_name.lower()
    if prac_name in RPA_CODE_DICT:
        return RPA_CODE_DICT[prac_name]
    else:
        available = ', '.join(RPA_CODE_DICT.keys())
        raise ValueError(f"Unknown RPA prac_name '{prac_name}'. Available: {available}")

def get_all_rpa_codes():
    """
    Get all RPA workflow steps as a dictionary.
    
    Returns:
        dict: Dictionary with RPA prac names as keys and workflow steps as values
    """
    return RPA_CODE_DICT.copy()

def print_rpa_code(prac_name):
    """
    Print the RPA workflow steps for a specific practical.
    
    Args:
        prac_name (str): Name of the RPA practical
    """
    code = get_rpa_code(prac_name)
    print(f"=== {prac_name.upper()} - RPA WORKFLOW STEPS ===")
    print(code)
    print("=" * 50)
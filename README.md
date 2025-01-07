# PyDBKP  

Python script for backing up all your MySQL databases to Google Drive.  

## Requirements  

Before starting, ensure you meet the following requirements:  

- The script is designed to run on **Linux** only;  
- Requires **Python 3** or later;  
- Requires **MySQL** and **mysqldump**.  

## Google Drive  

Before setting up Google Drive, run the following commands:  

```bash
# Clone the repository  
git clone repo_url  

# Create a Python virtual environment  
python3 -m venv venv  

# Activate the virtual environment  
source venv/bin/activate  

# Install the dependencies  
pip install -r requirements.txt  
```  

After executing the commands above, you can proceed with the setup:  

- Create a project on **Google Cloud Console**;  
- Enable the Google Drive API on the **Enabled APIs and Services** page;  
- Create credentials on the **Credentials** page;  
- Set up the OAuth permissions on the **OAuth Consent Screen** page;  
- Download the OAuth client as a JSON file from the **Credentials** page;  
- Rename the JSON file to **client_secrets.json** and place it in the project root.  

## Environment File  

This file contains the necessary values for the script to make backups and send emails:  

- Make a copy of the **.env.example** file and save it as **.env**;  
- Set the app name in the **APP_NAME** variable;  
- Create a folder on Google Drive to store the backups;  
- Get the folder ID and store it in the **FOLDER_ID** variable;  
- Set the email receiver and sender in the **RECIEVER_EMAIL** and **SENDER_EMAIL** variables;  
- Generate an app password for the sender email and store it in the **SENDER_EMAIL_PASSWD** variable.  

## MySQL Configuration File  

This file contains the values required for the script to access the database:  

- Locate the **.my.cnf** file;  
- Update the **user** and **password** keys with your values.  

After completing the steps above, you are ready to back up all your databases by running `python main.py` manually or by adding the script to a cron job.  

## Author  

João Faust  

# PyDBKP

Python script for backing up all your MySQL databases to Google Drive.

## Requirements

- **Operating System:** The script is designed to run on **Linux** only;

- **Python Version:** Requires **Python 3** to be installed on your system;

- **MySQL Tools:** The script depends on `mysqldump`, which must be installed and 
accessible from the command line;

- **Google Drive API:**
    - Ensure the Google Drive API is enabled for your account;
    - You must provide a credentials file (`client_secrets.json`) to authenticate 
    with the Google Drive API.

- **Google Drive Folder Configuration:**
    - You need to specify the ID of the Google Drive folder where backups will 
    be stored;
    - Set the folder ID in the `FOLDER_ID` variable in the `.env` file.

    Example of `.env` file configuration:
    ```dotenv
    FOLDER_ID = your_google_drive_folder_id
    ```

- **Authentication:** 
    - You need to configure a `.my.cnf` file in the project root directory with the MySQL 
    username and password for authentication.
    
    Example of `.my.cnf` configuration:
    ```ini
    [mysqldump]
    user=your_mysql_user
    password=your_mysql_password
    ```

## Installation

1. **Clone the repository:**
    - Clone the repository by using `git clone` command;
    - Extract the files to a directory of your choice.

    Exemple cloning repository:
    ```
    git clone repository_url
   ```

3. **Create Python virtual environment:**
    - Open a terminal and navigate to the project root directory;
    - Use `python3 -m venv venv` to create the environment;
    - Use `source venv/bin/activate` to access the environment. 

2. **Install dependencies:**
    - Open a terminal and navigate to the project root directory;
    - Ensure the Python virtual environment is activated;
    - Use `pip` to install the required Python libraries listed in `requirements.txt`. 

    Example installing dependencies:
    ```
    pip install -r requirements.txt
    ```

After finishing the above steps you are ready to backup all your databases by using `python main.py` manually or you can add the script to cron.
<p align="center">
  <img width="500px" src="https://github.com/PyBotDevs/isobot-resources/blob/base/lazer/icons/grey-transparent.png?raw=true">
</p>

<h1 align='center'>Isobot Data Migration Assistant</h1>

### ***Make sure to check out the Main Repository: [isobot](https://github.com/PyBotDevs/isobot)***

The Isobot Data Migration Assistant is a lightweight setup tool developed for the isobot client, that's quick and easy to use.

This tool was created after a major update was made to the Isobot Project, where the location of the database, logs and configuration directories in the bot, were moved from the main bot folder to a separate data folder in the user's home directory on their computer.

## What exactly does this do?
Since this Isobot update, all of the existing database, logs and config directories are now considered as **legacy directories**. This tool helps migrate all of the existing data from the legacy directories to the new folders located at the user's home directory.

***NOTE:*** The new directory location will be at:
- For Windows: `C:\Users\{your username}\.isobot\`
- For Linux/macOS: `/home/{your username}/.isobot/`

It copies all of the existing databases, logs and config files from the legacy directories into the new data directory

## How do I use this tool?
This is a very simple tool to use, as shown in the following steps:
1. Make sure that your Isobot installation is completely up to date. (any version after version `v2024.1225.0`)
2. Clone the migration assistant repository into a **separate folder** on your computer by running the following command:
   
   ```
   git clone https://github.com/pybotdevs/isobot-data-migration-assistant.git
   ```
3. Copy the `isobot-data-migration-assistant.py` file from the repository to the isobot directory, and enter isobot's working directory by running this command in command prompt:

   ```
   cd /path/to/isobot
   ```
4. Run the python file with the following command:

   ```
   python isobot-data-migration-assistant.py
   ```
5. Watch the tool do its magic, and you shall be informed when the migration process is finished.

## Troubleshooting
### I can't find the new folder! (Linux/macOS)
Since the folder is named as `.isobot`, the `.` before the folder name automatically marks this folder as a *hidden folder* in the filesystem.

If you are on **Windows**, you need not worry as this does not apply to your folder.

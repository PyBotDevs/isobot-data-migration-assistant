# Imports
import os
import shutil
import time

# Variables and Configuration
class Configuration:
    home_dir = os.path.expanduser('~')
    wdir = os.getcwd()
    database_files = (
        "automod.json",
        "currency.json",
        "embeds.json",
        "isocard.json",
        "isocard_transaction_history.json",
        "isocard_transactions.json",
        "items.json",
        "levels.json",
        "presence.json",
        "serverconfig.json",
        "serververification.json",
        "user_data.json",
        "warnings.json",
        "weather.json",
        "isobank/accounts.json",
        "isobank/auth.json"
    )
    config_files = (
        "commands.json",
        "settings.json",
        "shop.json",
        "words.json"
    )
    log_files = (
        "currency.log",
        "error-log.txt",
        "info-log.txt",
        "isocard_transactions.log",
        "startup-log.txt"
    )

print("Welcome to the isobot migration assistant!")
print("This migration assistant will migrate all your isobot client")
print("data from their legacy paths to the new isobot data directory.")
print("\nMigration Process Information:")
print(f"   Old Data Path: {Configuration.wdir}")
print(f"   New Data Path: {Configuration.home_dir}/.isobot")
print(f"\nDISCLAIMER: This migration assistant will delete ALL of your data from the legacy directory")
print("but, your data WILL be copied to the new data directory. This process is NOT reversible")
print("once completed.")
prompt = input("\nAre you sure you want to continue? (y/n): ")

if prompt.lower() != "y":
    raise SystemExit("[!] Migration process cancelled. Aborting isobot migration assistant...")
else: 
    print("[!] Migration process started. Please wait...\n")
    print("---------------------------------")

# Check whether the runtime working directory is the isobot directory or not
print("[1] [Check: 1/2] Checking runtime working directory for required files...")
identification_dirs = ("web", "api", "framework", "discord", "cogs", "utils")
for directory in identification_dirs:
    if not os.path.isdir(directory):
        raise SystemExit("[!] Either this isobot client is broken, or this is not the correct isobot directory. Aborting migration assistant...")
time.sleep(0.5)

# Check whether legacy paths exist
print(f"[2] [Check: 2/2] Checking whether legacy paths exist in {Configuration.wdir}...")
if not os.path.isdir("config") and not os.path.isdir("database") and not os.path.isdir("logs"):
    raise SystemExit("[!] Legacy data paths do not exist in this client. Aborting migration assistant...")
time.sleep(0.5)

# Transfer all files from legacy directory to new system data directory
print("[3] [Migrate: 1/3] Migrating all database files from database directory...")
for _file in Configuration.database_files:
    print(f"     MGR: {Configuration.wdir}/database/{_file} -> {Configuration.home_dir}/.isobot/database/{_file}")
    shutil.copyfile(f"database/{_file}", f"{Configuration.home_dir}/.isobot/database/{_file}")
time.sleep(0.5)
print("[4] [Migrate: 2/3] Migrating all config files from config directory...")
for _file in Configuration.config_files:
    print(f"     MGR: {Configuration.wdir}/config/{_file} -> {Configuration.home_dir}/.isobot/config/{_file}")
    shutil.copyfile(f"config/{_file}", f"{Configuration.home_dir}/.isobot/config/{_file}")
time.sleep(0.5)
print("[5] [Migrate: 3/3] Migrating all log files from logs directory...")
for _file in Configuration.log_files:
    print(f"     MGR: {Configuration.wdir}/logs/{_file} -> {Configuration.home_dir}/.isobot/logs/{_file}")
    shutil.copyfile(f"logs/{_file}", f"{Configuration.home_dir}/.isobot/logs/{_file}")
time.sleep(0.5)

# Delete all files from legacy directory
print("[6] [Cleanup: 1/3] Deleting all database files from legacy directory...")
for _file in Configuration.database_files:
    print(f"     DEL: database/{_file}")
    os.remove(f"database/{_file}")
time.sleep(0.5)
print("[7] [Cleanup: 2/3] Deleting all config files from legacy directory...")
for _file in Configuration.config_files:
    print(f"     DEL: config/{_file}")
    os.remove(f"config/{_file}")
time.sleep(0.5)
print("[8] [Cleanup: 3/3] Deleting all log files from legacy directory...")
for _file in Configuration.log_files:
    print(f"     DEL: logs/{_file}")
    os.remove(f"logs/{_file}")
time.sleep(0.5)

print("[✅] Migration process successfully completed. All of your data is now migrated to the new isobot data directory.")
input("Press enter or any key to exit.")

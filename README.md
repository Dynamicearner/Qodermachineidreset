# Qoder Machine ID Reset

A simple Python tool to reset your Qoder machine ID. Sometimes you just need a fresh start with your Qoder installation, and this script makes it easy.

## What it does

This script generates a new unique machine ID for your Qoder application. It works on both Windows and Linux systems. Before resetting, it shows you the old machine ID so you have a record of it.

## How to use

Just run the script with Python:
```bash
python QoderMachineidreset.py
```

The script will show you the current machine ID and wait for you to press Enter. Once you confirm, it generates a new ID and saves it.

## Requirements

Python 3.x with standard libraries (os, platform, uuid)

## File Locations

The script modifies the machine ID file at:
- Windows: %APPDATA%\Qoder\machineid
- Linux: ~/.config/Qoder/machineid

## Note

Make sure Qoder is closed before running this script to avoid any conflicts.

## Author

Created by @ismartSumit

## License

Free to use. No warranties provided.

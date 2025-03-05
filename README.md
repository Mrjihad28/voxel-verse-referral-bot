### README.md  

# Telegram Referral Bot  

This script automates the process of referring users to a Telegram bot using multiple accounts.  

## Features  
- Uses multiple Telegram accounts.  
- Automatically sends the referral command (`/start <referral_code>`).  
- Random delays to avoid detection.  
- Allows user input for referral code and session files.  

## Requirements  
- Python 3.7+  
- Telethon  
- Colorama  
- Pyfiglet  

## Installation  

1. Clone this repository or download the script.  
2. Install required dependencies:  
   ```bash
   pip install telethon colorama pyfiglet
   ```
3. Get your **API_ID** and **API_HASH** from [my.telegram.org](https://my.telegram.org/).  

## Usage  

1. Edit the script and replace the **API_ID** and **API_HASH** with your credentials.  
2. Run the script:  
   ```bash
   python script.py
   ```
3. Enter the number of Telegram accounts.  
4. Provide the session file names for each account.  
5. Enter your referral code.  
6. The bot will start sending referrals automatically.  

## Notes  
- Ensure your session files are valid and logged in.  
- If you get an error, check if the bot username is correct.  
- Do not use excessive referrals to avoid bans.  

## Disclaimer  
This script is for educational purposes only. Use it responsibly.
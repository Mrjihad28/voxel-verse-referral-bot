import asyncio
import random
from telethon import TelegramClient
from time import sleep
import pyfiglet
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Telegram API credentials (Replace these with your own)
API_ID = 22195720  # আপনার API ID দিন
API_HASH = '73f315374ff838005810aa638abbf2c3'  # আপনার API Hash দিন

# Voxel Verse Bot Information
BOT_USERNAME = "voxel_verse_bot"  # Bot username

# Number of referrals per account
REFERRALS_PER_ACCOUNT = 20

# Delay range (random time to avoid detection)
MIN_DELAY = 5
MAX_DELAY = 10

# Print the title in large letters using pyfiglet
ascii_art = pyfiglet.figlet_format("AIRDROP TUBE", font="slant")
print(Fore.GREEN + Style.BRIGHT + ascii_art)

# User input for the number of accounts to use
num_accounts = int(input("How many Telegram accounts do you want to use? "))

# Store the session file names in a list
ACCOUNTS = []
for i in range(num_accounts):
    account_name = input(f"Enter the session file name for account {i+1}: ")
    ACCOUNTS.append(account_name)

# Get the referral code from the user
REFERRAL_CODE = input("Enter your referral code: ")

async def send_referral(client):
    """Send referrals using /start <referral_code> method"""
    try:
        async with client:
            for _ in range(REFERRALS_PER_ACCOUNT):
                # Send referral start command
                message = f"/start {REFERRAL_CODE}"
                result = await client.send_message(BOT_USERNAME, message)

                # Print debug info
                print(Fore.CYAN + f"[✅] Referral sent from {client.session.filename}")
                print(Fore.YELLOW + f"Bot response: {result.text}")  # Check bot's response

                # Random delay to avoid detection
                sleep(random.randint(MIN_DELAY, MAX_DELAY))
    except Exception as e:
        print(Fore.RED + f"[❌] Error with {client.session.filename}: {e}")

async def main():
    """Login and send referrals from multiple Telegram accounts"""
    for session in ACCOUNTS:
        client = TelegramClient(session, API_ID, API_HASH)
        await client.start()
        print(Fore.BLUE + f"[🔄] Logged in as {session}")

        await send_referral(client)  # Send referrals
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
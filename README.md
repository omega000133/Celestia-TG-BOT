# Celestia-TG-BOT

A Celestia Blockchain infrastructure Telegram bot to work with various functionalities like monitoring and managing your Celestia nodes.

## Features

- Monitor Celestia blockchain nodes.
- Receive alerts and updates about node status.
- Execute commands to interact with nodes.

## Installation

Follow these steps to set up and run the Celestia-TG-BOT.

### Prerequisites

- Python 3.6 or higher
- Virtual environment (recommended)

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/clock-workorange/Celestia-TG-BOT.git
   cd Celestia-TG-BOT/LatamNodeBot

2. **Set Up a Virtual Environment:**
   ```bash
    python3 -m venv venv
    source venv/bin/activate
3. **Install Required Packages:**
   ```bash
    pip install -r requirements.txt

4. **Update Configuration:**
Edit config/settings.py with your specific details:

   ```bash
    TOKEN = "your_telegram_bot_token"
    CHAT_ID = "your_chat_id"
    BASE_URL_API = "https://api-celestia-1.latamnodes.org"
    BASE_URL_RPC = "https://rpc-celestia-1.latamnodes.org"
    DEBUG = False
    PORCENTAJE = False
    MIN_FREE_SPACE = 11  # Minimum free space required in GB
    VALOPER_ADDRESS = "your_validator_address"

5. **Run the Bot:**
   ```bash
    main.py
   
## Commands
Here are the commands you can use with the Celestia-TG-BOT:

-  ```/start``` - Start interacting with the bot.
- ```/status``` - Get the current status of the Celestia node.
- ```/monitor``` - Enable monitoring of the node.
- ```/stop``` - Stop the bot.

## Configuration
The configuration settings for the bot are located in config/settings.py:

- ```TOKEN```: The bot's token from Telegram.
- ```CHAT_ID```: The chat ID where the bot will operate.
- ```BASE_URL_API```: The base URL for the API endpoint.
- ```BASE_URL_RPC```: The base URL for the RPC endpoint.
- ```DEBUG```: Boolean to enable or disable debug mode.
- ```PORCENTAJE```: Boolean for some percentage-based logic.
- ```MIN_FREE_SPACE```: Minimum free space required (in GB).
- ```VALOPER_ADDRESS```: The validator address.

Example Configuration
   ```bash
    TOKEN = "your_telegram_bot_token"
    CHAT_ID = "your_chat_id"
    BASE_URL_API = "https://api-celestia-1.latamnodes.org"
    BASE_URL_RPC = "https://rpc-celestia-1.latamnodes.org"
    DEBUG = False
    PORCENTAJE = False
    MIN_FREE_SPACE = 11  # Minimum free space required in GB
    VALOPER_ADDRESS = "your_validator_address"
   ```
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the Celestia community for their support and contributions.

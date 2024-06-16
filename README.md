# Celestia-TG-BOT

A Celestia Blockchain infrastructure Telegram bot to work with various functionalities like monitoring and managing your Celestia nodes.

## Features

- Monitor Celestia blockchain nodes.
- Receive alerts and updates about node status.
- Execute commands to interact with nodes.

## Installation

Follow these steps to set up and run the Celestia-TG-BOT.

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/clock-workorange/Celestia-TG-BOT.git
   cd Celestia-TG-BOT

2. **Set Up a Virtual Environment:**
   ```bash
    python3 -m venv venv
    source venv/bin/activate
3. **Install Required Packages:**
   ```bash
    pip install -r requirements.txt

4. **Create Configuration File:**

   ```bash
    cp .env.example .env

5. **Update Configuration:**

   ```bash
    TOKEN = "your_telegram_bot_token"
    BASE_URL_API = "https://api-celestia-1.latamnodes.org"
    BASE_RPC_URL = "https://rpc-celestia-1.latamnodes.org"
    MISSED_BLOCK_NUMBER = 5

    DEBUG = False
    PORCENTAJE = False
    MIN_FREE_SPACE = 11  # Minimum free space required in GB
    VALOPER_ADDRESS = "your_validator_address"

6. **Run the Bot:**
   ```bash
    python main.py

## Commands
Here are the commands you can use with the Celestia-TG-BOT:

- ```/monitor help``` - Monitoring help.
- ```/monitor alert start``` - Enable monitoring of the node and Start interacting with the bot.
- ```/monitor alert stop``` - Stop the bot.
- ```/monitor status``` - Get the current status of the Celestia node.

## Configuration
The configuration settings for the bot are located in config/settings.py:

- ```TOKEN```: The bot's token from Telegram.
- ```BASE_URL_API```: The base URL for the API endpoint.
- ```BASE_RPC_URL```: The base RPC endpoint.
- ```MISSED_BLOCK_NUMBER```: Number of consecutive missing blocks.
- ```DEBUG```: Boolean to enable or disable debug mode.
- ```PORCENTAJE```: Boolean for some percentage-based logic.
- ```MIN_FREE_SPACE```: Minimum free space required (in GB).
- ```VALOPER_ADDRESS```: The validator address.

Example Configuration
   ```bash
    TOKEN = "your_telegram_bot_token"
    BASE_URL_API = "https://api-celestia-1.latamnodes.org"
    BASE_RPC_URL = "https://rpc-celestia-1.latamnodes.org"
    MISSED_BLOCK_NUMBER = 5
    DEBUG = False
    PORCENTAJE = False
    MIN_FREE_SPACE = 11  # Minimum free space required in GB
    VALOPER_ADDRESS = "your_validator_address"
   ```
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the Celestia community for their support and contributions.

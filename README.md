# Telegram Auto Bot

A fully automated Telegram bot that responds to messages and commands.

## Features
- Responds to the `/start` command with a welcome message.
- Echoes back any text message sent to it.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yuanfangbot/telegram-auto-bot.git
   cd telegram-auto-bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Telegram Bot Token:
   - Create a `.env` file and add your token:
     ```
     TELEGRAM_BOT_TOKEN=your_bot_token_here
     ```
4. Run the bot:
   ```bash
   python bot.py
   ```

## Usage
- Start the bot with `/start`.
- Send any text message to get an echo response.

## License
MIT
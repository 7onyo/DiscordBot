# My Discord Bot

This is a simple Discord bot I built with `discord.py`. It tracks user interactions and I've set it up to deploy automatically to my VPS.

## Status
I am actively developing this bot and adding more features regularly.

## Invitation Link
You can invite the bot to your server using this link: [Invite Bot](https://discord.com/oauth2/authorize?client_id=1503344437135413348&permissions=274877983744&integration_type=0&scope=bot)

*Note: The bot is currently deployed on a VPS for showcase purposes. I cannot guarantee 100% uptime.*



## Development Workflow
To maintain stability, I use a two-bot system:
- **Production Bot:** Connected to my `main` branch. It runs on my Hetzner VPS and uses my production API token.
- **Testing Bot:** I use this for local development and testing new features. It uses a separate API token so I don't interfere with the live bot.

## Setup & Installation

### Local Development
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd DiscordBot
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   DISCORD_API_TOKEN=your_testing_bot_token_here
   ```

4. **Run the bot:**
   ```bash
   python bot.py
   ```

## CI/CD and Deployment
I've implemented a fully automated CI/CD pipeline using **GitHub Actions**.

### Deployment Process
Whenever I push to the `main` branch, my deployment workflow (`.github/workflows/deploy.yml`) is triggered:
1. It connects to my **Hetzner VPS** via SSH.
2. It executes `deploy.sh`, which:
   - Pulls my latest code from the `main` branch.
   - Updates dependencies in the virtual environment.
   - Restarts my `discordbot` service via `systemctl`.

### Configuration
I use the following GitHub Secrets for my deployment workflow:
- `VPS_HOST`: My VPS IP address or hostname.
- `VPS_USERNAME`: My SSH username for deployment.
- `VPS_SSH_KEY`: My private SSH key for authentication.

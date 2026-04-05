# Teams Bot Example

Minimal Python example of a Microsoft Teams bot using the Bot Framework SDK and `aiohttp`.

## What This Is

This sample starts a bot endpoint at `/api/messages` and echoes back any text the user sends.

Use it when you want a real Teams chat surface instead of channel-only webhook style notifications.

## Files

- `.env.example`: local bot configuration template.
- `.gitignore`: local environment ignore rules.
- `pyproject.toml`: project metadata and Python dependencies.
- `app.py`: aiohttp entry point that hosts the bot endpoint.
- `bots/echo_bot.py`: minimal bot behavior.

## Prerequisites

- Python 3.10 or newer.
- A Microsoft Entra app registration / Bot registration.
- For local testing in Teams, a public HTTPS tunnel such as dev tunnels or ngrok.

## Setup

Create and activate a virtual environment, then install the package:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e .
```

Create a local environment file:

```bash
cp .env.example .env
```

Set these values in `.env`:

- `MicrosoftAppId`: the bot app ID.
- `MicrosoftAppPassword`: the bot client secret. Leave blank only for Emulator-only local testing when you intentionally run without auth.
- `PORT`: local HTTP port, default `3978`.

## Run

Start the bot server:

```bash
python app.py
```

The bot listens on:

```text
http://localhost:3978/api/messages
```

## Test Locally

You can test the bot with Bot Framework Emulator against `http://localhost:3978/api/messages`.

If your bot registration requires auth, enter the same app ID and password in the Emulator.

## Use In Teams

Typical path:

1. Create an Azure Bot or Bot Framework registration tied to your Entra app.
2. Expose your local bot with an HTTPS tunnel.
3. Set the bot messaging endpoint to your public URL plus `/api/messages`.
4. Create a Teams app manifest that references the same bot app ID.
5. Upload the app manifest to Teams and start a chat.

This sample does not include a Teams manifest because bot IDs, domains, and package metadata are deployment-specific.

## Notes

- This is a bot example, not a webhook client and not a Graph channel-posting client.
- Bots are the better fit for 1:1 chat, group chat, mentions, and interactive conversations.
- If you only need simple unattended channel notifications, a webhook or workflow is usually simpler.

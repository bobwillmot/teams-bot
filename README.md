# Teams Bot

Minimal Python example of a Microsoft Teams bot using the Bot Framework SDK and `aiohttp`. The bot echoes text, strips Teams mention markup, and supports simple `help` and greeting commands.

## What This Is

This sample starts a bot endpoint at `/api/messages` and echoes back any text the user sends.

Use it when you want a real Teams chat surface instead of channel-only webhook style notifications.

## Files

- `.env.example`: local bot configuration template.
- `.gitignore`: local environment ignore rules.
- `pyproject.toml`: project metadata and Python dependencies.
- `app.py`: aiohttp entry point that hosts the bot endpoint.
- `bots/echo_bot.py`: minimal bot behavior.
- `teams-app-manifest/manifest.json`: minimal Teams app manifest scaffold for local development.
- `teams-app-manifest/README.md`: packaging notes for the manifest scaffold.
- `tests/test_app.py`: smoke test for the bot endpoint.
- `docs/agent-transcripts/`: dated Markdown logs of agent requests and outcomes.
- `docs/adr/`: architecture and design decision records for the project.

## Git

This project is a Git repository with `main` tracking `origin/main`.

Configured remote:

```text
origin  https://github.com/bobwillmot/teams-bot.git
```

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

The checked-in `.env.example` includes the same keys with brief usage comments.

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

Useful messages to try:

- `help`: shows the supported commands.
- `hello`: returns a greeting.
- any other text: the bot echoes it back.

### Test In Emulator

1. Start the bot with `python app.py`.
2. Open Bot Framework Emulator.
3. Connect to `http://localhost:3978/api/messages`.
4. If you are running with auth enabled, provide the same app ID and password from `.env`.
5. Send `help`, `hello`, and a few free-form messages to verify the responses.

You can also run the automated smoke test:

```bash
.venv/bin/python -m unittest tests.test_app
```

### Test In Teams During Local Development

1. Start the bot locally with `python app.py`.
2. Expose `http://localhost:3978` through an HTTPS tunnel such as dev tunnels or ngrok.
3. Update the bot registration messaging endpoint to `https://<your-public-host>/api/messages`.
4. Create or update a Teams app manifest that references the same bot app ID.
5. Upload the manifest to Teams and open a 1:1 chat with the bot.
6. Mention the bot in Teams and send `help` or another message to confirm the bot strips the mention text before replying.

## Use In Teams

Typical path:

1. Create an Azure Bot or Bot Framework registration tied to your Entra app.
2. Expose your local bot with an HTTPS tunnel.
3. Set the bot messaging endpoint to your public URL plus `/api/messages`.
4. Create a Teams app manifest that references the same bot app ID.
5. Upload the app manifest to Teams and start a chat.

This sample does not include a ready-to-sideload Teams package because bot IDs, domains, icons, and package metadata are deployment-specific.

A starter manifest scaffold is included in `teams-app-manifest/manifest.json` with placeholder values you should replace before sideloading.

## Notes

- This is a bot example, not a webhook client and not a Graph channel-posting client.
- Bots are the better fit for 1:1 chat, group chat, mentions, and interactive conversations.
- If you only need simple unattended channel notifications, a webhook or workflow is usually simpler.

## Project Tracking

This repository tracks implementation history in Markdown:

- Agent request transcripts live under `docs/agent-transcripts/` as dated logs.
- Design decisions live under `docs/adr/` as ADR documents.

When the project changes in a meaningful way, add a short transcript entry and create or update an ADR if the change affects architecture, tooling, deployment, or long-term maintenance.

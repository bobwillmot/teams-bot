# Teams App Manifest Scaffold

This folder contains a minimal Microsoft Teams app manifest scaffold for local bot development.

Before packaging and sideloading it in Teams, replace the placeholder values in `manifest.json`:

- Set `id` to a stable app package ID.
- Set `botId` to the same Microsoft Entra app ID used by the bot.
- Replace the developer URLs and names.
- Replace `your-public-host.example.com` with the HTTPS host from your tunnel.

You must also add two icon files required by Teams packaging:

- `color.png`: 192x192 color icon.
- `outline.png`: 32x32 transparent outline icon.

After updating the placeholders, zip the contents of this folder and upload the package to Teams for sideloading.
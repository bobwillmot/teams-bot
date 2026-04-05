import os

from aiohttp import web
from botbuilder.core import BotFrameworkAdapterSettings, TurnContext
from botbuilder.integration.aiohttp import BotFrameworkHttpAdapter, aiohttp_error_middleware
from dotenv import load_dotenv

from bots import EchoBot


load_dotenv()

SETTINGS = BotFrameworkAdapterSettings(
    app_id=os.getenv("MicrosoftAppId", ""),
    app_password=os.getenv("MicrosoftAppPassword", ""),
)
ADAPTER = BotFrameworkHttpAdapter(SETTINGS)
BOT = EchoBot()


async def on_error(turn_context: TurnContext, error: Exception):
    print(f"Unhandled bot error: {error}")
    await turn_context.send_activity("The bot hit an unexpected error.")


ADAPTER.on_turn_error = on_error


async def messages(request: web.Request) -> web.StreamResponse:
    return await ADAPTER.process(request, BOT)


app = web.Application(middlewares=[aiohttp_error_middleware])
app.router.add_post("/api/messages", messages)


if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=int(os.getenv("PORT", "3978")))

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext


class EchoBot(ActivityHandler):
    async def on_members_added_activity(self, members_added, turn_context: TurnContext):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    MessageFactory.text(
                        "Hello. I am a minimal Teams bot example. Send a message and I will echo it back."
                    )
                )

    async def on_message_activity(self, turn_context: TurnContext):
        text = (turn_context.activity.text or "").strip()
        if not text:
            await turn_context.send_activity(
                MessageFactory.text("Send a text message and I will echo it back.")
            )
            return

        await turn_context.send_activity(MessageFactory.text(f"You said: {text}"))

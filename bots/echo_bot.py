from botbuilder.core import ActivityHandler, MessageFactory, TurnContext


class EchoBot(ActivityHandler):
    async def on_members_added_activity(self, members_added, turn_context: TurnContext):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    MessageFactory.text(
                        "Hello. I am a minimal Teams bot example. Send a message and I will echo it back, or send 'help' to see the supported commands."
                    )
                )

    async def on_message_activity(self, turn_context: TurnContext):
        text = self._clean_message_text(turn_context)
        if not text:
            await turn_context.send_activity(
                MessageFactory.text(
                    "Send a text message and I will echo it back. You can also send 'help'."
                )
            )
            return

        lowered = text.lower()

        if lowered in {"help", "menu"}:
            await turn_context.send_activity(
                MessageFactory.text(
                    "Try one of these commands:\n"
                    "- help: show this message\n"
                    "- hello: get a greeting\n"
                    "- anything else: I will echo it back"
                )
            )
            return

        if lowered in {"hello", "hi"}:
            await turn_context.send_activity(
                MessageFactory.text("Hello. Send me any message and I will echo it back.")
            )
            return

        await turn_context.send_activity(MessageFactory.text(f"You said: {text}"))

    def _clean_message_text(self, turn_context: TurnContext) -> str:
        text = (turn_context.activity.text or "").strip()

        for entity in turn_context.activity.entities or []:
            entity_type = entity.get("type") if isinstance(entity, dict) else getattr(entity, "type", None)
            entity_text = entity.get("text") if isinstance(entity, dict) else getattr(entity, "text", None)

            if entity_type == "mention" and entity_text:
                text = text.replace(entity_text, "")

        return " ".join(text.split())

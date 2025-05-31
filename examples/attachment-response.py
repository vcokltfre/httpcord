from io import BytesIO
from httpcord import (
    CommandResponse,
    HTTPBot,
    Interaction,
)
from httpcord.enums import InteractionResponseType
from httpcord.attachment import Attachment
from httpcord.file import File


CLIENT_ID = 0000000000000000000000
CLIENT_PUBLIC_KEY = "..."
CLIENT_TOKEN = "..."


bot = HTTPBot(
    client_id=CLIENT_ID,
    client_public_key=CLIENT_PUBLIC_KEY,
    register_commands_on_startup=True,
)


@bot.command("attachment-response")
async def attachment_response(interaction: Interaction, *, attachment: Attachment) -> CommandResponse:
    attachment_request = await interaction.bot.http._session.get(attachment.url)
    attachment_data = await attachment_request.read()
    attachment_bytes = BytesIO(attachment_data)
    attachment_bytes.seek(0)
    return CommandResponse(
        type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        content=f"You uploaded an attachment with name: {attachment.filename}, i've attached it to this message!",
        files=[
            File(
                fp=attachment_bytes,
                filename=attachment.filename,
            )
        ]
    )

bot.start(CLIENT_TOKEN)
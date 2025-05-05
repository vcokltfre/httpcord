from httpcord import (
    CommandResponse,
    HTTPBot,
    Interaction,
)
from httpcord.enums import InteractionResponseType
from httpcord.types import File


CLIENT_ID = 0000000000000000000000
CLIENT_PUBLIC_KEY = "..."
CLIENT_TOKEN = "..."


bot = HTTPBot(
    client_id=CLIENT_ID,
    client_public_key=CLIENT_PUBLIC_KEY,
    register_commands_on_startup=True,
)

@bot.command("upload-file")
async def upload_file(interaction: Interaction, *, file: File) -> CommandResponse:
    return CommandResponse(
        type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        content=f"You uploaded a file with name: {file.filename}!",
    )

bot.start(CLIENT_TOKEN)
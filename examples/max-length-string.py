from typing import Annotated

from httpcord import (
    CommandResponse,
    HTTPBot,
    Interaction,
)
from httpcord.enums import InteractionResponseType
from httpcord.types import String


CLIENT_ID = 0000000000000000000000
CLIENT_PUBLIC_KEY = "..."
CLIENT_TOKEN = "..."


bot = HTTPBot(
    client_id=CLIENT_ID,
    client_public_key=CLIENT_PUBLIC_KEY,
    register_commands_on_startup=True,
)

@bot.command("string-length-test")
async def string_length_test(
    interaction: Interaction,
    *,
    echo: Annotated[str, String(min_length=3, max_length=10)],
) -> CommandResponse:
    return CommandResponse(
        type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        content=f"Wow! {echo}",
    )

bot.start(CLIENT_TOKEN)
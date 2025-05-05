from typing import Annotated

from httpcord import (
    CommandResponse,
    HTTPBot,
    Interaction,
)
from httpcord.enums import InteractionResponseType
from httpcord.types import Float, Integer


CLIENT_ID = 0000000000000000000000
CLIENT_PUBLIC_KEY = "..."
CLIENT_TOKEN = "..."


bot = HTTPBot(
    client_id=CLIENT_ID,
    client_public_key=CLIENT_PUBLIC_KEY,
    register_commands_on_startup=True,
)

@bot.command("int-and-float-bounding")
async def int_and_float_bounding(
    interaction: Interaction,
    *,
    integer: Annotated[int, Integer(min_value=3, max_value=10)],
    number: Annotated[float, Float(min_value=0.5, max_value=2.5)],
) -> CommandResponse:
    return CommandResponse(
        type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        content=f"Wow! {integer} and {number}",
    )

bot.start(CLIENT_TOKEN)
from httpcord import (
    CommandResponse,
    HTTPBot,
    Interaction,
)
from httpcord.enums import InteractionResponseType
from httpcord.locale import Locale


CLIENT_ID = 0000000000000000000000
CLIENT_PUBLIC_KEY = "..."
CLIENT_TOKEN = "..."


bot = HTTPBot(
    client_id=CLIENT_ID,
    client_public_key=CLIENT_PUBLIC_KEY,
    register_commands_on_startup=True,
)

@bot.command(
    name="hello-world",
    name_localisations={
        "en-US": "hello-world",
        "fr": "bonjour-le-monde",
        "es-ES": "hola-mundo",
    },
    option_localisations={
        "parameter": Locale(description="This is a described parameter.")
    },
)
async def hello_world(interaction: Interaction, *, parameter: str) -> CommandResponse:
    return CommandResponse(
        type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        content=f"Hello, world!",
    )

bot.start(CLIENT_TOKEN)
from httpcord import (
    CommandResponse,
    HTTPBot,
    Interaction,
)
from httpcord.enums import ApplicationCommandType, InteractionResponseType


CLIENT_ID = 0000000000000000000000
CLIENT_PUBLIC_KEY = "..."
CLIENT_TOKEN = "..."


bot = HTTPBot(
    client_id=CLIENT_ID,
    client_public_key=CLIENT_PUBLIC_KEY,
    register_commands_on_startup=True,
)


@bot.command("Say hello!", command_type=ApplicationCommandType.USER)
async def hello_world(interaction: Interaction) -> CommandResponse:
    return CommandResponse(
        type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        content=f"Hey, {interaction.user.mention}!",
    )


bot.start(CLIENT_TOKEN)

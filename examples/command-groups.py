from httpcord import (
    CommandResponse,
    HTTPBot,
    Interaction,
)
from httpcord.command import Command
from httpcord.enums import InteractionResponseType


CLIENT_ID = 0000000000000000000000
CLIENT_PUBLIC_KEY = "..."
CLIENT_TOKEN = "..."


bot = HTTPBot(
    client_id=CLIENT_ID,
    client_public_key=CLIENT_PUBLIC_KEY,
    register_commands_on_startup=True,
)


async def hello_world(interaction: Interaction) -> CommandResponse:
    return CommandResponse(
        type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        content=f"Hello, world!",
    )


command_group = Command(
    name="group-name",
    description="This is the group description",
    sub_commands=[
        Command(
            name="hello",
            description="Say hello!",
            func=hello_world,
        ),
    ],
)


bot.register_command(command_group)


bot.start(CLIENT_TOKEN)
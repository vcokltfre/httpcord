__all__: tuple[str, ...] = (
    "from_timestamp",
    "null_type_to_bool",
)


from datetime import datetime, timezone


def from_timestamp(timestamp: int | float | str) -> datetime:
    if isinstance(timestamp, str):
        return datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    return datetime.fromtimestamp(float(timestamp), tz=timezone.utc)


def null_type_to_bool(input: dict, key: str) -> bool:
    """
    https://docs.discord.food/resources/guild#role-tags-structure

    Tags with type null represent booleans. They will be present and set to null if they are true, and will be not present if they are false.

    Yes, this is a real Discord API behavior.
    It took me being higher than the Discord engineers to figure this one out.
    """
    return key in input.keys()

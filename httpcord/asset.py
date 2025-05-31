__all__: tuple[str, ...] = (
    "Asset",
)


class Asset:
    __slots__: tuple[str, ...] = (
        "_base_url",
        "_code",
    )

    def __init__(self, base_url: str, code: str) -> None:
        self._base_url: str = base_url
        self._code: str = code

    @property
    def animated(self) -> bool:
        """Whether the avatar is animated."""
        return self.code.startswith("a_") if self._code else False

    @property
    def code(self) -> str:
        """The avatar code."""
        return self._code

    def url(self, *, animated: bool | None = None, size: int = 1024) -> str:
        """The URL of the avatar."""
        animated = self.animated if animated is None else animated
        return f"{self._base_url}/{self._code}.{'png' if not animated else 'gif'}?size={size}"

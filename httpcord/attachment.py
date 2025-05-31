from __future__ import annotations


__all__: tuple[str, ...] = (
    "Attachment",
)


class Attachment:
    __slots__: tuple[str, ...] = (
        "content_type",
        "filename",
        "id",
        "height",
        "width",
        "placeholder",
        "placeholder_version",
        "proxy_url",
        "size",
        "url",
        "_content",
    )

    @classmethod
    def from_option(cls, data: dict) -> Attachment:
        return cls(
            content_type=data["content_type"],
            filename=data["filename"],
            id=int(data["id"]),
            height=data["height"],
            width=data["width"],
            placeholder=data["placeholder"],
            placeholder_version=data["placeholder_version"],
            proxy_url=data["proxy_url"],
            size=data["size"],
            url=data["url"],
        )

    def __init__(
        self,
        content_type: str,
        filename: str,
        id: int,
        height: int,
        width: int,
        placeholder: bool,
        placeholder_version: int,
        proxy_url: str,
        size: int,
        url: str,
    ) -> None:
        self.content_type: str = content_type
        self.filename: str = filename
        self.id: int = id
        self.height: int = height
        self.width: int = width
        self.placeholder: bool = placeholder
        self.placeholder_version: int = placeholder_version
        self.proxy_url: str = proxy_url
        self.size: int = size
        self.url: str = url
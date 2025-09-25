from typing import Final

# The library version.
version: Final[str]
__version__: Final[str]

# The compression mode.
MODE_GENERIC: Final[int]
MODE_TEXT: Final[int]
MODE_FONT: Final[int]

# Raised if compression or decompression fails.
class error(Exception): ...

# The Compressor object.
class Compressor:
    def __init__(
        self, mode: int = ..., quality: int = ..., lgwin: int = ..., lgblock: int = ...
    ) -> None: ...
    def process(self, string: bytes) -> bytes: ...
    def finish(self) -> bytes: ...

# The Decompressor object.
class Decompressor:
    def decompress(self, string: bytes) -> bytes: ...
    def is_finished(self) -> bool: ...
    def process(self, string: bytes) -> bytes: ...

# Compress a byte string.
def compress(
    string: bytes,
    mode: int = ...,
    quality: int = ...,
    lgwin: int = ...,
    lgblock: int = ...,
) -> bytes: ...

# Decompress a compressed byte string.
def decompress(string: bytes) -> bytes: ...

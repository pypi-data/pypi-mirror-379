class Text2QNAError(Exception):
    pass


class PromptFormatError(Text2QNAError):
    pass


class EmbeddingError(Text2QNAError):
    pass


class ChunkingError(Text2QNAError):
    pass



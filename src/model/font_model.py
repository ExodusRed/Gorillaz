class FontModel:
    def __init__(self, name, glyphs: dict[str, list[str]], default_char: str = "?"):
        self.name = name
        self._glyphs = glyphs
        self._default_char = default_char

        


    def get_char_bitmap(self, char: str) -> list[str]:
        """Returns the bitmap for the given character, or fallback if not found."""
        return self._glyphs.get(char, self._glyphs.get(self._default_char))

    def has_char(self, char: str) -> bool:
        """Check if a character exists in the font."""
        return char in self._glyphs

    def all_chars(self) -> list[str]:
        """Returns all supported characters."""
        return list(self._glyphs.keys())
    
    def get_size(self) -> tuple[int, int]:
        sample_char = next(iter(self._glyphs.values()))
        print(f"get_size: {(len(sample_char[0]), len(sample_char))}")
        return (len(sample_char[0]), len(sample_char))
    
    def __repr__(self):
        return f"<FontModel name='{self.name}' chars={len(self._glyphs)}>"
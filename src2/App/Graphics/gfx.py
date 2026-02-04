


class screen:
    def __init__(self):
        self.lines: list[dict[str, str]] = []

    def print(self):
        for packet in self.lines:
            print(packet["line"], end=packet["end"])
from node import FSNode

class FSParser():
    def __init__(rootNode: FSNode):
        ...

    def parse(self, data: str, cwd: FSNode) -> None:
        ...

    def can_parse_data(self, data: str) -> bool:
        ...
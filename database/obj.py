import dataclasses


@dataclasses.dataclass
class Quiz:
    quiz_id: int
    name: str
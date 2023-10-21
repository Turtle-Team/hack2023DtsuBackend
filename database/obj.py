import dataclasses
import typing
import json

@dataclasses.dataclass
class Answer:
    id: int
    name: str
    is_answer: str

@dataclasses.dataclass
class Quiz:
    quiz_id: int
    name: str
    answers: typing.List[Answer]

    def to_json(self):
        answers_json = []

        for i in self.answers:
            answers_json.append(i.__dict__)

        self.answers = answers_json
        return json.dumps(self.__dict__, ensure_ascii=False)


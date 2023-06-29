from dataclasses import dataclass


@dataclass
class Article:
    id: int
    title: str
    text: str

    def __str__(self):
        return f"Article#{self.id} \"{self.title}\":\n{self.text}"

    def __repr__(self):
        return f"Article({self.id})"
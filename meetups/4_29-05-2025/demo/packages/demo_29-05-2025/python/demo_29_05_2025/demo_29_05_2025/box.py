from pathlib import Path
from pydantic import BaseModel

class Vector2(BaseModel):
    x: float = 0
    y: float = 0


class Rotation(BaseModel):
    x: float = 0
    y: float = 0
    z: float = 0


class Box(BaseModel):
    box_size: float = 1
    corner_bevel: float = 0.01
    text: str = "ToDo"
    rotation: Rotation = Rotation()
    spawn_points: list[Vector2] = []


def read_config(box_file: Path) -> Box:
    # read file
    with open(box_file) as file_handler:
        box_model_json = file_handler.read()
    # create config
    box = Box.model_validate_json(box_model_json)
    return box
from pathlib import Path
from pydantic import BaseModel

class Vector2(BaseModel):
    x: float
    y: float


class Rotation(BaseModel):
    x: float
    y: float
    z: float


class Box(BaseModel):
    box_size: float = 1
    corner_bevel: float = 0.01
    text: str = "ToDo"
    rotation: Rotation = [0,0,0]
    spawn_points: list[Vector2] = [Vector2(0,0)]


def read_config(box_file: Path) -> Box:
    # read file
    with open(box_file) as file_handler:
        box_model_json = file_handler.read()
    # create config
    box = Box.model_validate_json(box_model_json)
    return box
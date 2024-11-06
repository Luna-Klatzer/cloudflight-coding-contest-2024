# coding=utf-8
"""
Date: 25.10.2024
Author: Luna Klatzer
"""
from __future__ import annotations

import math
import pathlib
from os import PathLike
from typing import Tuple, List

DATA_PATH: pathlib.Path = pathlib.Path("../data/").resolve()
OUT_PATH: pathlib.Path = pathlib.Path("../output/").resolve()
EXAMPLE_PATH: pathlib.Path = pathlib.Path("../example/").resolve()


class Room:
    """
    Class representing a dimension object
    """
    x: int
    y: int
    tables: int

    def __init__(self, x: int, y: int, tables: int):
        self.x = x
        self.y = y
        self.tables = tables


class RoomManager:
    """
    Class representing a flight manager object.
    """
    room_dimensions: List[Room]
    room_count: int
    _room_table_positions: List[List[List[int]]]

    def __init__(self, file: PathLike):
        self.room_count = 0
        self.room_dimensions = []
        self._room_table_positions = []
        self._read_in_rooms(file)

    def _read_in_rooms(self, file: PathLike) -> None:
        """
        Reads in the locations from the specified file.
        :param file: The file to read from.
        :return: Every location
        """
        with open(file, "r+") as f:
            content: List[str] = f.readlines()

            # Parse the last line
            line_info = content[0].strip("\n").split(" ")
            self.room_count = int(line_info[0])

            for line in content[1:]:
                items = line.strip("\n").split(" ")
                x = int(items[0])
                y = int(items[1])
                tables = int(items[2])

                self.room_dimensions.append(Room(x, y, tables))

    def calculate(self, out_path: PathLike) -> None:
        """

        :param out_path:
        :return:
        """
        for room in self.room_dimensions:
            rooms_in_w: int = int(room.x / 3)
            rows: int = int(room.tables / rooms_in_w)

            room_tables: List[List[int]] = []
            for row in range(rows):
                room_tables.append([row * rooms_in_w + i + 1 for i in range(rooms_in_w)])

            self._room_table_positions.append(room_tables)

        self._write_out(out_path)

    def _write_out(self, out_path: PathLike) -> None:
        """

        :param out_path:
        :return:
        """
        with open(out_path, "w+") as f:
            i = 0
            for pos in self._room_table_positions:
                for row in pos:
                    for table in row:
                        f.write(" ".join(str(table) for _ in range(3)))
                        f.write(" ")
                    f.write("\n")



def first_task() -> None:
    """
    Prints out the solution for the first task
    """
    task_data: pathlib.Path = pathlib.Path(DATA_PATH, "level2")
    task_out: pathlib.Path = pathlib.Path(OUT_PATH, "level2")
    example: pathlib.Path = pathlib.Path(EXAMPLE_PATH, "level2")

    print(f"-- Writing to {task_out}")

    mng = RoomManager(pathlib.Path(example, "level2_example.in"))
    mng.calculate(pathlib.Path(task_out, "level2_example.out"))

    # Process in the first file
    mng = RoomManager(pathlib.Path(task_data, "level2_1.in"))
    mng.calculate(pathlib.Path(task_out, "level2_1.out"))

    # Process in the second file
    mng = RoomManager(pathlib.Path(task_data, "level2_2.in"))
    mng.calculate(pathlib.Path(task_out, "level2_2.out"))

    # Process in the third file
    mng = RoomManager(pathlib.Path(task_data, "level2_3.in"))
    mng.calculate(pathlib.Path(task_out, "level2_3.out"))

    # Process in the fourth file
    mng = RoomManager(pathlib.Path(task_data, "level2_4.in"))
    mng.calculate(pathlib.Path(task_out, "level2_4.out"))

    # Process in the fifth file
    mng = RoomManager(pathlib.Path(task_data, "level2_5.in"))
    mng.calculate(pathlib.Path(task_out, "level2_5.out"))


def main() -> None:
    """
    Entry function for the application
    """
    first_task()


if __name__ == "__main__":
    main()

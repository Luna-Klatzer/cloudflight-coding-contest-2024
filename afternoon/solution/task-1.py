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


class Dim:
    """
    Class representing a dimension object
    """
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y =y


class RoomManager:
    """
    Class representing a flight manager object.
    """
    room_dimensions: List[Dim]
    room_count: int
    _room_table_count: List[int]

    def __init__(self, file: PathLike):
        self.room_count = 0
        self.room_dimensions = []
        self._room_table_count = []
        self._read_in_dimensions(file)

    def _read_in_dimensions(self, file: PathLike) -> None:
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

                self.room_dimensions.append(Dim(x, y))

    def calculate(self, out_path: PathLike) -> None:
        """

        :param out_path:
        :return:
        """
        for room in self.room_dimensions:
            self._room_table_count.append(int(room.x * room.y / 3))

        self._write_out(out_path)

    def _write_out(self, out_path: PathLike) -> None:
        """

        :param out_path:
        :return:
        """
        with open(out_path, "w+") as f:
            i = 0
            for pos in self._room_table_count:
                f.write(f"{pos}")
                if i + 1 < len(self._room_table_count):
                    f.write("\n")
                i += 1



def first_task() -> None:
    """
    Prints out the solution for the first task
    """
    first_task_data: pathlib.Path = pathlib.Path(DATA_PATH, "level1")
    first_task_out: pathlib.Path = pathlib.Path(OUT_PATH, "level1")
    print(f"-- Writing to {first_task_out}")

    # Process in the first file
    mng = RoomManager(pathlib.Path(first_task_data, "level1_1.in"))
    mng.calculate(pathlib.Path(first_task_out, "level1_1.out"))

    # Process in the second file
    mng = RoomManager(pathlib.Path(first_task_data, "level1_2.in"))
    mng.calculate(pathlib.Path(first_task_out, "level1_2.out"))

    # Process in the third file
    mng = RoomManager(pathlib.Path(first_task_data, "level1_3.in"))
    mng.calculate(pathlib.Path(first_task_out, "level1_3.out"))

    # Process in the fourth file
    mng = RoomManager(pathlib.Path(first_task_data, "level1_4.in"))
    mng.calculate(pathlib.Path(first_task_out, "level1_4.out"))

    # Process in the fifth file
    mng = RoomManager(pathlib.Path(first_task_data, "level1_5.in"))
    mng.calculate(pathlib.Path(first_task_out, "level1_5.out"))


def main() -> None:
    """
    Entry function for the application
    """
    first_task()


if __name__ == "__main__":
    main()

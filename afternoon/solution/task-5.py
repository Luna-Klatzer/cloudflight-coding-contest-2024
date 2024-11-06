# coding=utf-8
"""
Date: 25.10.2024
Author: Luna Klatzer
"""
from __future__ import annotations

import math as m
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
            rooms_in_w: int = m.floor(room.x / 3)
            w_fits = room.x % 3 == 0
            empty_spaces_in_w = room.x * room.y % 3
            rows_width: int = room.x
            rows_count: int = room.y
            table_count: int = 0

            # We add 0 in the spaces that are empty
            rows: List[List[str]] = [["." for _ in range(rows_width)] for _ in range(rows_count)]
            for i, row in enumerate(rows):
                row: List[str]
                occupied_width: int = 0

                while occupied_width + 3 <= rows_width:
                    if row[occupied_width - 1] == "X":
                        occupied_width += 1

                    if i - 1 >= 0 and ((occupied_width - 1 >= 0 and rows[i - 1][occupied_width - 1] == "X")
                                  or rows[i - 1][occupied_width] == "X"
                                  or rows[i - 1][occupied_width + 1] == "X"
                                  or (occupied_width + 2 < rows_width and rows[i - 1][occupied_width + 2] == "X")
                                  or (occupied_width + 3 < rows_width and rows[i - 1][occupied_width + 3] == "X")) \
                        or i + 1 < rows_count and ((occupied_width - 1 >= 0 and rows[i + 1][occupied_width - 1] == "X")
                                 or rows[i + 1][occupied_width] == "X"
                                 or rows[i + 1][occupied_width + 1] == "X"
                                 or (occupied_width + 2 < rows_width and rows[i + 1][occupied_width + 2] == "X")
                                 or (occupied_width + 3 < rows_width and rows[i + 1][occupied_width + 3] == "X")):
                        occupied_width += 3
                        continue

                    if occupied_width + 3 <= rows_width:
                        row[occupied_width] = "X"
                        row[occupied_width + 1] = "X"
                        row[occupied_width + 2] = "X"

                        if i + 1 < rows_count:
                            rows[i + 1][occupied_width] = "."
                            rows[i + 1][occupied_width + 1] = "."
                            rows[i + 1][occupied_width + 2] = "."

                        table_count += 1
                        occupied_width += 3

            if table_count < room.tables:
                for i, row in enumerate(rows):
                    row: List[int]
                    for j, value in enumerate(row):
                        if value == "." and i + 2 < rows_count and (j - 1 >= 0 or rows[i + 1][j - 1] == ".") and rows[i + 1][j] == "." and rows[i + 2][j] == "." \
                            and (rows[i][j - 1] == "." and rows[i + 1][j - 1] == "." and rows[i + 2][j - 1] == ".") \
                                and (i - 1 < 0 or (rows[i - 1][j - 1] == "." and rows[i - 1][j] == "." and (j + 1 >= rows_width or rows[i - 1][j + 1] == ".")))\
                                    and (i + 3 >= rows_count or (rows[i + 3][j - 1] == "." and rows[i + 3][j] == "." and (j + 1 >= rows_width or rows[i + 3][j + 1] == "."))) \
                                        and (j + 1 >= rows_width or (rows[i][j + 1] == "." and rows[i + 1][j + 1] == "." and rows[i + 2][j + 1] == ".")):
                            row[j] = "X"
                            rows[i + 1][j] = "X"
                            rows[i + 2][j] = "X"
                            table_count += 1

            self._room_table_positions.append(rows)

        self._write_out(out_path)

    def _write_out(self, out_path: PathLike) -> None:
        """

        :param out_path:
        :return:
        """
        with open(out_path, "w+") as f:
            j = 0
            for room_id, pos in enumerate(self._room_table_positions):
                for i, row in enumerate(pos):
                    for j, value in enumerate(row):
                        f.write(value)

                    if i + 1 < len(pos) or room_id + 1 < len(self._room_table_positions):
                        f.write("\n")
                if room_id + 1 < len(self._room_table_positions):
                    f.write("\n")



def first_task() -> None:
    """
    Prints out the solution for the first task
    """
    task_data: pathlib.Path = pathlib.Path(DATA_PATH, "level4")
    task_out: pathlib.Path = pathlib.Path(OUT_PATH, "level4")
    example: pathlib.Path = pathlib.Path(EXAMPLE_PATH, "level4")

    print(f"-- Writing to {task_out}")

    mng = RoomManager(pathlib.Path(example, "level4_example.in"))
    mng.calculate(pathlib.Path(task_out, "level4_example.out"))

    # Process in the first file
    mng = RoomManager(pathlib.Path(task_data, "level4_1.in"))
    mng.calculate(pathlib.Path(task_out, "level4_1.out"))

    # Process in the second file
    mng = RoomManager(pathlib.Path(task_data, "level4_2.in"))
    mng.calculate(pathlib.Path(task_out, "level4_2.out"))

    # Process in the third file
    mng = RoomManager(pathlib.Path(task_data, "level4_3.in"))
    mng.calculate(pathlib.Path(task_out, "level4_3.out"))

    # Process in the fourth file
    mng = RoomManager(pathlib.Path(task_data, "level4_4.in"))
    mng.calculate(pathlib.Path(task_out, "level4_4.out"))

    # Process in the fifth file
    mng = RoomManager(pathlib.Path(task_data, "level4_5.in"))
    mng.calculate(pathlib.Path(task_out, "level4_5.out"))


def main() -> None:
    """
    Entry function for the application
    """
    first_task()


if __name__ == "__main__":
    main()

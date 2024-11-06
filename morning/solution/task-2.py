# coding=utf-8
"""
Entry file for the solution of the Cloudflight coding contest.

Date: 07.03.2023
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

GRAVITY: int = 10

def cartesian_distance(
        pos1: Tuple[float, float], pos2: Tuple[float, float]
) -> float:
    """
    Calculates the cartesian product for the distance between pos1 and pos2.
    :param pos1: The first position in x, y.
    :param pos2: The second position in x, y.
    :return: The distance in meters.
    """
    return math.sqrt(
        # x1 - x0 (Vectors)
        (pos2[0] - pos1[0]) ** 2 +
        # y1 - y0 (Vectors)
        (pos2[1] - pos1[1]) ** 2
    )


class FlightManager:
    """
    Class representing a flight manager object.
    """
    acceleration_per_flight: List[List[int]]
    flight_count: int
    _final_pos: List[int]

    def __init__(self, file: PathLike):
        self.acceleration_per_flight = []
        self._final_pos = []
        self._read_in_velocities(file)

    def _read_in_velocities(self, file: PathLike) -> None:
        """
        Reads in the locations from the specified file.
        :param file: The file to read from.
        :return: Every location
        """
        with open(file, "r+") as f:
            content: List[str] = f.readlines()

            # Parse the last line
            line_info = content[0].strip("\n").split(" ")
            self.flight_count = int(line_info[0])

            for line in content[1:]:
                items = line.strip("\n").split(" ")
                int_items = [int(item) for item in items]

                self.acceleration_per_flight.append(int_items)

    def calculate(self, out_path: PathLike) -> None:
        """

        :param out_path:
        :return:
        """
        for flight in self.acceleration_per_flight:
            pos: int = 0
            velocity: int = 0
            for acc in flight:
                final_acc = acc - GRAVITY
                velocity = velocity + final_acc
                pos = pos + velocity if pos + velocity >= 0 else 0

            self._final_pos.append(pos)

        self._write_out_final_distance(out_path)

    def _write_out_final_distance(self, out_path: PathLike) -> None:
        """

        :param out_path:
        :return:
        """
        with open(out_path, "w+") as f:
            for pos in self._final_pos:
                f.write(f"{pos}")
                if pos != self._final_pos[-1]:
                    f.write("\n")


def first_task() -> None:
    """
    Prints out the solution for the first task
    """
    task_data: pathlib.Path = pathlib.Path(DATA_PATH, "level2")
    task_out: pathlib.Path = pathlib.Path(OUT_PATH, "level2")
    example: pathlib.Path = pathlib.Path(EXAMPLE_PATH, "level2")

    print(f"-- Writing to {task_out}")

    mng = FlightManager(pathlib.Path(example, "level2_example.in"))
    mng.calculate(pathlib.Path(task_out, "level2_example.out"))

    # Process the first file
    mng = FlightManager(pathlib.Path(task_data, "level2_1.in"))
    mng.calculate(pathlib.Path(task_out, "level2_1.out"))

    # Process the second file
    mng = FlightManager(pathlib.Path(task_data, "level2_2.in"))
    mng.calculate(pathlib.Path(task_out, "level2_2.out"))

    # Process the third file
    mng = FlightManager(pathlib.Path(task_data, "level2_3.in"))
    mng.calculate(pathlib.Path(task_out, "level2_3.out"))

    # Process the fourth file
    mng = FlightManager(pathlib.Path(task_data, "level2_4.in"))
    mng.calculate(pathlib.Path(task_out, "level2_4.out"))

    # Process the fifth file
    mng = FlightManager(pathlib.Path(task_data, "level2_5.in"))
    mng.calculate(pathlib.Path(task_out, "level2_5.out"))


    example_3: pathlib.Path = pathlib.Path(EXAMPLE_PATH, "level3")
    mng = FlightManager(pathlib.Path(example_3, "level3_example.in"))
    mng.calculate(pathlib.Path(task_out, "level3_example.out"))


def main() -> None:
    """
    Entry function for the application
    """
    first_task()


if __name__ == "__main__":
    main()

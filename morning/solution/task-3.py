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
    _acceleration_per_flight: List[List[int]]
    flight_count: int
    time_limit: int
    positions_to_reach: List[int]

    def __init__(self, file: PathLike):
        self._acceleration_per_flight = []
        self.positions_to_reach = []
        self._read_in_velocities(file)

    def _read_in_velocities(self, file: PathLike) -> None:
        """
        Reads in the locations from the specified file.
        :param file: The file to read from.
        :return: Every location
        """
        with open(file, "r+") as f:
            content: List[str] = f.readlines()

            line_info = content[0].strip("\n").split(" ")
            self.flight_count = int(line_info[0])

            line_info = content[1].strip("\n").split(" ")
            self.time_limit = int(line_info[0])

            for line in content[2:]:
                items = line.strip("\n").split(" ")
                pos = int(items[0])

                self.positions_to_reach.append(pos)

    def calculate(self, out_path: PathLike) -> None:
        """

        :param out_path:
        :return:
        """
        for pos_to_reach in self.positions_to_reach:
            print(f"Trying to reach {pos_to_reach}")

            pos: int = 0
            velocity: int = 0
            acc_list: List[int] = []
            while pos < pos_to_reach:
                if velocity >= 10:
                    acc = GRAVITY - 5
                else:
                    acc = GRAVITY + 5

                if velocity + (acc - GRAVITY) + pos > pos_to_reach:
                    acc = GRAVITY - velocity + 1
                elif velocity + (acc - GRAVITY) + pos == pos_to_reach:
                    acc = GRAVITY - velocity + 1

                velocity = velocity + (acc - GRAVITY)
                pos = pos + velocity if pos + velocity >= 0 else 0
                acc_list.append(acc)

            if pos > pos_to_reach:
                raise Exception("Doesn't work")

            while pos > 0:
                if velocity > 10:
                    acc = GRAVITY - 10
                elif velocity < -10:
                    acc = GRAVITY + 10
                elif pos > 50:
                    acc = GRAVITY - 10
                elif velocity > 5:
                    acc = GRAVITY - 4
                elif velocity == -1:
                    acc = GRAVITY
                else:
                    acc = GRAVITY - 1
                velocity = velocity + (acc - GRAVITY)
                pos = pos + velocity
                acc_list.append(acc)

            if pos != 0 or velocity != -1:
                raise Exception("Doesn't work")

            self._acceleration_per_flight.append(acc_list)

        self._write_out_final_distance(out_path)

    def _write_out_final_distance(self, out_path: PathLike) -> None:
        """

        :param out_path:
        :return:
        """
        with open(out_path, "w+") as f:
            for pos in self._acceleration_per_flight:
                for acc in pos:
                    f.write(f"{acc} ")
                f.write("\n")


def first_task() -> None:
    """
    Prints out the solution for the first task
    """
    task_data: pathlib.Path = pathlib.Path(DATA_PATH, "level3")
    task_out: pathlib.Path = pathlib.Path(OUT_PATH, "level3")
    example: pathlib.Path = pathlib.Path(EXAMPLE_PATH, "level3")

    print(f"-- Writing to {task_out}")

    # mng = FlightManager(pathlib.Path(example, "level3_example.in"))
    # mng.calculate(pathlib.Path(task_out, "level3_example.out"))

    # Process the first file
    # mng = FlightManager(pathlib.Path(task_data, "level3_1.in"))
    # mng.calculate(pathlib.Path(task_out, "level3_1.out"))

    # Process the second file
    mng = FlightManager(pathlib.Path(task_data, "level3_2.in"))
    mng.calculate(pathlib.Path(task_out, "level3_2.out"))

    # Process the third file
    mng = FlightManager(pathlib.Path(task_data, "level3_3.in"))
    mng.calculate(pathlib.Path(task_out, "level3_3.out"))

    # Process the fourth file
    mng = FlightManager(pathlib.Path(task_data, "level3_4.in"))
    mng.calculate(pathlib.Path(task_out, "level3_4.out"))

    # Process the fifth file
    mng = FlightManager(pathlib.Path(task_data, "level3_5.in"))
    mng.calculate(pathlib.Path(task_out, "level3_5.out"))


def main() -> None:
    """
    Entry function for the application
    """
    first_task()


if __name__ == "__main__":
    main()

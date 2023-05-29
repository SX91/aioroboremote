#!/usr/bin/env python
import asyncio

from aioroboremote.deco import keyword
from aioroboremote.library import RoboLibraryBase
from aioroboremote.server import RoboServer


class MyRoboLibraryPOD(RoboLibraryBase):
    """Example aioroboremote library documentation.
    Implemented example methods for pod types.
    """

    @keyword()
    def sum_floats(self, lhs: float, rhs: float) -> float:
        """Sum two floating point numbers"""
        return lhs + rhs

    @keyword()
    def sum_ints(self, lhs: int, rhs: int) -> int:
        """Sum two integer numbers"""
        return lhs + rhs

    @keyword()
    def concat(self, lhs: str, rhs: str) -> str:
        """Concat two strings"""
        return lhs + rhs


class MyRoboLibraryContainers(RoboLibraryBase):
    """Example aioroboremote library documentation.
    Implemented methods for dict/list
    """

    @keyword()
    async def echo_dict(self, data: dict) -> dict:
        """Returns the same input dict"""
        data = dict(data)  # validate the arg type
        return data

    @keyword()
    def echo_list(self, data: list) -> list:
        """Returns the same input list"""
        return list(data)

    @keyword()
    def echo_tuple(self, data: tuple) -> tuple:
        """Returns the same input tuple"""
        return tuple(data)


if __name__ == "__main__":
    server = RoboServer({
        'pod': MyRoboLibraryPOD(),
        'containers': MyRoboLibraryContainers(),
    })

    server.serve(host='127.0.0.1', port=8270)

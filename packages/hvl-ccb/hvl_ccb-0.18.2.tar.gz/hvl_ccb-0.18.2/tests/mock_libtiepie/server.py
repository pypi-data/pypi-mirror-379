#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
"""
Mock Server
"""


class Server:
    """"""

    def __init__(self, handle) -> None:
        self._url = handle
        self._name = f"Mocked Server Name of {handle}"

    @property
    def url(self):
        return self._url

    @property
    def name(self):
        return self._name

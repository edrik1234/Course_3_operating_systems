from enum import Enum


class Process_State(Enum):
    New = 1
    Ready = 2
    Running = 3
    Waiting = 4
    Terminated = 5
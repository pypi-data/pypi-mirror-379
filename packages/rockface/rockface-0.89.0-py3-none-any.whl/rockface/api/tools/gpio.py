from enum import Enum
from typing import Optional

from pydantic import BaseModel, RootModel, field_validator


class SignalListModel(RootModel[list[str]]):
    "A list of signals"


class SignalMode(str, Enum):
    "The mode of a signal"

    INPUT = "input"
    OUTPUT_PP = "output_pp"
    OUTPUT_OD = "output_od"


class SignalState(str, Enum):
    "The state of a signal"

    INACTIVE = "inactive"
    ACTIVE = "active"


class SignalStateModel(RootModel[SignalState]):
    "Model for the state of a signal"


class SignalConfig(BaseModel):
    "The configuration of a signal"

    mode: SignalMode
    initial_state: Optional[SignalState] = None


class SignalSetStateParams(BaseModel):
    "Parameters for the tools.gpio.signal.set_state endpoint"

    tool_id: str
    signal: str
    state: SignalState


class SignalConfigureParams(BaseModel):
    "Parameters for the tools.gpio.signal.configure endpoint"

    tool_id: str
    signal: str
    config: SignalConfig


class SignalGetParams(BaseModel):
    "Parameters for the tools.gpio.signal.get_configuration endpoint"

    tool_id: str
    signal: str


class PlaylistState(str, Enum):
    "The state of a GPIO tool's playlist machinery"

    IDLE = "idle"
    PLAYING = "playing"


class PlaylistStateModel(RootModel[PlaylistState]):
    "Model for the state of a GPIO tool's playlist machinery"


class PlaylistEntry(BaseModel):
    "An entry in a playlist"

    signal: str
    state: SignalState
    delay_ms: int = 0

    @field_validator("delay_ms")
    @classmethod
    def delay_ms_must_not_be_negative(cls, v: int) -> int:  # pylint: disable=no-self-argument # https://github.com/PyCQA/pylint/issues/6900
        """Ensure that delay_ms is positive"""
        if v < 0:
            raise ValueError("delay_ms must not be negative")
        return v


class PlaylistPlayParams(BaseModel):
    "Parameters for the tools.gpio.playlist.play endpoint"

    tool_id: str
    playlist: list[PlaylistEntry]

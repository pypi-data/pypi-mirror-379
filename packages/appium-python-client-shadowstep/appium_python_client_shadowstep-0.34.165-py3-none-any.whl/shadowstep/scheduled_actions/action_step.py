# shadowstep/scheduled_actions/action_step.py
from __future__ import annotations

from typing import Any

from shadowstep.element.element import Element


class ActionStep:
    @staticmethod
    def gesture_click(name: str, locator: tuple[str, str] | dict[str, Any] | Element) -> ActionStep: ...
    @staticmethod
    def gesture_long_click(name: str, locator: tuple[str, str] | dict[str, Any] | Element) -> ActionStep: ...
    @staticmethod
    def gesture_double_click(name: str, element_id: str, x: int, y: int) -> ActionStep: ...
    @staticmethod
    def source(name: str) -> ActionStep: ...
    @staticmethod
    def screenshot(name: str) -> ActionStep: ...

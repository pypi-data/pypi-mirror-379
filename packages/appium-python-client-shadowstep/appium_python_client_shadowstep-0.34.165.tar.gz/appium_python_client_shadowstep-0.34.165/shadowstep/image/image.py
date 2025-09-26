from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

import numpy as np
from PIL import Image as PILImage

from shadowstep.utils.utils import get_current_func_name

if TYPE_CHECKING:
    from shadowstep.shadowstep import Shadowstep


class ShadowstepImage:
    """Lazy wrapper for image-based interactions"""

    def __init__(
        self,
        image: bytes | np.ndarray[Any, Any] | PILImage.Image | str,
        base: Shadowstep,
        threshold: float = 0.5,
        timeout: float = 5.0,
    ):
        self._image = image
        self._base: Shadowstep = base
        self.threshold = threshold
        self.timeout = timeout
        self._coords: tuple[int, int, int, int] | None = None
        self._center: tuple[int, int] | None = None
        self.logger = logging.getLogger(__name__)

    def _ensure_visible(self) -> None:
        """Check visibility and cache coordinates/center if found."""
        # self.logger.debug(f"{get_current_func_name()}")
        # if not self._base:
        #     raise RuntimeError("Shadowstep instance is not set.")
        # screen = self.to_ndarray(self._base.get_screenshot())
        # template = self.to_ndarray(self._image)
        #
        # screen = self._preprocess(screen)
        # template = self._preprocess(template)
        #
        # result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        # _, max_val, _, max_loc = cv2.minMaxLoc(result)
        #
        # self.logger.debug(f"[is_visible] direct match: max_val={max_val:.3f}, loc={max_loc}")
        #
        # if max_val >= self.threshold:
        #     x1, y1 = max_loc
        #     h, w = template.shape[:2]
        #     self._coords = (x1, y1, x1 + w, y1 + h)
        #     self._center = ((x1 + x1 + w) // 2, (y1 + y1 + h) // 2)
        #     return
        #
        # fallback_val, fallback_loc = self.multi_scale_matching(screen, template)
        # self.logger.debug(f"[is_visible] fallback multi-scale: max_val={fallback_val:.3f}, loc={fallback_loc}")
        #
        # if fallback_val >= self.threshold:
        #     x1, y1 = fallback_loc
        #     h, w = template.shape[:2]
        #     self._coords = (x1, y1, x1 + w, y1 + h)
        #     self._center = ((x1 + x1 + w) // 2, (y1 + y1 + h) // 2)
        #     return
        #
        # raise ValueError(f"Image not found on screen (max_val={max_val:.3f}, fallback_val={fallback_val:.3f}, threshold={self.threshold})")
        raise NotImplementedError

    def tap(self, duration: int | None = None) -> ShadowstepImage:
        # self.logger.debug(f"{get_current_func_name()}")
        # self._ensure_visible()
        # x, y = self.center
        # self._base.tap(x, y, duration=duration)
        # return self
        raise NotImplementedError

    def drag(self, to: tuple[int, int] | ShadowstepImage, duration: float = 1.0) -> ShadowstepImage:
        # self.logger.debug(f"{get_current_func_name()}")
        # self._ensure_visible()
        # x1, y1 = self.center
        # if isinstance(to, tuple):
        #     x2, y2 = to
        # elif isinstance(to, ShadowstepImage):
        #     to._ensure_visible()
        #     x2, y2 = to.center
        # else:
        #     raise TypeError(f"Unsupported drag target type: {type(to)}")
        # self._base.drag(x1, y1, x2, y2, duration=duration)
        # return self
        raise NotImplementedError

    def zoom(self, percent: float = 1.5, steps: int = 10) -> ShadowstepImage:
        # self.logger.debug(f"{get_current_func_name()}")
        # self._ensure_visible()
        # x, y = self.center
        # self._base.zoom(x, y, percent=percent, steps=steps)
        # return self
        raise NotImplementedError

    def unzoom(self, percent: float = 0.5, steps: int = 10) -> ShadowstepImage:
        # self.logger.debug(f"{get_current_func_name()}")
        # self._ensure_visible()
        # x, y = self.center
        # self._base.pinch(x, y, percent=percent, steps=steps)
        # return self
        raise NotImplementedError

    def wait(self) -> bool:
        # self.logger.debug(f"{get_current_func_name()}")
        # end_time = time.monotonic() + self.timeout
        # while time.monotonic() < end_time:
        #     try:
        #         self._ensure_visible()
        #         return True
        #     except Exception:
        #         time.sleep(0.5)
        # return False
        raise NotImplementedError

    def wait_not(self) -> bool:
        # self.logger.debug(f"{get_current_func_name()}")
        # end_time = time.monotonic() + self.timeout
        # while time.monotonic() < end_time:
        #     try:
        #         self._ensure_visible()
        #     except Exception:
        #         return True
        #     time.sleep(0.5)
        # return False
        raise NotImplementedError

    def is_visible(self) -> bool:
        # self.logger.debug(f"{get_current_func_name()} {self.threshold=}")
        # try:
        #     self._ensure_visible()
        #     return True
        # except Exception as e:
        #     self._base.logger.warning(f"[is_visible] failed: {e}")
        #     return False
        raise NotImplementedError

    @property
    def coordinates(self) -> tuple[int, int, int, int]:
        # self.logger.debug(f"{get_current_func_name()}")
        # if self._coords is None:
        #     self._ensure_visible()
        # return self._coords
        raise NotImplementedError

    @property
    def center(self) -> tuple[int, int]:
        # self.logger.debug(f"{get_current_func_name()}")
        # if self._center is None:
        #     self._ensure_visible()
        # return self._center
        raise NotImplementedError

    def scroll_down(
        self,
        from_percent: float = 0.5,
        to_percent: float = 0.1,
        max_attempts: int = 10,
        step_delay: float = 0.5,
    ) -> ShadowstepImage:
        # self.logger.debug(f"{get_current_func_name()}")
        #
        # if not self._base:
        #     raise RuntimeError("Shadowstep instance is not set.")
        #
        # self._ensure_visible()  # container should be visible
        #
        # for _ in range(max_attempts):
        #     try:
        #         x1, y1, x2, y2 = self.coordinates
        #     except Exception as e:
        #         raise ValueError(f"Cannot scroll container: {e}") from e
        #
        #     width = x2 - x1
        #     height = y2 - y1
        #     center_x = x1 + width // 2
        #     start_y = int(y1 + height * from_percent)
        #     end_y = int(y1 + height * to_percent)
        #
        #     self.logger.debug(f"Scroll swipe from ({center_x}, {start_y}) to ({center_x}, {end_y})")
        #     self._base.swipe(center_x, start_y, center_x, end_y)
        #     time.sleep(step_delay)
        #
        # return self
        raise NotImplementedError

    def scroll_up(self, max_attempts: int = 10, step_delay: float = 0.5) -> ShadowstepImage:
        # self.logger.debug(f"{get_current_func_name()}")
        # if not self._base:
        #     raise RuntimeError("Shadowstep instance is not set.")
        # width, height = self._base.get_screen_resolution()
        # x = width // 2
        # y_start = int(height * 0.2)
        # y_end = int(height * 0.8)
        # for _ in range(max_attempts):
        #     try:
        #         self._ensure_visible()
        #         return self
        #     except Exception:
        #         self._base.swipe(x, y_start, x, y_end, duration=0.3)
        #         time.sleep(step_delay)
        # raise ValueError("Image not found after scrolling up.")
        raise NotImplementedError

    def scroll_left(self, max_attempts: int = 10, step_delay: float = 0.5) -> ShadowstepImage:
        # self.logger.debug(f"{get_current_func_name()}")
        # if not self._base:
        #     raise RuntimeError("Shadowstep instance is not set.")
        # width, height = self._base.get_screen_resolution()
        # y = height // 2
        # x_start = int(width * 0.8)
        # x_end = int(width * 0.2)
        # for _ in range(max_attempts):
        #     try:
        #         self._ensure_visible()
        #         return self
        #     except Exception:
        #         self._base.swipe(x_start, y, x_end, y, duration=0.3)
        #         time.sleep(step_delay)
        # raise ValueError("Image not found after scrolling left.")
        raise NotImplementedError

    def scroll_right(self, max_attempts: int = 10, step_delay: float = 0.5) -> ShadowstepImage:
        # self.logger.debug(f"{get_current_func_name()}")
        # if not self._base:
        #     raise RuntimeError("Shadowstep instance is not set.")
        # width, height = self._base.get_screen_resolution()
        # y = height // 2
        # x_start = int(width * 0.2)
        # x_end = int(width * 0.8)
        # for _ in range(max_attempts):
        #     try:
        #         self._ensure_visible()
        #         return self
        #     except Exception:
        #         self._base.swipe(x_start, y, x_end, y, duration=0.3)
        #         time.sleep(step_delay)
        # raise ValueError("Image not found after scrolling right.")
        raise NotImplementedError

    def scroll_to(self, max_attempts: int = 10, step_delay: float = 0.5) -> ShadowstepImage:
        # self.logger.debug(f"{get_current_func_name()}")
        # if not self._base:
        #     raise RuntimeError("Shadowstep instance is not set.")
        # screen_w, screen_h = self._base.get_screen_resolution()
        # center_x, center_y = screen_w // 2, screen_h // 2
        # for _ in range(max_attempts):
        #     try:
        #         self._ensure_visible()
        #         return self
        #     except Exception:
        #         try:
        #             x, y = self.center
        #         except Exception:
        #             x, y = center_x, center_y
        #         if y > center_y:
        #             self._base.swipe(center_x, int(screen_h * 0.8), center_x, int(screen_h * 0.2), duration=0.3)
        #         else:
        #             self._base.swipe(center_x, int(screen_h * 0.2), center_x, int(screen_h * 0.8), duration=0.3)
        #         time.sleep(step_delay)
        # raise ValueError("Image not found after scroll_to().")
        raise NotImplementedError

    def is_contains(self, image: bytes | np.ndarray[Any, Any] | PILImage.Image | str) -> bool:
        # self.logger.debug(f"{get_current_func_name()}")
        # try:
        #     haystack = self.to_ndarray(self._image)
        #     needle = self.to_ndarray(image)
        #     haystack_gray = cv2.cvtColor(haystack, cv2.COLOR_RGB2GRAY)
        #     needle_gray = cv2.cvtColor(needle, cv2.COLOR_RGB2GRAY)
        #     result = cv2.matchTemplate(haystack_gray, needle_gray, cv2.TM_CCOEFF_NORMED)
        #     _, max_val, _, _ = cv2.minMaxLoc(result)
        #     return max_val >= self.threshold
        # except Exception:
        #     return False
        raise NotImplementedError

    @property
    def should(self) -> Any:  # type: ignore
        """ImageShould functionality - not yet implemented."""
        self.logger.debug(f"{get_current_func_name()}")
        raise NotImplementedError

    def to_ndarray(
        self, image: bytes | np.ndarray[Any, Any] | PILImage.Image | str,
    ) -> np.ndarray[Any, Any]:
        # self.logger.debug(f"{get_current_func_name()}")
        # if isinstance(image, np.ndarray):
        #     return image
        # if isinstance(image, bytes):
        #     image = PILImage.open(io.BytesIO(image))
        # elif isinstance(image, str):
        #     image = PILImage.open(image)
        # if isinstance(image, PILImage.Image):
        #     return np.array(image.convert("RGB"))
        # raise ValueError("Unsupported image format")
        raise NotImplementedError

    def _preprocess(self, image: np.ndarray[Any, Any]) -> np.ndarray[Any, Any]:
        # self.logger.debug(f"{get_current_func_name()}")
        # gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        # return clahe.apply(blurred)
        raise NotImplementedError

    def _enhance_image(self, image: np.ndarray[Any, Any]) -> np.ndarray[Any, Any]:
        # self.logger.debug(f"{get_current_func_name()}")
        # if len(image.shape) == 3 and image.shape[2] == 3:
        #     gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # else:
        #     gray = image
        # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        # enhanced = clahe.apply(gray)
        # return cv2.GaussianBlur(enhanced, (3, 3), 0)
        raise NotImplementedError

    def multi_scale_matching(
        self, full_image: np.ndarray[Any, Any], template_image: np.ndarray[Any, Any],
    ) -> tuple[float, tuple[int, int]]:
        # self.logger.debug(f"{get_current_func_name()}")
        # full_image = self._enhance_image(full_image)
        # template_image = self._enhance_image(template_image)
        # origin_w, origin_h = template_image.shape[::-1]
        # best_val = 0
        # best_loc = (0, 0)
        # for scale in np.concatenate([np.linspace(0.2, 1.0, 10)[::-1], np.linspace(1.1, 2.0, 10)]):
        #     resized = cv2.resize(full_image, (int(full_image.shape[1] * scale), int(full_image.shape[0] * scale)))
        #     if resized.shape[0] < origin_h or resized.shape[1] < origin_w:
        #         continue
        #     result = cv2.matchTemplate(resized, template_image, cv2.TM_CCOEFF_NORMED)
        #     _, max_val, _, max_loc = cv2.minMaxLoc(result)
        #     if max_val > best_val:
        #         best_val = max_val
        #         best_loc = (int(max_loc[0] / scale), int(max_loc[1] / scale))
        # return best_val, best_loc if best_val >= self.threshold else (0.0, (0, 0))
        raise NotImplementedError

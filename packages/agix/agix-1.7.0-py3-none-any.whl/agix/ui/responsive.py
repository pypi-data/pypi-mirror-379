from __future__ import annotations

"""Herramientas de diseño adaptable para la interfaz de AGIX."""

from enum import Enum
from typing import Callable, Iterable, List

import flet as ft


class Breakpoint(str, Enum):
    """Tipos de dispositivos soportados."""

    MOBILE = "mobile"
    TABLET = "tablet"
    DESKTOP = "desktop"


MOBILE_MAX_WIDTH = 600
TABLET_MAX_WIDTH = 1024


class ResponsiveManager:
    """Gestiona el breakpoint actual en función del ancho de la página."""

    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.breakpoint: Breakpoint = self._calculate(page.width)
        self._listeners: List[Callable[[Breakpoint], None]] = []
        page.on_resize = self._on_resize

    def _calculate(self, width: float | int) -> Breakpoint:
        if width < MOBILE_MAX_WIDTH:
            return Breakpoint.MOBILE
        if width < TABLET_MAX_WIDTH:
            return Breakpoint.TABLET
        return Breakpoint.DESKTOP

    def _on_resize(self, e: ft.ControlEvent) -> None:  # pragma: no cover - evento de Flet
        width = getattr(e, "width", self.page.width)
        bp = self._calculate(width)
        if bp != self.breakpoint:
            self.breakpoint = bp
            for cb in list(self._listeners):
                cb(bp)

    def add_listener(self, callback: Callable[[Breakpoint], None]) -> None:
        """Registra un callback para cambios de breakpoint."""

        self._listeners.append(callback)

    def remove_listener(self, callback: Callable[[Breakpoint], None]) -> None:
        if callback in self._listeners:
            self._listeners.remove(callback)

    # Helpers de estado ---------------------------------------------------
    def is_mobile(self) -> bool:
        return self.breakpoint == Breakpoint.MOBILE

    def is_tablet(self) -> bool:
        return self.breakpoint == Breakpoint.TABLET

    def is_desktop(self) -> bool:
        return self.breakpoint == Breakpoint.DESKTOP


def responsive_row(
    controls: Iterable[ft.Control],
    *,
    mobile_cols: int = 1,
    tablet_cols: int = 2,
    desktop_cols: int = 4,
    **kwargs,
) -> ft.ResponsiveRow:
    """Crea una fila que ajusta las columnas según el breakpoint.

    El layout se basa en una rejilla de 12 columnas. ``mobile_cols`` indica
    cuántos controles se muestran por fila en móvil; ``tablet_cols`` y
    ``desktop_cols`` se aplican para los demás breakpoints.
    """

    def _span(cols: int) -> int:
        return max(1, 12 // max(1, cols))

    styled_controls: list[ft.Control] = []
    for ctrl in controls:
        ctrl.col = {
            "xs": _span(mobile_cols),
            "md": _span(tablet_cols),
            "lg": _span(desktop_cols),
        }
        styled_controls.append(ctrl)
    return ft.ResponsiveRow(styled_controls, **kwargs)


def responsive_visibility(
    control: ft.Control,
    manager: ResponsiveManager,
    *,
    visible_on: Iterable[Breakpoint],
) -> ft.Control:
    """Ajusta la visibilidad de un control para los breakpoints dados."""

    allowed = set(visible_on)

    def _update(bp: Breakpoint) -> None:
        control.visible = bp in allowed
        try:  # pragma: no cover - ``update`` puede no existir en tests
            control.update()
        except Exception:
            pass

    _update(manager.breakpoint)
    manager.add_listener(_update)
    return control

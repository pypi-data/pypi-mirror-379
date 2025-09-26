"""Componentes reutilizables de interfaz basados en Flet.

Este módulo define clases sencillas para crear botones, tarjetas y
listas con parámetros de estilo personalizables. Todos los componentes
aceptan colores para los estados ``hover``, ``pressed`` y ``disabled`` a
través de diccionarios de :class:`flet.ControlState`.

Extender
--------
Para añadir nuevos tipos de controles (por ejemplo ``Checkbox``,
``Switch`` o ``Slider``) se puede seguir el mismo patrón que en las
clases incluidas:

1. Definir una ``dataclass`` con los parámetros de estilo deseados
   (color, tamaño e iconografía).
2. En el método ``build`` crear el control de Flet correspondiente.
3. Aplicar los colores de estado usando diccionarios de
   ``flet.ControlState``.

Ejemplo básico::

    @dataclass
    class Checkbox:
        label: str
        color: str = ft.colors.BLUE

        def build(self) -> ft.Checkbox:
            return ft.Checkbox(
                label=self.label,
                bgcolor={ft.ControlState.DEFAULT: self.color},
            )

Las clases aquí definidas pueden utilizarse como guía para nuevos
componentes reutilizables dentro de la aplicación.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import flet as ft

# ``flet`` 0.28 no expone ``colors`` en el módulo principal.
if not hasattr(ft, "colors"):
    ft.colors = ft.Colors  # type: ignore[attr-defined]


def _state_color(
    default: str,
    hover: Optional[str] = None,
    pressed: Optional[str] = None,
    disabled: Optional[str] = None,
) -> dict[ft.ControlState, str]:
    """Crea un diccionario de colores por estado."""

    return {
        ft.ControlState.DEFAULT: default,
        ft.ControlState.HOVERED: hover or default,
        ft.ControlState.PRESSED: pressed or default,
        ft.ControlState.DISABLED: disabled or default,
    }


@dataclass
class Button:
    """Botón estilizable con soporte de icono y estados."""

    text: str
    color: str = ft.colors.BLUE
    hover_color: Optional[str] = None
    pressed_color: Optional[str] = None
    disabled_color: Optional[str] = None
    size: int = 14
    icon: Optional[str] = None
    disabled: bool = False

    def build(self) -> ft.ElevatedButton:
        icon_value = getattr(ft.Icons, self.icon) if self.icon else None
        style = ft.ButtonStyle(
            bgcolor=_state_color(
                self.color, self.hover_color, self.pressed_color, self.disabled_color
            ),
            text_style=ft.TextStyle(size=self.size),
        )
        return ft.ElevatedButton(
            text=self.text,
            icon=icon_value,
            style=style,
            disabled=self.disabled,
        )


@dataclass
class Card:
    """Tarjeta simple con título e icono opcional."""

    title: str
    color: str = ft.colors.WHITE
    hover_color: Optional[str] = None
    pressed_color: Optional[str] = None
    disabled_color: Optional[str] = None
    size: int = 14
    icon: Optional[str] = None
    disabled: bool = False

    def build(self) -> ft.Card:
        icon_control = ft.Icon(getattr(ft.Icons, self.icon)) if self.icon else None
        content = ft.ListTile(
            leading=icon_control,
            title=ft.Text(self.title, size=self.size),
        )
        return ft.Card(
            content=content,
            color=_state_color(
                self.color, self.hover_color, self.pressed_color, self.disabled_color
            ),
            disabled=self.disabled,
        )


@dataclass
class ListItem:
    """Elemento de lista con icono y colores por estado."""

    title: str
    color: str = ft.colors.WHITE
    hover_color: Optional[str] = None
    pressed_color: Optional[str] = None
    disabled_color: Optional[str] = None
    size: int = 14
    icon: Optional[str] = None
    disabled: bool = False

    def build(self) -> ft.ListTile:
        icon_control = ft.Icon(getattr(ft.Icons, self.icon)) if self.icon else None
        return ft.ListTile(
            leading=icon_control,
            title=ft.Text(self.title, size=self.size),
            bgcolor=_state_color(
                self.color, self.hover_color, self.pressed_color, self.disabled_color
            ),
            disabled=self.disabled,
        )

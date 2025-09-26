"""Definiciones de estilos reutilizables para controles Flet.

Este módulo proporciona dataclasses para describir márgenes, padding,
bordes, tipografías y colores. También incluye funciones auxiliares
para aplicar estas definiciones a controles comunes de Flet, así como
un tema predeterminado y utilidades para crear temas personalizados.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import flet as ft


# --- Definiciones básicas de estilo -------------------------------------------------


@dataclass
class Margin:
    """Márgenes externos."""

    left: int = 0
    top: int = 0
    right: int = 0
    bottom: int = 0


@dataclass
class Padding:
    """Relleno interno."""

    left: int = 0
    top: int = 0
    right: int = 0
    bottom: int = 0


@dataclass
class Border:
    """Borde de los controles."""

    width: int = 0
    color: str = ft.colors.BLACK
    radius: int = 0


@dataclass
class Typography:
    """Propiedades tipográficas."""

    size: int = 14
    weight: ft.FontWeight = ft.FontWeight.NORMAL


@dataclass
class Colors:
    """Paleta de colores."""

    primary: str = ft.colors.BLUE
    secondary: str = ft.colors.BLUE_200
    background: str = ft.colors.WHITE
    text: str = ft.colors.BLACK
    on_primary: str = ft.colors.WHITE


@dataclass
class Theme:
    """Tema completo que agrupa todas las definiciones."""

    margin: Margin = field(default_factory=Margin)
    padding: Padding = field(default_factory=Padding)
    border: Border = field(default_factory=Border)
    typography: Typography = field(default_factory=Typography)
    colors: Colors = field(default_factory=Colors)


# Tema predeterminado ---------------------------------------------------------------

DEFAULT_THEME = Theme(
    margin=Margin(8, 8, 8, 8),
    padding=Padding(10, 10, 10, 10),
    border=Border(1, ft.colors.BLUE_GREY_100, 6),
    typography=Typography(14, ft.FontWeight.NORMAL),
    colors=Colors(
        primary=ft.colors.BLUE,
        secondary=ft.colors.BLUE_200,
        background=ft.colors.WHITE,
        text=ft.colors.BLACK,
        on_primary=ft.colors.WHITE,
    ),
)


def create_theme(
    *,
    margin: Margin | None = None,
    padding: Padding | None = None,
    border: Border | None = None,
    typography: Typography | None = None,
    colors: Colors | None = None,
) -> Theme:
    """Crea un tema personalizado combinando valores dados con el predeterminado."""

    base = DEFAULT_THEME
    return Theme(
        margin=margin or base.margin,
        padding=padding or base.padding,
        border=border or base.border,
        typography=typography or base.typography,
        colors=colors or base.colors,
    )


# --- Funciones de aplicación -------------------------------------------------------


def style_container(container: ft.Container, theme: Theme = DEFAULT_THEME) -> ft.Container:
    """Aplica estilo de contenedor basado en un tema."""

    container.margin = ft.Margin(
        theme.margin.left,
        theme.margin.top,
        theme.margin.right,
        theme.margin.bottom,
    )
    container.padding = ft.Padding(
        theme.padding.left,
        theme.padding.top,
        theme.padding.right,
        theme.padding.bottom,
    )
    container.border = ft.border.all(theme.border.width, theme.border.color)
    container.border_radius = theme.border.radius
    container.bgcolor = theme.colors.background
    return container


def style_text(text: ft.Text, theme: Theme = DEFAULT_THEME) -> ft.Text:
    """Aplica estilo tipográfico y de color a un texto."""

    text.color = theme.colors.text
    text.size = theme.typography.size
    text.weight = theme.typography.weight
    return text


def style_button(button: ft.ElevatedButton, theme: Theme = DEFAULT_THEME) -> ft.ElevatedButton:
    """Aplica estilo a un botón elevado."""

    button.style = ft.ButtonStyle(
        bgcolor=theme.colors.primary,
        color=theme.colors.on_primary,
        padding=ft.Padding(
            theme.padding.left,
            theme.padding.top,
            theme.padding.right,
            theme.padding.bottom,
        ),
        side=ft.BorderSide(width=theme.border.width, color=theme.border.color),
        shape=ft.RoundedRectangleBorder(radius=theme.border.radius),
        text_style=ft.TextStyle(
            size=theme.typography.size,
            weight=theme.typography.weight,
        ),
    )
    return button

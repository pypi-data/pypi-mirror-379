"""Interfaz básica en Flet para el dashboard de AGIX."""

from __future__ import annotations

import flet as ft
import requests

from .styles import DEFAULT_THEME, style_button, style_container, style_text

DASHBOARD_URL = "http://localhost:8000"


def main(page: ft.Page) -> None:
    """Configura la página principal con componentes básicos."""
    page.title = "AGIX Dashboard"
    page.appbar = ft.AppBar(title=style_text(ft.Text("AGIX Dashboard"), DEFAULT_THEME))
    page.drawer = ft.NavigationDrawer(
        controls=[
            style_container(ft.Container(style_text(ft.Text("Inicio"), DEFAULT_THEME)), DEFAULT_THEME),
            style_container(ft.Container(style_text(ft.Text("Qualia"), DEFAULT_THEME)), DEFAULT_THEME),
            style_container(ft.Container(style_text(ft.Text("Métricas"), DEFAULT_THEME)), DEFAULT_THEME),
        ]
    )

    metrics_container = ft.Column()
    qualia_container = ft.Column()

    def refresh_metrics(_=None) -> None:
        try:
            data = requests.get(f"{DASHBOARD_URL}/metrics", timeout=5).json()
        except Exception as exc:  # pragma: no cover - manejo básico de errores
            data = {"error": str(exc)}
        metrics_container.controls = [
            style_text(ft.Text(f"{k}: {v}"), DEFAULT_THEME) for k, v in data.items()
        ]
        page.update()

    def refresh_qualia(_=None) -> None:
        try:
            data = requests.get(f"{DASHBOARD_URL}/qualia", timeout=5).json()
        except Exception as exc:  # pragma: no cover - manejo básico de errores
            data = {"emociones": {}, "tono": str(exc)}
        qualia_container.controls = [
            style_text(ft.Text(f"{k}: {v}"), DEFAULT_THEME)
            for k, v in data.get("emociones", {}).items()
        ]
        if "tono" in data:
            qualia_container.controls.append(
                style_text(ft.Text(f"tono: {data['tono']}"), DEFAULT_THEME)
            )
        page.update()

    page.add(
        ft.Column(
            [
                style_button(
                    ft.ElevatedButton("Actualizar Métricas", on_click=refresh_metrics),
                    DEFAULT_THEME,
                ),
                metrics_container,
                style_button(
                    ft.ElevatedButton("Actualizar Qualia", on_click=refresh_qualia),
                    DEFAULT_THEME,
                ),
                qualia_container,
            ]
        )
    )

    refresh_metrics()
    refresh_qualia()


if __name__ == "__main__":  # pragma: no cover
    ft.app(target=main)

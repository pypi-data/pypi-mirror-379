"""
Absfuyu: GUI
------------
Custom tkinter GUI

Version: 5.9.0
Date updated: 23/09/2025 (dd/mm/yyyy)
"""

# Module level
# ---------------------------------------------------------------------------
__all__ = ["CustomTkinterApp"]


# Library
# ---------------------------------------------------------------------------
import tkinter as tk

from absfuyu.pkg_data.logo import AbsfuyuLogo


# Class
# ---------------------------------------------------------------------------
class CustomTkinterApp(tk.Tk):
    def __init__(self, title: str | None = None) -> None:
        super().__init__()

        # Set custom icon
        self.iconphoto(True, tk.PhotoImage(data=AbsfuyuLogo.SHORT))

        # Title
        self.title(title)

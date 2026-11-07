"""Tkinter desktop interface for the unit converter."""

import tkinter as tk
from tkinter import messagebox, ttk

from converter import TEMPERATURE_UNITS, UNITS, convert


class UnitConverterApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title("Unit Converter")
        root.geometry("480x430")
        root.minsize(420, 400)
        root.configure(bg="#f4f6fb")

        style = ttk.Style()
        style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"), foreground="#263991")
        style.configure("Result.TLabel", font=("Segoe UI", 18, "bold"), foreground="#263991")
        style.configure("TLabel", background="#f4f6fb")

        frame = ttk.Frame(root, padding=28)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="Unit Converter", style="Title.TLabel").pack(anchor="w")
        ttk.Label(frame, text="Convert everyday measurements").pack(anchor="w", pady=(2, 20))

        ttk.Label(frame, text="Category").pack(anchor="w")
        self.category = tk.StringVar(value="Length")
        self.category_box = ttk.Combobox(
            frame, textvariable=self.category,
            values=("Length", "Weight", "Temperature", "Volume"),
            state="readonly",
        )
        self.category_box.pack(fill="x", pady=(5, 14))
        self.category_box.bind("<<ComboboxSelected>>", self.update_units)

        ttk.Label(frame, text="Amount").pack(anchor="w")
        self.amount = ttk.Entry(frame)
        self.amount.insert(0, "1")
        self.amount.pack(fill="x", pady=(5, 14))

        units_row = ttk.Frame(frame)
        units_row.pack(fill="x")
        self.source = tk.StringVar()
        self.target = tk.StringVar()
        self.source_box = ttk.Combobox(units_row, textvariable=self.source, state="readonly")
        self.target_box = ttk.Combobox(units_row, textvariable=self.target, state="readonly")
        self.source_box.pack(side="left", fill="x", expand=True)
        ttk.Button(units_row, text="⇄", width=4, command=self.swap_units).pack(side="left", padx=8)
        self.target_box.pack(side="left", fill="x", expand=True)

        ttk.Button(frame, text="Convert", command=self.show_result).pack(fill="x", pady=18)
        self.result_label = ttk.Label(frame, text="Result will appear here", style="Result.TLabel")
        self.result_label.pack(anchor="w", pady=(4, 0))
        self.update_units()

    def update_units(self, _event: object = None) -> None:
        units = TEMPERATURE_UNITS if self.category.get() == "Temperature" else tuple(UNITS[self.category.get()])
        self.source_box["values"] = units
        self.target_box["values"] = units
        self.source.set(units[0])
        self.target.set(units[1])
        self.show_result()

    def swap_units(self) -> None:
        old_source = self.source.get()
        self.source.set(self.target.get())
        self.target.set(old_source)
        self.show_result()

    def show_result(self) -> None:
        try:
            value = float(self.amount.get())
            answer = convert(value, self.category.get(), self.source.get(), self.target.get())
            formatted = f"{answer:,.8g}"
            self.result_label.configure(
                text=f"{formatted} {self.target.get()}",
                foreground="#263991",
            )
        except ValueError:
            self.result_label.configure(text="Enter a valid number", foreground="#b42318")


if __name__ == "__main__":
    window = tk.Tk()
    UnitConverterApp(window)
    window.mainloop()

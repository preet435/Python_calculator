
import tkinter as tk

root = tk.Tk()
root.title("My Python Calculator")
root.geometry("320x450")
root.resizable(False, False)

expression = ""

display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    state="readonly"
)
display.pack(fill="x", padx=10, pady=15)


def update_display():
    display.config(state="normal")
    display.delete(0, tk.END)
    display.insert(0, expression)
    display.config(state="readonly")


def press(value):
    global expression
    expression += str(value)
    update_display()


def clear():
    global expression
    expression = ""
    update_display()


def backspace():
    global expression
    expression = expression[:-1]
    update_display()


def calculate():
    global expression
    try:
        import re

        if not expression or not re.fullmatch(
            r"[0-9+\-*/.() ]+", expression
        ):
            raise ValueError

        result = eval(
            expression,
            {"__builtins__": None},
            {}
        )
        expression = str(result)
        update_display()

    except Exception:
        expression = ""
        update_display()
        display.config(state="normal")
        display.insert(0, "Invalid Expression")
        display.config(state="readonly")


buttons = [
    ["AC", "⌫", "(", ")"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for item in row:
        if item == "AC":
            command = clear
        elif item == "⌫":
            command = backspace
        elif item == "=":
            command = calculate
        else:
            command = lambda x=item: press(x)

        tk.Button(
            frame,
            text=item,
            font=("Arial", 16),
            command=command
        ).pack(
            side="left",
            expand=True,
            fill="both",
            padx=2,
            pady=2
        )

root.mainloop()

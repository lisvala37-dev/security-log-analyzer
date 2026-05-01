import tkinter as tk
from tkinter import ttk


def analiz(entry, table, status):
    """Читает файл, парсит и заполняет таблицу."""
    filename = entry.get()
    if not filename:
        status.config(text="Enter file name", fg="orange")
        return
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read()
        # Разбиваем на строки, игнорируя пустые
        lines = [line.strip() for line in data.splitlines() if line.strip()]
        if not lines:
            status.config(text="File is empty", fg="orange")
            return
        fill_table_from_data(table, lines)
        status.config(text=f"Loaded events: {len(lines)}", fg="lightgreen")
    except FileNotFoundError:
        status.config(text="File not found", fg="red")
    except PermissionError:
        status.config(text="No read permissions", fg="orange")
    except Exception as e:
        status.config(text=f"Error: {e}", fg="red")

def parse_log_line(line):
    parts = line.split()
    
    if len(parts) < 6:
      raise ValueError("Invalid log line")

    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "ip": parts[3],
        "user": parts[4].replace("user=", ""),
        "action": parts[5].replace("action=", ""),
    }
def fill_table_from_data(table, log_lines):
    for row in table.get_children():
        table.delete(row)

    for line in log_lines:
        event = parse_log_line(line)
        table.insert("", "end", values=(
            event["date"],
            event["time"],
            event["level"],
            event["ip"],
            event["user"],
            event["action"]
        ))




def main():
    root = tk.Tk()
    root.title("Security Log Analyzer")
    root.geometry("950x600")
    root.configure(bg="black")

    # Заголовок
    title = tk.Label(root, text="Security Log Analyzer", font=("Arial", 18, "bold"), fg="lightgreen", bg="black")
    title.pack(pady=10)

    # Ряд: надпись + поле ввода + кнопка
    frame_input = tk.Frame(root, bg="black")
    frame_input.pack(pady=5)

    tk.Label(frame_input, text="File name:", bg="black", fg="lightgreen", font=("Arial", 12)).pack(side="left", padx=5)
    entry = tk.Entry(frame_input, width=40, bg="gray20", fg="white", font=("Arial", 12))
    entry.pack(side="left", padx=5)
    btn = tk.Button(frame_input, text="Analysis", bg="gray20", fg="lightgreen",
                    command=lambda: analiz(entry, table, status))
    btn.pack(side="left", padx=5)

    # Таблица
    columns = ("date", "time", "level", "ip", "user", "action")
    table = ttk.Treeview(root, columns=columns, show="headings")

    table.heading("date", text="Date")
    table.heading("time", text="Time")
    table.heading("level", text="Level")
    table.heading("ip", text="IP Address")
    table.heading("user", text="User")
    table.heading("action", text="Action")

    table.column("date", width=120)
    table.column("time", width=100)
    table.column("level", width=100)
    table.column("ip", width=150)
    table.column("user", width=120)
    table.column("action", width=200)

    table.pack(fill="both", expand=True, padx=15, pady=10)

    # Строка статуса
    status = tk.Label(root, text="No file loaded", anchor="w", bg="black", fg="lightgreen", font=("Arial", 10))
    status.pack(fill="x", padx=15, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
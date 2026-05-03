# Security Log Analyzer

This is my small Python learning project with a graphical interface.

The program can read a log file, parse log lines and show the result in a table.

## Why I made this project

I made this project because I want to improve my Python skills and prepare for an IT apprenticeship.

I am interested in software development, IT security and technical problem solving.

## What the program can do

- Open a log file
- Read log lines
- Parse date, time, level, IP, user and action
- Show the data in a table
- Show a status message
- Handle simple errors like file not found or empty file

## Technologies

- Python
- Tkinter
- ttk Treeview
- File handling
- Basic error handling

## Example log line

2026-05-01 10:16:02 WARNING 45.91.23.10 user=root action=login_failed

## How to run

Run the program:

python main.py

Then enter the file name:

log.txt

and click the Analyze button.

## Project status

This project is still in development.

Next steps:

- Count INFO, WARNING, ERROR and CRITICAL events
- Detect repeated failed login attempts
- Add a risk score
- Improve the user interface

## What I learned

With this project I learned how to create a simple graphical interface, read files, split text lines and show parsed data in a table.

## Security note

This project is a defensive learning project. It only reads example log files and does not scan, attack or connect to external systems.

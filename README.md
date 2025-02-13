# Task Timer

## Description
A simple command-line task timer that allows you to track time spent on tasks and export records as a CSV file. Built using a uv virtual environment.

## Features
Features
1) Start and stop multiple tasks with timestamps.
2) View running tasks and time summaries.
3) Export recorded task times to a CSV file.
4) Uses JSON to store task data.


## Usage

Each of these is a command you can enter into the command line tool.

Starts one or more tasks and tracks their duration using the datetime module.
```
python task_timer.py start
```
Stops a chosen task and records its duration, updating the JSON file with the runtime. 
```
python task_timer.py stop
```
Tells you what task is currently running, if there is one. 
```
python task_timer.py peek
```
Prints out a list summary of all task entries. 
```
python task_timer.py summary
```
Erases your entire timesheet. 
```
python task_timer.py clear-tasks
```
Exports the JSON file data into a CSV file to be used elsewhere. 
```
python task_timer.py transfer-to-csv
```


## Contact
isaac.dawson@student.cune.edu

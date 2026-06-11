# Log File Analyzer in Python

## Overview

This program analyzes a collection of application log messages and generates a summary report.

The application:
- Counts INFO messages
- Counts WARNING messages
- Counts ERROR messages
- Displays a log summary

The project demonstrates string processing, loops, conditional logic, and basic log analysis.

---

## Code

```python
logs = [
    "INFO: Application Started",
    "ERROR: Database Connection Failed",
    "INFO: User Logged In",
    "WARNING: Low Memory",
    "ERROR: Invalid Password",
    "INFO: User Logged Out"
]

info_count = 0
warning_count = 0
error_count = 0

for log in logs:
    if log.startswith("INFO"):
        info_count += 1
    elif log.startswith("WARNING"):
        warning_count += 1
    elif log.startswith("ERROR"):
        error_count += 1

print("Log Summary")
print("INFO:", info_count)
print("WARNING:", warning_count)
print("ERROR:", error_count)
```

---

## How It Works

1. Log messages are stored in a list
2. The program loops through each log entry
3. `startswith()` identifies the log level
4. Counters are updated accordingly
5. A final summary report is generated

---

## Example Output

```text
Log Summary
INFO: 3
WARNING: 1
ERROR: 2
```

---

## Concepts Covered

- Lists
- Loops
- String methods
- Conditional statements
- Data aggregation

---

## Why This Program?

This project introduces:

- Log analysis
- Monitoring systems
- Event classification
- Reporting and analytics

These concepts are commonly used in:

- Backend systems
- Cloud monitoring
- DevOps tools
- Security auditing
- Application support

---

## Possible Improvements

- Read logs from a text file
- Display detailed error messages
- Count unique errors
- Export reports to CSV
- Generate visual charts

---

## Author

Daily Python Practice  
Log File Analyzer

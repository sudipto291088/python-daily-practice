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



Log Summary
INFO: 3
WARNING: 1
ERROR: 2
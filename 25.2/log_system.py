from datetime import datetime


def create_log_function(type):
    def log_basic(msg):
        print(f"Log: {msg}")

    def log_with_timestamp(msg):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {msg}")

    def log_with_level(msg, level="info"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level.upper()}] {msg}")

    def log_event_with_date(event, date):
        print(f"Event: {event}, Date: {date}")

    if type == "basic":
        return log_basic
    elif type == "timestamp":
        return log_with_timestamp
    elif type == "level":
        return log_with_level
    elif type == "event":
        return log_event_with_date


# Factory function for log processing
def create_log_processor():
    def process_logs(logs, **filters):
        # Filter out logs without date/timestamp
        logs_with_date = [log for log in logs if "date" in log or "timestamp" in log]

        # Filter logs within timestamp range
        if "start_date" in filters and "end_date" in filters:
            start_date = datetime.strptime(filters["start_date"], "%Y-%m-%d")
            end_date = datetime.strptime(filters["end_date"], "%Y-%m-%d")
            logs_with_date = [log for log in logs_with_date if
                              start_date <= datetime.strptime(log.get("date") or log.get("timestamp"),
                                                              "%Y-%m-%d") <= end_date]

        # Filter logs with short msg
        if "short_msg" in filters:
            logs_with_date = [log for log in logs_with_date if len(log["msg"]) < 10]

        return logs_with_date

    return process_logs


def main():
    # Example logs
    logs = [
        {"msg": "System start", "timestamp": "2024-03-02"},
        {"msg": "Warning: low memory", "level": "warn", "timestamp": "2024-03-02"},
        {"msg": "User logged in", "date": "2024-03-02"},
        {"msg": "Short", "timestamp": "2024-03-02"}
    ]

    process_logs = create_log_processor()

    processed_logs = process_logs(logs, start_date="2024-03-01", end_date="2024-03-03", short_msg=True)
    print(processed_logs)


if __name__ == "__main__":
    main()

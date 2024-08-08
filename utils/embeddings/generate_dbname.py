import datetime

def generate_dbname():
    """Generates a filename with today's date and time."""
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{current_datetime}_db"
    return filename

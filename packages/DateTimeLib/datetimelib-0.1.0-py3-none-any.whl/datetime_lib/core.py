from datetime import datetime

def get_current_datetime() -> str:
    """إرجاع التاريخ والوقت الحالي بالثانية"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

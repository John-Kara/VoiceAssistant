import sys, datetime

current_logs = open(datetime.datetime.now().strftime("logs/%d-%m-%Y-%f.txt"), "w+")

sys.stdout = current_logs
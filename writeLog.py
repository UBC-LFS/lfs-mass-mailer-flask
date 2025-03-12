import time
import os

log_export_path = os.getenv("LOG_EXPORT_PATH") + "/"
log_export_path = log_export_path.replace("\\", "/")


def write_log(user, subject, cc, message, receivers, failedReceivers):
    time_file_str = time.strftime("%Y-%m-%d_%H-%M-%S")

    if not os.path.isdir(log_export_path):
        print("invalid export path")
        return "invalid export path"

    try:
        file_name = log_export_path + time_file_str + ".txt"

        f = open(file_name, "a")  # open file in append mode

        date_str = time.strftime("%Y/%m/%d")
        time_str = time.strftime("%H:%M:%S")

        sender_address = os.getenv("ACCOUNT_USER")
        if sender_address is None or sender_address == "":
            sender_address = os.getenv("ACCOUNT_USER_RELAY")

        message_parsed = (
            message.replace("<p>", "").replace("</p>", "").replace("<br>", "\n")
        )

        f.write("Date (YYYY/MM/DD): " + date_str + "\n")
        f.write("Time (HH:MM:SS): " + time_str + "\n\n")
        f.write("Sender: " + user + "\n")
        f.write("Sender Email: " + sender_address + "\n\n")
        f.write("Subject: " + subject + "\n")
        f.write("CC: " + cc + "\n\n")
        f.write(
            "Message: \n------------------------BEGIN_MESSAGE------------------------\n"
            + message_parsed
            + "\n-------------------------END_MESSAGE-------------------------\n\n\n"
        )

        f.write("Receivers:\n")
        for receiver in receivers:
            f.write(str(receiver) + "\n")
        f.write("\nFailed Receivers:\n")
        for failedReceiver in failedReceivers:
            f.write(str(failedReceiver) + "\n")
        f.close()
        print("log written succesfully")
        return "log written successfully"
    except Exception as e:
        print("\nError:\n" + str(e) + "\n")
        print("error writing log")
        return "error writing log"

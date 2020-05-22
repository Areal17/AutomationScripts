#!/usr/bin/env python3
import re
import operator
import csv
import sys


def read_sys_log(file_path):
    """ Parameter der Pfad und Name des log-files """
    with open(file_path) as f:
        lines = f.readlines()
        ticky_logs = get_ticky_logs(lines)
        write_error_file(ticky_logs)
        write_user_statistic_file(ticky_logs)
        f.close()


def get_ticky_logs(log_lines):
    # Error Count
    # Username INFO ERROR
    #Jan 31 14:56:35 ubuntu.local ticky: ERROR Tried to add information to closed ticket (noel)
    ticky_logs = []
    pattern = r"ticky: ([A-Z]*) ([\w' \[\]#]*) \(([\w.]*)\)$"
    for line in log_lines:
        line = line.strip()
        result = re.search(pattern, line)
        if result is not None:
            result_groups = result.groups()
            ticky_logs_dict = {"Username": result_groups[2], result_groups[0]: result_groups[1]}
            ticky_logs.append(ticky_logs_dict)
    return ticky_logs


def write_error_file(status_logs):
    """status_logs ist ein Dict mit allen Logs Error und Info """
    error_dict = {} #dict mit Fehlermeldung als key und anzahl als value
    error_file_path = "textFolder/error_message.csv"
    for status_log in status_logs:
        if "ERROR" in status_log:
            error_description = status_log["ERROR"]
            if error_description not in error_dict:
                error_dict[error_description] = 0
            error_dict[error_description] += 1
    # create csv
    with open(error_file_path, "w") as csv_file:
        # Header erzeugen
        sorted_error_list = sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True)
        fieldnames = ["Error", "Count"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for error in sorted_error_list:
            error_name, error_count = error
            #writer.writerow({fieldnames[0]: error, fieldnames[1]: error_count})
            writer.writerow({fieldnames[0]: error_name, fieldnames[1]: error_count})
        csv_file.close()


def write_user_statistic_file(status_logs):
    # name user_statistics.csv
    per_user = {}
    user_file_path = "textFolder/user_statistics.csv"
    for status_log in status_logs:
        user = status_log['Username']
        status_dict = {}
        if user not in per_user:
            status_dict["Error"] = 0
            status_dict["Info"] = 0
        else:
            status_dict = per_user[user]
        if 'ERROR' in status_log:
            status_dict["Error"] += 1
        elif 'INFO' in status_log:
            status_dict['Info'] += 1
        per_user[user] = status_dict
    with open(user_file_path, "w") as csv_file:
        fieldnames = ["Username", "INFO", "ERROR"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        sorted_user_stats = sorted(per_user.items())
        for user_stat in sorted_user_stats:
            username, user_stat_values = user_stat
            writer.writerow({fieldnames[0]: username, fieldnames[1]: user_stat_values[fieldnames[1].capitalize()], fieldnames[2]: user_stat_values[fieldnames[2].capitalize()]})
        csv_file.close()


if __name__ == "__main__":
    read_sys_log(sys.argv[1])
from my_database_functions import *


def fetch_and_send_info_data():
    read_info_file = open("C:/Users/Nathaniel_inc/Documents/DreyB53/student_info.csv", mode = "r")
    info_file_header = read_info_file.readlines(1)
    info_data = read_info_file.readlines()



    refined_info_data = [entry.rstrip("\n") for entry in info_data]

    for entry_info_data in refined_info_data:
        extracted_data = entry_info_data.split(",")
        write_info_data(extracted_data[1], extracted_data[2], int(extracted_data[3]))


def fetch_and_send_record_data():
    read_record_file = open("C:/Users/Nathaniel_inc/Documents/DreyB53/student_rec.csv", mode = "r")
    record_file_header = read_record_file.readlines(1)
    record_data = read_record_file.readlines()

    refined_record_data = [entry.rstrip("\n") for entry in record_data]

    for entry_record_data in refined_record_data:
        extracted_data = entry_record_data.split(",")
        write_records_data(int(extracted_data[0]), extracted_data[1], int(extracted_data[2]))





# fetch_and_send_info_data()
fetch_and_send_record_data()
#!/usr/bin/env python3
import os
import sys
import csv


def remove_hidden_files(files):
    cleanFiles = []
    for file in files:
        if not file.startswith("."):
            cleanFiles.append(file)
    return cleanFiles


def get_files(root_path):
    """Liefert alle Dateien inklusive der Datein in den Subfoldern"""
    file_list = []
    with os.scandir(root_path) as root_dir:
        for file_object in root_dir:
            if file_object.name.startswith('.'):
                continue
            if file_object.is_file():
                file_list.append(file_object)
            elif file_object.is_dir():
                sub_files = get_files(file_object.path)
                file_list.extend(sub_files)

    return file_list


def get_rows_in_csv(absolut_path):
    """liefert die Anzahl der Einträge in CSV-Datei. Parameter ist der Pfad ohne Datei"""
    content_dict = []
    complete_path = os.path.join(absolut_path,"images.csv")
    if os.path.exists(complete_path):
        with open(complete_path, "r") as csv_file:
            reader = csv.DictReader(csv_file) # ggf noch delimiter angeben.
            content_dict = list(reader) #in array umwandeln
            csv_file.close()
    return content_dict
        

def number_of_new_files(file_object_list,csv_file):
    """ermittelt die Zahl der Dateien und vergleicht sie mit der Zahl in der CSV Datei. Ist die Zahl größer als in der CSV Datei, dann gibt es neue Dateien"""
    rows_in_csv = get_rows_in_csv(csv_file)
    #print("In der CSV-Datei: {} im Ordner: {}".format(len(rows_in_csv), len(file_object_list)))
    return len(file_object_list) - len(rows_in_csv)


def get_file_date(file_object):
    return os.path.getmtime(file_object.path)

def get_new_files(csv_file_path, file_object_list):
    objects_in_csv = get_rows_in_csv(csv_file_path)
    objects_set = set(objects_in_csv)
    new_files = objects_set.difference_update(file_object_list) # entfernt in Object_set die Elemente,die auch in file_object_list stehen
    return new_files



def write_files_to_csv(file_list,csv_file_path):
    """ csv_file_path ist der komplete Pfad zur CSV-Datei """
    #file_list ist Liste mit File-Objekten nicht deren Namen
    field_keys = ["Änderungsdatum","Pfad","Datei","Beschreibung"]
    # CSV Datei anlegen
    if os.path.exists(csv_file_path) == False:
        os.mkdir(csv_file_path)
        complete_path = os.path.join(csv_file_path, "images.csv")
        with open(complete_path,"w") as csv_file:
            writer = csv.DictWriter(csv_file,fieldnames=field_keys)
            writer.writeheader()
            for file in file_list:
                writer.writerow({field_keys[0]: get_file_date(file), field_keys[1]: file.path, field_keys[2]: file.name, field_keys[3]: ""})
            csv_file.close()


def update_files_to_csv(new_files_list,csv_file_path):
    # new_files_list: muss liste aus file_objekten sein!
    """hängt neue Dateien an CSV. csv_file_path ist der komplette Pfad incl. Dateiname"""
    complete_path = os.path.join(csv_file_path,"images.csv")
    try:
        with open(complete_path, "w+") as csv_file:
            field_keys = ["Änderungsdatum","Pfad","Datei","Beschreibung"]
            writer = csv.writer(csv_file)
            row = {}
            for new_file in new_files_list:
                row[field_keys[0]] = get_file_date(new_file)
                row[field_keys[1]] = new_file.path
                row[field_keys[2]] = new_file.name
                row[field_keys[3]] = ""
                writer.writerow(row)
            csv_file.close()
    except:
        print("unable to open file")


def main():
    if sys.argv[1]:
        dir_path = sys.argv[1]
        file_objects = get_files(dir_path)
        csv_file_path = os.path.join(dir_path,"db")
        if not os.path.exists(os.path.join(csv_file_path,"images.csv")):
            write_files_to_csv(file_objects,csv_file_path)
        else:
            csv_file = os.path.join(csv_file_path,"images.csv")
            if number_of_new_files(file_objects,csv_file) > 1:
                # noch ermitteln, welche file neu sind
                new_files = get_new_files(csv_file_path,file_objects)
                update_files_to_csv(new_files,csv_file_path)
                print("Neue Dateien vorhanden")
    else:
        print("Pfadname angeben")
        sys.exit(1)


if __name__ == "__main__":
    main()
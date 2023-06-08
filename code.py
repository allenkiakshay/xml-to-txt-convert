import csv
import os
import xml.etree.ElementTree as ET

def xml_to_csv(file_path, file_name) -> None:
    tree = ET.parse(file_path)
    root = tree.getroot()

    with open(file_name, 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        headers = (child.tag for child in root[0])
        writer.writerow(headers)
        num_records = len(root)

        for i in range(num_records):
            rec = (child.text for child in root[i])
            writer.writerow(rec)


    # with open(s_name, 'r') as in_f, open(s_name, 'w') as out_f:
    #     content = in_f.read().replace(',',' ')
    #     out_f.write(content)



file_path = './xml trans/4oLp3bc9OSJbDrwM 1.xml'
file_name = os.path.splitext(os.path.basename(file_path))[0]
file1_name = ("./CSV Files/" + str(file_name) + ".csv")

xml_to_csv(file_path, file1_name)


s_name = "./" + file1_name
s1_name = "./Text Files/" + str(file_name) + ".txt"

with open(s_name, 'r', encoding='utf-8') as in_f, open(s1_name, 'w', encoding='utf-8') as out_f:
    content = in_f.read().replace(',',' ')
    out_f.write(content)
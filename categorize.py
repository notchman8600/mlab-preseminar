import pandas as pd
import os

ROOT_PATH = "./bmw/result"
# ROOT_PATH = "./toyota/result"


def categorize(filename):
    categorized_dict = {}
    sorted_dict = {}
    df = pd.read_csv(
        filename,
        chunksize=300,
        names=(
            "link",
            "folder",
            "filename"),
        header=1)
    for r in df:
        for row_index, row in r.iterrows():
            if len(row) != 3:
                continue
            if row[1] not in categorized_dict:
                categorized_dict[row[1]] = []
            categorized_dict[row[1]].append(
                "{},{},{}\n".format(row[0], row[1], row[2]))
    for key in categorized_dict.keys():
        make_path = ROOT_PATH + "/" + key
        sorted_dict[key] = len(categorized_dict[key])
        if not os.path.isdir(make_path):
            os.makedirs(make_path)
        with open(make_path + "/result.csv", 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(categorized_dict[key])
    print()
    with open(ROOT_PATH + "/status.txt", 'w', encoding='utf-8', newline='\n') as f:
        for value in sorted(sorted_dict.items(), key=lambda x: x[1]):
            f.write("{},{}\n".format(value[0], value[1]))


# categorize("toyota_image_dataset_v2/toyota_links.csv.out.result")
categorize("bmw_image_dataset_v2/BMW_links.csv.out.result")

import pandas as pd
import requests
import concurrent.futures


def check_link(filename, name):
    toyota_cnt = sum([1 for _ in open(filename)])
    execute_cnt = 0.0
    error_cnt = 0.0
    print("Total: {}".format(toyota_cnt))
    df = pd.read_csv(
        filename,
        chunksize=300,
        names=(
            "link",
            "folder",
            "filename"),
        header=1)
    write_f = open(filename + ".result", mode='w')
    for r in df:
        for row_index, row in r.iterrows():
            execute_cnt = execute_cnt + 1.0
            print("{} Progress: {:.5g}%".format(
                name, 100.0 * (execute_cnt / toyota_cnt)))
            if len(row) != 3:
                continue
            try:
                r = requests.get(row[0], timeout=5)
                if r.status_code == 200:
                    # print(row[2])
                    write_f.write("{},{},{}\n".format(row[0], row[1], row[2]))
            except BaseException:
                error_cnt += 1.0
                # print("some errors has occured")
                pass
    print("Error count of {}'s data: {} {:.5g}".format(
        name, error_cnt, 100.0 * (error_cnt / toyota_cnt)))
    write_f.close()


def execute_toyota():
    check_link("toyota_image_dataset_v2/toyota_links.csv.out", "Toyota")


def execute_bmw():
    check_link("bmw_image_dataset_v2/BMW_links.csv.out", "BMW")


if __name__ == "__main__":
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
    executor.submit(execute_toyota)
    executor.submit(execute_bmw)

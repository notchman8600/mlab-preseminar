# リンクにカンマが含まれるゴミデータを除去するプログラム


def cleansing(filename):
    f = open(filename)
    write_f = open(filename + ".out", mode='w')
    print(type(f))
    for s_line in f:
        if ',' not in s_line:
            write_f.write(s_line)
    f.close()
    write_f.close


# cleansing("toyota_image_dataset_v2/toyota_links.csv")
cleansing("bmw_image_dataset_v2/BMW_links.csv")

import random
with open("result.csv") as f:
    lines = f.readlines()
    lines_sorted = random.sample(lines,len(lines))
    with open("result.out.csv", 'w', encoding='utf-8', newline='\n') as write_f:
            write_f.writelines(lines_sorted)

path = '/home/phantomfeed/PycharmProjects/PythonAdvanced/mod2/output_file.txt'


def get_summary_rss(filename):
    with open(filename) as output_file:
        lines = output_file.readlines()[1:]
    summary_rss = 0
    for line in lines:
        columns = line.split()
        summary_rss += int(columns[5])
    size = ['B', 'KiB', 'MiB']
    i = 0
    while summary_rss >= 1024 and i < 3:
        summary_rss = round(summary_rss / 1024)
        i += 1
    return f'{summary_rss} {size[i]}'


if __name__ == '__main__':
    print(get_summary_rss(path))

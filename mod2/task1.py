def get_summary_rss(filepath):
    with open(filepath) as output_file:
        lines = output_file.readlines()[1:]
    summary_rss = 0
    for i in lines:
        cols = i.split()
        summary_rss += int(cols[5])
    size = ['B', 'KiB', 'MiB']
    x = 0
    while summary_rss >= 1024 and x < 3:
        summary_rss = round(summary_rss / 1024)
        x += 1
    return f'{summary_rss} {size[x]}'


path = '/home/phantomfeed/PycharmProjects/PythonAdvanced/mod2/output_file.txt'
if __name__ == '__main__':
    print(get_summary_rss(path))

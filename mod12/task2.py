import os


def process_count(username: str) -> int:
    output = os.popen(f"ps -u {username} -o pid=").read()
    count = len(output.strip().split('\n'))
    return count


def total_memory_usage(root_pid: int) -> float:
    output = os.popen(f"ps -o pid= --ppid {root_pid}").read()
    total_memory = float(os.popen(f"ps -o rss= --pid {root_pid} ; ps -o rss= --ppid {root_pid} | awk '{{s+=$1}} END {{print s}}'").read().strip()) / 1024
    return total_memory



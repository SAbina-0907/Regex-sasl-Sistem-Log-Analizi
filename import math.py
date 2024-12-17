import re
import csv

# Log faylını oxuyuruq
with open('access_log.txt', 'r') as file:
    log_lines = file.readlines()

# Müntəzəm ifadə nümunəsi
log_pattern = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d{3}) \S+'
)

# 404 səhvləri olan URL-ləri toplayırıq
error_urls = []

for line in log_lines:
    match = log_pattern.match(line)
    if match and match.group('status') == '404':
        error_urls.append(match.group('url'))

# Nəticələri CSV faylına yazırıq
with open('404_errors.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['URL'])
    for url in error_urls:
        csv_writer.writerow([url])



import os

process = os.popen("ipconfig")
results = str(process.read())
marker = results.find('IPv4')
print(results[marker:marker + 50].splitlines()[0])
input()
import re

CSVSPLIT = re.compile(r",\s*")
def csvstr2kvlist(csvstr, header=True):
    csvstr = csvstr.strip().splitlines()
    if not header:
        return [val.strip()
                for val in CSVSPLIT.split(line)
                for line in csvstr]
    keys = [key.strip() for key in CSVSPLIT.split(csvstr[0])]
    return [dict(zip(keys, [val.strip()
        for val in CSVSPLIT.split(line)]))
        for line in csvstr[1:]]

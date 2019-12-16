import sys
import re

''' Main entry point '''
if __name__ == '__main__':
    # Check Command line arguments
    if not(len(sys.argv) == 3):
        raise Exception(
            'Not enough command line arguments! Use "python test.py CONFIGFILE PROCESSFILE" command!')

    configfile = sys.argv[1]
    processfile = sys.argv[2]

    # Reading config file
    lines = []
    try:
        lines = open(configfile, 'r').readlines()
    except IOException:
        raise Exception('Error reading configuration file (%s)!' % configfile)

    # Parsing config
    rules = {}
    for line in lines:
        opts = re.split(r'=', line.rstrip())
        if not(len(opts) == 2):
            raise Exception(
                'Wrong pair (%s) in configuration file!' % (line.rstrip()))
        rules[opts[0]] = opts[1]

    # Reading process file
    lines = []
    try:
        lines = open(processfile, 'r').readlines()
    except IOException:
        raise Exception('Error reading processing file (%s)!' % processfile)
    import pprint

    # Reverse process lines
    lines.reverse()
    # Apply rules to each line
    for line in lines:
        for rule in rules:
            line = line.rstrip()
            line = re.sub(rule, rules[rule], line)
        # Output processed line
        print(line)

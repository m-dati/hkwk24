#!/usr/bin/python3
"""
Project for hack week 2024:
detect secrets/private data in perl code files and other types
"""

import sys
import argparse
import re
from pathlib import Path

# Defines a regular expression pattern to match secret codes or private keys
from secret_patterns import __secret_patterns__

# default name for out file
OFILE = 'out.log'
# list init.
lines = []

def code_inspection(rows, enabled, search_pattern, desc, also_comments):
    """
    Check search_pattern in each line of list
    """
    port = 1
    n = 0
    # Loop through each line in the file and search for matches of the pattern
    for line in rows:
        n +=1
        # Find all matches of the pattern on the current line
        match = [ found for found in re.findall(search_pattern, line) if found and enabled]
        # Report matches:
        if match:
            # print warning message once only at beginning:
            if port:
                txt = ' '
                print("---", file=fout)
                if args.patterns:
                    txt = " with pattern:\n\"" + search_pattern + "\" "
                print(f'Warning! {desc} detected{txt}in:', file=fout)
                port = 0
            # matched into a comment
            comment = re.search(r'\#.*' + search_pattern, line)
            # print result
            if not comment or (comment and also_comments):
                print(f'L{n}: {line.strip()}', file=fout)

# *****************
# *** Main code ***
# *****************

# Prepare input check:
parser = argparse.ArgumentParser(
    description='Detect private or secret data in a file, using patterns.')
parser.add_argument('--inputfile','-i',
    help='File name to inspect for secrets')
parser.add_argument('--outputfile','-o', default='stdout', action='store', nargs='?', const=OFILE,
    help='print results to a file - Default stdout / Default -f: out.log')
parser.add_argument('--comments','-c', default=False, action='store_true',
    help='Checks secrets also in comments.')
parser.add_argument('--patterns','-p', default=False, action='store_true',
    help='Print also secrets pattern matched, during run.')
parser.add_argument('--Patterns','-P', default=False, action='store_true',
    help='Print full secrets pattern list, even whithout run options.')

args = parser.parse_args()

# Open the input file for reading. Input file mandatory
fname = args.inputfile

# output file
if args.outputfile == 'stdout':
    fout = sys.stdout
else:
    if args.outputfile != OFILE:
        OFILE = args.outputfile
    fout = open(OFILE, 'w', encoding='utf-8')

if fname and Path(fname).exists():
    # Open the input file for reading
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()

if args.Patterns:
    for p in __secret_patterns__:
        print(f'{p[0]} "{p[1]}" "{p[2]}"', file=fout)

if len(lines) == 0:
    # Error handling: missing or empty file
    if not args.Patterns:
        parser.print_help()
    sys.exit(1)

# check empty patterns
patterns = [ p for p in __secret_patterns__ if (p[0] and p[1]+p[2]) ]

if len(patterns) == 0:
    if not args.Patterns:
        print("No secrets' pattern available to match.")
    sys.exit(1)


#*******************
# Elaboration start:
#
print(f"\nSensible data inspection in file: {args}", file=fout)
# check all patterns
for pattern in patterns:
    code_inspection(lines, pattern[0], pattern[1], pattern[2], bool(args.comments))
# loop end

print("\nInspection end.", file=fout)
# end

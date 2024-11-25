#!/usr/bin/python3
# project hackweek 2024 :
#   secrets/private leacks in perl code files:
################################

from sys import stdout
from pathlib import Path
import argparse
import re

from secret_patterns import __secret_patterns__

fout = None
outfile = 'out.log'
lines = []
# Define a regular expression pattern to match secret codes or private keys
# (to be changed as input parameter)
#patterns = [
#    [r'(\s*=\s*)[\"\']RSA-([0-9]+)', "potential RSA code"],
#    [r'(\s*=\s*)[\'\"]AES-([0-9]+)', "potential AES code"],
#    [r'\s*(?:my|our)\s*[a-z_]*(SCC_REGCODE|AUTH_TOKEN|password|secret|private|api_key|token|ssh_private_key)[a-z_]*\s*[=]?',"variables with potential secret keywords"],
#    [r'\s*[=]?\s*[a-z_]*(SCC_REGCODE|AUTH_TOKEN|password|secret|private|api_key|token|ssh_private_key)[a-z_]*\s*[=]?',"pattern matching potential reserved keywords"],
#    [r'\s*(?:my|our)\s*[a-z_]*(email|address|sex)[a-z_]*\s*[=]?',"variables with potential privacy-sensible keywords"],
#    [r'\s*[=]?\s*[a-z_]*(email|address|sex)[a-z_]*\s*[=]?',"pattern matching potential privacy-sensible keywords"],
#]

# check pattern in each line of list
def code_inspection(rows, enabled, pattern, desc, also_comments):
    port = 1
    n = 0
    # Loop through each line in the file and search for matches of the pattern
    for line in rows:
        n +=1
        # Find all matches of the pattern on the current line
        match = [ found for found in re.findall(pattern, line) if found and enabled]
        # Report matches: 
        if match:
            # print warning message once only at beginning:
            if port:
                p = ' '
                print("---", file=fout)
                if args.patterns: p = " with pattern:\n\"" + pattern + "\" "
                print(f'Warning! {desc} detected{p}in:', file=fout)
                port = 0
            # matched into a comment
            comment = re.search(r'\#.*' + pattern, line)
            # print result
            if not comment or (comment and also_comments):
                
                print(f'L{n}: {line.strip()}', file=fout)
# function end
#
#############################
#
# * Main code *
#
# input check
parser = argparse.ArgumentParser(description='Detect private or secret data in a file, based on predefined patterns.')
parser.add_argument('--inputfile','-i', help='File name to inspect for secrets')
parser.add_argument('--outputfile','-o', default='stdout', action='store', nargs='?', const=outfile, help='print results to a file - Default stdout / Default -f: out.log')
parser.add_argument('--comments','-c', default=False, action='store_true', help='Checks secrets also in comments.')
parser.add_argument('--patterns','-p', default=False, action='store_true', help='Print also secrets pattern matched, during run.')
parser.add_argument('--Patterns','-P', default=False, action='store_true', help='Print full secrets pattern list, even whithout run options.')

args = parser.parse_args()

# Open the input file for reading. Input file mandatory
fname = args.inputfile

if args.Patterns:
    for p in __secret_patterns__: print(f'{p[0]} "{p[1]}" "{p[2]}"')

if fname and Path(fname).exists():
    # Open the input file for reading
    with open(fname, 'r') as f:
        lines = f.readlines()

if len(lines) == 0:
    # Error handling: missing or empty file
    if not args.Patterns: parser.print_help()
    exit(1)

# check empty patterns
patterns = [ p for p in __secret_patterns__ if (p[0] and p[1]+p[2]) ]

if len(patterns) == 0:
    if not args.Patterns: print("No secrets' pattern available to match.")
    exit(1)

# output file
if args.outputfile == 'stdout':
    fout = stdout
else:
    if args.outputfile != outfile:
        outfile = args.outputfile
    fout = open(outfile, 'w')

# comments option
if args.comments:
    include_comments = True
else:
    include_comments = False
#
#  ************
#
print(f"\nSensible data inspection in file: {args}", file=fout)
# check all patterns
for pattern in patterns:
    code_inspection(lines, pattern[0], pattern[1], pattern[2], include_comments)
# loop end

print("\nInspection end.", file=fout)

fout.close
# end

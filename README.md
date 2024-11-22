# hkwk24

# Description

This project started during the **SUSE Hack week 2024** [prj#1](https://hackweek.opensuse.org/24/projects/bot-to-identify-reserved-data-leak-in-local-files-or-on-publishing-on-remote-repository).

Main scope of this project is creation of a tool to detect possible reserved or generally protected data, in source code files, mainly perl-code, basically used or stored in public environents or reporitories.

In other words, prevention of disclosure or leaking of reserved informations in archives exposed on public repository, like github.com. 

The above definition of reserved or protected may vary, depending on the context: sometime secret keys or password are stored in data or configuration files or hardcoded in source code and depending on the scope of the archive or the level of security, it can be either wanted, permitted or not at all.

Also possible target could be some personal information, like those subject to GDPR.

First target here are program varibles containing secrets like **registration** keys or **passwords** or **tokens**, that we want to detect and manage either locally or in C.I. pipelines.

The patterns are stored, into a separate module `secret_patterns.py`, that shall be ready to be loaded at run time.
Each pattern is a list of: enabled, pattern, alert-message. The integer `enabled` can be set ot 0 to exclude the pattern in the same row during a file check.


## Goals

- Detection:
  - Local detection: detect secret words present in local files;
  - Remote detection: detect secrets in files, in pipelines, going to be transferred on a remote repository, i.e. via `git push` [T.B.D];

- Reporting:
  - report the result of detection on stderr and/or log files, noticed excluding the secret values.

- Action:
  - Manage the detection, by either deleting or masking the impacted code or deleting/moving the file itself or simply notify it [T.B.D].


## Usage

**chksecret.py** 
```
usage: chksecret.py [-h] [--inputfile INPUTFILE] [--outputfile [OUTPUTFILE]] [--comments] [--patterns] [--Patterns]

Detect private or secret data in a file, based on predefined patterns.

options:
  -h, --help            show this help message and exit
  --inputfile INPUTFILE, -i INPUTFILE
                        File name to inspect for secrets
  --outputfile [OUTPUTFILE], -o [OUTPUTFILE]
                        print results to a file - Default stdout / Default -f: out.log
  --comments, -c        Checks secrets also in comments.
  --patterns, -p        Print also secrets pattern matched, during run.
  --Patterns, -P        Print full secrets pattern list, even whithout run options.
```


## Project components

README.md: This basic features description.  
chksecret/chksecret.py: The executable python script of this project.  
chksecret/secret_patterns.py: The module containing the list of secrets patterns to match  
chksecret/:
  tests/test1.pl: A simple perl test file  
  tests/out#.log: output examples.


## Tests

A file `tests/test1.pl` is available for basic tests and can be changed and used to run pattern matching.
Some out#.log are tests results.

Examples:

in checsecret folder, run:

chksecret.py -i tests/test1.pl: run the test, printing on stdout.  
chksecret.py -i tests/test1.pl -c: run the test on the comments too  
chksecret.py -i tests/test1.pl -c -o tests/out2.log: run the test also on the comments and save output on a file  
chksecret.py -i tests/test1.pl -p: run the test also printing matching the pattern  
chksecret.py -i tests/test1.pl -c -P: run the test, printing on top the full list of pattern  
chksecret.py -P: Print only the full patterns list present into module `secret_patterns.py`. 


[T.B.D = to be done.]
# Hack week 2024 - Personal project n.1

- Author: Maurizio Dati (SUSE Italy)
- Reference: mdati@suse.com
- Title: Secrete or personal data exposure detection in code files.


## Description

This project started during the **SUSE Hack week 2024** [prj#1](https://hackweek.opensuse.org/24/projects/bot-to-identify-reserved-data-leak-in-local-files-or-on-publishing-on-remote-repository).

Main scope is creation of a tool to detect possible reserved or generally protected data, in source code files, mainly perl-code, basically used or stored in public environments or reporitories.

In other words, notification and possibly prevention of disclosure or leaking of reserved informations in archives exposed on public repository, like github.com. 

The above definition of *reserved* and *protected* may vary, depending on the context: sometime secret keys or password are stored in data or configuration files or hardcoded in source codes and depending on the scope of the archive or the level of security, it can be either wanted, permitted or not at all.

Also possible target could be some personal information, like data subject to GDPR.

First target here are program varibles or expressions containing secrets like **registration** keys or **passwords** or **tokens**, that we want to detect and manage either locally or in C.I. pipelines, mainly in perl code modules.

The list of all patterns to match are stored, into a separate module `secret_patterns.py`, that shall be ready to be loaded at run time, preferably in the same folder of the main script, and activated by a proper flag.

Each pattern is itself an ordered array of: *enabled*, *pattern*, *alert-message*:
- `enabled`: a boolean 0/1: can be set ot 0 to exclude the related pattern during a file check run.
- `pattern`: a string contining a regexpr (python) to match, dedicated to a desired sequence to match;
- `alert-message`: a text sentence, describing the type of detection, printed at runtime when pattern matched.


## Goals

- Detection:
  - local detection: detect secret words/expressions present in a file, like a perl module or other type;
  - remote detection: detect secrets in files, in pipelines, going to be saved on a remote repository, i.e. via `git push` [T.B.D];

- Reporting:
  - report the result of detection on stderr and/or log file; 
  - report the result excluding the secret values [T.B.D];

- Action:
  - manage the detection, possibly: 
    (a) delete or mask the impacted code, into the impacted file [T.B.D]; 
    (b) delete or move the impacted file [T.B.D].


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


## Project structure

- README.md: This basic features description.  
- TESTS.md: Tests description.  
- `chksecret/`:  
  - chksecret.py: The executable python script of this project.  
  - secret_patterns.py: The module containing the list of secrets patterns to match  
  - `tests/`:  
    - test1.pl: A simple perl test file  
    - out#.log: output log examples.


## Tests

Refer to the description in [TESTING](TESTS.md)


[T.B.D = to be done.]
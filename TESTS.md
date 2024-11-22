# TESTING

## Test structure

A subfolder `tests/` contains a perl file `test1.pl`, available for basic verification runs, that can be changed and used to run pattern matching.

Some `out#.log` logs are exampres of tests results.


- Test examples:

Enter `chksecret/` folder, then run:
```
chksecret.py -i tests/test1.pl                         # run a test, printing on stdout.
chksecret.py -i tests/test1.pl       -o                # run a test sending output to default out.log file.
chksecret.py -i tests/test1.pl       -o tests/out1.log # run a test sending output to a file.
chksecret.py -i tests/test1.pl -c    -o tests/out2.log # run a test on the comments too, to a file.
chksecret.py -i tests/test1.pl    -p -o tests/out3.log # run a test, printing each matching pattern expression, to a file.
chksecret.py -i tests/test1.pl -c -p -o tests/out4.log # run a test, on comments too, also printing each matching pattern expression, to a file.
chksecret.py -i tests/test1.pl -P    -o tests/out5.log # run a test, printing on top the full patterns list, to a file.
chksecret.py -i tests/test1.pl -P -p -o tests/out6.log # run a test, also printing on top the full patterns list and each matching pattern expression, to a file.
chksecret.py                   -P;                     # print on stdout the full patterns list only, from module `secret_patterns.py`.

```

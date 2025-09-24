# Python test drive utility

## A nifty utility to test things.

 The test case file drives a send / expect engine. The expect is then evaluated and
the result is printed in a green colored 'OK' or a red colored 'ERR'.

    ./testvdrive.py testcase.txt

If you installed from pip, use:

    testvdrive testcase.txt

The test case file contains the test instructions, one line per test. The format:

    #   Context_string  Send_string     Expect_string   Find/Compare
    #   --------------  -----------     -------------   ------------
    #    for the user   what to test    what to expect  True if Find


### Example test cases:

    [ "Echo Command", "", "", True],                # NOOP
    [ "Test ls", "ls", "Make", True],               # Do we have a Make file
    [ "DF command", "df", "blocks", "regex" ],      # Search regex
    [ "DF mregex", "df", ".*blo",  "mregex" ],      # Match regex

### The output of example test cases (colored in terminal):

    Echo Command     	 OK
    Test ls          	 OK
    DF command       	 OK
    DF mregex        	 OK

### Help from command line:

     usage: testvdrive [-h] [-V] [-o] [-A] [-v] [-d DEBUGLEV] [-l FILL] [-s]
                      [test_cases ...]

    Test with send/expect by executing sub commands from test case scripts.

    positional arguments:
      test_cases            Test case file names to execute

    options:
      -h, --help            show this help message and exit
      -V, --version         Show version number
      -o, --outp            Show communication with program
      -A, --info            Show testcase file format info
      -v, --verbose         increase verbocity (Default: none)
      -d DEBUGLEV, --debug DEBUGLEV
                            Debug value (0-9). Show working info. Default: 0
      -l FILL, --fill FILL  Fill info string to lenght. Default: 16
      -s, --show_case       Show test case file(s).

    For info on TestCase File Format use -A option. The file 'testcase.txt' is
    executed by default.

## Git

    The source can be found on:

        https://github.com/pglen/testvdrive

// EOF

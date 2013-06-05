tmuxinator
==========

View your running tmux sessions in a browser.

Requires: Python 2.6/2.7, Flask, Ansi2html and of course tmux.

To install and run:

1. use virtualenv, if preferred
2. pip install -r requirements.txt
3. ./tmux.py
4. run some tmux sessions and screens

Better install instructions and running under Passenger yet to come.
 
Security
--------

None at the moment, except that it's read-only. For real access, use ssh. Tmuxinator was conceived as a monitoring tool -
use it to look at htop, running server logs, script output, hardware readouts. Run it behind a forwarding proxy (e.g. NginX), and
restrict access from there.

Features and non-features
-------------------------

* grabs tmux output from sessions belonging to the same user it runs as
* only local sessions, although it's not hard to run tmux over ssh and grab remote ones
* works on pane level, so your nicely split tmux windows will be dismantled into individual panes
* color support requires tmux 1.8, and is somewhat flaky (due to the underlying ansi2html library)
* assumes everything's UTF-8 (then again, you should too)
* bare and ugly - no CSS was used
* no configuration whatsoever: "use the source, Luke"

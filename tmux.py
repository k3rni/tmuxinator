#! /usr/bin/env python
# encoding: utf-8

from flask import Flask, render_template, url_for
import json, subprocess, re 
from ansi2html import Ansi2HTMLConverter

app = Flask(__name__)
color_support = False

PANE_INFO_RX = re.compile(r'(?P<session>\w+):(?P<window>\w+).(?P<pane>\w+): \[(?P<width>\d+)x(?P<height>\d+)\]')
def parse_pane_info(line):
  match = PANE_INFO_RX.match(line)
  if match:
    return match.groupdict()

def determine_color_support():
  major, minor = [int(x) for x in subprocess.check_output('tmux -V', shell=True).split()[-1].split('.')]
  if major == 1 and minor >= 8:
    return True
  elif major > 1:
    # projecting the future
    return True
  else:
    return False


def get_tmux_panes():
   output = subprocess.check_output('tmux list-panes -a', shell=True).split('\n')
   return filter(None, [parse_pane_info(row) for row in output])

@app.route('/')
def index():
  return render_template('index.html', static=lambda filename: url_for('static', filename=filename))

@app.route('/active_panes.json')
def active_panes():
  return json.dumps(get_tmux_panes())

@app.route('/pane/<name>')
def read_pane(name):
  if color_support:
    return Ansi2HTMLConverter().convert(subprocess.check_output('tmux capture-pane -t %s -e -b 0; tmux save-buffer -b 0 -' % name, shell=True).decode('utf-8'))
  else:
    return "<pre>%s</pre>" % subprocess.check_output('tmux capture-pane -t %s -b 0; tmux save-buffer -b 0 -' % name, shell=True)

if __name__ == "__main__":
  app.debug = True
  color_support = determine_color_support()
  app.run()

#! /usr/bin/env python
# encoding: utf-8

from flask import Flask, render_template, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', static=lambda filename: url_for('static', filename=filename))

@app.route('/active_panes.json')
def active_panes():
  return json.dumps(get_tmux_panes())

@app.route('/pane/<name>')
def read_pane(name):
  if name == 'foo':
    return 'Spierdalaj'
  elif name == 'bar1':
    return 'Bah'
  else:
    return 'No such pane'

if __name__ == "__main__":
  app.debug = True
  app.run()

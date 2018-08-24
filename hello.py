# -*- coding: utf-8 -*-
# https://qiita.com/ymgn_ll/items/96cac1dcf388bc7a8e4e

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

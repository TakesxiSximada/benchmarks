#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse
from flask import Flask

app = Flask(__name__)


@app.route('/')
def benchmark():
    return "Benchmarking..."


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=8888, type=int)
    args = parser.parse_args(argv)
    app.run(host='localhost', port=args.port)

if __name__ == '__main__':
    main()

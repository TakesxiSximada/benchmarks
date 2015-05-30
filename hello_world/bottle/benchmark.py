#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse
from bottle import (
    run,
    route,
    default_app,
    )


@route('/')
def benchmark():
    return 'Benchmarking...'


application = default_app()


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=8888, type=int)
    args = parser.parse_args(argv)

    run(host='0.0.0.0', port=args.port)

if __name__ == '__main__':
    main()

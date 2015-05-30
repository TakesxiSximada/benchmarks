#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse
from collections import OrderedDict
import lxml.etree


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('result')
    args = parser.parse_args(argv)

    with open(args.result, 'rt') as fp:
        tree = lxml.etree.HTML(fp.read())
        table = tree.xpath('//table')[0]
        data = OrderedDict()
        for tr in table.xpath('tr')[:14]:
            key = tr.xpath('th/text()')[0].strip(':')
            value = tr.xpath('td/text()')[0].strip(':')
            data[key] = value

        for key, value in data.items():

            print('{}: {}'.format(key, value))


if __name__ == '__main__':
    main()

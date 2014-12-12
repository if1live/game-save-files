#-*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import easylinker
import sys

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        filename = easylinker.to_unicode(filename)
        easylinker.run(filename)
    else:
        msg = 'Usage: {} <metadata>'.format(sys.argv[0])
        print(msg)

if __name__ == '__main__':
    main()

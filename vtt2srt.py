# -*- coding: utf-8 -*-
#encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re

def vtt2srt(fn_in, fn_out):
    with open(fn_in,'r') as fin, open(fn_out,'w') as fout:
        line_number = 0
        for line in fin:
            if line_number >= 10:
                break
            print line

def main():
    fn_in = ''
    fn_out = ''

    argv = sys.argv
    if len(argv)>1 :
        fn_in = argv[1]
        if len(argv)>=3 :
            fn_out = argv[2]
        else:
            fn_out = fn_in.replace('.vtt', '.srt')
    else:
        print '''Usages:
            vtt2srt.py vtt_file [srt_file_out]
            '''
        sys.exit(0)

    vtt2srt(fn_in, fn_out)

if __name__ == '__main__':
    main()

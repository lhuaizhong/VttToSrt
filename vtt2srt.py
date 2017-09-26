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
            #print '>',line
            r = re.findall(r'(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})', line)
            if r:
                line_number += 1
                fout.write('%d\n' % line_number)
                fout.write('%s --> %s\n' % (r[0][0].replace('.',','), r[0][1].replace('.',',')))
            else:
                # Content
                line = re.sub(r'<.+?>', '', line)
                if line_number:
                    fout.write(line)

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

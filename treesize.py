
import os, sys
trace  = lambda *pargs, **kargs: None    # or print or report
error  = lambda *pargs, **kargs: print(*pargs, file=sys.stderr, **kargs)
report = lambda *pargs, **kargs: print(*pargs, file=reportfile, **kargs)
prompt = lambda text: input(text + ' ')
reportfile = sys.stdout   # reset in main or callers as needed


def treesize(root, alldirs, allfiles, counts):
    """
    sum and return all space taken up by root (all its files + subdirs);
    record sizes by pathname in-place in alldirs+allfiles: [(path, size)];
    also tally dir/folder counts in-place in counts: [numdirs, numfiles]; 
    """
    sizehere = 0
    try:
        allhere = os.listdir(root)
    except:
        allhere = []
        error('Error accessing dir (skipped):', root)   # e.g., recycle bin

    for name in allhere:
        path = os.path.join(root, name)

        if os.path.islink(path):
            trace('skipping link:', path)   # [1.1]

        elif os.path.isfile(path):
            trace('file:', path)
            counts[1] += 1
            filesize = os.path.getsize(path)
            allfiles.append((path, filesize))
            sizehere += filesize
            
        elif os.path.isdir(path):
            trace('subdir', path)
            counts[0] += 1
            subsize = treesize(path, alldirs, allfiles, counts)
            sizehere += subsize

        else:
            error('Unknown file type (skipped):', path)   # fifo, etc.

    alldirs.append((root, sizehere))
    return sizehere


def genreport(toproot, totsize, alldirs, allfiles, counts):
    """
    print report to file, using commas and uniform-widths for numbers;
    caller should first set reportfile global unless routing to stdout;
    """
    report('\nTotal size of {}: {:,}'.format(toproot, totsize))
    report('    in {:,} dirs and {:,} files'.format(*counts))

    for (title, allitems) in [('Directories', alldirs), ('Files', allfiles)]:
        report('\n%s\n[%s]\n%s\n' % ('-' * 80, title, '-' * 80))
        
        allitems.sort(key=lambda pair: pair[1])   # sort by ascend size
        allitems.reverse()                        # order largest first
        
        maxsize = max(len('{:,}'.format(size)) for (path, size) in allitems)
        for (path, size) in allitems:
            report('{:,}'.format(size).rjust(maxsize), '=>', path)

    report('\n[End]')
    reportfile.close()   # flush output now


if __name__ == '__main__':
    # configure run
    if len(sys.argv) == 4:
        toproot, reportsuffix, showreport = sys.argv[1:]
    else:
        toproot = prompt('Root directory path?')
        reportsuffix = prompt('Report filename suffix (empty=use folder name)?')
        showreport = prompt('Show report on stdout at end (true: y or yes)?')

    if not os.path.isdir(toproot):
        error('Error: root path does not name a valid directory; run cancelled.')
        if sys.platform.startswith('win'): prompt('Press Enter.')   # clicked?
        sys.exit(1)
        
    if not reportsuffix:                         
        # use input or dir name
        if toproot.endswith('/') and len(toproot) > 1:
            toproot = toproot[:-1]               # unix: ends in '/' but not only
        rightmost = os.path.split(toproot)[-1]   # but no dir name for C:\
        reportsuffix = rightmost or 'root'

    showreport = showreport.lower() in ['y', 'yes']
        
    # collect sizes
    alldirs, allfiles = [], []
    counts = [1, 0]
    totsize = treesize(toproot, alldirs, allfiles, counts)
    assert counts[0] == len(alldirs) and counts[1] == len(allfiles) 

    # report results
    reportname = 'treesize-report-%s.txt' % reportsuffix
    reportfile = open(reportname, mode='w', encoding='utf8')
    genreport(toproot, totsize, alldirs, allfiles, counts)

    # echo report file?
    if showreport:
        for line in open(reportname, encoding='utf8'):   # show file on stdout
            print(line, end='')                          # by line, else delay?
        if sys.platform.startswith('win'):
            prompt('Press Enter.')   # stay open if Windows click; or isatty()?
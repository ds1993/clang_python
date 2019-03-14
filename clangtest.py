#!/usr/bin/python

import sys
import clang.cindex

from clang.cindex import Config
from clang.cindex import Cursor
from clang.cindex import CursorKind

def dumpClass(node):
    print 'Found %s [file=%s, start: line=%s, col=%s, end: line=%s, col=%s, type=%s, displayname=%s]' % (
            node.spelling, node.location.file.name, node.extent.start.line, node.extent.start.column, node.extent.end.line, node.extent.end.column, node.kind.name, node.displayname)
    if node.kind.name == "NAMESPACE":
        print "begin namespace " + node.spelling
    if node.kind.name == "CLASS_DECL":
        print "begin class " + node.spelling
    for child in node.get_children():
        dumpClass(child)
    if node.kind.name == "NAMESPACE":
        print "end namespace " + node.spelling
    if node.kind.name == "CLASS_DECL":
        print "end class " + node.spelling

Config.set_library_file("/usr/lib/llvm-3.4/lib/libclang-3.4.so")
index = clang.cindex.Index.create()

#the param 2 could put include dirs, like ["-Iinclude1", -Iinclude2]
tu = index.parse(sys.argv[1])

dumpClass(tu.cursor)

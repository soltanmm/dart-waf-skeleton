# vim: syntax=python:shiftwidth=4:tabstop=4:expandtab

def options(opt):
    opt.recurse(['tools','src'],mandatory=False)

def configure(cnf):
    cnf.recurse(['tools','src'],mandatory=False)

def build(bld):
    bld.recurse(['tools','src'],mandatory=False)


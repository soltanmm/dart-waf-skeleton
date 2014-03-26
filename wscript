# vim: syntax=python:shiftwidth=4:tabstop=4:expandtab

use_pub = True

def options(opt):
    opt.recurse(['tools','packages','web'],mandatory=False)

def configure(cnf):
    cnf.recurse('tools',mandatory=False)
    if use_pub:
        if 'PUB' not in cnf.env:
            cnf.fatal('Missing pub. Cannot retrieve packages.')
        cmd = [cnf.env['PUB'],'get']
        cnf.start_msg("Pulling Dart dependencies via pub.")
        cnf.end_msg(cnf.exec_command(cmd) == 0)
    cnf.env.append_value('PACKAGES',cnf.path.find_dir('packages').abspath())
    cnf.recurse(['packages','web'],mandatory=False)

def build(bld):
    bld.recurse(['tools','packages','web'],mandatory=False)


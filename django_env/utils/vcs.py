#!/usr/bin/env python

from subprocess import call

import os
import sys
import re
import shutil


def main():
    vcs_schemes = ['git', 'hg', 'svn']
    vcs_scheme_url = sys.argv[1]
    target_dir = sys.argv[2]
    url_match = re.search(r'^(?P<scheme>[a-z]{2,3})\+(?P<url>.+)', vcs_scheme_url)

    if not url_match:
        print "Error: VCS URL wasn't in the correct format (Example: git+git://github.com/epicserve/django-base-site.git)."

    url_match.groups()

    scheme = url_match.group('scheme')
    url = url_match.group('url')

    if not scheme in vcs_schemes:
        print "Error: Unsupported VCS. Supported VCS (%S)" % ", ".join(vcs_schemes)

    if scheme == "git":
        call(["git", "clone", url, target_dir])
        git_dir = os.path.join(target_dir, '.git')
        if os.path.isdir(git_dir):
            shutil.rmtree(git_dir)

    if scheme == "hg":
        call(["hg", "clone", url, target_dir])
        hg_dir = os.path.join(target_dir, '.hg')
        if os.path.isdir(hg_dir):
            shutil.rmtree(hg_dir)

    if scheme == "svn":
        call(["svn", "export", url, target_dir])


if __name__ == '__main__':
    main()

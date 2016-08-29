#!/usr/bin/env python2.7

import argparse
import sys

import git

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("branch",
            help="The git branch to rebase and squash on top of.")
    args = parser.parse_args(args)

    repo = git.Repo(".", search_parent_directories=True)

    if repo.is_dirty():
        print("The repo is dirty, please stash or commit changes")
        return 1

    # Get the merge base: `git merge-base <branch> HEAD`

    mb = repo.merge_base(args.branch, "HEAD")
    print(mb)

    # TODO(zmanji): What if the merge-base is HEAD? (no-op?)
    # Get all of the commits between the current branch and the merge base
    # `git log HEAD..<merge-base>`
    # Soft reset to the merge base? (just change HEAD to merge_base)
    # Double check the tree is dirty
    # Now commit the changes with the squash message

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

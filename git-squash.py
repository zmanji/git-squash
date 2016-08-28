#!/usr/bin/env python2.7

import argparse
import sys

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("branch", default="master",
            help="The git branch to rebase and squash on top of.")
    parser.parse_args(args)

    # TODO(zmanji): Check if the git tree is dirty or not

    # Get the merge base
    # Get all of the commits between the current branch and the merge base
    # Soft reset to the merge base?
    # Double check the tree is dirty
    # Now commit the changes with the squash message

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

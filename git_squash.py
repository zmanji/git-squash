#!/usr/bin/env python3

import argparse
import functools
import sys

import git

error = functools.partial(print, file=sys.stderr)


def squash(args) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "branch",
        help="The upstream branch to squash commits of the current branch on to.",
    )
    args = parser.parse_args(args)

    repo = git.Repo(".", search_parent_directories=True)

    if repo.is_dirty():
        error("The repo is dirty, please stash or commit changes")
        return 1

    # Find all commits betweent HEAD and branch
    mb = repo.merge_base(args.branch, "HEAD")
    if len(mb) == 1:
        mb = mb[0]
    else:
        error("No merge base between current branch and %s found!" % args.branch)
        return 1

    rev_range = "HEAD...%s" % mb.hexsha
    commits_to_squash = list(repo.iter_commits(rev=rev_range))
    if len(commits_to_squash) == 0:
        error("No commits to squash!")
        return 1
    elif len(commits_to_squash) == 1:
        error("Only one commit to squash. Exiting.")
        return 0

    log_message = "git-squash of %s commits." % len(commits_to_squash) + "\n"
    for commit in commits_to_squash:
        short_sha = repo.git.rev_parse(commit.hexsha, short=4)
        log_message = log_message + "\n" + commit.summary + " (%s)" % short_sha

    # Soft reset of HEAD to the merge base.
    git.refs.head.HEAD(repo).reset(commit=mb, index=False, working_tree=False)

    # Double check the tree is dirty
    if not repo.is_dirty():
        error("Squashing commits results in no change!")
        return 1

    # Commit the changes with the squash message

    repo.index.commit(log_message)
    return 0


def main():
    sys.exit(squash(sys.argv[1:]))


if __name__ == "__main__":
    main()

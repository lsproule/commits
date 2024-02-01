from os import system, popen
from random import randint


rand = randint(3, 14)


def add_commits():
    for x in range(rand):
        system(f'touch new_file/newfile{x}.txt')
        system("git add .")
        system(f"git commit -m 'new file {x}'")
        system("git push")


def add_issues():
    system("gh issue create -t 'new issue' -b 'this is a new issue'")


def add_pr():
    system("gh pr create -t 'new pr' -b 'this is a new pr'")


def get_pr():
    pr = popen("gh pr list").read()
    return pr


def merge_pr():
    get_pr()


def clean_up():
    system("rm -rf new_file/*")
    system("git add .")
    system("git commit -m 'clean up'")
    system("git push")


if __name__ == "__main__":
    add_commits()
    clean_up()

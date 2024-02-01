from os import system


for x in range(3400):
    system(f'touch newfile{x}.txt')
    system("git add .")
    system(f"git commit -m 'new file {x}'")
    system("git push")

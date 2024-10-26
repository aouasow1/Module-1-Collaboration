aouas@LAPTOP-AS9E0G9I MINGW64 ~
$ git init
Initialized empty Git repository in C:/Users/aouas/.git/

aouas@LAPTOP-AS9E0G9I MINGW64 ~ (master)
$ cd Downloads

aouas@LAPTOP-AS9E0G9I MINGW64 ~/Downloads (master)
$ git init
Initialized empty Git repository in C:/Users/aouas/Downloads/.git/

aouas@LAPTOP-AS9E0G9I MINGW64 ~/Downloads (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

aouas@LAPTOP-AS9E0G9I MINGW64 ~/Downloads (master)
$ touch hello_world_test.py

aouas@LAPTOP-AS9E0G9I MINGW64 ~/Downloads (master)
$ git add hello_world_test.py

aouas@LAPTOP-AS9E0G9I MINGW64 ~/Downloads (master)
$ git commit -m "create hello_world_test.py"
[master (root-commit) 45b18b3] create hello_world_test.py
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 hello_world_test.py

aouas@LAPTOP-AS9E0G9I MINGW64 ~/Downloads (master)
$ git log
commit 45b18b370ac730666c612a718f5a92647314feba (HEAD -> master)
Author: Aoua Sow <asow7@ivytech.edu>
Date:   Sat Oct 26 10:47:05 2024 -0400

    create hello_world_test.py

aouas@LAPTOP-AS9E0G9I MINGW64 ~/Downloads (master)
$

# Auto-judge sakai homework

This program is used to judge sakai homework to save time for TAs and Student Assistents.

For now, only .java program will be judged.

Follow the instruction below and feel free to use it.

__This is programmed by Boris, DISPLAY the origin author, which is me, on the screen if you want to modify and redistribute this program.__

## Dependency

This program is written in __python3.6__, python 2 is not tested.

You need to install (python packages)
- rarfile
- shutil
- patoolib
to run this program.

All unix system like __macOS__, __Linux__ can run this program.

__Windows__ may not be able to run.

After you setup the environment, you should create a `./judge` folder which contains your test files and `judge.profile`

In your `judge.profile`, you will format the file like:
```
key_word1 key_word2: test_file1 test_file2
```
while the key_word is some certain words in the path of .java file or the class name of which. The mach system is NOT case-sensatice.
## Take care

Only the multi-file download provided by sakai will be detected by this program.

Which mean you folder looks like:
```
./
├── auto_judge.py
├── judge
│   ├── 3.test
│   ├── 4.test
│   ├── 6.test
│   ├── 7.test
│   ├── 8.test
│   └── judge.profile
└── 王大锤, WANG Dachui(11912030)
    └── 提交作业的附件
        └── 11912030.zip
```
## To-do(Maybe)

__.cpp__ support.

## NOTICE

__You can freely modify this program, BUT YOU WILL DISPLAY the origin author, which is me, in your program.__


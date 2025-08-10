Below is a tabulated cheatsheet that compares key commands across Bash, PowerShell, and the Windows Command Prompt (cmd.exe). It also includes examples of piping and input/output redirection for each.

| Task Description                  | Bash Command                  | PowerShell Command            | CMD Command                 | Notes |
|-----------------------------------|-------------------------------|-------------------------------|-----------------------------|-------|
| List Directory Contents           | `ls`                          | `Get-ChildItem`               | `dir`                       | Lists files and directories in the current directory. |
| Change Directory                  | `cd /path/to/dir`             | `Set-Location -Path path\to\dir` | `cd \path\to\dir`            | Changes the current directory to the specified path. |
| Copy File or Directory            | `cp source destination`       | `Copy-Item source -Destination destination` | `copy source destination`  | Copies files or directories. |
| Move/Rename File or Directory     | `mv source destination`       | `Move-Item source -Destination destination` | `move source destination`  | Moves or renames files or directories. |
| Delete File                       | `rm file`                     | `Remove-Item file`            | `del file`                  | Deletes a file. |
| Delete Directory                  | `rm -r directory`             | `Remove-Item directory -Recurse` | `rmdir /S /Q directory`      | Deletes a directory and its contents. |
| Create New Directory              | `mkdir directory`             | `New-Item -Type Directory -Path directory` | `mkdir directory`          | Creates a new directory. |
| Display Text                      | `echo "text"`                 | `Write-Output "text"`         | `echo text`                 | Displays a line of text/string. |
| Find Text in Files                | `grep "pattern" file`         | `Select-String -Path file -Pattern "pattern"` | `findstr "pattern" file`   | Searches for text in files. |
| Display Command Help              | `man command`                 | `Get-Help command`            | `help command` or `command /?` | Displays help for a command. |
| View File Content                 | `cat file`                    | `Get-Content file`            | `type file`                 | Outputs the content of a file. |
| Redirect Output to File           | `command > file`              | `command | Out-File -FilePath file` | `command > file`            | Redirects the output of a command to a file, overwriting the file. |
| Append Output to File             | `command >> file`             | `command | Add-Content -Path file` | `command >> file`           | Redirects the output of a command to a file, appending to the file. |
| Pipe Output to Another Command    | `command1 \| command2`        | `command1 \| command2`        | `command1 | command2`       | Passes the output of one command as input to another command. |
| Chain Commands                    | `command1 && command2`        | `command1; command2`          | `command1 & command2`       | Executes multiple commands sequentially. |
| Display Current Directory         | `pwd`                         | `Get-Location`                | `cd`                        | Outputs the path of the current working directory. |
| Show Running Processes            | `ps`                          | `Get-Process`                 | `tasklist`                  | Lists currently running processes. |
| Kill a Process                    | `kill pid`                    | `Stop-Process -Id pid`        | `taskkill /PID pid`         | Terminates a process by its PID. |
| Download a File (non-native cmd)  | `wget -O file url` or `curl -o file url` | `Invoke-WebRequest -OutFile file -Uri url` | N/A                         | Downloads a file from the internet. `wget` and `curl` may need to be installed separately on some systems. |
| Display Environment Variables     | `printenv`                    | `Get-ChildItem Env:`          | `set`                       | Lists all environment variables. |

**Examples of Piping and Redirection:**

- **Bash:**
  - Piping: `ls -l | grep "Jan"`
  - Output Redirection: `echo "Hello World" > hello.txt`
  - Input Redirection: `grep "Hello" < hello.txt`

- **PowerShell:**
  - Piping: `Get-ChildItem | Where-Object { $_.LastWriteTime -ge (Get-Date).AddDays(-1) }`
  - Output Redirection: `Get-Process > processes.txt`
  - Input Redirection is less common in PowerShell but can be done using `Get-Content`.

- **CMD:**
  - Piping: `dir | find "File"`
  - Output Redirection: `echo Hello World > hello.txt`
  - Input Redirection: `find "Hello" < hello.txt`

Please note that PowerShell uses different cmdlets that can achieve similar tasks to Unix-like commands but often with different syntax and additional capabilities. The Command Prompt in Windows has some limitations compared to Bash and PowerShell, especially in terms of native support for operations commonly used in Unix-like systems, such as `wget` for file downloads.
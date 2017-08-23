# Taboola Git Server

Taboola DevOps developer, programing task.

Solution By Nissim Bitan, Mamram almuni with 5 years experience in multi Cloud Developing and DevOps

## Ansible

The Ansible roles its set the code of the client project in the client from git and install dependencies.

## Server

written in python in Flask Framework, the server listen and collect these reports, including committing user,
branch, repository name, file list, diff and commit message.

The data is sent from the clients to the server by a POST request that contains the commit details

## Server Output Example

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
----------------Commit Details------------------
Author: niso120b
Email: niso120b@gmail.com
Repository Name: taboola-java-jenkins
Branch: master
Commit Message: Update README.md file

Files:
directory : bin
file : bin/calc
directory : src
directory : src/main
directory : src/main/antlr
file : src/main/antlr/Expr.g4
directory : src/main/java
file : src/main/java/Calc.java
file : src/main/java/CalcEvalVisitor.java
directory : src/test
directory : src/test/java
file : src/test/java/CalcTest.java
file : README.md
file : jenkinsfile
file : pom.xml
Diffs:
File: README.md
Diff:
b'@@ -7,7 +7,7 @@ and create all the ci process in jenkins.

### Additional changes and extra files

-**the solution contain:**
+**the solution contains:**
* Jenkinsfile - which run all the process in the jenkins (in Groovy)
* pom.xml - add rpm-maven-plugin and create the process to create the rpm
* bin folder - the bin folder contain the calc file, its the **calc** command at the final result
'
------------------------------------------------
127.0.0.1 - - [23/Aug/2017 01:16:37] "POST /post_commit/ HTTP/1.1" 200 -
```

## Contact

Nissim Bitan - niso120b@gmail.com



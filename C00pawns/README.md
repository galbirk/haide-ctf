# C00pawns  
 
* Author: [Rubublik](https://github.com/Rubublik) 
* challenge: <b>ADD_MEMORY_IMAGE</b> 
* Level: :star::star::star::star::star:
* Dockerfile:
* References:  
* Attachments:  

## level 1 - pr0file:
* <b>Description: </b><br>
<div>
On one quite morning at Cyrebro inc. called that client with a problem with his computer...
According to his words, he had an unprotected file with important passwords that "turned unreadable". 
He suspects his computer "was hacked".
As a DFIR specialist at Cyrebro, you were assigned to the task. As you could not help remotely, the first thing you asked him to do is hibernate his computer and bring it to you.
Having the memory of the compromised computer, do what you know best.
Faster, the clock is ticking...<br>
what profile is the most appropriate for this machine? (ex: win10x86_14393)<br>
flag format: FLAG{PROFILE}
<br>
<br>
</div>

## level 2 - hey write this down:
* <b>Description: </b><br>
<div>
what is the pid of the running notepad process?<br>
flag format: FLAG{pid}
<br>
<br>
</div>

## level 3 - is the malware still running?
* <b>Description: </b><br>
<div>
wait, is the malware still running?<br>
what is the pid of the process running the malware?
flag format: FLAG{PID}
<br>
<br>
</div>

## level 4 - critical mistake
* <b>Description: </b><br>
<div>
ok, seems like common a ransom attack... but there is hope!<br>
looks like they used a symetrical encryption, maybe we can still recover the file?
if only we found the encryption key...

flag format: FLAG{encryption_key}<br>

note- i bet those hackers embeded it somewhere in the file.
<br>
<br>
</div>

## level 5 - just about there
* <b>Description: </b><br>
<div>
so you know the key, but which encryption type exactly did they use?
note - enter the very exact type and version.

flag format: FLAG{NAME-VERSION}
<br>
<br>
</div>

## level 6 - finito la comedia
* <b>Description: </b><br>
<div>
finish what's left and recover the file.

note, the flag is a fruit, as usual.
flag format: FLAG{fruit}
<br>
<br>
</div>

* final flag: <b>FLAG{Guava}</b>
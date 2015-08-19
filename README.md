# pgm

Initialize a process group named 'mine'
	$ pgm init mine
	
Initialize a group named 'mine' with config file
	$ pgm init mine --config launch.ini

List all groups
	$ pgm groups
	1 Group:
	mine

List all processes in group 'mine'
	$ pgm list mine
	3 Processes
	PGM Name	Status	PID	Command
	top		Running	35219	htop
	netstat		Running	57894   watch -n 1 'netstat -naltp'
	disksize	Exited		df -h
	tcpdump		Running	74983	sudo tcpdump -i eth0

Add the process 'syslog' to the session 'mine'
	$ pgm add mine syslog --cmd tail -f /var/log/syslog
	Adding process 'syslog' to 'mine' using: tail -f /var/log/syslog	

Add a sudo process to the session 'mine'
	$ pgm add mine iftop --sudo --cmd iftop -i eth0
	Adding process 'iftop' to 'mine' using: sudo iftop -i eth0
	[sudo] password for csrobot: 

Connect to process stdio
	$ pgm connect mine top
	(opens tmux session to that process)

Show latest output of a process
	$ pgm tail mine disksize
	Filesystem      Size  Used Avail Use% Mounted on
	/dev/sda1       209G  136G   63G  69% /

Kill a process (Ctrl-c) Note: does not remove the process output from pgm
	$ pgm stop mine --name top
	Sending Ctrl-c (SIGINT) to process 'top' in session 'mine'

Kill a process (Ctrl-c) and remove it
	$ pgm stop mine -r --name top
	Sending Ctrl-c (SIGINT) to process 'top' in session 'mine'
	Removing 'top' from session 'mine

Kill all processes (Ctrl-c)
    $ pgm stop mine --all

Kill a process (Ctrl-d)
	$ pgm stop mine -d --name top
	Sending Ctrl-d (EOF) to process 'top' in session 'mine'

Kill a process (Ctrl-\)
	$ pgm stop mine -q --name top
	Sending Ctrl-\ (SIGQUIT) to process 'top' in session 'mine'

Kill a process
	$ pgm stop mine -9 --name top
	Sending SIGINT to process 'top' in session 'mine'

Remove an exited process (only works on exited processes)
	$ pgm rm mine top
	Removing 'top' from session 'mine'


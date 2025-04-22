FROM ubuntu:18.04

ENV user acm
ENV chall_port 1337

RUN apt-get update
RUN apt-get -y install socat

RUN adduser $user

ADD ./deploy/flag /home/$user/flag
ADD ./deploy/pwn102 /home/$user/pwn102

RUN chown root:$user /home/$user/flag
RUN chown root:$user /home/$user/pwn102

RUN chmod 755 /home/$user/pwn102
RUN chmod 440 /home/$user/flag

WORKDIR /home/$user
USER $user
EXPOSE $chall_port
CMD socat -T 60 TCP-LISTEN:$chall_port,reuseaddr,fork EXEC:/home/$user/pwn102
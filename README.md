# <a name="_4x4de1qk77tr"></a>         **Learning Management System using gRPC**
`					  `**(Milestone - 3)**

`					   `**Readme File**

## <a name="_g99pa5vpmkfm"></a>**Operating System Used -** Ubuntu 24.04 LTS
**Setup**

Unzip the project folder.

We have five files in a folder server.py, client.py, lms.proto, tutoring\_server.py, tutoring.proto

First create a virtual environment to run a python program. 

pip install virtualenv

virtualenv env

To activate virtual environment run the command

Source env/bin/activate

Import grpc libraries-

pip install grpcio grpcio-tools pyJWT

Now compile lms.proto file by using command-

python -m grpc\_tools.protoc -I=. --python\_out=. --grpc\_python\_out=. lms.proto 

Now compile tutoring.proto file by using command-

python -m grpc\_tools.protoc -I=. --python\_out=. --grpc\_python\_out=. tutoring.proto 

Now we have 4 more file in the folder 

1. lms\_pb2.py
1. Lms\_pb2\_grpc.py
1. tutoring\_pb2.py
1. tutoring\_pb2\_grpc.py
## <a name="_cz3xxllfp3ue"></a>**Running the Project**
Firstly we need 6 terminals open in the same folder where all client and server files are present.We already have a virtual environment env file.

To activate the virtual environment in all terminals run this command in each terminal.

Source env/bin/activate

**Starting LMS Servers**

In one of the terminals we will run lms server1 by -

For running lms server1-

python server1.py

After this command we can see a prompt server is running at port 50051.

In another terminal we will run lms server2 by -

For running lms server-

python server2.py

->After this command we can see a prompt server is running at port 50052.

In one of the terminals we will run lms server by -

For running lms server3-

python server3.py

After this command we can see a prompt server is running at port 50053.

After starting all the servers we will see that one leader is elected among them and It will start sending heartbeats.

**Starting tutoring Server** (Not necessary for milestone3)

First install required dependencies in another terminal.

Pip install torch 

Pip install transformers

It will take some time to install these.

Now we will run tutoring server by -

python tutoring\_server.py

After this command we can see a prompt server is running at port 50054.

If we are running for the first time it will take some time to download the LLM model.

**Clients (Student)**

In the 5th terminal we will run a client which is a student.

And for running client run the command - 

python client.py

Now login windows will open up and we can give prompt 1 to Login.

It will ask for a username and password. 

**For student -** 

**username - student1 | username - student2 | username - student3**

**Password - Sanskar  | password - Aarnav   |  password - Ameer**

**We can use any of the above username and password set to login.**

**Clients (Instructor)**

In the 6th terminal we will run a client which is a student.

And for running client run the command - 

python client.py

Now login windows will open up and we can give prompt 1 to Login.

It will ask for a username and password. 

**For instructor -** 

**Username - instructor1**

**Password - instructorpass**


**Further Execution -** 

After logging in as instructor, instructor can post assignments by selecting the post assignment option from the instructor menu.

` `After the assignment is successfully posted then the student can view the assignment by selecting ViewAssignment from the Command Line. 

After submission instructor can see ViewSubmission and then he can grade submission. 

After grading we can see the message on terminals of raft follower - Entry successfully appended on node\_id.

If then shut down the leader and again from student terminal select view\_grades from student menu then also it will find new leader and can see grades which were replicated.



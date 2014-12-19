#####Java implementaion of a leader election using Ring Algorithm (Election In A Ring). 

*Background:

-assume that processes form a ring: each process only sends messages to the next process in the ring
- Active list: its info on all other active processes
- assumption: message continues around the ring even if a process along the way has crashed.
 
 
Background: any process Pi sends a message to the current coordinator; if no response in T time units, Pi initiates an election
initialize active list to empty.
Send an “Elect(i)” message to the right. + add i to active list.
 
If a process receives an “Elect(j)” message
            (a) this is the first message sent or seen
                        initialize its active list to [i,j]; send “Elect(i)” + send “Elect(j)”
            (b) if i != j, add i to active list + forward “Elect(j)” message to active list
            (c) otherwise (i = j), so process i has complete set of active processes in its active list.
                        => choose highest process ID + send “Elected (x)” message to neighbor
If a process receives “Elected(x)” message,
            set coordinator to x
           
Example:
 
Suppose that we have four processes arranged in a ring:  P1 à P2 à P3 à P4 à P1 …
P4 is coordinator
Suppose P1 + P4 crash
Suppose P2 detects that coordinator P4 is not responding
P2 sets active list to [ ]
P2 sends “Elect(2)” message to P3; P2 sets active list to [2]
P3 receives “Elect(2)”
This message is the first message seen, so P3 sets its active list to [2,3]
P3 sends “Elect(3)” towards P4 and then sends “Elect(2)” towards P4
The messages pass P4 +  P1 and then reach P2
P2 adds 3 to active list [2,3]
P2 forwards “Elect(3)” to P3
P2 receives the “Elect(2) message
            P2 chooses P3 as the highest process in its list [2, 3] and sends an “Elected(P3)” message
P3 receives the “Elect(3)” message
            P3 chooses P3 as the highest process in its list [2, 3] + sends an “Elected(P3)” message

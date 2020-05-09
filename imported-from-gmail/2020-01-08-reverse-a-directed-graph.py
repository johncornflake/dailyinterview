Hi, here's your problem today. This problem was recently asked by Facebook:


Given a directed graph, reverse the directed graph so all directed edges are reversed. 
Example:
Input:
A -> B, B -> C, A ->C
Output:
B->A, C -> B, C -> A
Here's a starting point:
from
 
collections
 
import
 
defaultdict
class
 
Node
:
  
def
 
__init__
(
self
,
 
value
):
    
self
.
adjacent
 
=
 
[]
    
self
.
value
 
=
 
value
def
 
reverse_graph
(
graph
):
  

# Fill this in.
a
 
=
 
Node
(
'a'
)
b
 
=
 
Node
(
'b'
)
c
 
=
 
Node
(
'c'
)
a
.
adjacent
 
+=
 
[
b
,
 
c
]
b
.
adjacent
 
+=
 
[
c
]
graph
 
=
 
{
    
a
.
value
:
 
a
,
    
b
.
value
:
 
b
,
    
c
.
value
:
 
c
,
}
for
 
_
,
 
val
 
in
 
reverse_graph
(
graph
)
.
items
():
  
print
(
val
.
adjacent
)

# []

# ['a', 'b']

# ['a']



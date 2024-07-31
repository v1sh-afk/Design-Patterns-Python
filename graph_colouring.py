# ****************************************************************************
# Title: 1.11-Graph Colouring.
# Author: Vishal Prakash (3122 21 5002 125)
# Exercise date: 08/10/2022
# Concept of Program: Data Structure - Graph Colouring - OOPS.
# ****************************************************************************
class graph_colouring:
  def add(g,n1,n2):
    g[n1].append(n2)
    g[n2].append(n1)
    return g

  #coloring of each node
  def Coloring(g,v):
    c = [0]*v
    c[0] = 'red'
    for i in range (len(c)):
      if c[i] == 'red':
        a = g[i]
        for i in a:
          if c[i] == 'red' or c[i]==0:
            c[i] ='green'
      else:
        b = g[i]
        for i in b:
          if c[i] == 'green' or c[i]==0:
            c[i] ='red'
    for i in range(len(c)):
      print('%d -----> %s'%(i,c[i]) )
      

#driver code
n = int(input('number of nodes:'))
g1 = [[] for i in range(n)]#graph
# Note:acyclic graph or simple cylic graph
if n% 2 == 0:
 for i in range (n):
  print("form edge between:")
  a = int(input('node1:'))
  b = int(input('node2:'))
  g1 = graph_colouring.add(g1,a,b)
else:
  for i in range (n-1):
    print("form edge between:")
    a = int(input('node1:'))
    b = int(input('node2:'))
    g1 = graph_colouring.add(g1,a,b)
print('the graph is :')
for i in range (len(g1)):
    print('%d :'%i,g1[i])
print('\n The colour of each node is :')
(graph_colouring.Coloring(g1,n))#call the function 


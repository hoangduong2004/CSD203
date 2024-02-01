from Stack import Stack
class Q3_1:
    def f1(self, a, start):
    # a is the adjacency matrix representing the given graph
    # start is a starting point 

    # Initialize the stack and visited list
    stack = Stack()
    visited = [False] * len(a)

    # Start the depth-first traversal
    stack.push(start)
    while not stack.isEmpty():
        v = stack.pop()
        if not visited[v]:
            self.depth(v, visited)

    # Helper function to get the degree of a vertex
    def degree(vertex):
        return sum(1 for i in a[vertex] if i != 0)

    # Helper function for depth-first traversal
    def depth(self, start, b):
    # Mark the vertex as visited and print it with its degree
    visited[start] = True
    print(f"{chr(start+65)}({self.deg(start)})", end=" ")

    # Visit all the vertices adjacent to this vertex
    for i in range(len(b)):
        if self.a[start][i] != 0 and not visited[i]:
            stack.push(i)
            self.depth(i, b)

    # Start the depth-first traversal
    stack.push(start)
    while not stack.isEmpty():
        depth(stack.pop())
    pass
        
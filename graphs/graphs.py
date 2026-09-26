

class Graph(self,adj_list):
    self.adj_list = {}
    
    def add_node(self,node):
        if node not in self.adjList:
            self.adj_list[node] = []
        else:
            print('no duplicate nodes allowed')

    # Vertices must be added before edges can connect them.
    def add_edge(self,vertex_1,vertex_2):
        if vertex_1 in self.adj_list and vertex_2 in self.adj_list:
            self.adj_list[vertex_1].append(vertex_2)
            self.adj_list[vertex_2].append(vertex_1)
        else:
            print(f'add {node} into adjancely lists before adding its edge')

            
    def print_graph(self):
        for k,v in self.adj_list.items():
            print('vertex', k)
            print('edge', v)


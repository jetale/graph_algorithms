
import networkx as nx
#import matplotlib.pyplot as plt





def do_work():

	'''
	g = nx.random_regular_graph(n=100, 0.6)



	#nx.draw_networkx(g, with_labels=True)
	#nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=nx.get_edge_attributes(g,'weight'))
	#plt.axis("off")
	#plt.show()

	#plt.savefig("sample.png")

	#nx.write_yaml(g, "sample.yaml")

	for item in nx.generate_edgelist(g):
		print(item)
	'''

	start_node = 1
	dst_node = 6

	graph = {
        1: {2: 1, 4:  1},
        2: {1: 1, 4:  1, 3:  2},
        3: {2:2, 4:1, 5:1, 6:1},
        4: {1:  1, 2:  1, 3:1, 5:2, 6:15},
        5: {3: 1, 4:2, 6:1},
        6: {3: 1, 4:15, 5:1}
     	}

	prev_node_dict = do_bsf(graph, start_node)

	find_path(prev_node_dict, start_node, dst_node)


def do_bsf(graph, strt_node):

	glen = len(graph)

	node_que = []

	visited = [0] * (glen + 1)

	#prev_list = [[0]] * (glen + 1)
	prev_dict = {}
	start_node = strt_node
	node_que.append(start_node)
	visited[start_node] = 1

	#print(node_que)

	while node_que:


		curr_node = node_que[0]
		nb_nodes = graph[curr_node]
		#print(nb_nodes)

		for  key, value in nb_nodes.items():

			if visited[key] == 0:
				#print(key)
				node_que.append(key)
				visited[key] = 1
				try:
					pl = prev_dict[key]
					pl.append(curr_node)
					#print(pl)
					prev_dict[key] = pl

				except KeyError:
					prev_dict[key] = [curr_node]

		node_que.pop(0)


	#print(prev_dict)

	return prev_dict



def find_path(prev_dict, start_node, dst_node):
	#Find path to start node

	dest_node = dst_node

	cr_node = prev_dict[dest_node][0]
	path_list = []
	path_list.append(cr_node)

	while cr_node != start_node:

		cr_node = prev_dict[cr_node][0]
		path_list.append(cr_node)


	print(path_list)



if __name__ == '__main__':
	do_work()

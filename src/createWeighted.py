import argparse
import networkx as nx

parser = argparse.ArgumentParser()
parser.add_argument('input', help='The path to the input file containing edges of the digraph')
parser.add_argument('output', help='The path to the output file')
args = parser.parse_args()

graph = nx.read_edgelist(args.input, create_using=nx.DiGraph())
#print(graph[u'3480'])
for u, neighbours in graph.adjacency_iter():
    num = len(neighbours)
    #print(neighbours)
    #print('node ', u, ' has ', num, ' neighbours')
    if num > 0:
        w = 1#1.0 / float(num)
        for k, _ in neighbours.iteritems():
            #print(u, ' , ', k)
            graph[u][k]['weight'] = w

nx.write_edgelist(graph, args.output, data=['weight'])





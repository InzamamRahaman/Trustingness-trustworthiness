import argparse
import networkx as nx

parser = argparse.ArgumentParser()
parser.add_argument('input', help='The path to the input file containing edges of the digraph')
parser.add_argument('output', help='The path to the output file')
args = parser.parse_args()

graph = nx.read_edgelist(args.input, create_using=nx.DiGraph())
for u, neighbours in graph.adjacency_iter():
    num = float(len(neighbours))
    w = 1.0 / num
    for k, _ in neighbours:
        graph[u][k]['weight'] = w

nx.write_edgelist(graph, args.output)





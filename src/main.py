import argparse

import networkx as nx

import TrustScores

parser = argparse.ArgumentParser()

parser.add_argument('--input', help='The path to the input file containing edges of the digraph and weights')
parser.add_argument('--output', help='The path to the output file that contains nodes, trustingness scores and '
                                   'trustworthiness scores')
parser.add_argument('--k', help='The maximum number of iterations to be made')
parser.add_argument('--s', help='involvement score')
parser.add_argument('-w', '--weighted', help='Indicates that the graph is weighted', action='store_true')

args = parser.parse_args()

input_filename = args.input
output_filename = args.output

graph = None
if args.weighted:
    graph = nx.read_edgelist(input_filename, create_using=nx.DiGraph(), data=[('weight', float)])
else:
    graph = nx.read_edgelist(input_filename, create_using=nx.DiGraph())
    
trustingness, trustworthiness = TrustScores.compute(graph, int(args.k), float(args.s))

with open(output_filename, 'w') as outf:
    for node in graph.nodes_iter():
        outf.write('{0} {1} {2}\n'.format(node, trustingness[node], trustworthiness[node]))



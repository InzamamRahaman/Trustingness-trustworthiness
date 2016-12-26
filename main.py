import argparse
import networkx as nx
import TrustScores

parser = argparse.ArgumentParser()

parser.add_argument('input', help='The path to the input file containing edges of the digraph and weights')
parser.add_argument('output', help='The path to the output file that contains nodes, trustingness scores and '
                                   'trustworthiness scores')
parser.add_argument('k', help='The maximum number of iterations to be made')

args = parser.parse_args()

input_filename = args.input
output_filename = args.output

graph = nx.read_edgelist(input_filename, create_using=nx.DiGraph(), data=[('weight', float)])
trustingness, trustworthiness = TrustScores.compute(graph, args.k)

with open(output_filename, 'w') as outf:
    for node in graph.nodes_iter():
        outf.write('{0} {1} {2}\n'.format(node, trustingness[node], trustworthiness[node]))



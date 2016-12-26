import networkx as nx
import numpy as np
import copy


def get_max_key_diff(d1, d2):
    m = 0
    for k1, v1 in d1.iteritems():
        if k1 in d2:
            m = max(abs(v1 - d2[k1]))
    return m


def get_change(prev_ti, prev_tw, curr_ti, curr_tw):
    return max(get_max_key_diff(prev_ti, curr_ti), get_max_key_diff(prev_tw, curr_tw))


def normalize(d):
    s = np.sum(d.values())
    for k, v in d.iteritems():
        d[k] = v / s


def compute(graph, k,involvement_score=1, delta=None):
    """
    Computes the trustingness and trustworthiness scores for the supplied
    graph
    :param graph: a Networkx graph storing the graph under consideration
                  NB: The code assumes that the edges are weighted
    :param k: the maximum number of iterations to be considered
    :param involvement_score: the involvement score [0 - 1](default 1)
    :param delta: minimum change in trustigness or trustworthiness scores to consider
    :return: a pair with the two dictionaries, the first containing the trustingness scores and the next the
             trustworthiness scores
    """
    prev_ti = dict()
    prev_tw = dict()
    curr_ti = dict()
    curr_tw = dict()
    nodes = graph.nodes_iter()
    for u in nodes:
        prev_ti[u] = 1
        prev_tw[u] = 1

    curr_k = 0

    while True:
        if curr_k >= 1:
            if curr_k > k:
                break
            elif delta and get_change(prev_ti, prev_tw, curr_ti, curr_tw) <= delta:
                break
        prev_ti = copy.copy(curr_ti)
        prev_tw = copy.copy(curr_tw)
        adj_list = graph.adjacency_iter()
        for u, neighbours in adj_list:
            score = 0
            for v, _ in neighbours:
                if involvement_score == 1:
                    score += graph[u][v]['weight'] / (1 + prev_tw[v])
                else:
                    score += graph[u][v]['weight'] / ((1 + prev_tw[v]) ** involvement_score)
            curr_ti[u] = score

        adj_list = graph.adjacency_iter()
        for u, neighbours in adj_list:
            score = 0
            for v, _ in neighbours:
                if involvement_score == 1:
                    score += graph[u][v]['weight'] / (1 + prev_ti[v])
                else:
                    score += graph[u][v]['weight'] / ((1 + prev_ti[v]) ** involvement_score)
            curr_tw[u] = score
        normalize(curr_ti)
        normalize(curr_tw)

    return curr_ti, curr_tw

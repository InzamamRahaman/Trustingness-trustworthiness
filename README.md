# Introduction
This Python programme implements the trustingness and trustiworthiness computations described in 
Roy et al.'s [Trustingness & trustworthiness: A pair of complementary trust mea"sures in a social network"](http://ieeexplore.ieee.org/document/7752289/)
presented at ASONAM2016. It accepts three command line arguments:

* the input file path
* the output file path
* the maximum number of iterations

and generates a file that contains on each line:

* the node label
* the trustingness score
* the trustworthiness score

# Required packages:

* Numpy
* Networkx

# TODO
1. Testing of code for correctness
2. Efficiency improvements ?
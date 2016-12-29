# Introduction
This Python programme implements the trustingness and trustiworthiness computations described in 
Roy et al.'s [Trustingness & trustworthiness: A pair of complementary trust measures in a social network"](http://ieeexplore.ieee.org/document/7752289/)
presented at ASONAM2016. It accepts three command line arguments:

* the input file path
* the output file path
* the maximum number of iterations
* the involvement score
* whether the graph is weighted or unweighted

and generates a file that contains on each line:

* the node label
* the trustingness score
* the trustworthiness score

# Required packages:

* Numpy
* Networkx

# Usage
Clone this repo by running
    ``git clone https://github.com/InzamamRahaman/Trustingness-trustworthiness.git``

There are four required command line arguments and a single optional:
* The input file; supplied by *--input*
* The output file; supplied by *--output*
* The number of iterations; supplied by *--k*
* The involvement score; supplied by *--s*
* Whether the input file contains a weighted graph; *-w* option

## Example with unweighted graph 
    python src/main.py --input graph/raw/epinions.edgelist --output scores/epinions.txt --k 10 --s 0.667

## Example with weighted graph 
    python src/main.py --input graph/weighted/epinions.edgelist --output scores/epinions.txt --k 10 --s 0.667 -w


# TODO
1. Testing of code for correctness
2. Write code to select normalisation function from command line
3. Efficiency improvements ?
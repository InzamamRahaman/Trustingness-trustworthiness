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

# Usage
Clone this repo by running
    ``git clone https://github.com/InzamamRahaman/Trustingness-trustworthiness.git``

There are four required command line arguments and a single optional:
1. The input file; supplied by *--input*
2. The output file; supplied by *--output*
3. The number of iterations; supplied by *--k*
4. The involvement score; supplied by *--s*
5. Whether the input file contains a weighted graph; *-w* option

## Example with unweighted graph 
    python src/main.py --input graph/raw/epinions.edgelist --output scores/epinions.txt --k 10 --s 0.667

## Example with weighted graph 
    python src/main.py --input graph/raw/epinions.edgelist --output scores/epinions.txt --k 10 --s 0.667 -w


# TODO
1. Testing of code for correctness
2. Efficiency improvements ?
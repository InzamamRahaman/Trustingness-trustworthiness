# Introduction
This Python programme implements the trustingness and trustiworthiness computations described in 
Roy et al.'s [Trustingness & trustworthiness: A pair of complementary trust measures in a social network"](http://ieeexplore.ieee.org/document/7752289/)
presented at ASONAM2016. The usage of the programme is described below.

# Required packages:

* Numpy
* Networkx

# Usage
Clone this repo by running
    ``git clone https://github.com/InzamamRahaman/Trustingness-trustworthiness.git``

There are four required command line arguments and two optional arguments:
* The input file; supplied by *--input*
* The output file; supplied by *--output*
* The number of iterations; supplied by *--k*
* The involvement score; supplied by *--s*
* Whether the input file contains a weighted graph; *-w* option  (default is unweighted)
* The normalisation method to use; *--normalisation*. There are three options: min-max, squared-sum, and sum. The default
  is squared-sum

## Example with unweighted graph 
    python src/main.py --input graph/raw/epinions.edgelist --output scores/epinions.txt --k 10 --s 0.667

## Example with weighted graph 
    python src/main.py --input graph/weighted/epinions.edgelist --output scores/epinions.txt --k 10 --s 0.667 -w

The programme outputs a .txt file with each line containing the node label, trustingness score, and trustworthiness score
in that order.

# TODO
1. Testing of code for correctness
2. Need to add requirements.txt
3. Efficiency improvements ?

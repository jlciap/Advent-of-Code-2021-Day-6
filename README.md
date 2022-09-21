# Problem 6 Advent of Code 2021

This short little repo documents my attempt at a solution for Advent of Code 2021 Day 6. To note is that, unlike other days, Part 1 and Part 2 are the exact same problem, so this solution should cover both cases.


## Problem Outline
The full problem description can and should be consulted [here](https://adventofcode.com/2021/day/6) but it is esstially a population modelling based on simple initial conditions + update rules. 

The most basic brute-forcing method works to solve Part 1, but the change in parameter in Part 2 renders the more basic brute force approaches computationally inctractable(for most normal machines at least).

## Experience and Approach

I decidede to use python with no external libraries as the language of choice(slow I know!)

I went through the following 4 steps while trying to solve the problem:

1. Making the most crude brute force algorithm 
2. Improving slightly on the brute force algorithm in Stage 1.
3. Changing data structures and finding a more 'efficient' method.
4. Failing at finding some close-formed solution (which I am 80% sure exists but not certain about).

Stage 1. was sufficient to solve Part 1, but insufficient to solve Part 2. Stage 2 was a performance improvement over 1., but was still insufficient to solve Part 2. Stage 3 was finally performant enough to solve Part 2(quite easily too - it had more in the tank for sure). Achieving 4. would be ideal but I couldn't find it despite spending quite a long time on it.

The key insight that enabled 1. to 2. and more importantly 2. to 3. was the fact that the exact sequence and ordering of the fish and their stages is largely irrelevant, there are no interactions between fish etc - and so just keeping a count of which fish are in which stage is sufficient to model the population frorm generation to generation. This is the idea behind using a hash map(dictionary in python) instead of an array as used in the most crude brute force solution.

## Repository Content

The repository contains two main files: the solution python file and a unit test file.  

There are also 2 txt files which contain test data and the actual data used to submit the answer on the advent of code website.

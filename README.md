# Generative model of non-assortative communities in networks

This code accompanies the paper  <i>"A generative model for community types in directed networks" </i>  by Cathy Liu, [Tristram J. Alexander](https://www.sydney.edu.au/science/about/our-people/academic-staff/tristram-alexander.html), and [Eduardo G. Altmann](https://www.maths.usyd.edu.au/u/ega/), [PNAS Nexus (2023)](https://doi.org/10.1093/pnasnexus/pgad364). 

The Tutorial.ipynb notebook shows how to use the model to reproduce community structures: Assortative, Core-Periphery, Disassortative and Source-Basin based on the classification we proposed in last paper <i> "Non-assortative relationships between groups of nodes are common in complex networks"</i>.

The model is performed in two steps:
1. Initialisation: Start with a an Erdős-Rényi directed graph with $N$ nodes, $\frac{\langle z\rangle}{N-1}$ edge creation probability, and random group allocation of nodes. 
2. Evolution: 
![illu](https://github.com/user-attachments/assets/279c9f01-c2d9-4e33-8646-b133e2e2986a)

## Repository structure:

1. The notebook shows examples of data analysis:

- Tutorial.ipynb: exemplifies the process of implementing generative model.

2. src: python files used to produce our result.

- Model.py includes the implementation of generative model
- User.py includes the node class that can perform rewiring/changing moves during network evolution process
- Statistics.py and summary_stats.py include the classification of community structures.

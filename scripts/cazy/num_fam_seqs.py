# /usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) University of St Andrews 2023
# (c) University of Strathclyde 2023
# (c) James Hutton Institute 2023
#
# Author:
# Emma E. M. Hobbs
#
# Contact
# eemh1@st-andrews.ac.uk
#
# Emma E. M. Hobbs,
# Biomolecular Sciences Building,
# University of St Andrews,
# North Haugh Campus,
# St Andrews,
# KY16 9ST
# Scotland,
# UK
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Count number of download seqs per family of interest"""


import pandas as pd

from Bio import SeqIO


FAMILIES = [
    ['PL1', "data/seqs/pl1.fasta"],
    ['PL9', "data/seqs/pl9.fasta"],
    ['CE8', "data/seqs/ce8.fasta"],
    ['CE12', "data/seqs/ce12.fasta"],
]


def count_seqs(fasta_path):
    """Count num of seqs in fasta file"""
    proteins = 0
    for record in SeqIO.parse(fasta_path, "fasta"):
        proteins += 1
    return proteins

data = []

for (fam, fasta) in FAMILIES:
    data.append([fam, count_seqs(fasta)])

df = pd.DataFrame(data, columns=['Family', 'Num_of_seqs'])
df.to_csv('results/fam_counts/num_of_seqs.csv')

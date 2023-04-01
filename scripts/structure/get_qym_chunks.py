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
"""Break down the QYM protein sequence into overlapping chunks of 500 AA"""


from copy import copy
from pathlib import Path

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

QYM_PATH = "data/seqs/qym_seq.fasta"
BEGIN_AT = 20  # Aa position to begin at - skips signal peptide
OUTDIR = Path("data/seqs/qym_chunks/")

for record in SeqIO.parse(QYM_PATH, "fasta"):
    sequence = str(record.seq)

seq_len = len(sequence)

position = copy(BEGIN_AT)
complete = False
while complete is False:
    chunk_start = position
    chunk_end = position + 501  # captures 500th position
    position = position + 500 - 150

    if (seq_len - position) < 100:  # only a few aa remaining so add to this chunk
        position = seq_len
        chunk_end = seq_len
        complete = True
    
    chunk_seq = sequence[chunk_start: chunk_end]

    print('Chunk:', chunk_start, '-', chunk_end, '-- length:', len(chunk_seq))
    fasta_path = OUTDIR / f"qym_{chunk_start}_{chunk_end}.fasta"
    SeqIO.write(
        [
            SeqRecord(
                seq=Seq(chunk_seq),
                id=f"QYM_{chunk_start}_{chunk_end}",
            ),
        ],
        fasta_path,
        "fasta",
    )

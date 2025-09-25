from itaxotools.blastax.resources import task_pixmaps_large, task_pixmaps_medium

title = "BLAST-Append"
description = "Append matching sequences"

pixmap = task_pixmaps_large.append
pixmap_medium = task_pixmaps_medium.append

long_description = (
    "Given one or more query files and a BLAST database, search the database for sequence matches. "
    "Then append the aligned part of any matching sequences from the database to the original query sequences and save as a new FASTA file. "
    "Query files must be in FASTA or FASTQ format. "
    "Output will consist of two files per query: the BLAST output and a FASTA file."
)

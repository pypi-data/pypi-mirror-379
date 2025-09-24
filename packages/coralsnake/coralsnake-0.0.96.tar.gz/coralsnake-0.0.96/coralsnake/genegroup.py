#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2024 Ye Chang yech1990@gmail.com
# Distributed under terms of the GNU license.
#
# Created: 2024-07-04 23:20


import re
from collections import defaultdict

import numpy as np
import rich.progress
from pyfamsa import Aligner, Sequence
from pysam import FastaFile
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import pdist

from .gtf2tx import read_gtf, top_transcript
from .utils import get_logger

LOGGER = get_logger(__name__)


def group_annot_by_gene_name(annot):
    # annot is dict of dict of Transcript object
    gene_dict = {}
    for _, gene_info in annot.items():
        for _, transcript in gene_info.items():
            if not transcript.gene_name:
                continue
            gene_name = transcript.gene_name
            if gene_name not in gene_dict:
                gene_dict[gene_name] = []
            gene_dict[gene_name].append(transcript)
    return gene_dict


def run_msa(names, seqs, threads=8):
    aligner = Aligner(guide_tree="upgma", threads=threads)
    seqs = [Sequence(n.encode(), s.encode()) for n, s in zip(names, seqs)]
    # tree = aligner.build_tree(seqs)
    # print(tree.dumps())
    msa = aligner.align(seqs)
    return msa


def show_msa(msa):
    for sequence in msa:
        print(sequence.sequence.decode())


def msa_to_array(msa, mask_ratio=0.5):
    arr = np.array([list(sequence.sequence) for sequence in msa])
    return arr


def cluster_sequences(alignment_array, threshold):
    # Calculate pairwise Hamming distances using scipy's pdist function
    def hamming(u, v, **kwargs):
        # return np.sum(u != v) / len(u)
        # but do not calculate the distance of positions where both sequence is a gap
        # note that if one sequence is a gap and the other is not, the distance is 1
        mask = (u == 45) & (v == 45)
        u1 = u[~mask]
        v1 = v[~mask]
        return np.sum(u1 != v1) / len(u1)

    distance_matrix = pdist(alignment_array, metric=hamming)

    if len(distance_matrix) == 0:
        return np.zeros(alignment_array.shape[0], dtype=int)

    # Perform hierarchical clustering using the 'average' method
    Z = linkage(distance_matrix, method="average")

    # Form clusters with a maximum distance threshold
    raw_clusters = fcluster(Z, t=threshold, criterion="distance")

    # Use NumPy to count and sort clusters by size
    unique, counts = np.unique(raw_clusters, return_counts=True)
    sorted_clusters = unique[np.argsort(-counts)]

    # Map original cluster IDs to new ordered IDs
    cluster_map = {cluster_id: i + 1 for i, cluster_id in enumerate(sorted_clusters)}
    ordered_clusters = np.vectorize(cluster_map.get)(raw_clusters)

    return ordered_clusters


def consensus_sequence(arr):
    # find the most common character in each column, and join to get the consensus sequence
    consensus = ""
    for i in range(arr.shape[1]):
        col = arr[:, i]
        unique, counts = np.unique(col, return_counts=True)
        max_count_index = np.argmax(counts)
        consensus += chr(unique[max_count_index])
    return consensus


def get_position_mapping_from_aligned_array(aligned_array):
    def map_positions(aligned_sequence):
        gap_positions = np.where(aligned_sequence == 45)[0]  # Find positions of '-'
        all_positions = np.arange(len(aligned_sequence))
        non_gap_positions = np.setdiff1d(all_positions, gap_positions)

        original_positions = []
        aligned_positions = []

        if len(non_gap_positions) == 0:
            return original_positions, aligned_positions

        start_orig = 0
        start_aligned = non_gap_positions[0]

        for i in range(1, len(non_gap_positions)):
            if non_gap_positions[i] != non_gap_positions[i - 1] + 1:
                end_orig = start_orig + (non_gap_positions[i - 1] - start_aligned) + 1
                end_aligned = non_gap_positions[i - 1] + 1

                original_positions.append((start_orig, end_orig))
                aligned_positions.append((start_aligned, end_aligned))

                start_orig = end_orig
                start_aligned = non_gap_positions[i]

        end_orig = start_orig + (non_gap_positions[-1] - start_aligned) + 1
        end_aligned = non_gap_positions[-1] + 1

        original_positions.append((start_orig, end_orig))
        aligned_positions.append((start_aligned, end_aligned))

        return list(zip(original_positions, aligned_positions))

    for i in range(aligned_array.shape[0]):
        aligned_sequence = aligned_array[i]
        mappings = map_positions(aligned_sequence)
        yield mappings


def map_genome_to_gap_open(genome_span_list, gap_open_list):
    mapping = {}
    gap_counter = 0
    current_gap_start, current_gap_end = gap_open_list[gap_counter]
    for genome_span in genome_span_list:
        genome_start, genome_end = genome_span
        for i in range(genome_start, genome_end + 1):
            if current_gap_start <= current_gap_end:
                mapping[i + 1] = current_gap_start + 1
                current_gap_start += 1
            else:
                gap_counter += 1
                if gap_counter < len(gap_open_list):
                    current_gap_start, current_gap_end = gap_open_list[gap_counter]
                    mapping[i + 1] = current_gap_start + 1
                    current_gap_start += 1
                else:
                    # In case there are more genome positions than gap open positions
                    mapping[i + 1] = None

    return mapping


def rename_snRNA(gene_name):
    # This a temporary fix for snRNA naming
    # RNU2-1 -> U2
    # RNU2-27P -> U2
    # RNU3-2 -> U3
    # RNU5E-10P -> RN5E
    # RNU5A-3P -> RN5E
    # RNU4ATAC7 -> U4ATAC -> U4atac
    # RNU6ATAC7 -> U6ATAC -> U6atac
    # RNVU1-1 -> U1V
    # .., etc
    # for drosophila, snRNA:U2:38ABb -> U2
    if gene_name.startswith("snRNA:"):
        gene_name = gene_name.split(":")[1]
        return gene_name
    patterns = [
        (r"RNU(\d+)(?:-\d+.*)?$", r"U\1"),
        (r"RNU(\d+[A-Z]+)(?:-\d+.*)?$", r"U\1"),
        (r"RNU(\d+)ATAC.*", r"U\1atac"),
        (r"Rnu(\d+)(?:-\d+.*)?$", r"U\1"),
        (r"Rnu(\d+[a-z]+)(?:-\d+.*)?$", r"U\1"),
        (r"Rnu(\d+)atac.*", r"U\1atac"),
        (r"RNVU(\d+)-\d+.*", r"U\1V"),
        (r"[Uu](\d+)ATAC$", r"U\1atac"),
        (r"u(\d+)$", r"U\1"),
        (r"snrnau.*$", r"U\1"),
    ]

    # Apply each pattern and replacement
    for pattern, replacement in patterns:
        gene_name = re.sub(pattern, replacement, gene_name)
    return gene_name


def rename_snoRNA(gene_name):
    # replace rule:
    # replace U3 with SNORD3A
    # replace U3b1 with SNORD3B-1
    # replace U8 with SNORD118
    # replace small nucleolar RNA ACA64 with SNORA64
    # replace Z6
    if gene_name.upper().startswith("ACA"):
        match = re.match(r"ACA(\d+)([A-Z]?)-?(\d*)", gene_name.upper())
        if match:
            number, letter, copy = match.groups()
            # ignore copy number
            return f"SNORA{number}{letter}"
    elif gene_name.upper().startswith("U8"):
        return "SNORD118"
    elif gene_name.upper().startswith("U"):
        # match all other U RNA (WARNING: all snoRD? are there some SNORA?)
        match = re.match(r"U(\d+)([A-Z]?)-?(\d*)", gene_name.upper())
        if match:
            number, letter, copy = match.groups()
            if letter == "":
                letter = "A"
            return f"SNORD{number}{letter}"
    elif gene_name.upper() == "Z6":
        return "Z6"
    return gene_name


def group_genes(
    fa_file_list,
    gtf_file_list,
    out_file=None,
    consensus_fa=None,
    gene_name_regex=None,
    gene_biotype_list=None,
    gene_length_limit=300,
    cluster_threshold=0.1,
    threads=8,
):
    # by default miRNA, tRNA, snoRNA, ...
    if gene_biotype_list is None:
        gene_biotype_list = [
            "tRNA",
            "rRNA",
            "Mt_rRNA",
            "Mt_tRNA",
            "ribozyme",
            "vault_RNA",
            # "7SL_RNA", --> scRNA
            # "7SK_RNA", --> snRNA
            "Y_RNA",
            "miRNA",
            "scaRNA",
            "snoRNA",
            "snRNA",
            "scRNA",
            "ncRNA",
            "misc_RNA",
            "vault_RNA_pseudogene",
            # "7SL_pseudogene",--> scRNA
            # "7SK_pseudogene", --> snRNA
            # "processed_pseudogene",
            "pseudogene",
        ]
    else:
        gene_biotype_list = gene_biotype_list.split(",")

    chrom_to_fa = {}
    LOGGER.info("Loading fasta files")
    for fa_file in fa_file_list:
        fasta = FastaFile(fa_file)
        chrom_to_fa.update({chrom: fasta for chrom in fasta.references})

    LOGGER.info("Loading annotations from gtf file")
    gene_dict_by_name = defaultdict(lambda: defaultdict(list))
    for gtf_file in gtf_file_list:
        gene_dict = read_gtf(
            gtf_file,
            is_gff=gtf_file.endswith("gff") or gtf_file.endswith("gff3"),
            keep_annotation=True,
        )
        for transcript in top_transcript(gene_dict):
            if not transcript.gene_name or not transcript.transcript_biotype:
                continue
            gene_name = transcript.gene_name
            gene_product = transcript._annotations.get("product", "")

            # This is a patch to fix misc_RNA gene names
            # eg, 4       ensembl gene    88330176        88330278        .       -       .       gene_id "ENSG00000207480"; gene_version "1"; gene_name "Y_RNA"; gene_source "ensembl"; gene_biotype "misc_RNA";
            if transcript.transcript_biotype == "misc_RNA":
                # --- Step 1: Prioritize matching specific pseudogene patterns ---
                # Vault RNA pseudogene (e.g., "VTRNA3-1P")
                if gene_name.startswith("VTRNA") and "P" in gene_name:
                    transcript.transcript_biotype = "Vault_RNA_pseudogene"

                # 7SL pseudogene (e.g., "RN7SL521P")
                elif gene_name.startswith("RN7SL") and gene_name.endswith("P"):
                    transcript.transcript_biotype = "scRNA"  # "scRNA_pseudogene"

                # 7SK pseudogene (e.g., "RN7SKP27")
                elif gene_name.startswith("RN7SKP"):
                    transcript.transcript_biotype = "snRNA"  # "snRNA_pseudogene"

                # Y_RNA pseudogene (e.g., "RNY4P28", "RNY1P4")
                elif gene_name.startswith("RNY") and "P" in gene_name:
                    transcript.transcript_biotype = "Y_RNA_pseudogene"

                # --- Step 2: Match the broader functional RNA patterns ---

                # Functional 7SL RNA (e.g., "Metazoa_SRP", "RN7SL2", "7SL")
                elif gene_name.startswith("RN7SL") or gene_name in [
                    "Metazoa_SRP",
                    "7SL",
                ]:
                    transcript.transcript_biotype = "scRNA"

                # Functional Y_RNA (e.g., "Y_RNA", "RNY3", "RNY4")
                elif gene_name.startswith("RNY") or gene_name == "Y_RNA":
                    transcript.transcript_biotype = "Y_RNA"

                # Functional 7SK RNA (now checks for "RN7SK" or "7SK")
                elif gene_name in ["RN7SK", "7SK"]:
                    transcript.transcript_biotype = "snRNA"

                # Functional Vault RNA (so far, only "Vault" is observed)
                elif gene_name == "Vault":
                    transcript.transcript_biotype = "vault_RNA"

                # small Cajal body-specific RNA
                elif gene_name.startswith("SCARNA") or (
                    hasattr(transcript, "product")
                    and "small cajal body" in gene_product.lower()
                ):
                    transcript.transcript_biotype = "scaRNA"

            tx_biotype = transcript.transcript_biotype

            # # This is a temporary fix for misc_RNA naming
            # if tx_biotype == "misc_RNA":
            #     # for mouse reference, there are too many unknown genes
            #     if re.match(r"^Gm\d+$", gene_name):
            #         continue

            # This a temporary fix for snRNA naming
            gene_name = rename_snRNA(gene_name)
            if transcript.transcript_biotype == "snRNA":
                if gene_name.upper().startswith("7SK"):
                    gene_name = "7SK"
                elif gene_name.upper().startswith("SNAR-"):
                    gene_name = re.sub(r"[0-9-]+$", "", gene_name)
                elif gene_name.upper().startswith("U"):
                    pass
                elif (
                    "small nuclear RNA" in gene_product
                    or "spliceosomal RNA" in gene_product
                ):
                    # eg:
                    # U6 spliceosomal RNA
                    # U7 small nuclear RNA
                    gene_name = (
                        gene_product.replace("small nuclear RNA", "")
                        .replace("spliceosomal RNA", "")
                        .strip()
                        .split()[0]
                    )
                else:
                    gene_name = "Ux"

            # This is a temporary fix for the naming of the Y_RNA genes
            if tx_biotype == "Y_RNA":
                if gene_name.upper() == "Y_RNA":
                    gene_name = "RNYx"

            # This is a temporary fix for the naming of the snoRNA genes
            # eg, SNORD115-1 and SNORD115-2 are the same gene
            if tx_biotype == "snoRNA":
                if gene_name.upper().startswith("SNOR"):
                    gene_name = gene_name.rsplit("-")[0]
                    # todo:
                    # SNORD109A and SNORD109B are the same gene
                    # SNORD62A and SNORD62B are the same gene
                elif gene_name.upper().startswith("U") or gene_name.upper().startswith(
                    "RNU"
                ):
                    gene_name = rename_snoRNA(gene_name)
                elif "small nucleolar" in gene_product:
                    # eg:
                    # small nucleolar RNA SNORD51
                    # small nucleolar SNORD12/SNORD106
                    _gene_name = (
                        gene_product.replace("small nucleolar RNA", "")
                        .replace("small nucleolar", "")
                        .strip()
                        .split()[0]
                    )
                    if (
                        gene_name.startswith("Gm")
                        or gene_name.startswith("AF")
                        or gene_name.startswith("DQ")
                    ):
                        gene_name = _gene_name.replace("SNORD", "Snord").replace(
                            "SNORA", "Snora"
                        )
                    elif not _gene_name.upper().startswith("SNOR"):
                        gene_name = rename_snoRNA(_gene_name)
                        if not gene_name.startswith("SNOR"):
                            gene_name = "SNORx"
                    else:
                        gene_name = _gene_name
                else:
                    gene_name = "SNORx"

            # This is a temporary fix for the naming of the scaRNA genes
            if tx_biotype == "scaRNA":
                if (
                    "small Cajal body-specific RNA" in gene_product
                    and not gene_name.upper().startswith("SCARNA")
                ):
                    gene_name = (
                        "SCARNA"
                        + gene_product.replace("small Cajal body-specific RNA", "")
                        .strip()
                        .split()[0]
                    )

            # This is a temporary fix for the naming of the miRNA genes
            if tx_biotype == "miRNA":
                if gene_name.upper().startswith("MIR"):
                    gene_name = gene_name.rsplit("-")[0]
                    # todo: MIR4436B1 and MIR4436B2 are the same gene
                    # patch: Mir3535 is snoRNA
                    if gene_name == "Mir3535":
                        tx_biotype = "snoRNA"
                        gene_name = "SNORx"
                elif "LET" in gene_name.upper() or "MIR" in gene_name.upper():
                    pass
                else:
                    gene_name = "MIRx"

            # This is a temporary fix for the naming of the tRNA genes
            if "_tRNA-" in gene_name:
                gene_name = "tRNA-" + gene_name.split("_tRNA-", 1)[1]
            if tx_biotype == "tRNA" and not gene_name.startswith("tRNA"):
                if gene_name == "":
                    gene_name = "unknown"
                gene_name = "tRNA-" + gene_name
            # Caenorhabditis_elegans_tRNA-Lys-CTT-1-7
            # remove the number suffix "-1-7"
            # loop from right to left and stop until reach a non-digit character
            # rmove digits and "-"
            if gene_name.startswith("tRNA-"):
                # gene_name = re.sub(r"-[0-9-]+$", "", gene_name)
                gene_name = re.sub(r"[0-9-]+$", "", gene_name)

            gene_dict_by_name[tx_biotype][gene_name].append(transcript)

    # sort the 1st level and 2nd level of gene_dict_by_name
    gene_dict_by_name = {
        k: dict(sorted(v.items(), key=lambda item: item[0]))
        for k, v in sorted(gene_dict_by_name.items(), key=lambda item: item[0])
    }

    # adjust gene dict, rule:
    # within each biotype, if the gene_name is one of ["SNORx", "MIRx", "Ux", "RNYx"]
    # iter the transcript list of this gene_name, and compare with other genes
    # 1. get the seq for each transcript (storge into tx._seq by default)
    tx_to_unname = {"snoRNA": "SNORx", "miRNA": "MIRx", "snRNA": "Ux", "Y_RNA": "RNYx"}
    for tx_biotype, tx_dict in rich.progress.track(
        gene_dict_by_name.items(),
        description="Preprocessing genes...",
    ):
        if all(not (x == tx_biotype and y in tx_dict) for x, y in tx_to_unname.items()):
            continue
        for gene_name, tx_list in rich.progress.track(
            tx_dict.items(),
            description=f"Preprocessing genes ({tx_biotype})...",
        ):
            for tx in tx_list:
                tx._seq = tx.get_seq(chrom_to_fa[tx.chrom])
        # 2. for each biotype, loop tx in gene_name in ["SNORx", "MIRx", "Ux", "RNYx"]
        unnamed_gene = tx_to_unname[tx_biotype]
        for tx in tx_dict[unnamed_gene]:
            for target_gene, tx_list in tx_dict.items():
                if target_gene == unnamed_gene:
                    continue
                for tx2 in tx_list:
                    if (tx._seq in tx2._seq and len(tx._seq) > 0.5 * len(tx2._seq)) or (
                        tx2._seq in tx._seq and len(tx2._seq) > 0.9 * len(tx._seq)
                    ):
                        tx_dict[unnamed_gene].remove(tx)
                        tx_dict[target_gene].append(tx)
                        break
                else:
                    continue
                break

    # if out_file is None write to stdout
    if out_file:
        out = open(out_file, "w")
    else:
        import sys

        out = sys.stdout
    # if consensus_fa is not None, write to the file
    if consensus_fa:
        out_fa = open(consensus_fa, "w")

    for tx_biotype, tx_dict in rich.progress.track(
        gene_dict_by_name.items(),
        description="Groupping genes...",
    ):
        if gene_biotype_list:
            if tx_biotype not in gene_biotype_list:
                continue
        for gene_name, tx_list in rich.progress.track(
            tx_dict.items(),
            description=f"Groupping genes ({tx_biotype})...",
        ):
            if gene_name_regex:
                if not re.search(gene_name_regex, gene_name):
                    continue

            # only cluster short genes shorter than 300bp
            if gene_length_limit:
                tx_list = [tx for tx in tx_list if tx.length <= gene_length_limit]

            names = [tx.gene_id for tx in tx_list]
            seqs = [tx.get_seq(chrom_to_fa[tx.chrom]) for tx in tx_list]
            if len(names) == 0:
                continue

            exon_spans_list = [tx.exons.values() for tx in tx_list]
            if len(tx_list) < 2:
                cluster_ids = np.arange(1, len(tx_list) + 1, dtype=int)
            else:
                msa = run_msa(names, seqs)
                aligned_array = msa_to_array(msa)
                cluster_ids = cluster_sequences(aligned_array, cluster_threshold)
            # loop the cluster ids and redo the msa for each sub-group
            for cluster_id in np.unique(cluster_ids):
                cluster_tx_list = [
                    tx for tx, cid in zip(tx_list, cluster_ids) if cid == cluster_id
                ]
                cluster_names = [
                    name for name, cid in zip(names, cluster_ids) if cid == cluster_id
                ]
                cluster_seqs = [
                    seq for seq, cid in zip(seqs, cluster_ids) if cid == cluster_id
                ]
                cluster_exon_spans_list = [
                    spans
                    for spans, cid in zip(exon_spans_list, cluster_ids)
                    if cid == cluster_id
                ]
                cluster_msa = run_msa(cluster_names, cluster_seqs, threads)
                cluster_aligned_array = msa_to_array(cluster_msa)
                cluster_consensus = consensus_sequence(cluster_aligned_array)

                # write artificial fasta file for the consensus sequences
                # header: >transcript_biotype-gene_name-cluster_id N={number of sequences in the cluster} list_of_gene_id_joined_by"|"
                # only output cluster_id less than or equal to 5, or the cluster size is greater than or equal to 3
                if consensus_fa:
                    if (
                        cluster_id <= 5
                        or len(cluster_names) >= 3
                        or gene_name in ["SNORx", "MIRx", "Ux", "RNYx"]
                        or not all(
                            n.startswith("ENS")
                            or n.startswith("LOC")
                            or n.startswith("Gm")
                            for n in cluster_names
                        )
                    ):
                        out_fa.write(
                            f">{tx_biotype}-{gene_name}-cluster{cluster_id} N={len(cluster_names)} members={'|'.join(cluster_names)}\n"
                            f"{cluster_consensus.replace('-', '').upper()}\n"
                        )

                for i, mapping in enumerate(
                    get_position_mapping_from_aligned_array(cluster_aligned_array)
                ):
                    msa_spans = []
                    for _, aligned_span in mapping:
                        msa_spans.append(aligned_span)
                    # d = map_genome_to_gap_open(cluster_exon_spans_list[i], msa_spans)
                    # d_str = ",".join([f"{k}:{v}" for k, v in d.items()])
                    # out.write(f"{gene_name}\t{cluster_id}\t{cluster_names[i]}\t{d_str}\n")
                    exon_spans_str = ",".join(
                        [
                            f"{start + 1}-{end + 1}"
                            for start, end in cluster_exon_spans_list[i]
                        ]
                    )
                    msa_spans_str = ",".join(
                        [
                            f"{start + 1}-{end + 1}"
                            for start, end in msa_spans
                            if start is not None and end is not None
                        ]
                    )
                    tx = cluster_tx_list[i]
                    tx_seq = tx.get_seq(chrom_to_fa[tx.chrom])
                    out.write(
                        f"{gene_name}\t{cluster_id}\t{len(cluster_names)}\t{cluster_consensus}\t"
                        f"{tx_biotype}\t{cluster_names[i]}\t{tx.chrom}\t{exon_spans_str}\t{tx.strand}\t{tx_seq}\t"
                        f"{msa_spans_str}\n"
                    )
    if out_file:
        out.close()
    if consensus_fa:
        out_fa.close()


if __name__ == "__main__":
    group_genes("../demo/subset.fa", "../demo/subset.tsv")

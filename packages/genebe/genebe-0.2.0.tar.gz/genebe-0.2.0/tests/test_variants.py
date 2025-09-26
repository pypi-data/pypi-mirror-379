"""Tests for variant annotation functionality."""

import pytest
import genebe as gb


def test_annotate_variants_list():
    """Test case for annotating variants."""
    variants = ["6-160585140-T-G"]
    annotations = gb.annotate_variants_list(
        variants,
        use_ensembl=True,
        use_refseq=False,
        genome="hg38",
        batch_size=500,
        use_netrc=False,
        endpoint_url="https://api.genebe.net/cloud/api-public/v1/variants",
    )

    # Assertions
    assert len(annotations) == len(variants)

    anns = annotations[0]
    print(anns)

    assert anns["chr"] == "6"
    assert anns["pos"] == 160585140


def test_gbid_generation():
    """Test GBID generation."""
    chr = "1"
    pos = 16044378
    ref = "C"
    alt = "CACACACACAT"
    encoded = gb.encode_vcf_variant_gbid(chr, pos, ref, alt)
    assert encoded == 17227519582999023


@pytest.mark.network
def test_annotate_with_list():
    """Test annotate with list of variants - marked as slow test."""
    variants = ["7-69599651-A-G", "6-160585140-T-G"]
    annotations = gb.annotate(
        variants,
        use_ensembl=True,
        use_refseq=False,
        genome="hg38",
        batch_size=500,
        flatten_consequences=True,
        use_netrc=True,
        output_format="list",
    )

    assert isinstance(annotations, list)
    assert len(annotations) == len(variants)

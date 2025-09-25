import pytest
import filecmp
import os

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

import sequensign

data_path = os.path.join("tests", "data")
seq_path = os.path.join(data_path, "seq.txt")
asc_path = os.path.join(data_path, "seq.asc")
genbank_path = os.path.join(data_path, "seq.gb")


def test_write_seq_in_record_to_file(tmpdir):
    # Also tests get_seq_from_record()
    # and write_text_to_file()
    record = SeqIO.read(genbank_path, "genbank")
    write_path = os.path.join(str(tmpdir), "seq.txt")
    sequensign.write_seq_in_record_to_file(record, filename=write_path)

    assert filecmp.cmp(write_path, seq_path)


def test_write_sigs_in_record_to_file(tmpdir):
    # Also tests get_sig_from_record()
    # and write_sigs_to_file()
    record = SeqIO.read(genbank_path, "genbank")
    write_stem = os.path.join(str(tmpdir), "seq")
    sequensign.write_sigs_in_record_to_file(record, filestem=write_stem)

    out_asc_path = write_stem + "_1.asc"

    assert filecmp.cmp(out_asc_path, asc_path)


def test_add_sig_to_record(tmpdir):
    # Also tests read_text_from_file()
    seq = sequensign.read_text_from_file(seq_path)
    sig = sequensign.read_text_from_file(asc_path)
    seqrecord = SeqRecord(Seq(seq), id="seq", annotations={"molecule_type": "DNA"})
    seqrecord.annotations["topology"] = "linear"
    seqrecord.annotations["data_file_division"] = "SYN"
    seqrecord.annotations["date"] = "24-SEP-2025"

    sequensign.add_sig_to_record(seqrecord, sig)

    write_path = os.path.join(str(tmpdir), "seq.gb")
    with open(write_path, "w") as output_handle:
        SeqIO.write(seqrecord, output_handle, "genbank")

    assert filecmp.cmp(write_path, genbank_path)

# Copyright 2025 Edinburgh Genome Foundry, University of Edinburgh
#
# This file is part of Sequensign.
#
# Sequensign is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# Sequensign is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Ediacara. If not, see <https://www.gnu.org/licenses/>.

import warnings


DNA_BASES = ["A", "C", "G", "T"]
RNA_BASES = ["A", "C", "G", "U"]
# For simplicity, we treat DNA/RNA together:
NA_BASES = ["A", "C", "G", "T"] + ["U"]
NA_IUPAC_BASES = [
    "G",
    "A",
    "T",
    "C",
    "R",
    "Y",
    "M",
    "K",
    "S",
    "W",
    "H",
    "B",
    "V",
    "D",
    "N",
] + ["U"]

AA_LETTERS = [
    "A",
    "R",
    "N",
    "D",
    "C",
    "Q",
    "E",
    "G",
    "H",
    "I",
    "L",
    "K",
    "M",
    "F",
    "P",
    "S",
    "T",
    "W",
    "Y",
    "V",
    "B",
    "J",
    "Z",
    "X",
    "*",
]


def get_seq_from_record(record):
    """Get sequence from a Biopython record.

    This is a key function that ensures text representation is always the same.

    Parameters
    ----------
    record: SeqRecord
    """
    sequence = str(record.seq).upper()
    seq_letters = set(sequence)
    if "NA" in record.annotations["molecule_type"]:
        if bool(set(seq_letters) - set(NA_BASES)):
            print("Note: the sequence contains nonstandard letters.")
            if bool(set(seq_letters) - set(NA_IUPAC_BASES)):
                warnings.warn("the sequence contains non-IUPAC letters!")
    if "protein" == record.annotations["molecule_type"]:
        if bool(set(seq_letters) - set(AA_LETTERS)):
            warnings.warn("the sequence contains nonstandard letters!")

    return sequence


def get_sig_from_record(record, sig_markers=None):
    """Get signatures from a Biopython record.

    The returned signatures include the begin/end tokens.
    Default setting looks for PGP signatures.

    Parameters
    ----------
    record: SeqRecord
    sig_markers: tuple
        Text that marks the begin and the end of a signature: `("begin", "end")`.
    """
    # We look for PGP signatures by default
    if not sig_markers:
        sig_begin_txt = "-----BEGIN PGP SIGNATURE-----"
        sig_end_txt = "-----END PGP SIGNATURE-----"
        is_pgp = True
    else:
        sig_begin_txt = sig_markers[0]
        sig_end_txt = sig_markers[1]
        is_pgp = False
    text = record.annotations["comment"]

    sig_index_pairs = []
    begin_length = len(sig_begin_txt)
    end_length = len(sig_end_txt)
    text_length = len(text)
    search_position = 0
    pending_begin_index = None

    # This block extracts all signatures bounded by a begin and an end token.
    # Signatures are sequential, don't overlap, not nested.
    # If a new begin appears before an end, discard the previous begin.
    while search_position <= text_length:
        if pending_begin_index is None:
            next_begin_index = text.find(sig_begin_txt, search_position)
            if next_begin_index == -1:  # "not found"
                break  # no signature
            pending_begin_index = next_begin_index
            search_position = next_begin_index + begin_length
        else:  # pending begin
            next_end_index = text.find(sig_end_txt, search_position)

            if next_end_index == -1:  # no end
                break
            else:  # we have an end
                next_begin_index = text.find(sig_begin_txt, search_position)
                if next_begin_index == -1:  # no other begin
                    sig_index_pairs.append((pending_begin_index, next_end_index))
                    pending_begin_index = None
                    search_position = next_end_index + end_length
                else:
                    if next_begin_index <= next_end_index:
                        # new begin before an end: reset the pending begin to this new one
                        pending_begin_index = next_begin_index
                        search_position = next_begin_index + begin_length
                    else:  # end before any new begin
                        sig_index_pairs.append((pending_begin_index, next_end_index))
                        pending_begin_index = None
                        search_position = next_end_index + end_length

    signatures = []
    for begin, end in sig_index_pairs:
        extracted_signature = text[begin : end + len(sig_end_txt)]
        # Biopython removes empty lines in Genbank `COMMENTS`.
        # That changes signatures with empty lines.
        # We fix this issue for PGP signatures:
        if is_pgp:
            if extracted_signature.startswith(sig_begin_txt + "\n\n"):
                corrected_signature = extracted_signature
            else:
                corrected_signature = extracted_signature.replace(
                    sig_begin_txt, sig_begin_txt + "\n", 1
                )
            # We also append a newline so that the signature text
            # is identical to the text file created by GPG:
            signatures += [corrected_signature + "\n"]

    if len(signatures) == 0:
        warnings.warn("there are no signatures in the record.")
    if len(signatures) > 1:
        print("Note: there are %d signatures in the record." % len(signatures))

    return signatures


def write_text_to_file(text, filename):
    """Write a `str` to a file.

    Parameters
    ----------
    text: str
    filename: str
    """
    with open(filename, "wb") as f:
        f.write(text.encode("utf-8"))


def write_seq_in_record_to_file(record, filename=None):
    """Write a sequence in a Biopython record into a file.

    Parameters
    ----------
    record: SeqRecord
    filename: str
        Default uses `record.id` as filestem.
    """
    if not filename:
        filename = record.id + ".txt"
    seq = get_seq_from_record(record)
    write_text_to_file(text=seq, filename=filename)


def write_sigs_to_file(sigs, filestem):
    """Write signatures into a file.

    Parameters
    ----------
    sigs: list
        List of signatures (`str`).
    filestem: str
        Each signature is saved in a different file, in the `filestem_1.txt` pattern.
    """
    counter = 1
    for sig in sigs:
        filename = filestem + "_" + str(counter) + ".asc"
        write_text_to_file(text=sig, filename=filename)
        counter += 1


def write_sigs_in_record_to_file(record, filestem=None):
    """Write signatures in a Biopython record into a file.

    Parameters
    ----------
    record: SeqRecord
    filestem: str
        Default uses `record.id` as filestem.
    """
    if not filestem:
        filestem = record.id
    signatures = get_sig_from_record(record)
    write_sigs_to_file(sigs=signatures, filestem=filestem)


def read_text_from_file(filename):
    """Read text from a file.

    Parameters
    ----------
    filename: str
    """
    with open(filename, "r") as file:
        text = file.read()
        return text


def add_sig_to_record(record, sig):
    """Append signature to a Biopython record.

    Parameters
    ----------
    record: SeqRecord
    sig: str
    """
    try:
        record.annotations["comment"] += "\n" + sig
    except KeyError:  # create if doesn't exist
        record.annotations["comment"] = sig

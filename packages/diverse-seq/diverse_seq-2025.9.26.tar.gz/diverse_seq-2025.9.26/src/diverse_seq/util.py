import contextlib
import functools
import math
import os
import pathlib
import re
import sys
import typing

import numpy
from cogent3 import get_moltype
from cogent3.app import composable
from rich import text as rich_text

try:
    from wakepy.keep import running as keep_running

    # trap flaky behaviour on linux
    with keep_running():
        ...

except (NotImplementedError, ImportError):
    keep_running = contextlib.nullcontext

if typing.TYPE_CHECKING:
    from click.core import Context, Option


@composable.define_app
class str2arr:
    """convert string to array of uint8"""

    def __init__(self, moltype: str = "dna", max_length: int | None = None) -> None:
        self.max_length = max_length
        mt = get_moltype(moltype)
        self.alphabet = mt.most_degen_alphabet()

    def main(self, data: str) -> numpy.ndarray:
        if self.max_length:
            data = data[: self.max_length]

        return self.alphabet.to_indices(data)


@composable.define_app
class arr2str:
    """convert array of uint8 to str"""

    def __init__(self, moltype: str = "dna", max_length: int | None = None) -> None:
        self.max_length = max_length
        mt = get_moltype(moltype)
        self.alphabet = mt.most_degen_alphabet()

    def main(self, data: numpy.ndarray) -> str:
        if self.max_length:
            data = data[: self.max_length]

        return self.alphabet.from_indices(data)


# we allow for file suffixes to include compression extensions
_fasta_format = re.compile("(fasta|mfa|faa|fna|fa)([.][a-zA-Z0-9]+)?$")
_genbank_format = re.compile("(genbank|gbk|gb|gbff)([.][a-zA-Z0-9]+)?$")


def get_seq_file_format(suffix: str) -> str:
    """returns format string

    Notes
    -----
    Based on cogent3 suffixes, returns either 'fasta' or 'genbank'
    or None.
    """
    if _fasta_format.match(suffix):
        return "fasta"
    return "genbank" if _genbank_format.match(suffix) else None


def determine_chunk_size(total_items, num_chunks):
    """chunk sizes for distributing items into approximately equal chunks"""
    base_chunk_size = total_items // num_chunks
    remainder = total_items % num_chunks

    return [
        base_chunk_size + 1 if i < remainder else base_chunk_size
        for i in range(num_chunks)
    ]


def chunked(iterable, num_chunks, verbose=False):
    sizes = determine_chunk_size(len(iterable), num_chunks)
    if verbose:
        print(f"chunk sizes: {sizes}")

    cum_sizes = numpy.array(sizes).cumsum()
    starts = [0] + cum_sizes[:-1].tolist()
    start_stop = numpy.array([starts, cum_sizes]).T
    for start, end in start_stop:
        yield iterable[start:end]


class summary_stats:
    """computes the summary statistics for a set of numbers"""

    def __init__(self, numbers: numpy.ndarray):
        self._numbers = numbers

    @functools.cached_property
    def n(self):
        return len(self._numbers)

    @functools.cached_property
    def mean(self):
        return math.fsum(self._numbers) / self.n

    @functools.cached_property
    def var(self):
        """unbiased estimate of the variance"""
        return math.fsum((x - self.mean) ** 2 for x in self._numbers) / (self.n - 1)

    @functools.cached_property
    def std(self):
        """standard deviation"""
        return self.var**0.5

    @functools.cached_property
    def cov(self):
        return self.std / self.mean


def _comma_sep_or_file(
    ctx: "Context",  # noqa: ARG001
    param: "Option",  # noqa: ARG001
    include: str,
) -> list[str] | None:
    if include is None:
        return None
    if pathlib.Path(include).is_file():
        path = pathlib.Path(include)
        names = path.read_text().splitlines()
        return [name.strip() for name in names]
    return [n.strip() for n in include.split(",") if n.strip()]


def _hide_progress(
    ctx: "Context",  # noqa: ARG001
    param: "Option",  # noqa: ARG001
    hide_progress: str,
) -> bool:
    return True if "DVS_HIDE_PROGRESS" in os.environ else hide_progress


def _check_h5_dstore(
    ctx: "Context",  # noqa: ARG001
    param: "Option",  # noqa: ARG001
    path: pathlib.Path,
) -> pathlib.Path:
    """makes sure minimum number of sequences are in the store"""
    from diverse_seq import data_store

    seqids = data_store.get_seqids_from_store(path)
    min_num = 5
    if len(seqids) >= min_num:
        return path

    msg = f"SKIPPING: '{path}' does not have ≥{min_num} sequences!"
    print_colour(msg, "red")
    sys.exit(1)


class _printer:
    from rich.console import Console

    def __init__(self) -> None:
        self._console = self.Console()

    def __call__(self, txt: str, colour: str):
        """print text in colour"""
        msg = rich_text.Text(txt)
        msg.stylize(colour)
        self._console.print(msg)


def get_sample_data_path() -> pathlib.Path:
    """returns path to sample data file"""
    from diverse_seq import data

    path = pathlib.Path(data.__path__[0]) / "brca1.fa"

    path = path.absolute()
    if not path.exists():
        msg = f"sample data file {str(path)!r} does not exist"
        raise ValueError(msg)

    return pathlib.Path(path)


print_colour = _printer()

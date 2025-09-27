import os
from io import BytesIO
import gzip
import urllib.request
import shutil
import fsspec
import numpy as np

import pysegy as seg  # noqa: E402
from pysegy.ibm import ibm_to_ieee  # noqa: E402
from pysegy.types import FileHeader, BinaryTraceHeader, SeisBlock  # noqa: E402

DATAFILE = os.path.join(
    os.path.dirname(__file__), "..", "..", "data",
    "overthrust_2D_shot_1_20.segy",
)


def test_read():
    block = seg.segy_read(DATAFILE)
    assert block.fileheader.bfh.ns == 751
    assert len(block.traceheaders) == 3300
    assert block.traceheaders[0].SourceX == 400
    assert block.traceheaders[0].GroupX == 100


def test_write_roundtrip(tmp_path):
    fh = FileHeader()
    fh.bfh.ns = 4
    fh.bfh.DataSampleFormat = 5
    headers = [BinaryTraceHeader() for _ in range(2)]
    for th in headers:
        th.ns = 4
        th.SourceX = 1234
    data = np.array([[float(i*j) for j in range(2)] for i in range(4)])
    block = SeisBlock(fh, headers, data)
    tmp = tmp_path / 'temp.segy'
    seg.segy_write(str(tmp), block)
    out = seg.segy_read(str(tmp))
    assert out.fileheader.bfh.ns == 4
    assert out.traceheaders[0].SourceX == 1234
    assert np.all(out.data == data)


def test_ibm_conversion():
    """
    Ensure IBM -> IEEE conversion works for known constant.
    """
    assert ibm_to_ieee(b"\x41\x10\x00\x00") == 1.0


def test_fileheader_io():
    """
    Round-trip a file header using in-memory bytes.
    """
    fh = FileHeader()
    fh.bfh.Job = 99
    fh.bfh.Line = 123
    buf = BytesIO()
    seg.write.write_fileheader(buf, fh)
    buf.seek(0)
    out = seg.read.read_fileheader(buf)
    assert out.bfh.Job == 99
    assert out.bfh.Line == 123
    assert len(buf.getvalue()) == 3600


def test_write_read_block_bytesio():
    """
    Write and read a simple block using BytesIO.
    """
    fh = FileHeader()
    fh.bfh.ns = 2
    fh.bfh.DataSampleFormat = 5
    headers = [BinaryTraceHeader() for _ in range(1)]
    headers[0].ns = 2
    data = np.array([[1.0], [2.0]])
    block = SeisBlock(fh, headers, data)
    bio = BytesIO()
    seg.write.write_block(bio, block)
    bio.seek(0)
    out = seg.read.read_file(bio)
    assert np.all(out.data == data)


def test_read_with_filesystem():
    fs = fsspec.filesystem("file")
    block = seg.segy_read(DATAFILE, fs=fs)
    assert block.fileheader.bfh.ns == 751


def test_write_with_filesystem(tmp_path):
    fs = fsspec.filesystem("file")
    fh = FileHeader()
    fh.bfh.ns = 2
    fh.bfh.DataSampleFormat = 5
    hdr = BinaryTraceHeader()
    hdr.ns = 2
    hdr.SourceX = 111
    data = np.array([[1.0], [2.0]])
    block = SeisBlock(fh, [hdr], data)
    dest = tmp_path / "fsout.segy"
    seg.segy_write(str(dest), block, fs=fs)
    out = seg.segy_read(str(dest), fs=fs)
    assert out.fileheader.bfh.ns == 2
    assert out.traceheaders[0].SourceX == 111


BP_URL = (
    "http://s3.amazonaws.com/open.source.geoscience/"
    "open_data/bpmodel94/Model94_shots.segy.gz"
)


def test_bp_model_headers():
    """
    Download a portion of the BP model data and verify header values.
    """
    response = urllib.request.urlopen(BP_URL)
    with gzip.GzipFile(fileobj=response) as gz:
        data = gz.read(40000)
    fh = seg.read.read_fileheader(BytesIO(data))
    assert fh.bfh.dt == 4000
    assert fh.bfh.ns == 2000
    assert fh.bfh.DataSampleFormat == 1
    bio = BytesIO(data)
    bio.seek(3600)
    th = seg.read.read_traceheader(bio)
    assert th.ns == 2000
    assert th.SourceX == 0
    assert th.GroupX == 15


def test_bp_model_scan(tmp_path):
    """Download the full BP Model dataset and verify shot statistics.

    The dataset contains 278 distinct shot locations. Receiver counts vary
    between 240 and 480 per shot. This test ensures the reader can process the
    entire file and that these counts match the known reference values.
    """
    dest = tmp_path / "Model94_shots.segy"
    response = urllib.request.urlopen(BP_URL)
    with gzip.GzipFile(fileobj=response) as gz, open(dest, "wb") as f:
        shutil.copyfileobj(gz, f)

    scan = seg.segy_scan(str(dest))

    fh = scan.fileheader
    shots = scan.shots
    counts = scan.counts

    ns = fh.bfh.ns
    trace_size = 240 + ns * 4
    with open(dest, "rb") as f:
        f.seek(0, os.SEEK_END)
        total = (f.tell() - 3600) // trace_size

    assert total == int(sum(counts))
    assert len(shots) == 278
    assert int(min(counts)) == 240
    assert int(max(counts)) == 480

    hdrs = scan.read_headers(0, keys=["GroupX"])
    assert hdrs[0].GroupX == 15
    assert len(hdrs) == counts[0]


def test_scan_directory_pattern():
    data_dir = os.path.join(
        os.path.dirname(__file__), "..", "..", "data"
    )
    scan = seg.segy_scan(
        data_dir, "overthrust_2D_shot_*.segy", keys=["GroupX"]
    )
    assert isinstance(scan, seg.SegyScan)
    assert len(scan.shots) == 97
    assert len(set(scan.paths)) == 5
    idx = 0  # first shot across all files
    assert scan.paths[idx].endswith("overthrust_2D_shot_1_20.segy")
    assert scan.counts[idx] == 127
    assert scan.summary(idx)["GroupX"] == (100, 6400)


def test_scan_with_filesystem():
    fs = fsspec.filesystem("file")
    data_dir = os.path.join(
        os.path.dirname(__file__), "..", "..", "data"
    )
    scan = seg.segy_scan(
        data_dir,
        "overthrust_2D_shot_*.segy",
        keys=["GroupX"],
        fs=fs,
    )
    assert isinstance(scan, seg.SegyScan)
    assert len(scan.shots) == 97


def test_scan_unsorted_traces(tmp_path):
    """
    Ensure scanning handles files with interleaved shots.
    """
    fh = FileHeader()
    fh.bfh.ns = 1
    fh.bfh.DataSampleFormat = 5

    hdr1 = BinaryTraceHeader()
    hdr1.ns = 1
    hdr1.SourceX = 1
    hdr1.SourceY = 1
    hdr1.GroupX = 1

    hdr2 = BinaryTraceHeader()
    hdr2.ns = 1
    hdr2.SourceX = 2
    hdr2.SourceY = 2
    hdr2.GroupX = 2

    hdr3 = BinaryTraceHeader()
    hdr3.ns = 1
    hdr3.SourceX = 1
    hdr3.SourceY = 1
    hdr3.GroupX = 3

    headers = [hdr1, hdr2, hdr3]
    data = np.zeros((1, 3), dtype=np.float32)
    block = SeisBlock(fh, headers, data)
    tmp = tmp_path / "unsorted.segy"
    with open(tmp, "wb") as f:
        seg.write.write_block(f, block)

    scan = seg.segy_scan(str(tmp), keys=["GroupX"])
    assert len(scan.shots) == 2
    assert scan.shots[0] == (1.0, 1.0, 0.0)
    assert scan.counts == [2, 1]
    assert scan.summary(0)["GroupX"] == (1, 3)


def test_scan_by_receiver_gather(tmp_path):
    """
    Group traces by receiver location instead of source.
    """
    fh = FileHeader()
    fh.bfh.ns = 1
    fh.bfh.DataSampleFormat = 5

    h1 = BinaryTraceHeader()
    h1.ns = 1
    h1.SourceX = 1
    h1.SourceY = 1
    h1.GroupX = 5
    h1.GroupY = 0

    h2 = BinaryTraceHeader()
    h2.ns = 1
    h2.SourceX = 2
    h2.SourceY = 2
    h2.GroupX = 5
    h2.GroupY = 0

    h3 = BinaryTraceHeader()
    h3.ns = 1
    h3.SourceX = 3
    h3.SourceY = 3
    h3.GroupX = 10
    h3.GroupY = 0

    headers = [h1, h2, h3]
    data = np.zeros((1, 3), dtype=np.float32)
    block = SeisBlock(fh, headers, data)
    tmp = tmp_path / "rec_gather.segy"
    with open(tmp, "wb") as f:
        seg.write.write_block(f, block)

    scan = seg.segy_scan(str(tmp), by_receiver=True)
    assert len(scan.shots) == 2
    assert scan.counts == [2, 1]
    assert scan.shots[0] == (5.0, 0.0, 0.0)
    coords = scan[0].rec_coordinates
    assert coords.shape == (2, 3)
    assert tuple(coords[0]) == (1.0, 1.0, 0.0)


def test_save_and_load_scan(tmp_path):
    scan = seg.segy_scan(DATAFILE)
    dest = tmp_path / "scan.pkl"
    seg.save_scan(str(dest), scan)
    out = seg.load_scan(str(dest))
    assert isinstance(out, seg.SegyScan)
    assert out.shots == scan.shots
    assert out.counts == scan.counts


def test_save_and_load_scan_fs(tmp_path):
    fs = fsspec.filesystem("file")
    scan = seg.segy_scan(DATAFILE)
    dest = tmp_path / "scan_fs.pkl"
    seg.save_scan(str(dest), scan, fs=fs)
    out = seg.load_scan(str(dest), fs=fs)
    assert out.shots == scan.shots


def test_index_and_lazy_data():
    scan = seg.segy_scan(DATAFILE)
    rec = scan[0]
    assert rec.coordinates == scan.shots[0]
    assert rec._data is None
    rec.data
    assert rec.data is not None
    assert rec._data is not None
    assert rec.fileheader.bfh.ns == scan.fileheader.bfh.ns
    all_blocks = scan.data
    assert len(all_blocks) == len(scan.shots)


def test_rec_coordinates():
    scan = seg.segy_scan(DATAFILE)
    rec = scan[0]
    coords = rec.rec_coordinates
    assert coords.shape[0] == scan.counts[0]
    assert tuple(coords[0]) == (100.0, 0.0, 0.0)


def test_get_header_scaling():
    fh = FileHeader()
    fh.bfh.ns = 1
    fh.bfh.DataSampleFormat = 5

    h1 = BinaryTraceHeader()
    h1.ns = 1
    h1.SourceX = 10
    h1.RecSourceScalar = 2

    h2 = BinaryTraceHeader()
    h2.ns = 1
    h2.SourceX = 20
    h2.RecSourceScalar = -2

    h3 = BinaryTraceHeader()
    h3.ns = 1
    h3.SourceX = 5
    h3.RecSourceScalar = 1

    h4 = BinaryTraceHeader()
    h4.ns = 1
    h4.SourceX = 7
    h4.RecSourceScalar = 0

    headers = [h1, h2, h3, h4]
    block = SeisBlock(fh, headers, np.zeros((1, 4), dtype=np.float32))

    vals = seg.get_header(block, "SourceX")
    assert vals[:2] == [20, 10]
    assert vals[2:] == [5, 7]

    raw = seg.get_header(block, "SourceX", scale=False)
    assert raw == [10, 20, 5, 7]

import pytest

from xferx.pdp11.dos11fs import DOS11Filesystem, UserFileDirectoryBlock
from xferx.shell import Shell

DSK = "tests/dsk/dos11_dectape.tap"


def test_dos11_dectape():
    shell = Shell(verbose=True)
    shell.onecmd(f"mount t: /dos11 {DSK}", batch=True)
    fs = shell.volumes.get_volume('T')
    assert isinstance(fs, DOS11Filesystem)

    shell.onecmd("dir t:[*,*]", batch=True)
    shell.onecmd("dir /uic t:", batch=True)
    shell.onecmd("type t:1.txt", batch=True)

    x = fs.read_bytes("1000.txt")
    x = x.rstrip(b"\0")
    assert len(x) == 44000
    for i in range(0, 1000):
        assert f"{i:5d} ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890".encode("ascii") in x

    l = list(fs.entries_list)
    assert len(l) == 9


def test_dos11_dectape_bitmap():
    shell = Shell(verbose=True)
    shell.onecmd(f"copy {DSK} {DSK}.mo", batch=True)
    shell.onecmd(f"mount t: /dos11 {DSK}.mo", batch=True)
    fs = shell.volumes.get_volume('T')
    assert isinstance(fs, DOS11Filesystem)

    d = fs.get_file_entry("[1,1]500.TXT")
    assert d is not None
    assert not d.contiguous

    # Write UFD
    d.ufd_block.write()
    ufd_block2 = UserFileDirectoryBlock.read(d.ufd_block.fs, d.ufd_block.uic, d.ufd_block.block_number)
    assert str(d.ufd_block) == str(ufd_block2)

    # Delete linked file
    d.delete()
    with pytest.raises(FileNotFoundError):
        fs.get_file_entry("[200,200]500.TXT")

    # UIC not found
    with pytest.raises(Exception):
        shell.onecmd("copy /TYPE:CONTIGUOUS t:10.TXT t:[123,321]10NEW.TXT", batch=True)

    # Create a contiguous file
    shell.onecmd("copy /TYPE:CONTIGUOUS t:10.TXT t:10NEW.TXT", batch=True)
    x2 = fs.read_bytes("10NEW.txt")
    x2 = x2.rstrip(b"\0")
    assert len(x2) == 440
    for i in range(0, 10):
        assert f"{i:5d} ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890".encode("ascii") in x2

    # Create a non-contiguous file
    shell.onecmd("copy /TYPE:NOCONTIGUOUS t:10.TXT t:10NEW2.TXT", batch=True)
    x2 = fs.read_bytes("10NEW2.txt")
    x2 = x2.rstrip(b"\0")
    assert len(x2) == 440
    for i in range(0, 10):
        assert f"{i:5d} ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890".encode("ascii") in x2


def test_dos11_init():
    shell = Shell(verbose=True)
    shell.onecmd(f"mount in: /dos11 {DSK}", batch=True)
    shell.onecmd(f"create /allocate:576 {DSK}.mo", batch=True)
    shell.onecmd(f"init /dos11 /dev:dectape {DSK}.mo", batch=True)
    shell.onecmd(f"mount ou: /dos11 {DSK}.mo", batch=True)
    shell.onecmd("dir ou:", batch=True)
    shell.onecmd("copy in:* ou:", batch=True)
    fs = shell.volumes.get_volume('OU')
    assert isinstance(fs, DOS11Filesystem)

    # Create the UIC
    shell.onecmd("create /directory ou:[10,20]", batch=True)
    with pytest.raises(Exception):
        shell.onecmd("create /directory ou:[10,20]", batch=True)
    shell.onecmd("create ou:[10,20]test /allocate:5", batch=True)
    fs.get_file_entry("[10,20]test")
    shell.onecmd("dir ou:[10,20]", batch=True)

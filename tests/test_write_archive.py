import numpy as np
import pyansys

from pyansys import examples


def test_writesector(tmpdir):
    archive = pyansys.ReadArchive(examples.sector_archive_file)
    grid = archive.ParseVTK()

    temp_archive = str(tmpdir.mkdir("tmpdir").join('tmp.cdb'))
    pyansys.WriteArchive(temp_archive, grid)

    archive2 = pyansys.ReadArchive(temp_archive)
    grid2 = archive.ParseVTK()

    assert np.allclose(grid.points, grid2.points)
    assert np.allclose(grid.cells, grid2.cells)


def test_writehex(tmpdir):
    archive = pyansys.ReadArchive(examples.hexarchivefile)
    grid = archive.ParseVTK()

    temp_archive = str(tmpdir.mkdir("tmpdir").join('tmp.cdb'))
    pyansys.WriteArchive(temp_archive, grid)

    archive2 = pyansys.ReadArchive(temp_archive)
    grid2 = archive.ParseVTK()

    assert np.allclose(grid.points, grid2.points)
    assert np.allclose(grid.cells, grid2.cells)

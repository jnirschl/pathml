import pytest
import numpy as np

from pathml.core.tile import Tile


@pytest.mark.parametrize("incorrect_input", ["string", True, 5, [5, 4, 3], {"dict": "testing"}])
@pytest.mark.parametrize("incorrect_input_name",  [True, 5, [5, 4, 3], {"dict": "testing"}])
def test_init_incorrect_input(incorrect_input, incorrect_input_name):
    with pytest.raises(AssertionError):
        testimage = Tile(incorrect_input, coords=(1,3))
        testcoords = Tile(np.random.randn((224,224,3)), coords=incorrect_input)
        testmasks = Tile(np.random.randn((224,224,3)), coords=(1,3), masks=incorrect_input)
        testname = Tile(np.random.randn((224,224,3)), coords=(1,3), name=incorrect_input_name)


def test_image():
    tile = Tile(np.ones((224,224,3)), coords=(1,3))
    assert (tile.image).all() == (np.ones((224,224,3))).all()


def test_repr(tile_withmasks):
    tile = tile_withmasks
    print(tile)

import pytest

from cabaret import Camera, generate_image


def test_simple():
    camera = Camera(width=100, height=100)
    ra, dec = 323.36152, -0.82325
    _ = generate_image(ra, dec, 1, camera=camera)


def test_timeout():
    camera = Camera(width=100, height=100)
    ra, dec = 323.36152, -0.82325

    with pytest.raises(TimeoutError):
        _ = generate_image(ra, dec, 1, camera=camera, timeout=0.1)

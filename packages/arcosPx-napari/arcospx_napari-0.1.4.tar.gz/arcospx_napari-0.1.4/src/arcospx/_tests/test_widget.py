from types import SimpleNamespace
import numpy as np
from numpy.testing import assert_array_equal
from skimage.io import imread
from arcospx._widget import track_events


def test_remove_background(make_napari_viewer, qtbot):
    """
    Test background removal on a simple image.
    """
    viewer = make_napari_viewer()
    test_img = imread("src/arcospx/_tests/test_data/1_growing.tif")

    viewer.add_image(test_img, name="test_img")
    imread("src/arcospx/_tests/test_data/1_growing_true.tif")
    _, widget = viewer.window.add_plugin_dock_widget(
        "arcosPx-napari", "Remove Background"
    )
    widget.image.value = viewer.layers["test_img"]
    widget.filter_type.value = "gaussian"
    widget.size_0.value = 2
    widget.size_1.value = 1
    widget.size_2.value = 1

    with qtbot.waitSignal(
        viewer.layers.events.inserted,
        timeout=10000,
    ):
        widget()

    assert len(viewer.layers) == 2


def test_track_events(make_napari_viewer, qtbot):
    """
    Test tracking on a simple image.
    """
    viewer = make_napari_viewer()
    test_img = np.where(
        imread("src/arcospx/_tests/test_data/1_growing.tif") == 0, 2, 0
    )
    viewer.add_image(test_img, name="test_img")
    true_img = imread(
        "src/arcospx/_tests/test_data/1_growing_track_events_true.tif"
    )
    _, widget = viewer.window.add_plugin_dock_widget(
        "arcosPx-napari", "Track Events"
    )
    widget.image.value = viewer.layers["test_img"]
    widget.eps.value = 1
    widget.eps_prev.value = 0
    widget.min_clustersize.value = 1
    widget.n_prev.value = 1

    with qtbot.waitSignal(
        viewer.layers.events.inserted,
        timeout=10000,
    ):
        widget()

    assert_array_equal(viewer.layers[1].data, true_img)


def test_track_events_eps_respects_downscale(monkeypatch):
    image_shape = (3, 8, 6)
    test_img = np.zeros(image_shape, dtype=np.uint8)
    test_img[:, 0, 0] = 1
    image_layer = SimpleNamespace(data=test_img, name="test_img")
    called = {}

    def fake_estimate_eps(*, image, **kwargs):
        called["shape"] = image.shape
        return 1.0

    monkeypatch.setattr("arcospx._widget.estimate_eps_func", fake_estimate_eps)
    monkeypatch.setattr("arcospx._widget.track_events.eps", SimpleNamespace(value=None), raising=False)

    function = track_events()._function
    worker = function(
        image=image_layer,
        estimate_eps="Mean",
        min_clustersize=1,
        downscale=2,
    )
    worker.quit()

    assert called["shape"] == (image_shape[0], image_shape[1] // 2, image_shape[2] // 2)

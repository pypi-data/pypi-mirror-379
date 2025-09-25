from unittest.mock import patch

from ordeq_huggingface import HuggingfaceDataset


class DummyDataset:
    pass


@patch("ordeq_huggingface.dataset.load_dataset")
def test_load_calls_load_dataset(mock_load_dataset):
    mock_result = DummyDataset()
    mock_load_dataset.return_value = mock_result
    ds = HuggingfaceDataset(path="my/path")
    result = ds.load()
    mock_load_dataset.assert_called_once_with("my/path")
    assert result is mock_result


@patch("ordeq_huggingface.dataset.load_dataset")
def test_load_with_args(mock_load_dataset):
    mock_result = DummyDataset()
    mock_load_dataset.return_value = mock_result
    ds = HuggingfaceDataset(path="my/path")
    result = ds.load(split="train", foo=123)
    mock_load_dataset.assert_called_once_with(
        "my/path", split="train", foo=123
    )
    assert result is mock_result


def test_init_sets_path():
    ds = HuggingfaceDataset(path="abc")
    assert ds.path == "abc"

def test_sync_empty_iterators() -> None:
    """Test sync on empty iterators."""
    from syncup import sync

    result: list = list(sync(iter([]), iter([]), key1=lambda x: x, key2=lambda x: x))
    assert result == []

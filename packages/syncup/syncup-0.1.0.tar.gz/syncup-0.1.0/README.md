# syncup

[![PyPI Release](https://badge.fury.io/py/syncup.svg)](https://badge.fury.io/py/syncup)
[![CI](https://github.com/clintval/syncup/actions/workflows/python_package.yml/badge.svg?branch=main)](https://github.com/clintval/syncup/actions/workflows/python_package.yml?query=branch%3Amain)
[![Python Versions](https://img.shields.io/badge/python-3.11_|_3.12_|_3.13-blue)](https://github.com/clintval/syncup)
[![MyPy Checked](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://docs.astral.sh/ruff/)

Synchronizers for lazy iterators.

```console
pip install syncup
```

## Example

Iterate though a complete FASTX file and a filtered FASTX file, synchronizing on records present in both:

```python
with (
    FastxFile(in_source) as source,
    FastxFile(in_subseq) as subseq,
):
    for count, (fq, fq_subseq) in enumerate(
        sync(
            iter1=source,
            iter2=subseq,
            key1=lambda rec: rec.name,
            key2=lambda rec: rec.name,
            cmp_func=lambda x, y: (x == y) - 1,  # only advance iter1 when non-equal
        ),
        start=1,
    ):
        assert fq.name == fq_subseq.name, f"Names for record {count} should be equal!"
```

## Development and Testing

See the [contributing guide](./CONTRIBUTING.md) for more information.

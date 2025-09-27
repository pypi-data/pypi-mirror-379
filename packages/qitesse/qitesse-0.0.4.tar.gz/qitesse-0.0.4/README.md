# qitesse
[![PyPI Version](https://img.shields.io/pypi/v/qitesse.svg)](https://pypi.org/project/qitesse/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/OsamaMIT/qitesse/blob/main/LICENSE)
[![Python Versions](https://img.shields.io/pypi/pyversions/qitesse.svg)](https://pypi.org/project/qitesse/)

**qitesse** is an open-source python API for qitesse-sim, the performant Rust quantum simulator.

qitesse is built upon qitesse-sim, the **high-performance CPU-based state-vector simulator** for quantum circuits, fully built in Rust.

This PyPI module provides a high-level python interface for the purpose of production, research, and development.

## Features

- Performant CPU based simulation
- Amplitude measurements on quantum circuits
- _More soon!_

## Installation

qitesse requires **Python 3.8+**. Install it via pip:

```bash
pip install qitesse
```

Or install from source:

```bash
git clone https://github.com/OsamaMIT/qitesse.git

pip install maturin

maturin develop --release
```
To run examples:

`python examples/h_example.py`

`python examples/qft_example.py`

## Documentation
_**Avaliable soon!**_


## Planned Features
- Differentiable gradients
- Implementing more quantum gates

## Contributing
Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (feature-branch)
3. Commit your changes and open a pull request

## License
This project is licensed under the MIT License. See the LICENSE file for details.


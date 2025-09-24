# Instructions to use this project and publish to PyPI

1. Rename package (optional)
   - If you want a different PyPI package name, edit `pyproject.toml` `name` field and rename `src/matrixutils` accordingly.

2. Local usage
   ```bash
   git init
   git add .
   git commit -m "Initial commit: simple matrix multiplication package"
   python -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip build
   python -m build
   pip install dist/*.whl
   python -c "from matrixutils import matrix_multiply; print(matrix_multiply([[1,2],[3,4]], [[5,6],[7,8]]))"

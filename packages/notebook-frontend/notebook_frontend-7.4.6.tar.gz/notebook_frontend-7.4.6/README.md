# notebook-frontend

A Python package distributing Notebook's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output notebook-7.4.6-py3-none-any.whl https://files.pythonhosted.org/packages/dd/33/8cfe8678444c52173b4f490e2f72b8eca30d99ddc1e0dcc6e1aea63d48c4/notebook-7.4.6-py3-none-any.whl
unzip notebook-7.4.6-py3-none-any.whl
mkdir -p share
cp -r notebook-7.4.6.data/data/share/jupyter share/
cp -r notebook/static src/notebook_frontend/
cp -r notebook/templates src/notebook_frontend/
hatch build
hatch publish
```

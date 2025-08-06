# learning-testcontainers

## setup python venv
* activate venv: `python -m venv ./.venv && source .venv/bin/activate`
* install dependencies: `pip install -r requirements.txt`

## delete all installed pip dependencies
`pip freeze | grep -v " @ " | cut -d'=' -f1 | xargs pip uninstall -y`
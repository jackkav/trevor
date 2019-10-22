poetry install
if using vscode: add your poetry venv to vscode settings
`tmp=$(mktemp) && jq '."python.pythonPath" = "'$(poetry run which python)'"' settings.json > "$tmp" && mv "$tmp" settings.json`

poetry run which python
poetry run ptw


TODO
memoize
bitwise
sets
frequency
string numbers
async io
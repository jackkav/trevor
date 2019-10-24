### get started
- 
`poetry install`


if using vscode: add your poetry venv to vscode settings

`tmp=$(mktemp) && jq '."python.pythonPath" = "'$(poetry run which python)'"' .vscode/settings.json > "$tmp" && mv "$tmp" .vscode/settings.json`

`poetry run ptw`
or
`poetry shell`
`ptw`


### TODO
- [x] primes
- [x] basics
- [x] fizzbuzz
- [x] guards
- [x] ordinals
- memoize
- bitwise
- sets, intersections
- string numbers
- async io
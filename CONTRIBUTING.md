# Contributing to Dundie Project

Summary of project

## Guidelines


- Backwards compatibility
- Multiplataform
- Python 3 Only

## Code of Conduct

- Be gentle

## How to contribute

### Fork repository

- Click fork button on [github repo](https://github.com/...)

### Clone to local dev environment

```bash
git clone https://github.com/...
```

### Prepare virtual env

```bash
cd dundie-rewards
make virtualenv
make install
```

### Coding style

- This project follows PEP8

### run tests

```bash
make test
# or
make watch
```

### Commit rules

- We follow conventional commit message ex: `[bugfix] reason #issue`
- We require signed commits

### Pull request rules

- We require all tests to be passing

# thrim

## Requirement

- Python3.6

- pipenv

## Installation

1. `$ pipenv shell`

1. `$ pipenv install -e .`

## Usage

`$ thrim run`

## Test

`$ python -m unittest`

When this command is executed, the following test is performed.

- test_require_confirmation

	Test the input(y/N) before executing `thrim run`.

- test_dryrun_iptables

	Test the `iptables` command example before executing `thrim run`.

- test_run_iptables

	Test whether `thrim run` was successfully execute.
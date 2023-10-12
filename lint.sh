# TODO: add flake8 here.
flake8 .
autoflake --in-place --recursive .
autopep8 --in-place --recursive .
isort .
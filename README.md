# Week 4 Lecture Exercises

This repository contains lecture exercises for Week 4 of Chem 274A. To
complete the lecture exercises, clone this repository, complete each Python or
shell exercise, and push your work to GitHub.

The Python exercises are tested with
[pytest](https://docs.pytest.org/en/stable/). The command-line exercises have a
Bash test script. When you push to GitHub, all exercises will be autograded.

## Making an environment

First make sure you have a Python environment with `pytest` installed. If you
made an environment in Chem 280 that had `pytest`, you may use that. If you
need to make an environment, use these commands to create and activate one:

```bash
conda create --name chem274a conda-forge::python
conda activate chem274a
```

After activating it, install `pytest`:

```bash
conda install conda-forge::pytest
```

The environment is active when `(chem274a)` appears at the beginning of your
terminal prompt. Run `conda deactivate` when you are finished working.

The command-line exercises require Bash and standard Unix command-line tools.
On Windows, complete them in WSL or another Unix-like environment.

## Complete the exercises

Edit only the exercise files.

Do not modify files in `tests/`, `.github/scripts/`, or `.github/workflows/`.
Those files define how your work is checked.

## Run the tests locally

Run the same grading command used by GitHub Actions from the repository
directory:

```bash
python .github/scripts/grade.py
```

The starter code is intentionally incomplete, so tests will fail at first.
The grader runs every exercise separately, prints a summary, and writes a
machine-readable report to `grading-results.json`.

Use the grading script instead of `pytest -v` to run the complete suite; it
runs each Python exercise separately and includes the command-line tests.

Run an individual Python exercise with its corresponding command:

```bash
pytest -v -k test_introspection01
pytest -v -k test_DataTypes01
pytest -v -k test_DataTypes02
pytest -v -k test_DataTypes03
pytest -v -k test_DataTypes04
pytest -v -k test_DataTypes05
pytest -v -k test_DataTypes06
pytest -v -k test_DataTypes07
```

Run an individual command-line exercise with its corresponding command:

```bash
bash tests/test_common_tools.sh CommonTools01
bash tests/test_common_tools.sh CommonTools02
bash tests/test_common_tools.sh CommonTools03
bash tests/test_common_tools.sh CommonTools04
```

The command-line tests may create files while running. Those files are test
output and should not be committed.

When all exercises are correct, the autograder reports 12 out of 12 points,
with each exercise worth one point.

## Submit your work

Review your changes, commit them, and push your branch to GitHub.

If a test passes locally but fails on GitHub, confirm that you committed and
pushed the latest version of every exercise file.

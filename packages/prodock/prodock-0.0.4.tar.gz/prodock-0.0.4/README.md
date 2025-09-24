# ProDock
Automatic pipeline for molecular modeling

[![PyPI version](https://img.shields.io/pypi/v/prodock.svg)](https://pypi.org/project/prodock/)
[![Docker Pulls](https://img.shields.io/docker/pulls/tieulongphan/prodock.svg)](https://hub.docker.com/r/tieulongphan/prodock)
[![Docker Image Version](https://img.shields.io/docker/v/tieulongphan/prodock/latest?label=container)](https://hub.docker.com/r/tieulongphan/prodock)
[![License](https://img.shields.io/github/license/Medicine-Artificial-Intelligence/prodock.svg)](https://github.com/Medicine-Artificial-Intelligence/prodock/blob/main/LICENSE)
[![Release](https://img.shields.io/github/v/release/Medicine-Artificial-Intelligence/prodock.svg)](https://github.com/Medicine-Artificial-Intelligence/prodock/releases)
[![Last Commit](https://img.shields.io/github/last-commit/Medicine-Artificial-Intelligence/prodock.svg)](https://github.com/Medicine-Artificial-Intelligence/prodock/commits)
[![CI](https://github.com/Medicine-Artificial-Intelligence/prodock/actions/workflows/test-and-lint.yml/badge.svg?branch=main)](https://github.com/Medicine-Artificial-Intelligence/prodock/actions/workflows/test-and-lint.yml)
[![Dependency PRs](https://img.shields.io/github/issues-pr-raw/Medicine-Artificial-Intelligence/prodock?label=dependency%20PRs)](https://github.com/Medicine-Artificial-Intelligence/prodock/pulls?q=is%3Apr+label%3Adependencies)
[![Stars](https://img.shields.io/github/stars/Medicine-Artificial-Intelligence/prodock.svg?style=social&label=Star)](https://github.com/Medicine-Artificial-Intelligence/prodock/stargazers)


**Toolkit for molecular modeling**
![ProDock](https://raw.githubusercontent.com/Medicine-Artificial-Intelligence/ProDock/main/doc/fig/prodock.png)
For more details on each utility within the repository, please refer to the documentation provided in the respective folders.

## Step-by-Step Installation Guide

1. **Python Installation:**
  Ensure that Python 3.11 or later is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Creating a Virtual Environment (Optional but Recommended):**
  It's recommended to use a virtual environment to avoid conflicts with other projects or system-wide packages. Use the following commands to create and activate a virtual environment:

  ```bash
  python -m venv prodock-env
  source prodock-env/bin/activate  
  ```
  Or Conda

  ```bash
  conda create --name prodock-env python=3.11
  conda activate prodock-env
  ```

3. **Cloning and Installing SynTemp:**
  Clone the SynTemp repository from GitHub and install it:

  ```bash
  git clone https://github.com/Medicine-Artificial-Intelligence/ProDock.git
  cd ProDock
  pip install -r requirements.txt
  pip install black flake8 pytest # black for formating, flake8 for checking format, pytest for testing
  ```

## Setting Up Your Development Environment

Before you start, ensure your local development environment is set up correctly. Pull the latest version of the `main` branch to start with the most recent stable code.

```bash
git checkout main
git pull
```

## Working on New Features

1. **Create a New Branch**:  
   For every new feature or bug fix, create a new branch from the `main` branch. Name your branch meaningfully, related to the feature or fix you are working on.

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Develop and Commit Changes**:  
   Make your changes locally, commit them to your branch. Keep your commits small and focused; each should represent a logical unit of work.

   ```bash
   git commit -m "Describe the change"
   ```

3. **Run Quality Checks**:  
   Before finalizing your feature, run the following commands to ensure your code meets our formatting standards and passes all tests:

   ```bash
   ./lint.sh # Check code format
   pytest Test # Run tests
   ```

   Fix any issues or errors highlighted by these checks.

## Integrating Changes

1. **Rebase onto Staging**:  
   Once your feature is complete and tests pass, rebase your changes onto the `staging` branch to prepare for integration.

   ```bash
   git fetch origin
   git rebase origin/staging
   ```

   Carefully resolve any conflicts that arise during the rebase.

2. **Push to Your Feature Branch**:
   After successfully rebasing, push your branch to the remote repository.

   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request**:
   Open a pull request from your feature branch to the `staging` branch. Ensure the pull request description clearly describes the changes and any additional context necessary for review.

## Important Notes

- **Direct Commits Prohibited**: Do not push changes directly to the `main` or `staging` branches. All changes must come through pull requests reviewed by at least one other team member.
- **Merge Restrictions**: The `main` branch can only be updated from the `staging` branch, not directly from feature branches.

## Publication

[**ProDock**]()

## License

This project is licensed under MIT License - see the [License](LICENSE) file for details.

## Acknowledgments

This work has received support from the Korea International Cooperation Agency (KOICA) under the project entitled “Education and Research Capacity Building Project at University of Medicine and Pharmacy at Ho Chi Minh City”, conducted from 2024 to 2025 (Project No. 2021-00020-3).
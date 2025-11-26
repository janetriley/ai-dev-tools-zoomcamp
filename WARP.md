# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a personal learning repository for the DataTalks.Club 2025 AI Dev Tools Zoomcamp course. The repository is organized into module directories (`module_1/`, `module_2/`, etc.) corresponding to course modules.

## Repository Structure

```
.
├── module_1/          # Course Module 1 materials and exercises
├── module_2/          # Course Module 2 materials and exercises
├── module_3/          # Course Module 3 materials and exercises
├── module_4/          # Course Module 4 materials and exercises
├── module_5/          # Course Module 5 materials and exercises
└── README.md          # Quick links to course resources
```

## Course Resources

- **Course Repository**: https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/
- **2025 Cohort README**: https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/blob/main/cohorts/2025/README.md
- **Course Playlist**: https://www.youtube.com/playlist?list=PL3MmuxUbc_hLuyafXPyhTdbF4s_uNhc43
- **Homework Submissions**: https://courses.datatalks.club/ai-dev-tools-2025/
- **Course FAQ**: https://docs.google.com/document/d/1uBSxORcxOewXMzMDHwADpVSiS0kBRXhTQ3qWd86CjlI/

## Module Organization

Each module directory is intended to contain:
- Exercise files and solutions
- Homework assignments
- Notes and experiments
- Any supporting code or data

When creating files for a specific module, place them in the appropriate `module_*/` directory.

## Python Development

The repository uses Python with standard gitignore patterns for:
- Virtual environments (`.venv/`, `venv/`, etc.)
- Python caching (`__pycache__/`, `*.pyc`)
- Jupyter notebooks (`.ipynb_checkpoints/`)
- Common Python tooling (`.ruff_cache/`, `.mypy_cache/`, `.pytest_cache/`)

### Environment Setup

When setting up Python environments for exercises:
- Create virtual environments within module directories if needed
- Check for `requirements.txt` or `pyproject.toml` in each module
- The `.gitignore` excludes common virtual environment directory names

## Working with Course Materials

When working on homework or exercises:
1. Check the course repository for official instructions and starter code
2. Organize work by module number
3. Reference the course FAQ for common questions
4. Submit homework via the course platform linked in README.md

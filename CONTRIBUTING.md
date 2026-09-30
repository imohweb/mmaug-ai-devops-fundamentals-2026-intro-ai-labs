# Contributing

Thank you for helping improve the MMAUG AI & DevOps Fundamentals Bootcamp labs.

## Contribution priorities

We welcome improvements that make the material:

- easier for beginners to follow;
- more technically correct;
- safer and more privacy-aware;
- reproducible on normal participant laptops;
- clearer about the difference between classroom demonstration and production practice.

## Before opening a pull request

1. Create a branch.
2. Keep each change focused.
3. Do not add real personal or customer data.
4. If you add a dependency, update `requirements.txt` and explain why it is needed.
5. Run:

```bash
pytest -q
python scripts/run_all_demos.py
```

6. Update the relevant lab README when behaviour changes.

## Dataset contributions

Prefer synthetic or properly licensed public data. Add the source and licence to `datasets/README.md` and `docs/dataset-sources.md`.

## Code style

Prioritise readability over cleverness. The primary audience includes people writing their first ML code.

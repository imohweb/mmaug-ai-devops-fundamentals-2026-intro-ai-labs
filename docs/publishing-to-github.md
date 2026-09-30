# Publishing This Lab Repository to GitHub

Recommended repository name:

`mmaug-ai-devops-fundamentals-2026-intro-ai-labs`

## Option 1 — GitHub web interface

1. Create a new empty repository on GitHub.
2. Do **not** add another README, licence or `.gitignore` because this package already includes them.
3. Upload the complete contents of this folder.
4. In the GitHub repository **About** section, use this description:

   `Beginner labs for the MMAUG AI & DevOps Fundamentals Bootcamp 2026 — Introduction to AI Concepts and Tools.`

5. Suggested topics: `ai`, `machine-learning`, `rag`, `ai-agents`, `python`, `beginner`, `bootcamp`, `mmaug`.
6. After publishing, replace `<REPLACE-WITH-REPOSITORY-URL>` in the root README with the final clone URL.

## Option 2 — Git command line

From inside this folder:

```bash
git init
git branch -M main
git add .
git commit -m "Initial MMAUG AI concepts lab release"
git remote add origin <REPLACE-WITH-REPOSITORY-URL>
git push -u origin main
```

## Recommended GitHub settings

- Keep GitHub Actions enabled so the included workflow can test the scripts.
- Enable Issues if participants will report lab problems.
- Consider enabling Discussions for bootcamp questions.
- Protect `main` if multiple maintainers will contribute.
- Never commit `.env` files, API keys or credentials.

## Before publishing

Run:

```bash
pip install -r requirements-dev.txt
pytest -q
python scripts/run_all_demos.py
```

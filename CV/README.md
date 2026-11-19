# One CV source, five outputs

Run `make -C CV` from the repository root to regenerate the public CV and all four application profiles. Run `make -C CV cv-genetics` (or another profile name) to rebuild just one. PDFs are written under `CV/_build/` and are not committed.

## Edit content once

- `CV/cv.tex`: education, experience, skills, contact details, references, and the general layout.
- `_bibliography/papers.bib`: papers and software, including descriptions, links, dates, authors, and publication status.
- `CV/profiles.tex`: presentation rules only: section order, interest order, and which existing entries come first.

The default `cv.tex` remains the website entry point. The four two-line `cv-*.tex` files select a profile and load that same source; never copy CV content into them.

## New papers and repositories

Add each paper or software project once to `papers.bib`, just as for the website. All profiles include new entries automatically. Papers need the existing `published`, `preprint`, or `work-in-progress` keyword; software uses `@software`. The current profile priorities are not inclusion lists: unlisted new entries still appear, using the normal bibliography sorting after prioritized entries within their category. Update priorities only if a new item deserves earlier placement. Publication-status groups are preserved.

A GitHub repository is not imported merely because it exists: register it once in the shared bibliography. This avoids listing unfinished or irrelevant repositories automatically.

These initial profiles retain the existing prose and all papers/projects. Any later contribution explanations should be edited in the shared source, not separately in four PDFs. Content edits can change page count; review generated PDFs before applying. The website deployment still builds only the general CV. `_config.yml` explicitly excludes application CV entry points, profiles, documentation, build/check tooling, and generated `cv-*` outputs from the published site. The public `CV/_build/cv.pdf` remains included. These exclusions also apply when building the site locally after generating every CV. Repository files are still visible to anyone who can access the Git repository; this is a publishing exclusion, not private storage.

| Output | Emphasis |
| --- | --- |
| `cv.pdf` | General website CV |
| `cv-ml.pdf` | Mathematical ML / optimization |
| `cv-econ-ai.pdf` | Economics / AI |
| `cv-genetics.pdf` | Statistical genetics / scientific computing |
| `cv-quant.pdf` | Quantitative research |

## Verify automatic inclusion

Run `python3 CV/check_profiles.py` from the repository root. It builds all five profiles in a temporary copy with an extra paper and software project, checks that both appear exactly once, and checks that all profiles retain the same bibliography entries. It does not modify your real bibliography.

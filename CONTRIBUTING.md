# Contributing to QSPQuest Models

Contributions are welcome: problems with a model, documentation fixes, new
published models and better examples.

## How to contribute

1. **Open an issue first.** For a problem, give the model ID and version, the
   scenario, the code you ran, and the expected and actual results. To propose
   a model, give the paper (DOI), where its equations or code come from, their
   license and the experiment you want to run. Except for typo fixes, wait for
   a maintainer to agree on the approach before you open a pull request.
2. **Open a focused pull request.** Make one change per pull request, link its
   issue (`Closes #123`) and run `python -B -m unittest discover -s tests -v`
   from the checkout root first; no separate test runner is required.
3. **Review and release.** Maintainers check the source, units, license and
   numerical results. Accepted changes are tested and published in the next
   library release, and you are credited. Released model versions are never
   edited; a fix becomes a new version.

Model guides (`MODEL_CARD.md` and `MODEL_CATALOG.md`), parameter records
(`parameters.json`) and discovery records (`qspquest_models/discovery.json`) are
generated, so describe changes to them in the issue rather than editing them
directly.

A model contains only the paper's model, study and results. Do not add values
that record how the paper was found or retrieved, such as citation counts,
PMIDs, download flags or page counts; `scripts/check_export_content.py` refuses
them.

Ubi-owned contributions are licensed under [Apache-2.0](LICENSE); a published
model keeps its source's terms (see its notice). Do not submit restricted
publisher material, unlicensed data or personal data. Report security issues
privately to [helpdesk@unibiointelligence.com](mailto:helpdesk@unibiointelligence.com),
not in public issues.

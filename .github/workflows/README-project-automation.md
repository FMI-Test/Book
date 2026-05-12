# Project Automation Configuration

The workflow `.github/workflows/update-projects-on-pr-merge.yml` updates project items when a pull request is merged.

## Required repository variables

- `PROJECT_IDS`: Comma-separated GitHub ProjectV2 node IDs.

## Optional repository variables

- `PROJECT_STATUS_FIELD_NAME`: Single-select status field name (default: `Status`).
- `PROJECT_DONE_OPTION_NAME`: Status option to apply on merge (default: `Done`).

## Optional repository secret

- `PROJECTS_TOKEN`: Personal access token with permission to read/write the target projects.
  - If omitted, the workflow falls back to `${{ github.token }}`.

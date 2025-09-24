# CodeMie Test Harness

End-to-end, integration, and UI test suite for CodeMie services. This repository exercises CodeMie APIs (LLM, assistants, workflows, tools) and common integrations.

The suite is designed for high-parallel execution (pytest-xdist), resilient runs (pytest-rerunfailures), and optional reporting to ReportPortal.

## Table of Contents

- Part 1: codemie-test-harness command line (recommended)
  - Installation
  - Configuration (CLI)
  - Run with command line
  - Useful CLI commands and common markers
- Part 2: Contributors (pytest from repo)
  - Install and configure with .env (PREVIEW/AZURE/GCP/AWS/PROD/LOCAL)
  - Local with custom GitLab, GitHub, Jira and Confluence tokens
  - UI tests (Playwright)
  - ReportPortal integration
  - Makefile targets
  - Troubleshooting

---

## Part 1: codemie-test-harness command line (recommended)

Use the CLI to install, configure, and run tests against your custom environment. No .env file is used in this flow. Values are stored in ~/.codemie/test-harness.json.

### Installation

Install from PyPI:

```shell
pip install codemie-test-harness
```

Tip: Use a virtual environment (e.g., python -m venv .venv && source .venv/bin/activate).

### Configuration (CLI)

Set required Auth/API values once (saved under ~/.codemie/test-harness.json):

```shell
codemie-test-harness config set AUTH_SERVER_URL <auth_server_url>
codemie-test-harness config set AUTH_CLIENT_ID <client_id>
codemie-test-harness config set AUTH_CLIENT_SECRET <client_secret>
codemie-test-harness config set AUTH_REALM_NAME <realm_name>
codemie-test-harness config set CODEMIE_API_DOMAIN <codemie_api_domain_url>
```

Optional defaults for pytest:

```shell
codemie-test-harness config set PYTEST_MARKS "smoke"
codemie-test-harness config set PYTEST_N 8
codemie-test-harness config set PYTEST_RERUNS 2
```

Optional integrations used by e2e tests:

```shell
# Git provider selection
codemie-test-harness config set GIT_ENV gitlab   # or github

# GitLab
codemie-test-harness config set GITLAB_URL https://gitlab.example.com
codemie-test-harness config set GITLAB_TOKEN <gitlab_token>
codemie-test-harness config set GITLAB_PROJECT https://gitlab.example.com/group/project
codemie-test-harness config set GITLAB_PROJECT_ID 12345

# GitHub
codemie-test-harness config set GITHUB_URL https://github.com
codemie-test-harness config set GITHUB_TOKEN <github_token>
codemie-test-harness config set GITHUB_PROJECT https://github.com/org/repo

# Jira
codemie-test-harness config set JIRA_URL https://jira.example.com
codemie-test-harness config set JIRA_TOKEN <jira_token>
codemie-test-harness config set JQL "project = 'EPMCDME' and issuetype = 'Epic' and status = 'Closed'"

# Confluence
codemie-test-harness config set CONFLUENCE_URL https://confluence.example.com
codemie-test-harness config set CONFLUENCE_TOKEN <confluence_token>
codemie-test-harness config set CQL "space = EPMCDME and type = page and title = 'AQA Backlog Estimation'"
```

Notes:
- Quoting is required for values with spaces (e.g., JQL/CQL).
- Resolution precedence when running: CLI flags > environment variables > saved config > defaults.
- Config file path: ~/.codemie/test-harness.json

### Run with command line

Default run (uses saved config or defaults):

```shell
codemie-test-harness run
```

Override at runtime:

```shell
# Change marks, workers, reruns just for this run
codemie-test-harness run --marks "smoke or gitlab or jira_kb" -n 8 --reruns 2
```

Provider-specific examples:

```shell
# Only GitLab
codemie-test-harness run --marks gitlab

# Only GitHub
codemie-test-harness run --marks github

# Jira knowledge base
codemie-test-harness run --marks jira_kb

# Confluence knowledge base
codemie-test-harness run --marks confluence_kb

# Code knowledge base
codemie-test-harness --git-env gitlab run --marks code_kb

# Git tool
codemie-test-harness --git-env github run --marks git
```

### Useful CLI commands and common markers

CLI basics:

```shell
codemie-test-harness --help
codemie-test-harness config list
codemie-test-harness config get AUTH_SERVER_URL
codemie-test-harness config set PYTEST_N 12
```

Common markers in this repo include:
- smoke
- mcp
- plugin
- regression
- ui
- jira_kb, confluence_kb, code_kb
- gitlab, github, git

---

## Part 2: Contributors (pytest from repo)

This section is for contributors who run tests from a cloned codemie-sdk repository (test-harness package). This flow uses a .env file and may pull values from AWS SSM Parameter Store.

### Install and configure with .env (PREVIEW/AZURE/GCP/AWS/PROD/LOCAL)

1) Clone the codemie-sdk repository and navigate to the test-harness folder.
2) Create a .env file in the project root. If you provide AWS credentials, the suite will fetch additional values from AWS Systems Manager Parameter Store and recreate .env accordingly.

```properties
ENV=local

AWS_ACCESS_KEY=<aws_access_token>
AWS_SECRET_KEY=<aws_secret_key>
```

### Local with custom GitLab, GitHub, Jira and Confluence tokens

1) Start from a .env populated via AWS (optional)
2) Replace the tokens below with your personal values
3) Important: After replacing tokens, remove AWS_ACCESS_KEY and AWS_SECRET_KEY from .env — otherwise they will overwrite your changes next time .env is regenerated

Full .env example:

```properties
ENV=local
PROJECT_NAME=codemie
GIT_ENV=gitlab # required for e2e tests only
DEFAULT_TIMEOUT=60
CLEANUP_DATA=True
LANGFUSE_TRACES_ENABLED=False

CODEMIE_API_DOMAIN=http://localhost:8080

FRONTEND_URL=https://localhost:5173/
HEADLESS=False

NATS_URL=nats://localhost:4222

TEST_USER_FULL_NAME=dev-codemie-user

GITLAB_URL=<gitlab_url>
GITLAB_TOKEN=<gitlab_token>
GITLAB_PROJECT=<gitlab_project>
GITLAB_PROJECT_ID=<gitlab_project_id>

GITHUB_URL=<github_url>
GITHUB_TOKEN=<github_token>
GITHUB_PROJECT=<github_project>

JIRA_URL=<jira_url>
JIRA_TOKEN=<jira_token>
JQL="project = 'EPMCDME' and issuetype = 'Epic' and status = 'Closed'"

CONFLUENCE_URL=<confluence_url>
CONFLUENCE_TOKEN=<confluence_token>
CQL="space = EPMCDME and type = page and title = 'AQA Backlog Estimation'"

RP_API_KEY=<report_portal_api_key>
```

Now you can run full or subset packs. Examples:

```shell
# All tests except tests that cannot be run in parallel (-n controls the number of workers)
pytest -n 10 -m "not not_for_parallel_run" --reruns 2

# Tests that cannot be run in parallel
pytest -m not_for_parallel_run --reruns 2

# Regression tests
pytest -n 10 -m "regression and not not_for_parallel_run" --reruns 2
pytest -m not_for_parallel_run --reruns 3
```

Note: "--reruns 2" uses pytest-rerunfailures to improve resiliency in flaky environments.

### UI tests (Playwright)

Install browsers once:

```shell
playwright install
```

Then run UI pack:

```shell
pytest -n 4 -m ui --reruns 2
```

Playwright docs: https://playwright.dev/python/docs/intro

### ReportPortal integration

pytest.ini is preconfigured with rp_endpoint, rp_project, and a default rp_launch. To publish results:

1) Set RP_API_KEY in .env
2) Add the flag:

```shell
pytest -n 10 -m "regression and not not_for_parallel_run" --reruns 2 --reportportal
```

If you need access to the ReportPortal project, contact: Anton Yeromin (anton_yeromin@epam.com).

### Makefile targets

- install — poetry install
- ruff — lint and format with Ruff
- ruff-format — format only
- ruff-fix — apply autofixes
- build — poetry build
- publish — poetry publish

Example:

```shell
make install
make ruff
```

### Troubleshooting

- Playwright not installed: Run playwright install.
- Headless issues locally: Set HEADLESS=True in .env for CI or False for local debugging.
- Env values keep reverting: Ensure AWS_ACCESS_KEY and AWS_SECRET_KEY are removed after manual edits to .env.
- Authentication failures: Verify AUTH_* variables and CODEMIE_API_DOMAIN are correct for the target environment.
- Slow or flaky runs: Reduce -n, increase timeouts, and/or use --reruns.

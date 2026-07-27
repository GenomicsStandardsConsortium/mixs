# Security Policy

## Reporting a vulnerability

Please do not report security vulnerabilities through public GitHub issues,
discussions, or pull requests.

Report them privately through GitHub's
[private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability):
open the repository's **Security** tab and choose **Report a vulnerability**.
This opens a private channel visible only to the maintainers.

If that option is not available, open a public issue that says only that you
have found a security concern and asks a maintainer to open a private channel.
Do not include exploit details in the public issue.

Please include, as far as you can determine them:

- the affected file, schema element, or generated artifact
- a description of the problem and its impact
- steps to reproduce
- any suggested remediation

We will acknowledge the report and keep you informed as we investigate and
prepare a fix.

## Scope

This repository holds the MIxS schema (LinkML source in `src/mixs/`), the
generated artifacts derived from it, the build and documentation tooling, and
its Python dependencies. Reports about any of these are in scope. Reports about
third-party services that merely host or mirror MIxS are best directed to those
services.

## Dependencies

Dependency vulnerabilities are tracked through GitHub Dependabot. Fixes are
applied by updating the version constraints in `pyproject.toml` and the pinned
versions in `poetry.lock`.

# Security Policy

## Reporting a problem

Do not publish secrets, credentials, real personal data or a working exploit in a public issue.

For classroom code problems that are not security-sensitive, open an issue with the steps to reproduce.

## Repository security rules

- Never commit API keys, passwords or tokens.
- Use environment variables for optional cloud extensions.
- Treat retrieved documents and model output as untrusted input.
- Validate structured output before downstream use.
- Use least privilege for any tool/action integration.
- Keep human approval for consequential actions in classroom examples.

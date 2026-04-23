# Code Review Guidelines

## Always check for
- Security vulnerabilities (SQL injection, XSS, hardcoded secrets)
- Missing error handling
- TypeScript `any` types — flag every one
- Missing unit tests for new functions
- Performance issues (N+1 queries, memory leaks)
- console.log left in production code

## Review tone
- Be constructive and specific
- Reference exact line numbers
- Suggest concrete fixes, not just problems
- Praise good patterns too

## Never approve PRs that
- Expose API keys or passwords in code
- Remove existing tests
- Have failing linting
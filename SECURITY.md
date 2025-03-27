# Security Policy

## Supported Versions

ArchiPy is currently in active development. We provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.x.x   | :white_check_mark: |

## Reporting a Vulnerability

We take the security of ArchiPy seriously. If you believe you've found a security vulnerability, please follow these steps:

1. **Please do not disclose the vulnerability publicly**
2. **Email us directly** at [hosseinnejati14@gmail.com](mailto:hosseinnejati14@gmail.com)
3. **Include details** in your report:
   - Type of vulnerability
   - Full path to the vulnerable file(s)
   - Proof of concept if possible
   - Steps to reproduce
   - Impact of the vulnerability

### What to expect
- We will acknowledge receipt of your vulnerability report within 48 hours
- We will provide a timeline for a fix and release after assessing the report
- We will notify you when the vulnerability is fixed
- We will acknowledge your contribution (if desired) when we disclose the vulnerability

## Security Measures

ArchiPy implements several security best practices:

### Code Quality and Vulnerability Prevention
- Static code analysis using `ruff` and `mypy`
- Pre-commit hooks for catching security issues early
- Regular dependency updates and security audits

### Authentication and Authorization
- Built-in JWT token validation
- Secure password handling with proper hashing
- Role-based access control support

### Data Protection
- Encryption support for sensitive data
- Secure transport via TLS
- Data validation via Pydantic models

### Infrastructure Security
- Secure connection pooling for databases
- Rate limiting support to prevent abuse
- Monitoring and logging for security events

## Security Recommendations

When using ArchiPy in your projects, we recommend:

1. Always use the latest version with security updates
2. Set appropriate rate limits for APIs
3. Implement proper authentication and authorization
4. Keep your dependencies updated regularly
5. Use environment variables for sensitive configuration
6. Apply the principle of least privilege for database connections

## Disclosure Policy

When security vulnerabilities are reported, we follow this disclosure process:

1. Confirm the vulnerability and determine its scope
2. Develop and test a fix
3. Release a patch for the vulnerability
4. Announce the vulnerability (without specific exploit details) and credit the reporter (if desired)

## Security Update Process

Security updates are released as patch versions (e.g., 0.1.1 → 0.1.2) and are announced through:

- GitHub releases
- Release notes in the project documentation
- Communications to users who have opted in for security notifications

## Third-Party Dependencies

ArchiPy relies on several third-party packages. We regularly monitor:

- Security advisories for dependencies
- CVE databases for relevant vulnerabilities
- Updates and patches for all dependencies

We recommend users regularly run `poetry update` to ensure they have the latest secure versions of all dependencies.

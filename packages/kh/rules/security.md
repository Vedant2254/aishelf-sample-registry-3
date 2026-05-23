# Security Rules

This rule defines security best practices and guidelines that should be followed in code development.

## Core Principles

1. **Never trust user input** - Always validate and sanitize
2. **Principle of least privilege** - Grant minimum necessary permissions
3. **Defense in depth** - Implement multiple layers of security
4. **Secure by default** - Default configurations should be secure

## Specific Rules

### Authentication & Authorization
- Use strong password policies
- Implement multi-factor authentication where possible
- Validate all authentication tokens
- Check authorization on every sensitive operation

### Data Protection
- Encrypt sensitive data at rest and in transit
- Never log sensitive information
- Use secure key management practices
- Implement data retention policies

### Code Security
- Avoid hardcoded credentials and secrets
- Use parameterized queries to prevent SQL injection
- Sanitize all user inputs to prevent XSS
- Keep dependencies updated and secure

### Infrastructure Security
- Use HTTPS everywhere
- Implement proper CORS policies
- Secure all API endpoints
- Monitor for security events

## Enforcement

These rules should be enforced through:
- Code reviews
- Automated security scanning
- Security testing
- Regular security audits

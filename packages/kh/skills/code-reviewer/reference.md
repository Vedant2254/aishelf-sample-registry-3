# Code Review Reference Guide

## Security Checklist

### Input Validation
- [ ] All user inputs are validated and sanitized
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] CSRF tokens for state-changing operations
- [ ] File upload restrictions (type, size, content validation)

### Authentication & Authorization
- [ ] Proper authentication mechanisms
- [ ] Authorization checks on all protected resources
- [ ] Secure password storage (hashing + salt)
- [ ] Session management (timeout, secure cookies)
- [ ] API key/token security

### Data Protection
- [ ] Sensitive data encrypted at rest and in transit
- [ ] No hardcoded secrets or credentials
- [ ] Proper error handling (no sensitive info in errors)
- [ ] Secure logging (no passwords/tokens in logs)

## Performance Checklist

### Algorithm Efficiency
- [ ] Appropriate data structures used
- [ ] No unnecessary nested loops
- [ ] Database queries optimized (indexes, no N+1)
- [ ] Caching implemented where beneficial
- [ ] Pagination for large datasets

### Resource Management
- [ ] Proper connection pooling
- [ ] File handles and streams closed
- [ ] Memory leaks prevented
- [ ] Async operations for I/O-bound tasks

## Best Practices Checklist

### Code Quality
- [ ] Functions are small and focused (single responsibility)
- [ ] Meaningful variable and function names
- [ ] No magic numbers (use named constants)
- [ ] DRY principle followed (no code duplication)
- [ ] Proper error handling and logging

### Documentation
- [ ] Public APIs documented
- [ ] Complex logic explained with comments
- [ ] README updated if needed
- [ ] Breaking changes noted

### Testing
- [ ] Unit tests for new functionality
- [ ] Edge cases covered
- [ ] Test coverage maintained or improved
- [ ] Integration tests for critical paths

## Common Anti-Patterns to Avoid

1. **God Objects**: Classes that do too much
2. **Spaghetti Code**: Tangled control flow
3. **Copy-Paste Programming**: Duplicated code blocks
4. **Premature Optimization**: Optimizing before profiling
5. **Callback Hell**: Deeply nested callbacks (use async/await)
6. **Tight Coupling**: Components too dependent on each other

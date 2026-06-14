---
name: code-reviewer
description: Comprehensive code review with security, performance, and best practice checks
tags: [code-review, security, performance, best-practices]
---

# Code Review Process

Follow these steps to perform a thorough code review:

## 1. Load Review Guidelines

First, read the detailed review checklist:
- Load `reference.md` for the complete review criteria
- Load `examples.md` to see examples of good and bad patterns

## 2. Analyze the Code

Review the code against these key areas:
- **Security**: Check for vulnerabilities, input validation, authentication issues
- **Performance**: Look for inefficient algorithms, memory leaks, unnecessary operations
- **Best Practices**: Verify code follows language conventions and team standards
- **Maintainability**: Assess readability, documentation, and code organization

## 3. Run Automated Checks

Execute the automated review script:
```bash
python scripts/review_checker.py <file_path>
```

This script will:
- Run static analysis
- Check for common anti-patterns
- Validate code formatting
- Output a summary report

## 4. Provide Structured Feedback

Use the template from `templates/review-template.md` to structure your feedback:
- List critical issues first
- Provide specific line numbers and suggestions
- Include positive observations
- Suggest concrete improvements

## 5. Generate Summary

Create a concise summary including:
- Overall code quality score (1-10)
- Number of critical/major/minor issues
- Top 3 recommendations
- Approval status (Approved/Needs Changes/Rejected)

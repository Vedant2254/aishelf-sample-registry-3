#!/usr/bin/env python3
"""
Automated code review checker
Analyzes code files for common issues and anti-patterns
"""

import sys
import re
from pathlib import Path

def check_file(file_path):
    """Run automated checks on a code file"""
    
    issues = {
        'critical': [],
        'major': [],
        'minor': []
    }
    
    try:
        content = Path(file_path).read_text()
        lines = content.split('\n')
        
        # Check for common issues
        for i, line in enumerate(lines, 1):
            # Check for hardcoded secrets
            if re.search(r'(password|secret|api_key|token)\s*=\s*["\'][^"\']+["\']', line, re.I):
                issues['critical'].append(f"Line {i}: Possible hardcoded secret")
            
            # Check for SQL injection risk
            if re.search(r'execute\s*\(\s*["\'].*%s.*["\'].*%', line):
                issues['critical'].append(f"Line {i}: Potential SQL injection risk")
            
            # Check for long lines
            if len(line) > 120:
                issues['minor'].append(f"Line {i}: Line too long ({len(line)} chars)")
            
            # Check for TODO/FIXME
            if re.search(r'(TODO|FIXME)', line, re.I):
                issues['minor'].append(f"Line {i}: Unresolved TODO/FIXME")
        
        # Print results
        print(f"\n{'='*60}")
        print(f"Code Review Report: {file_path}")
        print(f"{'='*60}\n")
        
        total_issues = sum(len(v) for v in issues.values())
        
        if total_issues == 0:
            print("✓ No issues found!")
        else:
            if issues['critical']:
                print(f"🔴 CRITICAL ({len(issues['critical'])} issues):")
                for issue in issues['critical']:
                    print(f"  - {issue}")
                print()
            
            if issues['major']:
                print(f"🟡 MAJOR ({len(issues['major'])} issues):")
                for issue in issues['major']:
                    print(f"  - {issue}")
                print()
            
            if issues['minor']:
                print(f"🔵 MINOR ({len(issues['minor'])} issues):")
                for issue in issues['minor'][:5]:  # Show first 5
                    print(f"  - {issue}")
                if len(issues['minor']) > 5:
                    print(f"  ... and {len(issues['minor']) - 5} more")
                print()
        
        print(f"Total issues: {total_issues}")
        print(f"{'='*60}\n")
        
        return total_issues
        
    except Exception as e:
        print(f"Error analyzing file: {e}")
        return -1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python review_checker.py <file_path>")
        sys.exit(1)
    
    exit_code = check_file(sys.argv[1])
    sys.exit(0 if exit_code >= 0 else 1)

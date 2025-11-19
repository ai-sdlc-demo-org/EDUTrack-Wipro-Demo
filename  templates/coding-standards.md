# Coding Standards

## Document Control
| Version | Date | Author | Reviewer | Changes |
|---------|------|--------|----------|---------|
| 0.1     |      |        |          | Draft   |
| 1.0     |      |        |          | Baseline |

## Approvals
| Name | Role | Signature | Date |
|------|------|-----------|------|
|      |      |           |      |

## 1. Executive Summary
### 1.1 Purpose
_Establish coding standards, conventions, and best practices to ensure code quality, maintainability, security, and team consistency._

### 1.2 Scope
_Applicable to all source code, configuration files, scripts, and documentation in the project._

### 1.3 Enforcement
- **Code Reviews:** All code must be reviewed before merge
- **Automated Linting:** CI pipeline enforces linting rules
- **Static Analysis:** SonarQube/CodeQL scans for violations
- **Training:** Onboarding and continuous education

## 2. General Principles
- **Readability:** Code is read more than written; optimise for clarity
- **Simplicity:** Favour simple solutions over clever ones (KISS)
- **Consistency:** Follow established patterns and conventions (DRY)
- **Testability:** Design for unit, integration, and e2e testing
- **Security First:** Validate input, sanitize output, use parameterized queries
- **Performance Awareness:** Profile before optimizing; avoid premature optimization

## 3. Language-Specific Standards
### 3.1 Python
- **Style Guide:** PEP 8
- **Linter:** pylint, flake8, black (formatter)
- **Type Hints:** Use type annotations for function signatures
- **Docstrings:** Google-style or NumPy-style
- **Max Line Length:** 100 characters
- **Import Order:** Standard library, third-party, local (sorted alphabetically)
- **Naming:** `snake_case` for functions/variables, `PascalCase` for classes

### 3.2 JavaScript/TypeScript
- **Style Guide:** Airbnb JavaScript Style Guide
- **Linter:** ESLint with TypeScript plugin
- **Formatter:** Prettier
- **Type Safety:** Strict TypeScript (`strict: true`)
- **Max Line Length:** 100 characters
- **Naming:** `camelCase` for variables/functions, `PascalCase` for classes/components
- **File Extensions:** `.ts` for TypeScript, `.tsx` for React components

### 3.3 Java
- **Style Guide:** Google Java Style Guide
- **Linter:** Checkstyle, SpotBugs, PMD
- **Formatter:** google-java-format
- **Naming:** `camelCase` for methods/variables, `PascalCase` for classes
- **Package Naming:** Reverse domain (com.company.product)
- **Constants:** `UPPER_SNAKE_CASE`

### 3.4 Go
- **Style Guide:** Effective Go
- **Linter:** golint, golangci-lint
- **Formatter:** gofmt, goimports
- **Naming:** `MixedCase` (no underscores), exported names start with capital
- **Error Handling:** Always check errors; use `errors.Is()`, `errors.As()`

## 4. Naming Conventions
### 4.1 Variables & Functions
| Language | Convention | Example |
|----------|------------|---------|
| Python   | snake_case | `user_count`, `calculate_total()` |
| JavaScript/TypeScript | camelCase | `userCount`, `calculateTotal()` |
| Java     | camelCase | `userCount`, `calculateTotal()` |
| Go       | MixedCase | `UserCount`, `CalculateTotal()` |

### 4.2 Constants
| Language | Convention | Example |
|----------|------------|---------|
| Python   | UPPER_SNAKE_CASE | `MAX_RETRIES = 3` |
| JavaScript/TypeScript | UPPER_SNAKE_CASE | `const MAX_RETRIES = 3;` |
| Java     | UPPER_SNAKE_CASE | `public static final int MAX_RETRIES = 3;` |
| Go       | MixedCase | `const MaxRetries = 3` |

### 4.3 Classes & Interfaces
| Language | Convention | Example |
|----------|------------|---------|
| Python   | PascalCase | `class UserService:` |
| TypeScript | PascalCase, prefix interfaces with `I` | `class UserService`, `interface IUser` |
| Java     | PascalCase | `public class UserService` |
| Go       | PascalCase | `type UserService struct` |

### 4.4 Files & Directories
- **Files:** Match primary class/module name (`UserService.java`, `user_service.py`)
- **Directories:** `lowercase` or `snake_case` (`src/user_service/`, `src/userService/`)
- **Test Files:** Suffix with `_test` or `.test` (`user_service_test.py`, `UserService.test.ts`)

## 5. Code Structure & Organization
### 5.1 File Organization
```
src/
├── controllers/       # HTTP request handlers
├── services/          # Business logic
├── repositories/      # Data access layer
├── models/            # Data models, entities
├── utils/             # Utility functions
├── middleware/        # Express/FastAPI middleware
├── config/            # Configuration files
└── tests/             # Test files (mirror src structure)
```

### 5.2 Function Length
- **Target:** <50 lines per function
- **Maximum:** 100 lines (refactor if exceeded)
- **Single Responsibility:** Each function should do one thing

### 5.3 Class Length
- **Target:** <300 lines per class
- **Maximum:** 500 lines (consider splitting into multiple classes)

## 6. Documentation Standards
### 6.1 Inline Comments
- **When:** Explain *why*, not *what* (code should be self-explanatory)
- **Avoid:** Redundant comments (`i++; // increment i`)
- **Use:** For complex logic, edge cases, workarounds, TODOs

### 6.2 Function Documentation
**Python (Google-style docstring):**
```python
def calculate_total(items: List[Item], tax_rate: float) -> float:
    """Calculate the total price including tax.
    
    Args:
        items: List of items to calculate total for.
        tax_rate: Tax rate as decimal (e.g., 0.08 for 8%).
    
    Returns:
        Total price including tax.
    
    Raises:
        ValueError: If tax_rate is negative.
    """
```

**TypeScript (JSDoc):**
```typescript
/**
 * Calculate the total price including tax.
 * @param items - List of items to calculate total for
 * @param taxRate - Tax rate as decimal (e.g., 0.08 for 8%)
 * @returns Total price including tax
 * @throws {Error} If taxRate is negative
 */
function calculateTotal(items: Item[], taxRate: number): number {
```

### 6.3 README Files
Every module/package should have a README with:
- Purpose and overview
- Installation/setup instructions
- Usage examples
- API documentation (if applicable)
- Contributing guidelines
- License

## 7. Error Handling & Logging
### 7.1 Error Handling
- **Never** swallow exceptions silently
- **Always** log errors with context
- **Use** specific exception types
- **Fail fast:** Validate early, fail gracefully

**Python:**
```python
try:
    result = risky_operation()
except SpecificException as e:
    logger.error(f"Operation failed: {e}", exc_info=True)
    raise ServiceException("User-friendly message") from e
```

**TypeScript:**
```typescript
try {
    const result = await riskyOperation();
} catch (error) {
    logger.error('Operation failed', { error, context });
    throw new ServiceException('User-friendly message', { cause: error });
}
```

### 7.2 Logging Standards
- **Levels:** DEBUG, INFO, WARN, ERROR, CRITICAL
- **Structure:** JSON format for production
- **Content:** Include request ID, user ID, timestamp, context
- **Secrets:** Never log passwords, tokens, PII
- **Performance:** Use async logging for high-throughput services

**Example:**
```json
{
  "level": "ERROR",
  "timestamp": "2025-11-14T12:00:00Z",
  "request_id": "req_abc123",
  "user_id": "usr_456",
  "service": "user-service",
  "message": "Failed to create user",
  "error": "DatabaseConnectionError",
  "stack_trace": "..."
}
```

## 8. Security Coding Practices
### 8.1 Input Validation
- **Validate** all user input (whitelist, not blacklist)
- **Sanitize** before output (prevent XSS)
- **Use** parameterized queries (prevent SQL injection)
- **Limit** input length, type, format

### 8.2 Authentication & Authorization
- **Never** store passwords in plain text (use bcrypt, scrypt, Argon2)
- **Use** JWT with short expiration (1 hour)
- **Implement** role-based access control (RBAC)
- **Check** authorization at every endpoint

### 8.3 Secrets Management
- **Never** commit secrets to version control
- **Use** environment variables or secret managers (Vault, AWS Secrets Manager)
- **Rotate** secrets regularly
- **Audit** secret access

### 8.4 OWASP Top 10 Compliance
- **A01: Broken Access Control** → Implement RBAC, check permissions
- **A02: Cryptographic Failures** → Use TLS 1.3, encrypt PII
- **A03: Injection** → Use parameterized queries, input validation
- **A07: Identification & Authentication** → MFA, strong password policy
- **A10: SSRF** → Validate URLs, use allowlists

## 9. Testing Requirements
### 9.1 Unit Test Coverage
- **Target:** 80% code coverage
- **Minimum:** 70% coverage (CI gate)
- **Focus:** Business logic, edge cases, error paths

### 9.2 Test Naming
```python
def test_calculate_total_with_valid_input_returns_correct_sum():
    # Given
    items = [Item(price=10.0), Item(price=20.0)]
    tax_rate = 0.1
    
    # When
    result = calculate_total(items, tax_rate)
    
    # Then
    assert result == 33.0
```

### 9.3 Test Organization
- **Arrange-Act-Assert (AAA)** pattern
- **Given-When-Then** for BDD
- **One assertion** per test (when possible)
- **Independent tests:** No shared state

## 10. Version Control Standards
### 10.1 Git Commit Messages
**Format:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Example:**
```
feat(user-service): add email validation

Implement regex-based email validation for user registration.
Validates format and checks for disposable email domains.

Closes #123
```

### 10.2 Branch Naming
- **Feature:** `feature/USER-123-add-email-validation`
- **Bugfix:** `bugfix/USER-456-fix-login-error`
- **Hotfix:** `hotfix/USER-789-critical-security-patch`
- **Release:** `release/v1.2.0`

### 10.3 Pull Request Standards
- **Title:** Clear, concise description
- **Description:** What, why, how, testing performed
- **Reviewers:** At least 2 approvals required
- **Checks:** All CI checks must pass
- **Size:** <500 lines changed (split large PRs)

## 11. Code Review Checklist
- [ ] Code follows language-specific style guide
- [ ] Functions and variables have meaningful names
- [ ] Code is well-documented with docstrings/comments
- [ ] Error handling is implemented correctly
- [ ] No secrets or PII in code or logs
- [ ] Input validation and output sanitization in place
- [ ] Unit tests written with adequate coverage
- [ ] No code duplication (DRY principle)
- [ ] Performance considerations addressed
- [ ] Security best practices followed (OWASP)
- [ ] Logging is appropriate and structured
- [ ] No deprecated APIs or libraries used

## 12. Performance Guidelines
- **Database Queries:** Use indexes, avoid N+1 queries, pagination
- **API Calls:** Implement caching, rate limiting, timeouts
- **Algorithms:** O(n) or better for large datasets
- **Memory:** Avoid memory leaks, use streaming for large files
- **Profiling:** Profile before optimizing

## 13. Accessibility Standards
- **HTML:** Semantic tags, ARIA labels, keyboard navigation
- **Colors:** WCAG 2.1 AA contrast ratios (4.5:1 for text)
- **Forms:** Labels, error messages, focus indicators
- **Testing:** Screen reader testing, keyboard-only navigation

## 14. Third-Party Libraries
### 14.1 Selection Criteria
- **License:** Compatible with project license
- **Maintenance:** Active development, recent updates
- **Security:** No known vulnerabilities (npm audit, Snyk)
- **Size:** Minimize bundle size

### 14.2 Approval Process
- **Review:** Architect or tech lead approval required
- **Document:** Record in SBOM (Software Bill of Materials)
- **Update:** Quarterly dependency updates

## 15. Configuration Management
- **Environment Variables:** Use `.env` files (not committed)
- **Config Files:** YAML, JSON, TOML (not hardcoded)
- **Secrets:** Never in code; use secret managers
- **Defaults:** Provide sensible defaults

## 16. Traceability
| Standard | Requirement IDs (RTM) | Rationale |
|----------|----------------------|-----------|
| Security coding practices | NFR-SEC-001 | OWASP compliance |
| Test coverage 80% | NFR-QA-002 | Quality assurance |
| Accessibility | NFR-ACC-001 | WCAG 2.1 AA compliance |

## Validation & Quality Checklist
- [ ] Coding standards cover all languages used in the project.
- [ ] Naming conventions are clearly defined and consistent.
- [ ] Code structure and organization guidelines are established.
- [ ] Documentation standards (inline comments, docstrings, README) are specified.
- [ ] Error handling and logging standards are comprehensive.
- [ ] Security coding practices address OWASP Top 10.
- [ ] Testing requirements include coverage targets and naming conventions.
- [ ] Version control standards (commits, branches, PRs) are defined.
- [ ] Code review checklist covers quality, security, and performance.
- [ ] Third-party library selection and approval process is documented.
- [ ] Standards are enforced via automated linting, CI checks, and code reviews.
- [ ] Document has been reviewed and approved by engineering leadership.

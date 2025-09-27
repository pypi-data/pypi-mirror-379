# Blank Line Enforcement Script Design

## Overview

A standalone script that enforces the blank line rules defined in CLAUDE.md, similar to `black` or `ruff`. The script processes Python files in-place, applying complex blank line rules while preserving existing multiline formatting.

## Architecture

### Core Components

1. **MultilineParser**: Handles line-by-line reading with bracket tracking for multiline statements
2. **StatementClassifier**: Identifies statement types and maintains block classification
3. **BlankLineRuleEngine**: Applies configurable blank line rules based on block transitions
4. **FileAnalyzer**: Manages parsing and analysis of file structure
5. **BlankLineConfig**: Configuration system for customizable blank line rules
6. **CLI Interface**: Command-line tool with file/directory processing and configuration support
7. **FileProcessor**: Handles file I/O and change detection

### Architecture Overview

Prism uses a two-pass architecture with configurable rules:

```
Configuration Layer:
├── BlankLineConfig (TOML parsing, CLI overrides)
├── Validation (0-3 range, valid block types)
└── Default + Override system

Processing Pipeline:
├── Pass 1: FileAnalyzer
│   ├── MultilineParser (bracket tracking, statement completion)
│   └── StatementClassifier (block type identification)
├── Pass 2: BlankLineRuleEngine
│   ├── Configuration-driven rule application
│   ├── Scope-aware processing (nested indentation)
│   └── Special rule handling (consecutive Control/Definition)
└── Pass 3: FileProcessor
    ├── File reconstruction with correct spacing
    └── Change detection and conditional writing
```

## Key Design Decisions

### 1. Configuration System Architecture
- **Default + Override Pattern**: Simple default for common cases, fine-grained overrides for specific needs
- **TOML Configuration**: Standard format with validation (0-3 blank lines)
- **CLI Precedence**: Command-line flags override config file settings
- **Backward Compatibility**: No configuration = current behavior (1 blank line)

### 2. Multiline Statement Handling
- **Buffer physical lines** until complete logical statement is formed
- **Preserve original formatting** - do not alter line breaks within multiline statements
- **Classify entire statement** once complete (e.g., `x = func(\n  arg\n)` is Assignment)

#### 2.1 Docstring Preservation (Critical)
**Docstrings are atomic units** - their internal structure must NEVER be modified:

- **Triple-quoted strings** (`"""` or `'''`) are tracked from opening to closing quotes
- **All content within docstrings is preserved exactly**, including:
  - Blank lines
  - Lines starting with `#` (not treated as comments)
  - Indentation patterns
  - Special formatting (markdown, reStructuredText, etc.)
  
**Implementation Details:**
- `MultilineParser` tracks `inString` state and `stringDelim` for proper quote matching
- `FileAnalyzer` checks `parser.inString` before processing blank lines or comments
- When `inString=True`, lines are added to current statement without special handling

### 3. Block Classification Priority
```python
# Classification precedence (highest to lowest):
1. Assignment block (x = foo(), comprehensions, lambdas)
2. Import block (import statements)
3. Definition block (def/class complete structures)
4. Control block (if/for/while/try/with complete structures)
5. Declaration block (global/nonlocal)
6. Call block (foo(), del, assert, pass, raise, yield, return)
7. Comment block (consecutive comment lines)
```

### 4. Configuration Structure
```toml
# prism.toml
[blank_lines]
default_between_different = 1  # Default spacing
consecutive_control = 1        # Special consecutive rules
consecutive_definition = 1

# Fine-grained overrides (optional)
assignment_to_call = 2
import_to_assignment = 0
```

### 5. Nested Control Structure Tracking
- **Independent rule application** at each indentation level
- **Secondary clause handling**: No blank lines before `elif`/`else`/`except`/`finally`
- **Complete structure detection**: Track when control blocks end with/without optional clauses
- **Scope boundary enforcement**: Always 0 blank lines at start/end of scopes (non-configurable)

### 6. Comment Block Behavior - Special "Leave-As-Is" Rules

Comments have **fundamentally different behavior** from other block types and do NOT follow normal block transition rules:

#### 6.1 Consecutive Comments Within a Block
- **No blank lines between consecutive comments** (e.g., copyright headers)
- **Comment break rule**: Only add blank lines before a comment if the previous block was NOT a comment
- **Implementation**: `if prevBlockType != BlockType.COMMENT` check prevents breaking up comment blocks

#### 6.2 Transitions FROM Comment Blocks to Other Blocks  
Comments follow a **"leave-as-is"** policy that overrides normal block transition rules:

**Case 1: Existing blank line after comment block**
```python
# Comment block
# More comments

import foo  # <- Preserve existing blank line (leave-as-is)
```
- **Behavior**: Preserve the existing blank line
- **Implementation**: `preserveExistingBlank` logic detects and preserves

**Case 2: No existing blank line after comment block**
```python
# Comment block  
import foo  # <- Do NOT add blank line
```
- **Behavior**: Do NOT apply normal block transition rules
- **Implementation**: `if prevBlockType != BlockType.COMMENT` check bypasses normal transition logic

#### 6.3 Algorithm Details

**Step 1: Detect existing blank lines after comments (lines 57-64)**
```python
for i in range(len(statements) - 1):
  if statements[i].isComment and statements[i + 1].isBlank:
    # Find next non-blank statement and mark for preservation
    preserveExistingBlank[next_non_blank_idx] = True
```

**Step 2: Comment break rule (lines 95-96)**  
```python
if prevBlockType != BlockType.COMMENT and not startsNewScope[i]:
  shouldHaveBlankLine[i] = True  # Only add blank BEFORE comment if prev wasn't comment
```

**Step 3: Prevent normal transitions after comments (lines 171-172)**
```python  
if prevBlockType != BlockType.COMMENT:
  shouldHaveBlankLine[i] = self._needsBlankLineBetween(prevBlockType, stmt.blockType) > 0
# If prevBlockType == BlockType.COMMENT, no blank line logic applies
```

#### 6.4 Critical Edge Cases

1. **Copyright headers**: Multiple consecutive comment lines with no internal blank lines
2. **Inline documentation**: Comments within function bodies preserve existing spacing
3. **Mixed scenarios**: Comments followed by different block types only get blank lines if they already existed

#### 6.5 Key Principle
**Comments are "transparent" to blank line rules** - they don't trigger normal block transitions, they only preserve what already exists.

## Implementation Architecture

### Configuration System
```python
@dataclass
class BlankLineConfig:
    defaultBetweenDifferent: int = 1
    transitions: dict[tuple[BlockType, BlockType], int]
    consecutiveControl: int = 1
    consecutiveDefinition: int = 1
    
    @classmethod
    def fromToml(cls, path: Path) -> 'BlankLineConfig'
    def getBlankLines(self, fromBlock: BlockType, toBlock: BlockType) -> int
```

### Rule Engine with Configuration
```python
class BlankLineRuleEngine:
    def __init__(self, config: BlankLineConfig):
        self.config = config
        
    def applyRules(self, statements: list[Statement]) -> list[int]:
        # Returns list of blank line counts (not just boolean)
        pass
        
    def _needsBlankLineBetween(self, prevType: BlockType, currentType: BlockType) -> int:
        return self.config.getBlankLines(prevType, currentType)
```

### CLI with Configuration Support
```python
def loadConfiguration(args) -> BlankLineConfig:
    # Load from TOML file (./prism.toml by default)
    # Apply CLI overrides
    # Validate all values (0-3 range)
    pass
```

## Critical Edge Cases

1. **Nested control with secondary clauses**:
```python
if condition:
    if nested:
        pass
    # NO blank line here
    else:
        pass
# NO blank line here  
else:
    pass
```

2. **Comment breaks with preserved spacing**:
```python
x = 1

# Comment causes break
y = 2  # This starts new Assignment block
```

3. **Multiline classification**:
```python
result = complexFunction(
    arg1,
    arg2
)  # Entire construct is Assignment block
```

4. **Mixed statement classification**:
```python
x = someCall()  # Assignment block (precedence rule)
```

## Testing Strategy

1. **Unit tests** for each component (LineParser, BlockClassifier, BlankLineEngine)
2. **Integration tests** with complex nested scenarios
3. **Edge case validation** for all rule combinations
4. **Performance tests** on large Python files
5. **Regression tests** to ensure no unintended modifications

## CLI Interface Design

```bash
# Basic usage (same as before)
prism file.py
prism src/
prism --check file.py

# Configuration options
prism --config custom.toml file.py
prism --no-config file.py
prism --blank-lines-default=2 file.py
prism --blank-lines assignment_to_call=0 file.py
prism --blank-lines-consecutive-control=2 file.py

# Multiple overrides
prism --blank-lines assignment_to_call=0 --blank-lines import_to_control=2 file.py
```

### Configuration File Format
```toml
# prism.toml - Complete example
[blank_lines]
# Default spacing between different block types
default_between_different = 1

# Special consecutive block rules
consecutive_control = 1
consecutive_definition = 1

# Fine-grained transition overrides
assignment_to_call = 2
call_to_assignment = 2
import_to_assignment = 0
assignment_to_import = 0
control_to_definition = 2
```

## Performance Considerations

- **Two-pass processing** (analyze, then apply rules)
- **Configuration loaded once** per execution, not per file
- **Fast bracket tracking** with simple character scanning
- **Efficient indentation detection** without full AST parsing
- **Change detection** to avoid unnecessary file writes
- **TOML parsing** only when configuration file exists and is newer

## Future Improvements

- Add support for additional file types beyond Python
- Implement parallel processing for large codebases
- Add more granular configuration options for different block types
- Consider adding support for custom user-defined rules

## Enhancement Suggestions from Code Review

### ENHANCEMENT-001: Visitor Pattern for Statement Analysis
**Benefit**: Make the code more extensible for future block types
**Approach**: Implement visitor pattern for statement analysis instead of current switch-based classification
**Impact**: Easier to add new block types without modifying core analysis logic

### ENHANCEMENT-002: Configuration Validation Schema
**Benefit**: Better user feedback on configuration errors
**Approach**: Add configuration validation schema using a library like Pydantic
**Impact**: Clearer error messages and validation, better developer experience

### ENHANCEMENT-003: Parallel Processing for Multiple Files
**Benefit**: Improve performance on large codebases
**Approach**: Implement parallel processing when multiple files are specified
**Impact**: Significant performance improvement for batch operations

### ENHANCEMENT-004: Comprehensive Logging Framework
**Benefit**: Aid debugging and provide insights into processing decisions
**Approach**: Add structured logging to show rule decisions, block classifications, etc.
**Impact**: Better troubleshooting and understanding of tool behavior

## Outstanding Code Review Issues (Non-Critical)

### MAJOR-003: Excessive Complexity in Rules Engine
**File**: `src/prism/rules.py:174-204`
**Problem**: The main blank line decision logic contains deeply nested conditionals with multiple boolean flags and complex state tracking. Cyclomatic complexity likely exceeds 10.
**Risk**: High - Core logic that determines all blank line placement decisions
**Approach**: Break down into smaller, focused helper methods; separate concerns for scope detection, comment handling, and block transitions; consider state machine pattern
**Priority**: Medium - affects maintainability but current logic works correctly

### MAJOR-004: Inconsistent Error Handling Strategy
**File**: Multiple files across codebase
**Problem**: Mixed error handling patterns - some functions return `False` on errors, others print and return `False`, others might raise exceptions
**Risk**: Medium - requires coordinated changes across entire codebase
**Approach**: Establish consistent error handling strategy (exceptions vs return codes); ensure all error messages are actionable; document strategy for future development
**Priority**: Low - current patterns work but inconsistent developer experience
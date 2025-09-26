# Phase 0: Research & Decisions

## Project Analysis Summary

**Current State**: AI-generated MCP project with messy structure but functional 18 PDF processing tools
**Goal**: Professional refactoring for PyPI publication with uvx support
**Constraint**: Zero functional changes to existing tools

## Research Areas & Decisions

### 1. Project Structure Optimization
**Decision**: Keep current `src/pdfreadermcp/` structure, improve organization
**Rationale**: 
- Current structure follows Python packaging standards
- Tools are logically organized by functionality
- No need for major restructuring, just cleanup

**Alternatives considered**: 
- Flat structure: Rejected - too many tools for flat organization
- Functional grouping: Rejected - current grouping by tool type works well

### 2. PyPI Packaging Configuration
**Decision**: Update pyproject.toml for proper uvx support and metadata
**Rationale**: 
- Current pyproject.toml has good foundation
- Needs entry point optimization for uvx execution
- Missing important PyPI metadata fields

**Alternatives considered**:
- setup.py: Rejected - pyproject.toml is modern standard
- Poetry: Rejected - project already uses uv

### 3. Entry Point Strategy
**Decision**: Modify entry point to support both `pdfreadermcp` and `uvx pdfreadmcp`
**Rationale**: 
- Current entry point works but needs uvx optimization
- Should maintain backward compatibility
- Main function in __main__.py already exists

**Alternatives considered**:
- New entry script: Rejected - adds complexity
- CLI wrapper: Rejected - overkill for MCP server

### 4. Dependency Management
**Decision**: Clean up and optimize current dependencies, add testing framework
**Rationale**: 
- Current deps are appropriate but may have unused/redundant packages
- Need pytest for proper testing
- uv.lock needs regeneration after cleanup

**Alternatives considered**:
- Switch to pip: Rejected - uv is superior for this use case
- Keep all deps: Rejected - cleanup needed for professional package

### 5. Code Quality Improvements
**Decision**: Apply Python best practices without changing tool interfaces
**Rationale**: 
- Improve type hints and documentation
- Add proper error handling
- Maintain all existing tool signatures and behavior

**Alternatives considered**:
- Major refactor: Rejected - violates constraint to preserve tools
- No changes: Rejected - defeats purpose of cleanup

### 6. Testing Strategy
**Decision**: Add comprehensive testing framework with tool validation
**Rationale**: 
- Currently minimal testing exists
- Need to verify tools work after refactoring
- Required for professional PyPI package

**Alternatives considered**:
- Manual testing only: Rejected - not scalable or reliable
- Integration tests only: Rejected - need both unit and integration

### 7. Documentation Updates
**Decision**: Update README and add proper package documentation
**Rationale**: 
- Current README is comprehensive but needs PyPI installation instructions
- Need proper docstrings throughout codebase

**Alternatives considered**:
- Keep existing docs: Rejected - needs uvx installation info
- Complete rewrite: Rejected - current docs are good foundation

## Technical Research Results

### MCP Server Best Practices
- FastMCP is the right choice for this project
- Current tool registration pattern is correct
- No changes needed to MCP implementation

### PyPI Publishing Requirements
- Need proper classifier metadata
- Requires long_description from README
- Should include development dependencies section
- Need proper version management strategy

### uv/uvx Integration
- Entry point should work with uvx out of the box
- Current console_scripts configuration needs minor tweaks
- No special uvx configuration needed beyond proper entry point

## Implementation Priorities

1. **High Priority**: Cleanup project structure, optimize pyproject.toml
2. **High Priority**: Add comprehensive testing framework
3. **Medium Priority**: Improve code quality and documentation
4. **Medium Priority**: Optimize dependencies and regenerate lockfile
5. **Low Priority**: Enhanced error messages and logging

## Risk Assessment

**Low Risk**: 
- Structure cleanup
- Dependency optimization  
- Documentation updates

**Medium Risk**: 
- Entry point modifications
- Testing framework addition

**High Risk**: 
- None identified - all changes are additive/cleanup only

## Phase 0 Complete
✅ All research areas identified and decisions documented
✅ No NEEDS CLARIFICATION items remain
✅ Ready for Phase 1 (Design & Contracts)

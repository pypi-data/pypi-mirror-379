
# Implementation Plan: PDF Reader MCP Refactoring and PyPI Publication

**Branch**: `001-ai-mcp-pypi` | **Date**: September 24, 2025 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-ai-mcp-pypi/spec.md`

## Execution Flow (/plan command scope)
```
1. Load feature spec from Input path
   → If not found: ERROR "No feature spec at {path}"
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
   → Detect Project Type from context (web=frontend+backend, mobile=app+api)
   → Set Structure Decision based on project type
3. Fill the Constitution Check section based on the content of the constitution document.
4. Evaluate Constitution Check section below
   → If violations exist: Document in Complexity Tracking
   → If no justification possible: ERROR "Simplify approach first"
   → Update Progress Tracking: Initial Constitution Check
5. Execute Phase 0 → research.md
   → If NEEDS CLARIFICATION remain: ERROR "Resolve unknowns"
6. Execute Phase 1 → contracts, data-model.md, quickstart.md, agent-specific template file (e.g., `CLAUDE.md` for Claude Code, `.github/copilot-instructions.md` for GitHub Copilot, `GEMINI.md` for Gemini CLI, `QWEN.md` for Qwen Code or `AGENTS.md` for opencode).
7. Re-evaluate Constitution Check section
   → If new violations: Refactor design, return to Phase 1
   → Update Progress Tracking: Post-Design Constitution Check
8. Plan Phase 2 → Describe task generation approach (DO NOT create tasks.md)
9. STOP - Ready for /tasks command
```

**IMPORTANT**: The /plan command STOPS at step 7. Phases 2-4 are executed by other commands:
- Phase 2: /tasks command creates tasks.md
- Phase 3-4: Implementation execution (manual or via tools)

## Summary
Refactor AI-generated PDF Reader MCP project to clean up messy code structure, optimize dependencies, and publish as professional PyPI package with uvx support. Preserve all 18 existing PDF processing tools while improving code organization and enabling easy installation via `uvx pdfreadmcp`.

## Technical Context
**Language/Version**: Python 3.11+ (current: using uv package manager)  
**Primary Dependencies**: FastMCP (MCP server), pdfplumber (text extraction), pypdf (PDF operations), pytesseract (OCR), pillow (imaging), pdf2image (conversion), langchain-text-splitters (chunking)  
**Storage**: File-based caching system with automatic invalidation, PDF files on disk  
**Testing**: pytest (needs to be added for comprehensive testing framework)  
**Target Platform**: Cross-platform (macOS, Linux, Windows) with Tesseract OCR system dependency
**Project Type**: single (MCP server with tools collection)  
**Performance Goals**: Fast PDF processing with intelligent caching, chunked text extraction for large documents  
**Constraints**: Must preserve all 18 existing tools unchanged, uvx executable requirement, clean dependency management  
**Scale/Scope**: 18 PDF tools across 7 modules, comprehensive metadata/OCR/optimization capabilities, production-ready PyPI package

**User Input Context**: 请开始对项目进行计划，要求你完全了解，再进行任务。

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Analysis**: Constitution template found but not project-specific. For MCP refactoring project:
- **Library-First Principle**: ✅ Each PDF tool is self-contained with clear interfaces
- **Testing Requirements**: ❌ Currently minimal testing, needs comprehensive test suite
- **Simplicity Principle**: ✅ Single MCP server project, not over-engineered
- **Documentation**: ✅ Comprehensive README and tool documentation exists

**Gate Status**: CONDITIONAL PASS - must add testing framework during refactoring

## Project Structure

### Documentation (this feature)
```
specs/[###-feature]/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)
```
# Option 1: Single project (DEFAULT)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# Option 2: Web application (when "frontend" + "backend" detected)
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# Option 3: Mobile + API (when "iOS/Android" detected)
api/
└── [same as backend above]

ios/ or android/
└── [platform-specific structure]
```

**Structure Decision**: Option 1 (Single project) - MCP server with tools collection, current structure is appropriate

## Phase 0: Outline & Research
1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:
   ```
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

## Phase 1: Design & Contracts
*Prerequisites: research.md complete*

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Generate contract tests** from contracts:
   - One test file per endpoint
   - Assert request/response schemas
   - Tests must fail (no implementation yet)

4. **Extract test scenarios** from user stories:
   - Each story → integration test scenario
   - Quickstart test = story validation steps

5. **Update agent file incrementally** (O(1) operation):
   - Run `.specify/scripts/bash/update-agent-context.sh cursor`
     **IMPORTANT**: Execute it exactly as specified above. Do not add or remove any arguments.
   - If exists: Add only NEW tech from current plan
   - Preserve manual additions between markers
   - Update recent changes (keep last 3)
   - Keep under 150 lines for token efficiency
   - Output to repository root

**Output**: data-model.md, /contracts/*, failing tests, quickstart.md, agent-specific file

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
- Load `.specify/templates/tasks-template.md` as base
- Generate refactoring tasks from contracts, data model, and quickstart validation
- Each tool interface → contract preservation test [P]
- Code cleanup → incremental refactoring tasks [P]
- PyPI packaging → build and publish tasks
- Integration validation → quickstart scenario tests

**Specific Task Categories**:
1. **Structure Cleanup** (5-7 tasks): Remove unnecessary files, organize imports, clean up project structure
2. **Code Quality** (8-10 tasks): Add type hints, improve documentation, refactor messy code sections  
3. **Testing Framework** (6-8 tasks): Add pytest, create contract tests, integration tests
4. **Packaging** (4-5 tasks): Update pyproject.toml, optimize dependencies, test building
5. **Publication** (3-4 tasks): PyPI publishing, uvx validation, documentation updates
6. **Validation** (3-4 tasks): Run quickstart scenarios, performance testing

**Ordering Strategy**:
- Structure cleanup first (prerequisite for other work)
- Testing framework parallel with code quality improvements [P]
- Package building after code stabilization
- Publication only after all tests pass
- Final validation as integration testing

**Estimated Output**: 30-35 numbered, ordered tasks with clear dependencies and parallelization markers

**IMPORTANT**: This phase is executed by the /tasks command, NOT by /plan

## Phase 3+: Future Implementation
*These phases are beyond the scope of the /plan command*

**Phase 3**: Task execution (/tasks command creates tasks.md)  
**Phase 4**: Implementation (execute tasks.md following constitutional principles)  
**Phase 5**: Validation (run tests, execute quickstart.md, performance validation)

## Complexity Tracking
*Fill ONLY if Constitution Check has violations that must be justified*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |


## Progress Tracking
*This checklist is updated during execution flow*

**Phase Status**:
- [x] Phase 0: Research complete (/plan command)
- [x] Phase 1: Design complete (/plan command)
- [x] Phase 2: Task planning complete (/plan command - describe approach only)
- [ ] Phase 3: Tasks generated (/tasks command)
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [x] Initial Constitution Check: CONDITIONAL PASS (testing framework needed)
- [x] Post-Design Constitution Check: PASS (testing addressed in task planning)
- [x] All NEEDS CLARIFICATION resolved
- [x] Complexity deviations documented (none - straightforward refactoring)

---
*Based on Constitution v2.1.1 - See `/memory/constitution.md`*

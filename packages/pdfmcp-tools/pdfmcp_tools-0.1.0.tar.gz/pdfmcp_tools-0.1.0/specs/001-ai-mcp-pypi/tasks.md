# Tasks: PDF Reader MCP Refactoring and PyPI Publication

**Input**: Design documents from `/specs/001-ai-mcp-pypi/`
**Prerequisites**: plan.md ✅, research.md ✅, data-model.md ✅, contracts/ ✅, quickstart.md ✅

## Execution Flow
```
1. ✅ Load plan.md from feature directory
   → Tech stack: Python 3.11+, FastMCP, uv package manager
   → Libraries: pdfplumber, pypdf, pytesseract, pillow, pdf2image, langchain-text-splitters
   → Structure: Single project (src/pdfreadermcp/)
2. ✅ Load design documents:
   → contracts/: 18 PDF tools across 5 categories (MUST preserve interfaces)
   → data-model.md: PDFDocument, ToolResult, CacheEntry entities
   → research.md: Keep structure, add testing, optimize packaging
3. ✅ Generate tasks by category: Setup → Tests → Refactoring → Packaging → Publication → Validation
4. ✅ Apply rules: Different files = [P], Tests before implementation (TDD)
5. ✅ Numbered T001-T035, dependency-ordered
6. ✅ Ready for execution
```

## Task Categories Summary
- **Setup & Cleanup** (6 tasks): Project structure, dependencies, cleanup
- **Testing Framework** (8 tasks): pytest setup, contract tests, integration tests  
- **Code Refactoring** (10 tasks): Type hints, documentation, code quality
- **Packaging** (6 tasks): pyproject.toml, dependencies, build testing
- **Publication** (3 tasks): PyPI upload, uvx validation
- **Final Validation** (2 tasks): Quickstart scenarios, performance testing

---

## Phase 3.1: Setup & Project Cleanup ✅ COMPLETE

- [x] **T001** Clean up unnecessary files and directories (remove __pycache__, .DS_Store, temp files)
- [x] **T002** [P] Add pytest testing framework to pyproject.toml dev dependencies  
- [x] **T003** [P] Create comprehensive .gitignore file for Python/PyPI project
- [x] **T004** [P] Create tests/ directory structure (tests/unit/, tests/integration/, tests/contract/)
- [x] **T005** Backup current uv.lock and prepare for dependency cleanup
- [x] **T006** Initialize pytest configuration in pyproject.toml and pytest.ini

## Phase 3.2: Contract Tests First (TDD) ✅ COMPLETE

**✅ CRITICAL TDD SUCCESS: 283 tests written, 20 strategic failures found real issues**

### Text Processing Tools Contract Tests (5 tools) ✅
- [x] **T007** [P] Contract test read_pdf in tests/contract/test_read_pdf.py
- [x] **T008** [P] Contract test extract_page_text in tests/contract/test_extract_page_text.py  
- [x] **T009** [P] Contract test search_pdf_text in tests/contract/test_search_pdf_text.py
- [x] **T010** [P] Contract test find_and_highlight_text in tests/contract/test_find_highlight.py
- [x] **T011** [P] Contract test get_pdf_metadata in tests/contract/test_get_metadata.py

### Document Operations Contract Tests (5 tools) ✅
- [x] **T012** [P] Contract test split_pdf in tests/contract/test_split_pdf.py
- [x] **T013** [P] Contract test extract_pages in tests/contract/test_extract_pages.py
- [x] **T014** [P] Contract test merge_pdfs in tests/contract/test_merge_pdfs.py

### Additional Contract Tests Completed (8 tools) ✅
- [x] **T015-T022** Contract tests for OCR, metadata, image conversion, and optimization tools

**TDD Results**: 283 total tests (263 passed, 20 failed) - failures identified real interface issues to fix during refactoring

## Phase 3.3: Code Refactoring (ONLY after contract tests are failing)

### Core Server & Structure Refactoring
- [x] **T015** Refactor src/pdfreadermcp/server.py - improve imports, add type hints, clean up structure ✅ **283/283 contract tests passing**
- [x] **T016** Refactor src/pdfreadermcp/__main__.py - optimize entry point for uvx compatibility ✅ **Enhanced logging, error handling, uvx optimization**
- [x] **T017** [P] Refactor src/pdfreadermcp/tools/pdf_reader.py - add type hints, improve error handling ✅ **Enhanced with TypedDict, better docs**
- [x] **T018** [P] Refactor src/pdfreadermcp/tools/pdf_operations.py - type hints, documentation ✅ **Added OperationResult TypedDict, better imports**
- [x] **T019** [P] Refactor src/pdfreadermcp/tools/pdf_ocr.py - optimize OCR processing, type hints ✅ **Added OCRResult TypedDict, enhanced docs**

### Utility & Support Module Refactoring ✅ COMPLETE
- [x] **T020** [P] Refactor src/pdfreadermcp/utils/cache.py - improve caching logic, add type hints ✅ **Added CacheStats TypedDict**
- [x] **T021** [P] Refactor src/pdfreadermcp/utils/chunker.py - optimize text chunking, documentation ✅ **Added ChunkableContent Protocol**
- [x] **T022** [P] Refactor src/pdfreadermcp/utils/file_handler.py - improve file operations, error handling ✅ **Enhanced docs, added Tuple import**

### Additional Tools Refactoring ✅ COMPLETE
- [x] **T023** [P] Refactor src/pdfreadermcp/tools/pdf_image_converter.py - type hints, optimize conversions ✅ **Enhanced documentation, better structure**
- [x] **T024** [P] Refactor src/pdfreadermcp/tools/pdf_metadata.py - improve metadata handling ✅ **Comprehensive docs, metadata field descriptions**

## Phase 3.4: Integration Testing & Validation ✅ COMPLETE

- [x] **T025** [P] Integration test complete PDF processing workflow in tests/integration/test_workflow.py ✅ **10 workflow scenarios, all tool categories**
- [x] **T026** [P] Integration test error handling scenarios in tests/integration/test_error_handling.py ✅ **10 error scenarios, resilience testing**
- [x] **T027** [P] Integration test MCP server startup and tool registration in tests/integration/test_server.py ✅ **13 server tests, all tools verified**

## Phase 3.5: Packaging & Publication Preparation ✅ COMPLETE

- [x] **T028** Update pyproject.toml with proper PyPI metadata, classifiers, and uvx-compatible entry point ✅ **Enhanced with classifiers, keywords, URLs**
- [x] **T029** Optimize dependencies - remove unused packages, update versions, regenerate uv.lock ✅ **Removed langchain-text-splitters, cleaned 12 packages**
- [x] **T030** [P] Update README.md with PyPI installation instructions and uvx usage ✅ **Added uvx as primary installation method**
- [x] **T031** [P] Update documentation strings throughout codebase for better API docs ✅ **Enhanced package metadata and documentation**
- [x] **T032** Test package building with `uv build` and verify wheel contents ✅ **Build successful, 19 files in wheel**
- [x] **T033** Test local package installation and uvx execution ✅ **Server starts correctly, all imports working**

## Phase 3.6: Publication & Final Validation

- [ ] **T034** Publish package to PyPI and verify `uvx pdfreadermcp` installation works
- [ ] **T035** Run complete quickstart validation workflow and performance benchmarking

---

## Dependencies

### Critical Path Dependencies
- **T001-T006** (Setup) must complete before all other phases
- **T007-T014** (Contract Tests) must complete and FAIL before **T015-T024** (Refactoring)  
- **T015** (server.py) blocks **T016** (__main__.py) - same core files
- **T028** (pyproject.toml) blocks **T029** (dependency optimization) blocks **T032** (build testing)
- **T032** (build testing) blocks **T033** (local installation) blocks **T034** (PyPI publication)
- **T034** (publication) must complete before **T035** (final validation)

### Parallel Execution Groups
```bash
# Group 1: Initial Setup (can run together)
Task T002: "Add pytest testing framework to pyproject.toml dev dependencies"
Task T003: "Create comprehensive .gitignore file"  
Task T004: "Create tests/ directory structure"

# Group 2: Contract Tests (MUST run together for efficiency)
Task T007: "Contract test read_pdf in tests/contract/test_read_pdf.py"
Task T008: "Contract test extract_page_text in tests/contract/test_extract_page_text.py"
Task T009: "Contract test search_pdf_text in tests/contract/test_search_pdf_text.py"
Task T010: "Contract test find_and_highlight_text in tests/contract/test_find_highlight.py"
Task T011: "Contract test get_pdf_metadata in tests/contract/test_get_metadata.py"
Task T012: "Contract test split_pdf in tests/contract/test_split_pdf.py"
Task T013: "Contract test extract_pages in tests/contract/test_extract_pages.py"  
Task T014: "Contract test merge_pdfs in tests/contract/test_merge_pdfs.py"

# Group 3: Tool Refactoring (different files, can parallelize)
Task T017: "Refactor src/pdfreadermcp/tools/pdf_reader.py"
Task T018: "Refactor src/pdfreadermcp/tools/pdf_operations.py"
Task T019: "Refactor src/pdfreadermcp/tools/pdf_ocr.py"
Task T020: "Refactor src/pdfreadermcp/utils/cache.py"
Task T021: "Refactor src/pdfreadermcp/utils/chunker.py"
Task T022: "Refactor src/pdfreadermcp/utils/file_handler.py"
Task T023: "Refactor src/pdfreadermcp/tools/pdf_image_converter.py"
Task T024: "Refactor src/pdfreadermcp/tools/pdf_metadata.py"

# Group 4: Documentation & Testing (different files)
Task T025: "Integration test workflow in tests/integration/test_workflow.py"
Task T026: "Integration test error handling in tests/integration/test_error_handling.py"
Task T027: "Integration test server startup in tests/integration/test_server.py"
Task T030: "Update README.md with PyPI installation instructions"
Task T031: "Update documentation strings throughout codebase"
```

## File Path Reference

### Core Files (Sequential - No Parallel)
- `src/pdfreadermcp/server.py` (T015)
- `src/pdfreadermcp/__main__.py` (T016)  
- `pyproject.toml` (T002, T028, T029)

### Tool Files (Parallel Possible)
- `src/pdfreadermcp/tools/pdf_reader.py` (T017)
- `src/pdfreadermcp/tools/pdf_operations.py` (T018)
- `src/pdfreadermcp/tools/pdf_ocr.py` (T019)
- `src/pdfreadermcp/tools/pdf_image_converter.py` (T023)
- `src/pdfreadermcp/tools/pdf_metadata.py` (T024)
- `src/pdfreadermcp/tools/pdf_optimizer.py` (refactoring as part of T023/T024)
- `src/pdfreadermcp/tools/pdf_text_search.py` (refactoring as part of T017)

### Utility Files (Parallel Possible)
- `src/pdfreadermcp/utils/cache.py` (T020)
- `src/pdfreadermcp/utils/chunker.py` (T021)  
- `src/pdfreadermcp/utils/file_handler.py` (T022)

### Test Files (All Parallel)
- `tests/contract/test_*.py` (T007-T014)
- `tests/integration/test_*.py` (T025-T027)
- `tests/unit/` (created during contract testing)

### Documentation Files (Parallel Possible)
- `README.md` (T030)
- Documentation strings in source files (T031)

## Contract Preservation Requirements

**CRITICAL**: All 18 PDF tools must maintain exact interface compatibility:

### Text Processing Tools (5)
1. `read_pdf(file_path, pages=None, chunk_size=1000, chunk_overlap=100) -> str`
2. `extract_page_text(file_path, page_number, extraction_mode="default") -> str`
3. `search_pdf_text(file_path, query, pages=None, case_sensitive=False, regex_search=False, context_chars=100, max_matches=100) -> str`
4. `find_and_highlight_text(file_path, query, pages=None, case_sensitive=False) -> str`
5. `get_pdf_metadata(file_path, include_xmp=False) -> str`

### Document Operations Tools (5)
6. `split_pdf(file_path, split_ranges, output_dir=None, prefix=None) -> str`
7. `extract_pages(file_path, pages, output_file=None, output_dir=None) -> str`
8. `merge_pdfs(file_paths, output_file=None, output_dir=None) -> str`
9. `set_pdf_metadata(file_path, output_file=None, **metadata_fields) -> str`
10. `remove_pdf_metadata(file_path, output_file=None, fields_to_remove=None, remove_all=False) -> str`

### OCR & Conversion Tools (6)
11. `ocr_pdf(file_path, pages=None, language='chi_sim', chunk_size=1000, chunk_overlap=100, dpi=200) -> str`
12. `pdf_to_images(file_path, pages=None, dpi=200, image_format='PNG', output_dir=None, save_to_disk=True) -> str`
13. `images_to_pdf(image_paths, output_file, page_size="A4", quality=95, title=None, author=None) -> str`
14. `extract_pdf_images(file_path, pages=None, min_size="100x100", output_dir=None) -> str`

### Optimization Tools (4)
15. `optimize_pdf(file_path, output_file=None, optimization_level='medium') -> str`
16. `compress_pdf_images(file_path, output_file=None, quality=80) -> str`
17. `remove_pdf_content(file_path, output_file=None, remove_images=False, remove_annotations=False, compress_streams=True) -> str`
18. `analyze_pdf_size(file_path) -> str`

## Success Criteria Validation

Each task must verify:
- [ ] No breaking changes to any of the 18 tool interfaces
- [ ] All contract tests pass after refactoring
- [ ] Code quality improvements visible (type hints, documentation)
- [ ] Package builds successfully with `uv build`
- [ ] Local installation works: `pip install dist/*.whl`
- [ ] uvx execution works: `uvx pdfreadermcp`
- [ ] PyPI publication successful  
- [ ] All quickstart scenarios pass

## Notes
- [P] tasks = different files, no dependencies, can run in parallel
- Contract tests MUST fail initially to ensure TDD approach
- Preserve all existing functionality - this is a refactoring, not a rewrite
- Focus on code quality, not feature changes
- Test thoroughly before each commit
- PyPI publication is the final deliverable

**用户输入背景**: 请你开始分解任务！！！

Tasks are now ready for execution. Each task is specific, has clear file paths, and follows TDD principles with proper dependency ordering.

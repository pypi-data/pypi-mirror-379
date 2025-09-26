# PDF Reader MCP Server (PDF阅读器MCP服务器)

一个基于MCP（模型上下文协议）的服务器，提供全面的PDF处理能力，包含18个强大的工具用于文本提取、OCR识别、图像转换、元数据管理和文件优化。

## 🚀 最新更新
- **✅ 全部18个工具经过全面测试，完全可用** (2025年9月)
- **🔧 修复JSON序列化问题** - 实现100%兼容性
- **⚡ 性能增强** 智能缓存系统
- **🌍 多语言OCR支持** 优化中英文识别效果

## 功能特性

### 📖 智能文本提取
- **智能PDF解析** 使用`pypdf`进行高质量文本提取
- **自动质量检测** 识别何时需要OCR处理
- **页面级处理** 支持灵活的页面范围语法

### 🔍 高级OCR支持
- **Tesseract集成** 支持扫描文档和图像型PDF
- **多语言支持** 专注中文和英文处理
- **置信度评分** OCR质量评估
- **Windows友好** 安装和配置简单

### ⚡ 性能优化
- **智能缓存系统** 避免重复处理未变更文件
- **分块策略** 处理大型文档
- **并行页面处理** 提升性能

### 🎯 灵活页面选择
支持复杂的页面范围语法：
- `"1,3,5"` - 指定页面
- `"1-10"` - 页面范围  
- `"-1"` - 最后一页
- `"1,3,5-10,-1"` - 组合语法

## 安装

### 系统要求
- Python 3.11+
- uv 包管理器
- Tesseract OCR引擎 (用于OCR功能)

### 安装 uv (如果尚未安装)

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 安装 Tesseract OCR引擎

**Windows:**
1. 下载地址: https://github.com/UB-Mannheim/tesseract/wiki
2. 安装最新版本 (推荐: tesseract-ocr-w64-setup-v5.3.3.20231005.exe)
3. 安装时选择"Additional Language Data"并安装中文语言包
4. 将Tesseract添加到PATH，或记录安装路径用于配置

**macOS:**
```bash
# 使用 Homebrew
brew install tesseract tesseract-lang
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-chi-sim tesseract-ocr-chi-tra
```

### 安装 MCP 服务器

1. 克隆或下载此项目
2. 导航到项目目录
3. 安装依赖：
```bash
uv sync
```

## 使用方法

### 运行服务器

```bash
uv run pdfreadermcp
```

### 与 Claude Desktop 集成

在Claude Desktop MCP配置文件中添加：

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "pdfreadermcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/pdfreadermcp",
        "run",
        "pdfreadermcp"
      ]
    }
  }
}
```

## 📚 完整工具套件 (18个工具)

所有工具都经过全面测试，完全可用。服务器提供跨多个类别的综合PDF处理能力：

### 📖 文本处理工具 (5个工具)
- `read_pdf` - 智能文本提取与分块
- `extract_page_text` - 多模式单页文本提取
- `search_pdf_text` - 高级文本搜索，支持正则和上下文
- `find_and_highlight_text` - 文本搜索与高亮坐标定位
- `get_pdf_metadata` - 全面元数据读取，支持XMP

### 📄 文档操作工具 (5个工具)
- `split_pdf` - 按页面范围分割PDF为多个文件
- `extract_pages` - 提取指定页面到新PDF文件
- `merge_pdfs` - 合并多个PDF为单个文档
- `set_pdf_metadata` - 写入/更新PDF元数据字段
- `remove_pdf_metadata` - 删除特定或全部元数据字段

### 🖼️ 图像转换工具 (3个工具)  
- `pdf_to_images` - 将PDF页面转换为高质量图像
- `images_to_pdf` - 将多个图像转换为单个PDF
- `extract_pdf_images` - 从PDF页面提取嵌入图像

### 🔍 OCR工具 (1个工具)
- `ocr_pdf` - 高级OCR，支持多语言和置信度评分

### ⚡ 优化工具 (4个工具)
- `optimize_pdf` - 多级别综合PDF优化
- `compress_pdf_images` - PDF文档内图像压缩
- `remove_pdf_content` - 删除特定内容以减小文件大小
- `analyze_pdf_size` - 文件大小分析和优化建议

## 工具详细说明

### `read_pdf` - 文本提取工具

从PDF文件中提取文本，具有智能处理功能。

**参数:**
- `file_path` (必需): PDF文件路径
- `pages` (可选): 页面范围字符串 (例如: "1,3,5-10,-1")
- `chunk_size` (可选): 最大块大小 (默认: 1000)
- `chunk_overlap` (可选): 块重叠 (默认: 100)

**示例:**
```
从 document.pdf 提取文本，处理第1-5页和最后一页
```

### `ocr_pdf` - OCR识别工具

使用Tesseract对PDF页面进行OCR识别，适用于扫描文档和图像型PDF。

**参数:**
- `file_path` (必需): PDF文件路径
- `pages` (可选): 页面范围字符串 (例如: "1,3,5-10,-1")
- `language` (可选): OCR语言代码 (默认: "chi_sim" 简体中文)
- `chunk_size` (可选): 最大块大小 (默认: 1000)
- `chunk_overlap` (可选): 块重叠 (默认: 100)
- `dpi` (可选): PDF转图像的DPI (默认: 200)

**支持的语言:**
- `chi_sim`: 简体中文 (默认)
- `chi_tra`: 繁体中文
- `eng`: 英文
- `chi_sim+eng`: 中英文混合

**示例:**
```
对 scanned_doc.pdf 进行中文OCR识别
```

### `search_pdf_text` - PDF文本搜索引擎

在PDF页面中搜索文本内容，提供详细匹配信息。

**参数:**
- `file_path` (必需): PDF文件路径
- `query` (必需): 要搜索的文本 (或正则表达式模式)
- `pages` (可选): 页面范围 (例如: "1,3,5-10,-1")
- `case_sensitive` (可选): 区分大小写搜索 (默认: False)
- `regex_search` (可选): 将查询视为正则表达式 (默认: False)
- `context_chars` (可选): 匹配周围的上下文字符数 (默认: 100)
- `max_matches` (可选): 返回的最大匹配数 (默认: 100)

## 输出格式

所有工具返回包含相关数据的结构化JSON。文本提取和OCR工具返回：

```json
{
  "success": true,
  "file_path": "/path/to/file.pdf",
  "total_pages": 10,
  "processed_pages": [1, 2, 3],
  "chunks": [
    {
      "content": "提取的文本...",
      "page_number": 1,
      "chunk_index": 0,
      "metadata": {
        "quality_score": 0.95,
        "word_count": 150
      }
    }
  ],
  "summary": {
    "total_chunks": 5,
    "total_chars": 2500,
    "pages": [1, 2, 3]
  },
  "extraction_method": "text_extraction"
}
```

## 语言支持

### OCR语言
`ocr_pdf` 工具通过Tesseract支持多种语言：

- **中文:** `chi_sim` (简体), `chi_tra` (繁体)
- **英文:** `eng`
- **组合:** `chi_sim+eng` (中英文混合)
- **其他:** 基于您的Tesseract安装可用

## 性能特性

### 缓存系统
- **基于文件的失效机制** - 文件更改时缓存自动失效
- **操作特定缓存** - 不同操作使用不同缓存条目
- **内存管理** - 可配置的缓存大小和TTL

### 文本质量分析
系统自动分析提取文本质量，使用：
- 字符与单词比率
- 句子结构分析
- 字母与字符比率
- 特殊字符检测

低质量文本会触发OCR建议。

### 分块策略
- **递归字符分割** 使用语义分隔符
- **可配置重叠** 保持上下文
- **元数据保留** 包括页码和位置信息

## 错误处理

服务器提供详细的错误信息：
- 文件缺失错误
- 无效页面范围错误
- OCR引擎初始化错误
- 处理超时错误

## Windows兼容性

### 特别说明
- **完全支持Windows 10/11**
- **自动路径处理** - 支持Windows路径格式
- **中文路径支持** - 正确处理包含中文字符的路径
- **Tesseract集成** - 简化的Windows安装和配置

### Windows特定安装注意事项
1. **管理员权限:** 安装Tesseract时可能需要管理员权限
2. **PATH配置:** 确保Tesseract添加到系统PATH中
3. **中文支持:** 安装时选择中文语言包以获得最佳OCR效果

## 故障排除

### 常见问题

**1. Tesseract OCR安装问题**

如果Tesseract未找到，可能看到"TesseractNotFoundError"错误。解决方案：

**Windows:**
- 确保Tesseract已安装并添加到PATH
- 或手动设置路径：
```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

**2. 中文语言包问题**

如果中文文本OCR失败或效果差：
- **Windows:** Tesseract安装时选择"Additional Language Data"并安装中文包
- **macOS:** `brew install tesseract-lang` 
- **Linux:** `sudo apt install tesseract-ocr-chi-sim tesseract-ocr-chi-tra`

验证语言包已安装：
```bash
tesseract --list-langs
```

**3. 大型PDF内存问题**
- 减少 `chunk_size` 参数
- 分小范围处理页面
- 确保系统有足够内存
- 降低 `dpi` 参数以加快处理速度

### 性能提示

1. **使用缓存** - 相同文件和参数会使用缓存结果
2. **处理特定页面** - 使用页面范围而非处理整个文档
3. **调整块大小** - 内存受限环境使用较小块
4. **选择合适工具** - 先用 `read_pdf`，需要时再用 `ocr_pdf`
5. **OCR优化**:
   - 使用较低 `dpi` (150-200) 以加快处理
   - 纯中文文档仅使用 `chi_sim`
   - 仅对有问题的页面进行OCR，而非整个文档

## 🧪 测试与质量保证

此项目经过全面测试，具有完整的测试覆盖：
- **✅ 18/18工具完全可用** (100%成功率)
- **🔧 所有JSON序列化问题已解决**
- **📋 使用真实PDF文档进行广泛测试**
- **⚡ 缓存系统性能验证**
- **🌍 多语言OCR测试 (中英文)**

## 开发

### 项目结构
```
pdfreadermcp/
   pyproject.toml              # uv项目配置
   README.md / README_zh.md    # 文档（英文/中文）
   src/pdfreadermcp/
       __init__.py
       __main__.py             # 入口点
       server.py               # MCP服务器实现
       tools/
          pdf_reader.py       # 文本提取工具
          pdf_ocr.py          # OCR处理工具
          pdf_operations.py   # PDF分割、合并、提取
          pdf_image_converter.py  # PDF-图像转换工具
          pdf_metadata.py         # PDF元数据管理
          pdf_text_search.py      # PDF文本搜索和高亮
          pdf_optimizer.py        # PDF压缩和优化
       utils/
           chunker.py          # 文本分块工具
           cache.py            # 缓存系统
           file_handler.py     # 文件操作
```

## 依赖项

### 核心依赖
- **mcp** - 模型上下文协议服务器框架
- **pypdf** - PDF文本提取和操作
- **pdf2image** - PDF转图像转换
- **pytesseract** - Tesseract OCR的Python包装器
- **tesseract** - OCR引擎
- **pillow** - 图像处理和操作

### 系统要求
- OCR功能需要安装Tesseract OCR引擎
- PDF转换在某些系统上可能需要poppler-utils

## 许可证

此项目使用MIT许可证。

## 贡献

欢迎贡献！请随时提交问题和功能请求。

## 支持

如有问题和支持需求：
- 在项目仓库中创建issue
- 查看上述故障排除部分
- 参考MCP文档 https://modelcontextprotocol.io

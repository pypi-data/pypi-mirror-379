# mkdocs-excel-plugin

[![Tests](https://github.com/Wangjunyu/mkdocs-excel-plugin/workflows/Tests/badge.svg)](https://github.com/Wangjunyu/mkdocs-excel-plugin/actions)
[![PyPI version](https://badge.fury.io/py/mkdocs-excel-plugin.svg)](https://badge.fury.io/py/mkdocs-excel-plugin)
[![Python versions](https://img.shields.io/pypi/pyversions/mkdocs-excel-plugin.svg)](https://pypi.org/project/mkdocs-excel-plugin/)
[![License](https://img.shields.io/pypi/l/mkdocs-excel-plugin.svg)](https://github.com/Wangjunyu/mkdocs-excel-plugin/blob/main/LICENSE)

A MkDocs plugin that renders Excel files as beautiful HTML tables with complete style preservation.

## ✨ Features

- 🎨 **Complete Style Preservation**: Maintains Excel's background colors, fonts, borders, and alignment
- 📊 **Merged Cell Support**: Perfect handling of colspan and rowspan
- 🔄 **Multi-sheet Processing**: Render single sheets or all sheets at once
- ⚡ **Smart Caching**: Built-in caching for improved performance
- 🎯 **Size Control**: Configurable row/column limits for large files
- 🌓 **Theme Compatibility**: Works seamlessly with Material and other MkDocs themes
- 🛡️ **Error Handling**: Friendly error messages for missing files or sheets

## 🚀 Installation

```bash
pip install mkdocs-excel-plugin
```

## 📖 Quick Start

1. Add the plugin to your `mkdocs.yml`:

```yaml
plugins:
  - excel
```

2. Use Excel macros in your markdown:

```markdown
<!-- Render a single sheet -->
{{ render_excel_sheet('data.xlsx', 'Sheet1') }}

<!-- Render all sheets -->
{{ render_excel_all_sheets('data.xlsx') }}

<!-- List available sheets -->
{{ list_excel_sheets('data.xlsx') }}
```

## ⚙️ Configuration

```yaml
plugins:
  - excel:
      cache_enabled: true        # Enable smart caching
      max_file_size_mb: 5       # Maximum file size
      default_max_rows: 1000    # Default row limit
      default_max_cols: 50      # Default column limit
      theme: "material"         # Theme compatibility
```

## 📝 Usage Examples

### Basic Usage
```markdown
{{ render_excel_sheet('sales.xlsx', 'Q1 Data') }}
```

### Advanced Usage
```markdown
<!-- Limit table size -->
{{ render_excel_sheet('large.xlsx', 'Data', max_rows=100, max_cols=20) }}

<!-- Selective rendering -->
{{ render_excel_all_sheets('report.xlsx', include_sheets=['Summary', 'Details']) }}

<!-- Exclude specific sheets -->
{{ render_excel_all_sheets('report.xlsx', exclude_sheets=['Raw Data']) }}
```

## 🎯 Supported Features

- ✅ Background colors and gradients
- ✅ Font colors, bold, italic, sizes
- ✅ Text alignment (horizontal/vertical)
- ✅ Border styles and colors
- ✅ Merged cells with proper span
- ✅ Excel theme colors
- ✅ Multiple worksheets
- ✅ Relative file paths
- ✅ Performance warnings
- ✅ Comprehensive error handling

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and contribute to the project.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

If you encounter any issues or have questions, please file an issue on [GitHub](https://github.com/Wangjunyu/mkdocs-excel-plugin/issues).
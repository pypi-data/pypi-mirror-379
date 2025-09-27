# Basic Example

This example shows the most basic usage of the mkdocs-excel-plugin.

## Setup

1. Install the plugin:
```bash
pip install mkdocs-excel-plugin
```

2. Add to your `mkdocs.yml`:
```yaml
plugins:
  - excel
```

## Usage

Place your Excel files in your docs directory and reference them in markdown:

```markdown
# My Data Report

## Sales Data
{{ render_excel_sheet('sales-2024.xlsx', 'Q1 Results') }}

## All Sheets
{{ render_excel_all_sheets('monthly-report.xlsx') }}

## Available Sheets
{{ list_excel_sheets('data.xlsx') }}
```

## File Structure
```
docs/
├── index.md
├── sales-2024.xlsx
├── monthly-report.xlsx
└── data.xlsx
```

That's it! The plugin will automatically render your Excel files as beautiful HTML tables.
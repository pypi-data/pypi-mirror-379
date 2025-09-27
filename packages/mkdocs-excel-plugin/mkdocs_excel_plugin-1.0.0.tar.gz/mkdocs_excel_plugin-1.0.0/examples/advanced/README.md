# Advanced Example

This example demonstrates advanced configuration and usage patterns.

## Configuration

```yaml
# mkdocs.yml
plugins:
  - excel:
      cache_enabled: true
      max_file_size_mb: 10
      default_max_rows: 500
      default_max_cols: 25
      theme: "material"

extra_css:
  - assets/custom-excel.css  # Optional custom styling
```

## Advanced Usage

### Size Control
```markdown
<!-- Limit large tables -->
{{ render_excel_sheet('big-data.xlsx', 'Sheet1', max_rows=100, max_cols=15) }}
```

### Selective Rendering
```markdown
<!-- Only render specific sheets -->
{{ render_excel_all_sheets('report.xlsx', include_sheets=['Summary', 'Charts']) }}

<!-- Exclude certain sheets -->
{{ render_excel_all_sheets('data.xlsx', exclude_sheets=['Raw Data', 'Temp']) }}
```

### Complex Layouts
```markdown
# Financial Report

## Executive Summary
{{ render_excel_sheet('financial-2024.xlsx', 'Executive Summary') }}

## Detailed Analysis
{{ render_excel_all_sheets('financial-2024.xlsx', exclude_sheets=['Executive Summary', 'Notes']) }}

## Data Sources
{{ list_excel_sheets('financial-2024.xlsx') }}
```

### Custom Styling

Create `assets/custom-excel.css`:
```css
.excel-table {
    font-family: 'Roboto Mono', monospace;
    border-radius: 8px;
    overflow: hidden;
}

.excel-info {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}
```

## Performance Tips

1. **Use size limits**: Always set reasonable `max_rows` and `max_cols` for large files
2. **Enable caching**: Keep `cache_enabled: true` for better performance
3. **Optimize file sizes**: Keep Excel files under 5MB when possible
4. **Selective rendering**: Use `include_sheets` or `exclude_sheets` for multi-sheet files
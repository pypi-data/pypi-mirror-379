# PyPI 发布脚本
# 在你完成注册后运行

# 安装发布工具
pip install build twine

# 构建包
python -m build

# 检查包
twine check dist/*

# 先发布到测试 PyPI（推荐）
twine upload --repository testpypi dist/*

# 测试安装
pip install --index-url https://test.pypi.org/simple/ mkdocs-excel-plugin

# 如果测试成功，发布到正式 PyPI
twine upload dist/*
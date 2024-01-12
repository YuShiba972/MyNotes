# -*- encoding: utf-8 -*-

"""

@File    :   conf.py
@Author  :   Yushiba972
@description  :   source url - https://www.sphinx-doc.org/en/master/usage/configuration.html 

"""  

from recommonmark.parser import CommonMarkParser


# -- 1. 项目信息 -----------------------------------------------------

project = 'Notes'
copyright = '2024, Arthur'
author = 'Arthur'
release = 'dev'



# -- 2. 拓展的python module模块 -----------------------------------------------------

extensions = [    
     'recommonmark',  # markdown语法支持插件配合sphinx_markdown_tables使用
    #  'sphinx_markdown_tables' # markdown语法支持插件
 ]



# -- 3. 模板路径，相对conf.py的位置 -----------------------------------------------------
templates_path = ['_templates']
exclude_patterns = []



# -- 4. HTML输出渲染 -------------------------------------------------
html_theme = 'sphinx_rtd_theme'     # 主题
html_static_path = ['_static']  # 静态资源相对位置



# -- 5. 其他配置 -------------------------------------------------
# 指定后缀文件使用的解析器
source_parsers = {
    '.md': CommonMarkParser,
    '.MD': CommonMarkParser,
}

# 指定后缀文件识别格式
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

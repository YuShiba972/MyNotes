# -*- encoding: utf-8 -*-

"""

@File    :   conf.py
@Author  :   Yushiba972
@description  :   source url - https://www.sphinx-doc.org/en/master/usage/configuration.html 

""" 


############################################################################
# --- 1. 项目信息 ----------------------------------------------------------

project = 'Notes'
copyright = '2024, Arthur'
author = 'Arthur'
release = 'dev'

############################################################################





############################################################################
# -- 2. 拓展的python module模块 --------------------------------------------

from recommonmark.parser import CommonMarkParser

extensions = [    
     'recommonmark',  # markdown语法支持插件配合sphinx_markdown_tables使用
     'sphinx_markdown_tables', # markdown语法支持插件
     'sphinx_tabs.tabs'  ,# tabs插件
     'sphinx_copybutton',    #代码复制插件,排序在tabs前
        #  https://sphinx-copybutton.readthedocs.io/en/latest/index.html
 ]

############################################################################





############################################################################
# -- 3. 模板路径，相对conf.py的位置 -----------------------------------------

templates_path = ['_templates']
exclude_patterns = []

############################################################################





############################################################################
# -- 4. HTML输出渲染 -------------------------------------------------------

html_theme = 'sphinx_rtd_theme'     # 主题
html_static_path = ['_static']  # 静态资源相对位置
html_css_files = ['custom.css'] # 指定样式表文件

############################################################################





############################################################################
# -- 5. 其他配置 -----------------------------------------------------------

# 语言配置
language = 'zh_CN'

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

############################################################################
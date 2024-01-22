============================================
sphinx-rst 指令
============================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
01 文档树指令
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **基础**
.. code-block:: rst
  :linenos:

  .. toctree::
   :maxdepth: 2
   :caption: 目录

   index1.rst
   index2.rst

- **可选项**
.. code-block:: rst
  :linenos:

  .. toctree::
   :maxdepth: 
   :caption: 
   :hidden:
   :glob:  
   :reversed:
   :includehidden:
   :titlesonly:
   :numbered:
   :name:

   index1.rst
   index2.rst

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
02 提示块指令
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

  .. admonition:: 这是自定义标题

    这是admonition内容

  .. note:: 这是note内容

  .. attention:: 这是attention内容

  .. caution:: 这是caution内容

  .. warning:: 这是warning内容

  .. tip:: 这是tip内容

  .. important:: 这是important内容

  .. hint:: 这是hint内容

  .. error:: 这是error内容

  .. danger:: 这是danger内容

.. admonition:: 这是自定义标题

   这是admonition内容

.. note:: 这是note内容

.. attention:: 这是attention内容

.. caution:: 这是caution内容

.. warning:: 这是warning内容

.. tip:: 这是tip内容

.. important:: 这是important内容

.. hint:: 这是hint内容

.. error:: 这是error内容

.. danger:: 这是danger内容

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
03 版本管理块指令
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

  .. versionadded:: 版本1.0 
    *新增内容*

  .. versionchanged:: 版本2.0
    *改变内容*

  .. deprecated:: 版本3.0
    *弃用内容*

.. versionadded:: 版本1.0 
  *新增内容*

.. versionchanged:: 版本2.0
  *改变内容*

.. deprecated:: 版本3.0
  *弃用内容*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
04 文字处理指令
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

  .. centered:: 居中文本

  .. rubric:: 不记录目录树的标题

  .. hlist::
    :columns: 3

    * 多列项目元素1
    * 多列项目元素2
    * 多列项目元素3
    * 多列项目元素4
    * 多列项目元素5

.. centered:: 居中文本

.. rubric:: 不记录目录树的标题

.. hlist::
   :columns: 3

   * 多列项目元素1
   * 多列项目元素2
   * 多列项目元素3
   * 多列项目元素4
   * 多列项目元素5

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
05 代码块指令
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: **全局代码配置：highlight**
.. code-block:: rst

  设置文档中大于5行的python代码显示行数:

  .. highlight:: python
    :linenothreshold: 5

.. code-block:: rst

  设置文档所有python代码显示行数(force优先级大):

  .. highlight:: python
    :force:

.. note:: **代码块：使用code-block或sourcecode**

.. code-block:: rst

  shell代码块：

  .. code-block:: shell

    echo 'hello world!'
    
  python代码块：
  .. sourcecode:: python

    def main():
      print('hello world')

shell代码块：

.. code-block:: shell

  echo 'hello world!'
  
python代码块：

.. sourcecode:: python

  def main():
    print('hello world')

.. note:: **代码块可选项：linenos行数显示 | emphasize-lines强调行 | caption导航文本 | name预定义引用名**

.. code-block:: rst

  .. code-block:: 
    :linenos:
    :emphasize-lines: 3,5
    :caption: this.py
    :name: this-py

    def some_function():
      interesting = False
      print('This line is highlighted.')
      print('This one is not...')
      print('...but this one is.')

.. code-block:: 
  :linenos:
  :lineno-start: 2
  :emphasize-lines: 3,5
  :caption: this.py
  :name: this-py

  def some_function():
    interesting = False
    print('This line is highlighted.')
    print('This one is not...')
    print('...but this one is.')

.. note:: **外部代码文件引用：literalinclude，可选项：encoding编码 | lines引用指定行 | ...**

.. code-block:: rst

  .. literalinclude:: index.rst
    :linenos:
    :language: rst
    :emphasize-lines: 1-7,10
    :encoding: utf-8
    :lines: 1-11

.. literalinclude:: index.rst
  :linenos:
  :language: rst
  :emphasize-lines: 1-7,10
  :encoding: utf-8
  :lines: 1-11



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
06 专业术语指令
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: **glossary指令定义术语，:term:`术语名`引用**

.. code-block:: rst


  .. glossary::

      term1
          This is the definition of term1.

      term2
          Definition of term2 goes here.
          
  :term:`term1` an important concept in our system.


.. glossary::

    term1
        This is the definition of term1.

    term2
        Definition of term2 goes here.
        
:term:`term1` an important concept in our system.



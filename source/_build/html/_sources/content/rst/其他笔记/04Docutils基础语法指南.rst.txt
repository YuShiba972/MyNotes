基础语法
==============================

.. warning:: 
  - **文档提供 docutils 下的解析 reStructuredText 的常用语法指南**
  - `参考链接(https://docutils-zh-cn.readthedocs.io/zh-cn/latest/user/rst/quickstart.html) <https://docutils-zh-cn.readthedocs.io/zh-cn/latest/user/rst/quickstart.html>`_

01 标题
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   - 标题文本 ``顶格写``
   - 标题文本下一行顶格写指定级别的标题符号
   - 标题符号长度 ``不小于`` 标题文本长度

- **源代码**
  
.. code-block:: RST

    一级标题文本
    =====================

    二级标题文本
    ~~~~~~~~~~~~~~~~~~~~~

    三级标题文本
    ------------------

    四级标题文本
    ^^^^^^^^^^^^^^^^^^^^^

    五级标题文本
    """""""""""""""""

    六级标题文本
    *****************

*********************************************

02 段落
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: 
    - 缩进表示层级，同一行的文字缩进相等，精确分行使用 ``空行`` 或者 ``|`` 符号
    - 两个空格表示缩进，四个空格表示代码块.

- **源代码**

.. code-block:: rst

    | 这是第一行
    | 这是第二行
    | 这是第三行

- | **实现效果**
  
  | 这是第一行
  | 这是第二行
  | 这是第三行

03 行内字符处理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

  - 字符处理符号前后需要预留空格，否则不生效.

- **源代码**
  
.. code-block:: RST

    *斜体文本*

    **强调文本**

    ``高亮文本``  

- **实现效果**
  
  *斜体文本*

  **强调文本**

  ``高亮文本``  

*********************************************

04 项目列表
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   - 无序列表符号后需要 ``接一个空格`` 。
   - 有序列表符号后需要接一个空格， ``支持数字、大小写字母和罗马数字`` 。

- **源代码**

.. code-block:: RST

    无序列表，序号可以是"* + -"

    - test text
    - test text
    - test text

    有序列表，支持数字、大小写字母和罗马数字

    1. test text
    #. test text
    #. test text

    a. test text
    #. test text
    #. test text

    A. test text
    #. test text
    #. test text

- **实现效果**

无序列表，序号可以是"* + -"

- test text
- test text
- test text

有序列表，支持数字、大小写字母和罗马数字

1. test text
#. test text
#. test text

a. test text
#. test text
#. test text

A. test text
#. test text
#. test text


05 参考链接
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **内部链接源代码**
  
.. code-block:: RST
    
    `链接显示文本 <链接地址>`_

    `python官网 <https://www.python.org/>`_   

- **实现效果**

  `python官网 <https://www.python.org/>`_ 

- **外部引用链接源代码**

.. code-block:: RST

    通用格式

        文档预定义：
        .. _链接显示文本: 链接地址

        文档中引用
        `链接显示文本`_

    源代码示例：

        .. _python官网: https://www.python.org/

        以下链接可点击：`python官网`_


- **实现效果**
  
  .. _python官网: https://www.python.org/

  以下链接可点击：`python官网`_

06 图片
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **源代码**
  
.. code-block:: RST

  .. image:: ../_static/restructuredtext/moon.webp

  .. image:: ../_static/restructuredtext/moon.webp
    :height: 100
    :width: 200
    :scale: 50 
    :alt: 资源不存在显示文本

- **实现效果**

.. image:: ../_static/restructuredtext/moon.webp

.. image:: ../_static/restructuredtext/moon.webp
  :height: 100
  :width: 200
  :scale: 50
  :alt: 资源不存在显示文本


07 变量定义
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: 
    **变量定义列表中的第一行为定义行顶格写，下一行开始为解释行，需要缩进，同一缩进量表示同一行文本，分行使用空行分割.**

- **源代码**
.. code-block:: rst

    这里是定义变量1的标识
        这里是定义变量1的文本解释内容。(单行)

    这里是定义变量2的标识
        这里是定义变量2的文本解释内容。(多行不换行)
        这里是定义变量2的文本解释内容。

    这里是定义变量3的标识
        这里是定义变量3的文本解释内容。(多行换行)
        
        这里是定义变量3的文本解释内容。(多行换行)

- **实现效果**

这里是定义变量1的标识
    这里是定义变量1的文本解释内容。(单行)

这里是定义变量2的标识
    这里是定义变量2的文本解释内容。(多行不换行)
    这里是定义变量2的文本解释内容。

这里是定义变量3的标识
    这里是定义变量3的文本解释内容。(多行换行)
    
    这里是定义变量3的文本解释内容。(多行换行)

    这里是定义变量3的文本解释内容。

08 选项定义
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **源代码**
  
.. code-block:: rst

  -a            命令行选项"a"
  -b file       选项可以有参数和描述
  --long        选项也可以长
  --input=file  长选项也可以有参数
  /v            DOS/VMS风格的选项也行

- **实现效果**

  -a            命令行选项"a"
  -b file       选项可以有参数和描述
  --long        选项也可以长
  --input=file  长选项也可以有参数
  /v            DOS/VMS风格的选项也行

09 文本块
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **源代码**

.. code-block:: rst

  这是一个文本块::

    while True:
      if literal_block:
        text = 'is left as-is'
        spaces_and_linebreaks = 'are preserved'
        markup_processing = None
      else:
        break
    print('exec')
  
- **实现效果**

这是一个文本块::

  while True:
    if literal_block:
      text = 'is left as-is'
      spaces_and_linebreaks = 'are preserved'
      markup_processing = None
    else:
      break
  print('exec')

10 块
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: restructuredtext

    文本块::

        if literal_block:
          text = 'is left as-is'

11 指令
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. attention::
   Beware killer rabbits!
.. tip::
   Beware killer rabbits!
.. important::
   Beware killer rabbits!
attention橙, caution橙色, danger红粉, error红粉, 
hint绿, important绿, note蓝, tip绿, warning橙, admonition自定义蓝

.. admonition:: And, by the way...

   You can make up your own admonition too.

.. admonition:: 京
  
   You can make up your own admonition too.



.. topic:: Topic Title

  之后的所缩进行包含话题的正文
  并不解释为正文元素

.. sidebar:: Sidebar Title
   :subtitle: Optional Sidebar Subtitle

   Subsequent indented lines comprise
   the body of the sidebar, and are
   interpreted as body elements.
  

.. code:: python

  def my_function():
      "just a test"
      print 8/2

.. epigraph::

   No matter where you go, there you are.

   -- Buckaroo Banzai

.. compound::

   The 'rm' command is very dangerous.  If you are logged
   in as root and enter ::

       cd /
       rm -rf *

   you will erase the entire contents of your file system.

.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

.. table:: Truth table for "not"

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====

.. list-table:: Frozen Del
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

.. |reST| replace:: reStructuredText

Yes, |reST| is a long word, so I can't blame anyone for wanting to
abbreviate it.

.. include:: inclusion.txt

    这是第二个例子，它会在一个引用块上下文中解析。
    因此它只能包含正文元素，而不能包含章节标题。 

    .. include:: inclusion.txt

.. deprecated:: 3.1
   Use :func:`spam` instead.
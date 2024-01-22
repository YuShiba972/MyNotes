**版本管理**

.. sectionauthor:: 
    Guido van Rossum <guido@python.org>

.. index::
   single: execution; context
   pair: module; __main__
   pair: module; sys
   triple: module; search; path
   seealso: scope

The execution context
---------------------

.. productionlist::
   try_stmt: try1_stmt | try2_stmt
   try1_stmt: "try" ":" `suite`
            : ("except" [`expression` ["," `target`]] ":" `suite`)+
            : ["else" ":" `suite`]
            : ["finally" ":" `suite`]
   try2_stmt: "try" ":" `suite`
            : "finally" ":" `suite`

            
...

.. code-block:: 

    .. spam:: 3.1 
    
    Use :func:`spam` instead.

.. spam:: 
    
    3.1 

.. seealso:: modules :py:mod:`zipfile`, :py:mod:`tarfile`
.. seealso::

   Module :py:mod:`zipfile`
      Documentation of the :py:mod:`zipfile` standard module.

   `GNU tar manual, Basic Tar Format <https://link>`_
      Documentation for tar archive files, including GNU tar extensions.

.. centered:: 居中文字

.. rubric:: 不创建目录节点的标题

.. hlist::
   :columns: 3

   * 有行列的列表
   * short items
   * that should be
   * displayed
   * horizontally

.. code-block:: ruby
   :linenos:

   Some more Ruby code.

.. highlight:: python
   :linenothreshold: 1

.. code-block:: python
   :caption: this.py
   :name: this-py
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print('This line is highlighted.')
       print('This one is not...')
       print('...but this one is.')

See :ref:`this code snippet <this-py>` for an example.


.. glossary::

   term 1
   term 2

      Definition of both terms.


.. sectionauthor:: Guido van Rossum <guido@python.org>

.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2

.. math::
   :nowrap:

   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2
   \end{eqnarray}

.. toctree::
   :numbered:
   :caption: Table of Contents
   :name: mastertoc
   :titlesonly:

   :glob:

   intro*
   recipe/*

.. toctree::
   :hidden:

   doc_1
   doc_2

.. function:: foo(x)
              foo(y, z)
   :module: some.module.name

   Return a line of text input from the user.

:fieldname: Field content


脚注Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.


引用
Lorem ipsum [Ref]_ dolor sit amet.

.. [Ref] Book or article reference, URL or whatever.
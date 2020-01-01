
Demo
#####

********
chapters
********


.. _sections-label:

=================
sections
=================


.. _my-figure:

-----------
subsections
-----------

^^^^^^^^^^^^^^
subsubsections
^^^^^^^^^^^^^^

""""""""""
paragraphs
""""""""""

* 这是一个项目符号列表.
* 它有两项，
  第二项使用两行.

1. 这是个有序列表.
2. 也有两项.

#. 是个有序列表.
#. 也有两项.

| 这些行
| 在源文件里

> 被分隔的一模一样.

..
   这整个缩进块都是
   一个评论.

   仍是一个评论.

.. image:: http://www.iedusg.com/public/uploads/article//5572275fe37422c4cf6d6c851c845cfb.jpg
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: alternate text
   :align: center

Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.

This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.

.. note::

   该功能不适于发送垃圾邮件.

.. versionadded:: 2.5
   The *spam* parameter.

.. centered:: LICENSE AGREEMENT

.. hlist::
   :columns: 3

   * 列表
   * 的子
   * 项会
   * 水平
   * 排列

environment
      一个结构，包含信息是所有文档的保存路径，使用的参考文献等.
      在解析的阶段使用，因此连续运行时仅需解析新的或修改过的文档.

      .. image:: http://www.iedusg.com/public/uploads/article//5572275fe37422c4cf6d6c851c845cfb.jpg
         :height: 100px
         :width: 200 px
         :scale: 50 %
         :alt: alternate text
         :align: center

      dsfdsf


.. glossary::

   environment
      一个结构，包含信息是所有文档的保存路径，使用的参考文献等.
      在解析的阶段使用，因此连续运行时仅需解析新的或修改过的文档.

      .. image:: http://www.iedusg.com/public/uploads/article//5572275fe37422c4cf6d6c851c845cfb.jpg
         :height: 100px
         :width: 200 px
         :scale: 50 %
         :alt: alternate text
         :align: center

      dsfdsf

   source directory
      根路径，包含子目录，包含一个Sphinx工程的所有源文件.

.. productionlist::
   try_stmt: try1_stmt | try2_stmt
   try1_stmt: "try" ":" `suite`
            : ("except" [`expression` ["," `target`]] ":" `suite`)+
            : ["else" ":" `suite`]
            : ["finally" ":" `suite`]
   try2_stmt: "try" ":" `suite`
            : "finally" ":" `suite`



`flash <https://www.flash.cn/>`_

This is the text of the section.

It refers to the section itself, see :ref:`sections-label`.


This is the text of the section.


This is the text of the section.

It refers to the section itself, see :ref:`my-figure`.


This is the text of the section.
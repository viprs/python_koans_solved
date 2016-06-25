#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutNone(Koan):

    def test_none_is_an_object(self):
        "Python 里的 NULL 与其他的编程语言不同"
        self.assertEqual(__, isinstance(None, object))

    def test_none_is_universal(self):
        "在Python里，空只有一个 None"
        self.assertEqual(__, None is None)

    def test_what_exception_do_you_get_when_calling_nonexistent_methods(self):
        """
        异常是如何产生的？
        当你调用对象一个不存在的方法时，就会抛出异常

        提示: 用下面的代码在 python 控制台里试验一下。
        try ... except ... 还不太懂，没有关系，我们稍后会讲
        """
        try:
            None.some_method_none_does_not_know_about()
        except Exception as ex:
            # 在这里捕获异常
            # 进行异常处理
            #   更多参考资料：
            #   https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute

            self.assertEqual(__, ex.__class__)

            # 观察这个异常的说明是什么，把__替换成那个字符串，就可以了
            self.assertMatch(__, ex.args[0])

    def test_none_is_distinct(self):
        """
        切记：None 与 0、False都不一样
        """
        self.assertEqual(____, None is not 0)
        self.assertEqual(____, None is not False)

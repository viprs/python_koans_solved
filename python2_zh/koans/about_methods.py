#!/usr/bin/env python
# -*- coding: utf-8 -*-


from runner.koan import *


def my_global_function(a, b):
    return a + b


class AboutMethods(Koan):
    def test_calling_a_global_function(self):
        self.assertEqual(__, my_global_function(2, 3))

    # 注意，参数个数错误并不是语法错误，而是运行时错误
    def test_calling_functions_with_wrong_number_of_arguments(self):
        try:
            my_global_function()
        except Exception as exception:
            # 提示： 对象的 .__name__ 属性将类名转换成一个字符串
            self.assertEqual(__, exception.__class__.__name__)
            self.assertMatch(
                r'my_global_function\(\) takes exactly 2 arguments \(0 given\)',
                exception[0])
            # 注意，小括号前有反斜杠

        try:
            my_global_function(1, 2, 3)
        except Exception as e:
            self.assertMatch(__, e[0])

    # ------------------------------------------------------------------

    def pointless_method(self, a, b):
        sum = a + b

    def test_which_does_not_return_anything(self):
        self.assertEqual(__, self.pointless_method(1, 2))
        # 提示，class的方法不需要你传递self参数，类帮你完成了


    # ------------------------------------------------------------------

    def method_with_defaults(self, a, b='default_value'):
        return [a, b]

    def test_calling_with_default_values(self):
        self.assertEqual(__, self.method_with_defaults(1))
        self.assertEqual(__, self.method_with_defaults(1, 2))

    # ------------------------------------------------------------------

    def method_with_var_args(self, *args):
        return args

    def test_calling_with_variable_arguments(self):
        self.assertEqual(__, self.method_with_var_args())
        self.assertEqual(('one', ), self.method_with_var_args('one'))
        self.assertEqual(__, self.method_with_var_args('one', 'two'))

    # ------------------------------------------------------------------

    def function_with_the_same_name(self, a, b):
        return a + b

    def test_functions_without_self_arg_are_global_functions(self):
        def function_with_the_same_name(a, b):
            return a * b

        self.assertEqual(__, function_with_the_same_name(3, 4))

    def test_calling_methods_in_same_class_with_explicit_receiver(self):
        def function_with_the_same_name(a, b):
            return a * b

        self.assertEqual(__, self.function_with_the_same_name(3, 4))

    # ------------------------------------------------------------------

    def another_method_with_the_same_name(self):
        return 10

    link_to_overlapped_method = another_method_with_the_same_name

    def another_method_with_the_same_name(self):
        return 42

    def test_that_old_methods_are_hidden_by_redefinitions(self):
        self.assertEqual(__, self.another_method_with_the_same_name())

    def test_that_overlapped_method_is_still_there(self):
        self.assertEqual(__, self.link_to_overlapped_method())

    # ------------------------------------------------------------------

    def empty_method(self):
        pass

    def test_methods_that_do_nothing_need_to_use_pass_as_a_filler(self):
        self.assertEqual(__, self.empty_method())

    def test_pass_does_nothing_at_all(self):
        "You"
        "shall"
        "not"
        pass
        self.assertEqual(____, "Still got to this line" != None)

    # ------------------------------------------------------------------

    def one_line_method(self): return 'Madagascar'

    def test_no_indentation_required_for_one_line_statement_bodies(self):
        self.assertEqual(__, self.one_line_method())

    # ------------------------------------------------------------------

    def method_with_documentation(self):
        "A string placed at the beginning of a function is used for documentation"
        return "ok"

    def test_the_documentation_can_be_viewed_with_the_doc_method(self):
        self.assertMatch(__, self.method_with_documentation.__doc__)

    # ------------------------------------------------------------------

    class Dog(object):
        def name(self):
            return "Fido"

        def _tail(self):
            # 前置下划线表示这是一个类的私有方法
            return "wagging"

        def __password(self):
            return 'password'  # Genius!

    def test_calling_methods_in_other_objects(self):
        rover = self.Dog()
        self.assertEqual(__, rover.name())

    def test_private_access_is_implied_but_not_enforced(self):
        rover = self.Dog()

        # 可以访问私有方法，但不推荐这么做
        self.assertEqual(__, rover._tail())

    def test_double_underscore_attribute_prefixes_cause_name_mangling(self):
        """当创建一个实例时，以双下划线(__)开头的属性名就会损坏，
        就不能使用普通调用了."""
        rover = self.Dog()
        try:
            #直接调用__password方法就不行了
            password = rover.__password()
        except Exception as ex:
            self.assertEqual(__, ex.__class__.__name__)

        # 但下面这种方法可以访问
        self.assertEqual(__, rover._Dog__password())

        # Name mangling exists to avoid name clash issues when subclassing.
        # It is not for providing effective access protection

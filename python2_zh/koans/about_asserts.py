#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutAsserts(Koan):

    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        # 如果你感到困惑，下面的视频可能会有所帮助（需要科学上网）
        #
        #   http://bit.ly/about_asserts

        self.assertTrue(True)  # 这里应该填 True

    def test_assert_with_message(self):
        """
        assertTrue可以在第二个参数添加一些提示，帮助你发现错误
        """
        self.assertTrue(True, "This should be True -- please fix it")

    def test_fill_in_values(self):
        """
        有时候，你需要填写一些数值，占位符一般是__
        """
        self.assertEqual(1 + 1, 2)

    def test_assert_equality(self):
        """
        为了验证实际值与期望值，我们必须将两者比较
        """
        expected_value = 2
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):
        """
        有些情况，assertEqual比assertTrue更适合做比较
        """
        expected_value = 2
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)

    def test_that_unittest_asserts_work_the_same_way_as_python_asserts(self):
        """
        验证表达式是否为真
        格式: assert 表达式
        """

        # assert 如果是False会抛出一个 AssertionError 异常
        assert True

    def test_that_sometimes_we_need_to_know_the_class_type(self):
        """
        What is in a class name?
        """

        # Sometimes we will ask you what the class type of an object is.
        #
        # For example, contemplate the text string "navel". What is its class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> FILL ME IN! <=-' != <type 'str'>
        #
        # So "navel".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # See for yourself:

        self.assertEqual(str, "navel".__class__) # It's str, not <type 'str'>

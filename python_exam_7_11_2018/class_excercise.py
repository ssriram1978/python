#!/usr/bin/env python3
#The above said line is called hashbang or shebang. This is done to make this code a standalone executable piece of code.

if __name__=="__main__":

    import os
    os.system('python python_exam/parent_child/parent.py')

    import python_exam.parent_child.child

    import python_exam.usage.exception_class

    print("---------Demonstrating how to use super class.----------")

    from python_exam.parent_child.super_child import how_to_use_super

    obj4=how_to_use_super()

    import python_exam.usage.decorator_fn

    import python_exam.usage.generator_fn

    import python_exam.usage.map_filter_reduce

    import python_exam.usage.reverse_sorted

    import python_exam.usage.file_operations

    import python_exam.usage.while_else_if_else

    import python_exam.usage.shortcut_operators

    import python_exam.usage.floating_point

    #print("***********input() ************")
    #x=eval(input("Enter a number"))
    #print(type(x))

    #this is a demo of a simple class.
    class xyz:
        pass


    import python_exam.usage.demo_scientific_notation

    import python_exam.usage.shallow_deep

    import python_exam.usage.tuple_fn

    import python_exam.usage.string_manip

    import python_exam.usage.unicode

    #import python_exam.usage.py_compile_fn

    import python_exam.usage.iterator

    import python_exam.usage.keyword_non_keyword_args


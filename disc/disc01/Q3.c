/*************************************************
 * 说明：
 * 要求仅更改标注注释的函数体，以实现输出和指定输出相同
 * 指定输出如下：
hello
0
hello, world
0

*************************************************/
#include <stdio.h>

int cond()
{
    // Your Code Here.
}

int true_func()
{
    // Your Code Here.
}

int false_func()
{
    // Code Here.
}

int if_function(int condition, int true_result, int false_result)
{
    if (condition)
        return true_result;
    else
        return false_result;
}

int with_if_function()
{
    return if_function(cond(), true_func(), false_func());
}

int with_if_statement()
{
    if (cond())
        return true_func();
    else
        return false_func();
}

int main()
{
    printf("\n%d\n", with_if_statement());
    printf("\n%d\n", with_if_function());
    return 0;
}

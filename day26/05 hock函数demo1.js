function foo() {
    console.log("foo功能...")
    return 123
}
foo()

var old_foo = foo

foo = function () {
    console.log("截断开始...")
    debugger;
    old_foo()
    console.log("截断结束...")
}
foo()
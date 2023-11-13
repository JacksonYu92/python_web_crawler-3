function foo(a,b,c,d,e,f){
    console.log("foo功能...")
    console.log(a,b,c,d,e,f)
    return 123
}

var _foo = foo

foo = function () {
    console.log("截断开始...")
    _foo.apply(this,arguments)
    console.log("截断结束...")
}

foo(1,2,3,4,5,6,7)

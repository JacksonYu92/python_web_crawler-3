var _eval = eval

eval = function (src) {
    console.log("eval截断开始...")
    debugger;
    _eval.apply(this, src)
    console.log("eval截断结束...")
}
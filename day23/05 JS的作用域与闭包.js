

(function () {
    console.log("AAA")
    function foo() {
        console.log("foo01")
    }
})();
var x = 1000
!(function () {
    console.log("AAA")
    function a(){}
    function b(){}
    function foo() {
        console.log("foo01")
        a()
        b()
        console.log(x)
    }
})()
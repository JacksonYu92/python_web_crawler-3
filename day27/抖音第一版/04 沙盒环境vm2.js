var fs = require("fs")
var vm = require("vm2")
// 初始化vm对象
const {VM, VMScript} = vm
var myvm = new VM()

var code = fs.readFileSync("05 沙盒测试源码.js")
// console.log(code.toString())


ret = myvm.run(code.toString())
console.log(ret(1.34))







// jsCode = ""
// // (1) 添加补环境的代码
// code01 = fs.readFileSync("./补环境.js")
// // console.log(code01.toString())
// jsCode += code01
// jsCode += ";;;\n"
// // (2) 添加源码
// code02 = fs.readFileSync("./源码.js")
// // console.log(code01.toString())
// jsCode += code02
// jsCode += ";;;\n"
// // console.log(jsCode)
// fn = myvm.run(jsCode)
// console.log(fn(1.23))
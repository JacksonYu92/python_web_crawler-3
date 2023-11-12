const CryptoJS = require("crypto-js")

l = {
    key: CryptoJS.enc.Utf8.parse("fX@VyCQVvpdj8RCa"),
    iv: CryptoJS.enc.Utf8.parse(function (t) {
        for (var e = "", i = 0; i < t.length - 1; i += 2) {
            var n = parseInt(t[i] + "" + t[i + 1], 16);
            e += String.fromCharCode(n)
        }
        return e
    }("00000000000000000000000000000000"))
}

v = function (data) {
    return function (data) {
        return CryptoJS.AES.encrypt(data, l.key, {
            iv: l.iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        }).toString()
    }(data)
}

d = function (data) {
    var v = CryptoJS.MD5(data).toString()
    // console.log("md5的值：", v)
    return v
}

f = function (t) {
    var e = "";
    return Object.keys(t).sort().forEach((function (n) {
            e += n + ("object" === typeof (t[n]) ? JSON.stringify(t[n], (function (t, e) {
                    return "number" == typeof e && (e = String(e)),
                        e
                }
            )).replace(/\//g, "\\/") : t[n])
        }
    )),
        e
}


h = function (t) {
    var data = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , e = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : "a75846eb4ac490420ac63db46d2a03bf"
        , n = e + f(data) + f(t) + e;
    return n = d(n),
        n = v(n)
}


// var sign = h(U, L, C)
// console.log(sign)

function get_headers(data) {

    var Timer = parseInt((new Date).getTime() / 1000)

    var U = {
        "App-Ver": "",
        "Os-Ver": "",
        "Device-Ver": "",
        Imei: "",
        "Access-Token": "",
        Timestemp: Timer.toString(),
        NonceStr: "".concat(Timer).concat("xxxxx"),
        "App-Id": "4ac490420ac63db4",
        "Device-Os": "web"
    };

// console.log(U)

    C = "a75846eb4ac490420ac63db46d2a03bf"

    U["Signature"] = h(U, data, C)

    return U
}

// data = {
//     "username": "asdas",
//     "password": "asdsad",
//     "code": "3c1b",
//     "hdn_refer": ""
// }
//
// console.log(get_headers(data))
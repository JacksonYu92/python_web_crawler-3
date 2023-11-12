window = global

function h(n, t) {
    for (var e = (n = n["split"](""))["length"], r = t["length"], a = "charCodeAt", i = 0; i < e; i++)
        n[i] = o(n[i][a](0) ^ t[(i + 10) % r][a](0));
    return n["join"]("")
}

function o(n) {
    t = "",
        ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']["forEach"](function (n) {
            t += window["unescape"]("%u00" + n)
        });
    var t, e = t;
    return window["String"]["fromCharCode"](n)
}

function getV(t) {
    t = window["encodeURIComponent"](t)["replace"](/%([0-9A-F]{2})/g, function (n, t) {
        return o("0x" + t)
    });
    try {
        return window["btoa"](t)
    } catch (n) {
        return window["Buffer"]["from"](t)["toString"]("base64")
    }
}

function get_analysis(url, params) {
    var baseURL = "https://api.qimai.cn"
    var n;
    var s = 1013
    var e, r = +new Date() - s - 1661224081041, a = [];
    return void 0 === params && (params = {}),
        window["Object"]["keys"](params)["forEach"](function (n) {
            if (n == "analysis")
                return !1;
            params["hasOwnProperty"](n) && a["push"](params[n])
        }),
        a = a["sort"]()["join"](""),
        a = getV(a),
        a = (a += "@#" + url["replace"](baseURL, "")) + ("@#" + r) + ("@#" + 3),
        e = getV(h(a, "xyz517cda96efgh"))
    // -1 == url["indexOf"]("analysis") && (url += (-1 != url["indexOf"]("?") ? "&" : "?") + "analysis" + "=" + window["encodeURIComponent"](e)),
    return e
}

// var data = {
//     "url": "/indexV2/getUserModules",
//     "method": "get",
//     "headers": {
//         "common": {
//             "Accept": "application/json, text/plain, */*"
//         },
//         "delete": {},
//         "get": {},
//         "head": {},
//         "post": {
//             "Content-Type": "application/x-www-form-urlencoded"
//         },
//         "put": {
//             "Content-Type": "application/x-www-form-urlencoded"
//         },
//         "patch": {
//             "Content-Type": "application/x-www-form-urlencoded"
//         }
//     },
//     "params": {
//         "setting": 1
//     },
//
//     "transformRequest": [
//         null
//     ],
//     "transformResponse": [
//         null
//     ],
//     "timeout": 15000,
//     "withCredentials": true,
//     "xsrfCookieName": "XSRF-TOKEN",
//     "xsrfHeaderName": "X-XSRF-TOKEN",
//     "maxContentLength": -1,
//     "maxBodyLength": -1
// }
var url = "/indexV2/getUserModules"
var params = {
    "setting": 1
}
console.log(get_analysis(url, params))
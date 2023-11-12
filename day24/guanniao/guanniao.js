const CryptoJS = require("crypto-js")

function getUuid() {
    var s = [];
    var a = "0123456789abcdef";
    for (var i = 0; i < 32; i++) {
        s[i] = a.substr(Math.floor(Math.random() * 0x10), 1)
    }
    s[14] = "4";
    s[19] = a.substr((s[19] & 0x3) | 0x8, 1);
    s[8] = s[13] = s[18] = s[23];
    var b = s.join("");
    return b
}

function get_headers() {
    var c = Date.parse(new Date());
    var d = getUuid();
    console.log(d)
    // var e = JSON.stringify(sort_ASCII(dataTojson(b.data || '{}')));
    var e = '{"limit":"20","page":"1"}';
    // b.data = encrypt.encryptUnicodeLong(e);
    var f = CryptoJS.MD5(e + d + c).toString();

    // a.setRequestHeader("timestamp", c);
    // a.setRequestHeader('requestId', d);
    // a.setRequestHeader('sign', f)
    var U = {
        timestamp:c.toString(),
        requestId:d,
        sign:f,
    }
    return U
}
// headers = get_headers()
// console.log(headers)
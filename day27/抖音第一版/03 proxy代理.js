window = new Proxy(window, {
    get: function (target, property1) {
        console.log('获取对象-->', obj_name, '属性-->', property1, '值-->', target[property1])
        debugger
        return Reflect.get(target, property1)
    },
    set: function (target, property1, value) {
        console.log('设置对象-->', obj_name, '属性-->', property1, '值-->', target[property1])
        debugger
        Reflect.set(target, property1, value)
    }
})




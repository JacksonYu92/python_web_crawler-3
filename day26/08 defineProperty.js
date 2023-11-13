var people = {
    name: '张三',
}

var count = 0

Object.defineProperty(people, "age", {
    get: function () {
        console.log('获取值...');
        return count;
    },
    set: function (val) {
        console.log('设置值...', val);
        count = val > 100 ? 100 : val


    },
})

console.log(people.age)

people.age = 1000
console.log(people.age)

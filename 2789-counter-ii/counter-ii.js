var createCounter = function(init) {
    let current = init

    return {
        increment() {
            current++
            return current
        },
        decrement() {
            current--
            return current
        },
        reset() {
            current = init
            return current
        }
    }
}

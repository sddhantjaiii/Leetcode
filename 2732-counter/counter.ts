function createCounter(n: number): () => number {
    let x=-1
    return function() {
         x=x+1
        return n+x

       
    }
}


/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
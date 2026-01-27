/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let fa=[];
    for(let i=0;i< arr.length ; i++){
        let r=fn(arr[i],i);
        if ((r===true) || (r<0)||(r>0)){
            fa.push(arr[i])
        }
        
    }
    return fa;
};
promise1 = new Promise(resolve => setTimeout(() => resolve(2), 20));
promise2 = new Promise(resolve => setTimeout(() => resolve(5), 60));


var addTwoPromises = async function(promise1, promise2) {
    return new Promise (async (resolve, reject) => {
        promise1.then((value1) => {
            promise2.then((value2) => {
                resolve(value1 + value2);
            })
        })
    })
};

addTwoPromises(promise1, promise2).then((result) => {
    try {
        console.log(result)
    } catch (error) {
        console.error(error)
    }
})


export function checkAccessMiddleware(to, from, next) {
    // store.dispatch("fitness/allFitnessPlans");
    // store.dispatch("user/allProfiles");
    // if(sessionStorage.getItem('user') !== null){
    //     let data = {'username': sessionStorage.getItem('user'),};
    //     // let id = {'personID': sessionStorage.getItem('personID'),};
    //     store.dispatch('user/getUser', data)
    //     // store.dispatch('fitness/getFitnessPlan', id)
    //     next();
    // }else {
    //     next();
    // }
    next()
}
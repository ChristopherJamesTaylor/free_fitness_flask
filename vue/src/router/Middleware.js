import store from "@/state/store"

export function checkAccessMiddleware(to, from, next) {
    if(sessionStorage.getItem('user') !== null){
        let data = {'username': sessionStorage.getItem('user'),};
        store.dispatch('user/getUser', data).then((response) => {
            if(response){
                next();
            }
        })
    } else{
        next();
    }
}
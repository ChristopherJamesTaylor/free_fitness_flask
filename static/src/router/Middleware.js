import store from "@/state/store"

export function checkAccessMiddleware(to, from, next) {
    if(store.state.user.authData.FullName == ""){
        store.dispatch('user/getSession').then((response) => {
            if(response){
                next();
            }
        })
    } else{
        next();
    }
}
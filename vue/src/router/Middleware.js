import store from "@/state/store"

export function checkAccessMiddleware(to, from, next) {
    // eslint-disable-next-line no-console
    console.log("middleware");
    // eslint-disable-next-line no-console
    console.log(sessionStorage.getItem('user'));
    if(sessionStorage.getItem('user') !== null){
        let data = {'username': sessionStorage.getItem('user'),};
        store.dispatch('user/getUser', data).then((response) => {
            if(response){
                // eslint-disable-next-line no-console
                console.log('success');
                // eslint-disable-next-line no-console
                console.log(response);
                next();
            }
        })
    } else{
        next();
    }
}
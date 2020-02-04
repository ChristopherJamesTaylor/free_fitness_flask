import {api} from "../../api/user";

export const state = {
    authData: null,
};

export const getters = {
    listSession(){
        return state.authData
    }
};

export const mutations = {
    SET_SESSION(state, payload){
        state.authData = payload;
    },
};

export const actions = {
    async getSession({ commit }){
        // eslint-disable-next-line no-console
        console.log('about to hit api');
        const response = await api.getSession();
        if(response){
            const payload = response;
            // eslint-disable-next-line no-console
            console.log(payload);
            commit("SET_SESSION", payload);
            return payload
        }
        else {
            // eslint-disable-next-line no-console
            console.log("NO DATA!")
        }
    },
};




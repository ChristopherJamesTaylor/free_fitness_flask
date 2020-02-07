import {api} from "../../api/user";

export const state = {
    user: null,
};

export const getters = {
    listUser(){
        return state.user
    }
};

export const mutations = {
    SET_USER(state, payload){
        state.user = payload;
    },
};

export const actions = {
    async getUser({ commit }, data){
        const response = await api.getUser(data);
        if(response){
            const payload = response.data;
            commit("SET_USER", payload);
            return payload
        }
    },
};




import {api} from "../../api/macros";

export const state = {
    macros: null

};

export const getters = {
    listMacros(){
        return state.macros;
    }
};

export const mutations = {
    SET_MACROS(state, payload){
        state.macros = payload;
    },
};

export const actions = {
    async getMacros({ commit }, data){
        const response = await api.getMacros(data);
        if(response){
            const payload = response.data;
            commit("SET_MACROS", payload);
            return payload;
        }
    },
};
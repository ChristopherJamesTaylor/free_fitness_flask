import {api} from "../../api/gym";

export const state = {
    gym: null

};

export const getters = {
    listGyms(){
        return state.gym;
    }
};

export const mutations = {
    SET_GYM(state, payload){
        state.gym = payload;
    },
};

export const actions = {
    async getGyms({ commit }, data){
        const response = await api.getGyms(data);
        if(response){
            const payload = response.data;
            commit("SET_GYM", payload);
            return payload;
        }
    },
};
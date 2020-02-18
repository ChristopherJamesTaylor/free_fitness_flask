import {api} from "../../api/user";

export const state = {
    user: null,
    fitnessPlan: null,
};

export const getters = {
    listUser(){
        return state.user;
    },
    listFitnessPlan(){
        return state.user;
    }
};

export const mutations = {
    SET_USER(state, payload){
        state.user = payload;
    },
    SET_FITNESS_PLAN(state,payload){
        state.fitnessPlan = payload;
    }
};

export const actions = {
    async getUser({ commit }, data){
        const response = await api.getUser(data);
        if(response){
            const payload = response.data;
            commit("SET_USER", payload);
            return payload;
        }
    },
    async getFitnessPlan({ commit }, data){
        const response = await api.getFitnessPlan(data);
        if(response){
            const payload = response.data;
            commit("SET_FITNESS_PLAN", payload);
            return payload;
        }
    },
};




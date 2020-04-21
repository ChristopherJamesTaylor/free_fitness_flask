import {api} from "../../api/user";

export const state = {
    user: null,
    fitnessPlan: null,
    editProfile: null,
};

export const getters = {
    listUser(){
        return state.user;
    },
    listFitnessPlan(state){
        return state.user;
    },
    listEditedProfile(state){
        return  state.editProfile;
    }
};

export const mutations = {
    SET_USER(state, payload){
        state.user = payload;
    },
    SET_FITNESS_PLAN(state,payload){
        state.fitnessPlan = payload;
    },
    SET_EDITED_PROFILE(state, payload){
        state.editProfile = payload;
    }
};

export const actions = {
    async getUser({ commit }, data){
        const response = await api.getUser(data);
        if(response){
            console.log(response.data);
            const payload = response.data;
            commit("SET_USER", payload);
            return payload;
        }
    },
    async allProfiles({ commit }, data){
        const response = await api.allProfiles(data);
        if(response){
            const payload = response.data;
            commit("SET_ALL_PROFILES", payload);
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
    async editProfile({ commit }, data){
        const response = await api.editProfile(data);
        if(response){
            const payload = response.data;
            commit("SET_EDITED_PROFILE", payload);
            return payload;
        }
    },
};




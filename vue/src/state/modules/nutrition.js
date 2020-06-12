import {api} from "../../api/nutrition";

export const state = {
    meals: null,
    savePlan:null,
};

export const getters = {
    listMeals(){
        return state.meals;
    },
    listSavedPlan(){
        return state.savePlan;
    }

};

export const mutations = {
    SET_MEAL(state, payload){
        state.meals = payload;
    },
    SET_SAVED_PLAN(state, payload){
        state.savedPlan = payload;
    },
};

export const actions = {
    async getMealPlan({ commit }, data){
        const response = await api.getMealPlan(data);
        if(response){
            const payload = response.data;
            commit("SET_MEAL", payload);
            return payload;
        }
    },
    async savePlan({ commit }, data){
        const response = await api.savePlan(data);
        if(response){
            const payload = response.data;
            commit("SET_SAVED_PLAN", payload);
            return payload;
        }
    },
};
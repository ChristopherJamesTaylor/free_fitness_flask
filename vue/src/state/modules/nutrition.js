import {api} from "../../api/nutrition";

export const state = {
    meals: null

};

export const getters = {
    listMeals(){
        return state.exercises;
    }
};

export const mutations = {
    SET_MEAL(state, payload){
        state.meals = payload;
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
};
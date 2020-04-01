import {api} from "../../api/fitness";

export const state = {
    exercises: null,
    plan: null
};

export const getters = {
    listExercises(){
        return state.exercises;
    },
    listPlan(){
        return state.plan;
    }
};

export const mutations = {
    SET_EXERCISES(state, payload){
        state.exercises = payload;
    },
    SET_PLAN(state, payload){
        state.plan = payload;
    },
};

export const actions = {
    async getExercises({ commit }, data){
        const response = await api.getExercises(data);
        if(response){
            const payload = response.data;
            commit("SET_EXERCISES", payload);
            return payload;
        }
    },
    async savePlan({ commit }, data){
        const response = await api.savePlan(data);
        if(response){
            // eslint-disable-next-line no-console
            console.log(response);
            const payload = response.data;
            commit("SET_PLAN", payload);
            return payload;
        }
    },
};
import {api} from "../../api/fitness";

export const state = {
    exercises: null,
    plan: null,
    currentPlan:null,
    editedPlan:null,
};

export const getters = {
    listExercises(){
        return state.exercises;
    },
    listPlan(){
        return state.plan;
    },
    listCurrentPlan(){
        return state.currentPlan;
    },
    listEditedPlan(){
        return state.editedPlan;
    }
};

export const mutations = {
    SET_EXERCISES(state, payload){
        state.exercises = payload;
    },
    SET_PLAN(state, payload){
        state.plan = payload;
    },
    SET_CURRENT_PLAN(state, payload){
        state.currentPlan = payload;
    },
    SET_EDITED_PLAN(state, payload){
        state.editedPlan = payload;
    }
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
    async getFitnessPlan({ commit }, data){
        const response = await api.getFitnessPlan(data);
        if(response){
            // eslint-disable-next-line no-console
            console.log(response);
            const payload = response.data;
            commit("SET_CURRENT_PLAN", payload);
            return payload;
        }
    },
    async saveEditedPlan({ commit }, data){
        const response = await api.saveEditedPlan(data);
        if(response){
            // eslint-disable-next-line no-console
            console.log(response);
            const payload = response.data;
            commit("SET_EDITED_PLAN", payload);
            return payload;
        }
    },
};
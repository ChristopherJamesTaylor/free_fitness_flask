import {api} from "../../api/fitness";

export const state = {
    exercises: null,
    plan: null,
    currentPlan:null,
    editedPlan:null,
    allFitnessPlans:null,
    deletedPlan:null,
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
    },
    listAllFitnessPlans(){
        return state.allFitnessPlans;
    }
};

export const mutations = {
    SET_ALL_FITNESS_PLANS(state, payload) {
        state.allFitnessPlans = payload;
    },
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
    },
    SET_DELETED_PLAN(state, payload){
        state.deletedPlan = payload;
    }
};

export const actions = {
    async getExercises({ commit }, data){
        const response = await api.getExercises(data);
        if(response){
            // eslint-disable-next-line no-console
            console.log(response);
            const payload = response.data;
            commit("SET_EXERCISES", payload);
            return payload;
        }
    },
    async savePlan({ commit }, data){
        const response = await api.savePlan(data);
        if(response){
            const payload = response.data;
            commit("SET_PLAN", payload);
            return payload;
        }
    },
    async getFitnessPlan({ commit }, data){
        const response = await api.getFitnessPlan(data);
        if(response){
            const payload = response.data;
            commit("SET_CURRENT_PLAN", payload);
            return payload;
        }
    },
    async saveEditedPlan({ commit }, data){
        const response = await api.saveEditedPlan(data);
        if(response){
            const payload = response.data;
            commit("SET_EDITED_PLAN", payload);
            return payload;
        }
    },
    async allFitnessPlans({ commit }){
        const response = await api.allFitnessPlans();
        if(response){
            const payload = response.data;
            commit("SET_ALL_FITNESS_PLANS", payload);
            return payload;
        }
    },
    async deleteFitnessPlan({ commit }, data){
        const response = await api.deleteFitnessPlan(data);
        if(response){
            const payload = response.data;
            commit("SET_DELETED_PLAN", payload);
            return payload;
        }
    },
};
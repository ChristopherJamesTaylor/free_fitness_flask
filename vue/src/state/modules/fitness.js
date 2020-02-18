import {api} from "../../api/fitness";

export const state = {
    exercises: null

};

export const getters = {
    listExercises(){
        return state.exercises;
    }
};

export const mutations = {
    SET_EXERCISES(state, payload){
        state.exercises = payload;
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
};
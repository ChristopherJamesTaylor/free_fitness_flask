import { instance } from "@/api";
import { api_url } from "./constants";

export const api = {
    Exercises(data) {
        return instance.post(`${api_url}/Exercises`, data);
    },
    allFitnessPlans() {
        return instance.get(`${api_url}/allFitnessPlans`);
    },
    savePlan(data) {
        return instance.post(`${api_url}/savePlan`, data);
    },
    getFitnessPlan(data){
        return instance.post(`${api_url}/getFitnessPlan`, data);
    },
    saveEditedPlan(data){
        return instance.post(`${api_url}/editedPlan`, data);
    },
    deleteFitnessPlan(data){
        return instance.post(`${api_url}/deleteFitnessPlan`, data);
    },
};
import { instance } from "@/api";
import { api_url } from "./constants";

export const api = {
    getExercises(data) {
        return instance.post(`${api_url}/getExercises`, data);
    },
    savePlan(data) {
        return instance.post(`${api_url}/savePlan`, data);
    },
    getFitnessPlan(data){
        return instance.post(`${api_url}/getFitnessPlan`, data);
    },
    saveEditedPlan(data){
        return instance.post(`${api_url}/editedPlan`, data);
    }
};
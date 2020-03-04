import { instance } from "@/api";
import { api_url } from "./constants";

export const api = {
    getMealPlan(data) {
        return instance.post(`${api_url}/getMealPlan`, data);
    },
};
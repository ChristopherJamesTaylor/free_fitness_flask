import { instance } from "@/api";
import { api_url } from "./constants";

export const api = {
    getMealPlan(data) {
        return instance.get(`${api_url}/getMealPlan`, data);
    },
};
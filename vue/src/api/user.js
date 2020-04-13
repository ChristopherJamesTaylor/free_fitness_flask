import { instance } from "@/api";
import { api_url } from "./constants";

export const api = {
    getUser(data) {
        return instance.post(`${api_url}/getUser`, data);
    },
    getFitnessPlan(data) {
        return instance.post(`${api_url}/getFitnessPlan`, data);
    },
    editProfile(data) {
        return instance.post(`${api_url}/editProfile`, data);
    },
};
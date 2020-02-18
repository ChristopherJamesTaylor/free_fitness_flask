import { instance } from "@/api";

export const api = {
    getUser(data) {
        return instance.post("http://localhost:5000/getUser", data);
    },
    getFitnessPlan(data) {
        return instance.post("http://localhost:5000/getFitnessPlan", data);
    },
};
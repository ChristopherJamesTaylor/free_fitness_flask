import { instance } from "@/api";
import { api_url } from "./constants";

export const api = {
        getGyms(data) {
        return instance.post(`${api_url}/getGyms`, data);
    },
};
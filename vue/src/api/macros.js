import { instance } from "@/api";
import { api_url } from "./constants";

export const api = {
        getMacros(data) {
        return instance.post(`${api_url}/getMacros`, data);
    },
};
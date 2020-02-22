import { instance } from "@/api";
import { api_url } from "./constants"
export const api = {
    getAdmin() {
        return instance.get(`${api_url}/getAdmins`);
    },
    checkUser(data) {
        return instance.post(`${api_url}/checkUser`, data);
    },

    registerUser(data) {
        return instance.post(`${api_url}/registerUser`, data);
    }


}
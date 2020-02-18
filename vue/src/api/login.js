import { instance } from "@/api";
import { api_url } from "./constants"
export const api = {
    getAdmin() {
        // eslint-disable-next-line no-console
        console.log("Getting the admins");
        return instance.get(`${api_url}/getAdmins`);
    },
    checkUser(data) {
        // eslint-disable-next-line no-console
        console.log('your api is sending: ', data);
        return instance.post(`${api_url}/checkUser`, data);
    },

    registerUser(data) {
        // eslint-disable-next-line no-console
        console.log('your api is sending: ', data);
        return instance.post(`${api_url}/registerUser`, data);
    }


}
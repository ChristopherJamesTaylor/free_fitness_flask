import { instance } from "@/api";

export const api = {
    getAdmin() {
        // eslint-disable-next-line no-console
        console.log("Getting the admins");
        return instance.get("/getAdmins");
    },
    checkUser(data) {
        // eslint-disable-next-line no-console
        console.log('your api is sending: ', data);
        return instance.post("http://localhost:5000/checkUser", data);
    }
}
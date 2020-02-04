import { instance } from "@/api";

export const api = {
     getSession() {
        // eslint-disable-next-line no-console
        console.log('Hitting session');
        return instance.get("http://localhost:5000/getSession");
    },
};
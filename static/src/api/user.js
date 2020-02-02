import { instance } from "@/api";

export const api = {
     getSession() {
         // eslint-disable-next-line no-console
         console.log(instance.get("/getSession"));
        return instance.get("/getSession");
    },
};
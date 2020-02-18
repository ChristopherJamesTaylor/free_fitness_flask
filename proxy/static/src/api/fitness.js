import { instance } from "@/api";

export const api = {
    getExercises(data) {
        return instance.post("http://localhost:5000/getExercises", data);
    },
};
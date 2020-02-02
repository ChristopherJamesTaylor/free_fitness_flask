import {api} from "../../api/user";

export const state = {
    authData: {
      firstName: null,
      lastName: null,
      fullName: null,
    },
};

export const getters = {
  listUsers(state) {
      // eslint-disable-next-line no-console
      console.log(state.authData.fullName);
      return state.authData.fullName;
  }
};

export const mutations = {
    SET_SESSION(state, payload){
        state.authData = payload;
    },
};

export const actions = {
    async getSession({ commit }){
        const response = await api.getSession();
        if(response){
            const payload = response.data.row;
            // eslint-disable-next-line no-console
            console.log(payload);
            commit("SET_SESSION", payload);
            return payload
        }
        else {
            // eslint-disable-next-line no-console
            console.log("NO DATA!")
        }
    },
};




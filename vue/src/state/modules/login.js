import {api} from "../../api/login";

export const state = {
    user: null,
    admin: null,
    new_user:null,
};

export const getters = {
  listAdmins(state) {
      return state.admin;
  },
  listUsers(state) {
      return state.user;
  }
};

export const mutations = {
    SET_USER(state, payload){
        state.user = payload;
    },
    SET_ADMIN(state, payload){
        state.admin = payload;
    },
    REGISTER_USER(payload){
        state.new_user = payload;
    }
};

export const actions = {
    async getAdmins({ commit }){
        const response = await api.getAdmin();
        if(response){
            const payload = response.data.row;
            // eslint-disable-next-line no-console
            console.log(payload);
            commit("SET_ADMIN", payload);
            return payload
        }
        else {
            // eslint-disable-next-line no-console
            console.log("NO DATA!")
        }
    },
    async checkUser({ commit }, data){
        const response = await api.checkUser(data);
        if(response){
            const payload = response;
            commit("SET_USER", payload);
            return payload
        }
        else {
            // eslint-disable-next-line no-console
            console.log("NO DATA!")
        }
    },

    async registerUser({ commit }, data){
        // eslint-disable-next-line no-console
        console.log('your name is: ', data);
        const response = await api.registerUser(data);
        if(response){
            const payload = response;
            commit("REGISTER_USER", payload);
            return payload
        }
        else {
            // eslint-disable-next-line no-console
            console.log("NO DATA!")
        }
    },
};




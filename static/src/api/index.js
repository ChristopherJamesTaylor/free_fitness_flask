import axios from "axios";

const instance = axios.create({
  timeout: 60000
});

// create cancel token
const CancelToken = axios.CancelToken;
const source = CancelToken.source();

// Add a request interceptor
instance.interceptors.request.use(
  function(config) {
    // Do something before request is sent
    config.cancelToken = source.token;
    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

// Add a response interceptor
instance.interceptors.response.use(
  function(response) {
    // Do something with response data
    return response;
  },
  function(error) {
    // Do something with response error
    if (error.response.status == 401) {
      source.cancel("Operation canceled by the user.");
      window.location.replace("/");
    }
  }
);

export { instance };
